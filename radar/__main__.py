"""Command line entry point.

    python -m radar run                         # fetch, rank, summarize, write digest
    python -m radar run --no-summary            # skip the AI summaries
    python -m radar run --offline tests/fixtures   # test data; writes to offline-output/
    python -m radar presets                     # list the built-in topic presets
"""

from __future__ import annotations

import argparse
import logging
import os
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from . import sources
from .config import load_config, load_presets
from .digest import TopicStats, render
from .discord import post_daily
from .mailer import send_daily
from .models import Paper
from .runlog import RunLog
from .rank import assign_unique, score_papers
from .archive import Archive, to_paper
from .site import export_site
from .state import SeenState
from .summarize import summarize_all

log = logging.getLogger("radar")

TOPIC_PAUSE = 5   # seconds between topics; arXiv rate-limits bursts
HEAL_LIMIT = 150  # earlier items without AI summaries to retry per run


def run(args: argparse.Namespace) -> Path | None:
    cfg = load_config(args.config)
    if args.no_summary:
        cfg.summarize = False
    if args.offline and not getattr(args, "keep_paths", False):
        # Offline runs use test data: never let them overwrite the real digests or state.
        cfg.output_dir, cfg.site_dir = "offline-output/digests", "offline-output"
        cfg.state_path = "offline-output/seen.json"
        cfg.archive_path = "offline-output/archive.jsonl"
        cfg.runs_path = "offline-output/runs.json"

    runs = RunLog(cfg.runs_path)
    if getattr(args, "skip_if_done", False) and runs.done("build", datetime.now(timezone.utc).date()):
        log.info("today's digest is already built; nothing to do")
        return None

    started = time.monotonic()
    budget = 60 * float(getattr(args, "max_minutes", 0) or 0)      # 0 = no limit
    deadline = started + budget if budget else None

    def left() -> float:
        return (deadline - time.monotonic()) if deadline else float("inf")

    now = datetime.now(timezone.utc)
    today = now.date()
    backfill = max(0, int(getattr(args, "backfill", 0) or 0))
    # The days this run fills in: normally just today; with --backfill N, the last N days.
    days = [today - timedelta(days=k) for k in range(max(backfill, 1) - 1, -1, -1)]

    # Look back a few extra days: arXiv and bioRxiv announce papers with a delay, so a
    # paper submitted just before the last run may only have appeared afterwards.
    # The seen-state makes sure nothing is recommended twice.
    start = now - timedelta(days=max(cfg.days, backfill) + cfg.overlap_days)
    state = SeenState(cfg.state_path)
    # Re-running a day (say, after adding an API key) should redo that day's selection,
    # not skip its papers as already seen.
    for d in days:
        state.forget_day(d)
    offline = sources.load_offline(args.offline) if args.offline else None
    sources.clear_arxiv_today()
    if offline is None and not backfill and cfg.arxiv_daily == "rss":
        try:
            n = sources.load_arxiv_today(cfg.topics)
            log.info("arXiv: %d new papers in today's listings", n)
        except Exception as exc:       # fall back to one API query per topic
            log.warning("arXiv RSS failed (%s); using the API instead", exc)
            sources.clear_arxiv_today()

    cands_by_topic: dict[str, list[Paper]] = {}
    seeds_by_topic: dict[str, list[str]] = {}
    stats: dict[str, TopicStats] = {}
    for i, topic in enumerate(cfg.topics):
        st = stats[topic.slug] = TopicStats()
        if deadline and left() < 0.4 * budget:
            # keep most of the time for summaries; skipped topics are fetched tomorrow
            st.error = "skipped this run to stay within the time limit"
            cands_by_topic[topic.slug] = []
            continue
        try:
            if offline is not None:
                cands = sources.offline_candidates(topic, offline)
                seeds: list[Paper] = []
            else:
                if i and sources.uses_network(topic):
                    time.sleep(TOPIC_PAUSE)  # be polite to the APIs
                log.info("[%s] fetching from %s", topic.slug, topic.source)
                cands = sources.fetch(topic, start, now, cfg.max_per_topic)
                seeds = sources.fetch_seeds(topic)
            if topic.primary_only:
                # drop papers merely cross-listed into this topic from other fields
                cands = [p for p in cands if p.primary_category in topic.categories]
            if not cfg.include_revisions:
                # bioRxiv lists a preprint again whenever a new version is posted;
                # by default only first versions count as new research
                cands = [p for p in cands if p.source == "arxiv" or p.version <= 1]
            new = [p for p in cands if not state.is_seen(p.uid)]
            cands_by_topic[topic.slug] = new
            seeds_by_topic[topic.slug] = [s.text for s in seeds]
            st.fetched, st.new = len(cands), len(new)
        except Exception as exc:  # one failing topic should not kill the digest
            log.error("[%s] failed: %s", topic.slug, exc)
            st.error = str(exc)
            cands_by_topic[topic.slug] = []

    def day_of(p: Paper):
        """The morning a paper shows up in the feed: the day after it was posted."""
        return min(today, max(days[0], p.published.date() + timedelta(days=1)))

    top_k = {t.slug: t.top_k for t in cfg.topics}
    chosen_by_day: dict = {}
    for d in days:
        ranked = {}
        for t in cfg.topics:
            pool = cands_by_topic.get(t.slug, [])
            if backfill:
                pool = [p for p in pool if day_of(p) == d]
            ranked[t.slug] = score_papers(pool, t, seeds_by_topic.get(t.slug))
        chosen_by_day[d] = assign_unique(ranked, top_k, cfg.min_score)

    log.info("fetching took %.0f min", (time.monotonic() - started) / 60)
    name_of = {t.slug: t.display_name(cfg.language) for t in cfg.topics}
    # newest day first, so today's items get their summaries before older ones
    pairs = [(p, name_of[slug]) for d in reversed(days)
             for slug, ps in chosen_by_day[d].items() for p in ps]
    log.info("selected %d items over %d day(s)", len(pairs), len(days))
    margin = 5 * 60                      # time kept for writing files and committing
    summarize_all(pairs, enabled=cfg.summarize, model=cfg.model, language=cfg.language,
                  deadline=(deadline - margin) if deadline else None)

    chosen = chosen_by_day[today]
    topic_of = {p.uid: name_of[slug] for slug, ps in chosen.items() for p in ps}
    todays = [p for ps in chosen.values() for p in ps]
    # Highlights compare z-scores, because raw scores are higher in topics with keywords.
    must_read = sorted(todays, key=lambda p: p.zscore, reverse=True)[:cfg.must_read]
    md = render(chosen, cfg.topics, must_read, stats,
                (now - timedelta(days=cfg.days), now), topic_of, cfg.language)

    out_dir = Path(cfg.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{now:%Y-%m-%d}.md"
    out.write_text(md, encoding="utf-8")
    (out_dir / "latest.md").write_text(md, encoding="utf-8")
    log.info("wrote %s (%d items today)", out, len(todays))

    archive = Archive(cfg.archive_path)
    for d, ch in chosen_by_day.items():
        archive.add(ch, d)
    archive.prune(today, cfg.archive_days)
    heal_archive(archive, cfg, name_of, deadline=(deadline - margin) if deadline else None)
    log.info("total run time %.0f min", (time.monotonic() - started) / 60)
    if cfg.site_dir:
        files = export_site(Path(cfg.site_dir), cfg, archive, today)
        log.info("wrote %d data files for the website", len(files))

    if not args.dry_run:
        for d, ch in chosen_by_day.items():
            state.mark([p.uid for ps in ch.values() for p in ps], d)
        state.prune(today)
        state.save()
        archive.save()
        runs.mark("build", today)
    return out


def heal_archive(archive: Archive, cfg, name_of: dict[str, str], deadline: float | None,
                 limit: int = HEAL_LIMIT) -> int:
    """Give AI summaries to earlier items that ran out of time (newest first)."""
    if not (cfg.summarize and os.environ.get("ANTHROPIC_API_KEY")):
        return 0
    if deadline is not None and time.monotonic() > deadline:
        return 0
    todo = [r for r in sorted(archive.records, key=lambda r: r["date"], reverse=True)
            if not (r.get("summary") or {}).get("ai") and r["topic"] in name_of][:limit]
    if not todo:
        return 0
    papers = [to_paper(r) for r in todo]
    summarize_all([(p, name_of[r["topic"]]) for p, r in zip(papers, todo)], enabled=True,
                  model=cfg.model, language=cfg.language, deadline=deadline)
    fixed = 0
    for p, r in zip(papers, todo):
        if p.summary.get("ai"):
            r["summary"] = p.summary
            fixed += 1
    log.info("filled in %d earlier summaries", fixed)
    return fixed


def notify(args: argparse.Namespace) -> bool:
    """Send today's email and Discord post, each at most once a day. False if one failed."""
    cfg = load_config(args.config)
    archive, today = Archive(cfg.archive_path), datetime.now(timezone.utc).date()
    runs = RunLog(cfg.runs_path)
    channels = [("email", send_daily)]
    if args.cmd == "notify":
        channels.append(("discord", post_daily))
    ok = True
    for job, channel in channels:      # one channel failing must not stop the others
        if runs.done(job, today) and not getattr(args, "force", False):
            log.info("%s: already sent today", job)
            continue
        try:
            result = channel(cfg, archive, today, args.dry_run)
        except Exception as exc:       # not marked as done, so a later run tries again
            log.error("%s failed: %s", job, exc)
            ok = False
            continue
        if result is not None and not args.dry_run:   # None: not set up yet
            runs.mark(job, today)
    return ok


def list_presets() -> None:
    by_field: dict[str, list[tuple[str, dict]]] = {}
    for key, p in load_presets().items():
        by_field.setdefault(p.get("field", "Other"), []).append((key, p))
    for fld, items in by_field.items():
        print(f"\n{fld}")
        for key, p in items:
            src = p.get("source", "arxiv")
            where = p.get("categories") or [u.split("/")[2] for u in p.get("feeds", [])]
            print(f"  {key:<24} {p['name']}  [{src}: {', '.join(where)}]")


def main() -> None:
    parser = argparse.ArgumentParser(prog="radar", description="Weekly research digest")
    parser.add_argument("-v", "--verbose", action="store_true")
    sub = parser.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="build this week's digest")
    r.add_argument("--config", default="config.yaml")
    r.add_argument("--no-summary", action="store_true", help="skip AI summaries")
    r.add_argument("--offline", metavar="DIR",
                   help="read saved responses (arxiv.xml, biorxiv.json, medrxiv.json) from DIR")
    r.add_argument("--dry-run", action="store_true", help="do not update state/seen.json")
    r.add_argument("--skip-if-done", action="store_true",
                   help="do nothing if today's digest was already built (for scheduled runs)")
    r.add_argument("--max-minutes", type=float, default=0, metavar="M",
                   help="finish and save within about M minutes (0 = no limit)")
    r.add_argument("--backfill", type=int, default=0, metavar="N",
                   help="also fill the website for the past N days (one-time, e.g. 7)")
    sub.add_parser("presets", help="list built-in topic presets")
    e = sub.add_parser("email", help="email today's papers to readers who turned on daily email")
    e.add_argument("--config", default="config.yaml")
    e.add_argument("--dry-run", action="store_true", help="list the emails without sending")
    e.add_argument("--force", action="store_true", help="send even if already sent today")
    n = sub.add_parser("notify", help="send today's daily email and Discord post")
    n.add_argument("--config", default="config.yaml")
    n.add_argument("--dry-run", action="store_true", help="show what would be sent")
    n.add_argument("--force", action="store_true", help="send even if already sent today")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO,
                        format="%(levelname)s %(message)s")
    if args.cmd == "run":
        run(args)
    elif args.cmd == "presets":
        list_presets()
    elif args.cmd in ("email", "notify"):
        if not notify(args):
            raise SystemExit(1)

if __name__ == "__main__":
    main()
