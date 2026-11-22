"""Command line entry point.

    python -m radar run                         # fetch, rank, summarize, write digest
    python -m radar run --no-summary            # skip the AI summaries
    python -m radar run --offline tests/fixtures --dry-run   # test without network
    python -m radar presets                     # list the built-in topic presets
"""

from __future__ import annotations

import argparse
import logging
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from . import sources
from .config import load_config, load_presets
from .digest import TopicStats, render
from .models import Paper
from .rank import assign_unique, score_papers
from .state import SeenState
from .summarize import summarize_all

log = logging.getLogger("radar")


def run(args: argparse.Namespace) -> Path:
    cfg = load_config(args.config)
    if args.no_summary:
        cfg.summarize = False

    now = datetime.now(timezone.utc)
    # Look back a few extra days: arXiv and bioRxiv announce papers with a delay, so a
    # paper submitted just before last week's run may only have appeared afterwards.
    # The seen-state makes sure nothing is recommended twice.
    start = now - timedelta(days=cfg.days + cfg.overlap_days)
    state = SeenState(cfg.state_path)
    offline = sources.load_offline(args.offline) if args.offline else None

    ranked: dict[str, list[Paper]] = {}
    stats: dict[str, TopicStats] = {}
    for i, topic in enumerate(cfg.topics):
        st = stats[topic.slug] = TopicStats()
        try:
            if offline is not None:
                cands = sources.offline_candidates(topic, offline)
                seeds: list[Paper] = []
            else:
                if i:
                    time.sleep(3)  # be polite to the APIs
                log.info("[%s] fetching from %s", topic.slug, topic.source)
                cands = sources.fetch(topic, start, now, cfg.max_per_topic)
                seeds = sources.fetch_seeds(topic)
            new = [p for p in cands if not state.is_seen(p.uid)]
            ranked[topic.slug] = score_papers(new, topic, [s.text for s in seeds])
            st.fetched, st.new = len(cands), len(new)
        except Exception as exc:  # one failing topic should not kill the digest
            log.error("[%s] failed: %s", topic.slug, exc)
            st.error = str(exc)
            ranked[topic.slug] = []

    chosen = assign_unique(ranked, {t.slug: t.top_k for t in cfg.topics}, cfg.min_score)
    name_of = {t.slug: t.display_name(cfg.language) for t in cfg.topics}
    pairs = [(p, name_of[slug]) for slug, ps in chosen.items() for p in ps]
    topic_of = {p.uid: name for p, name in pairs}

    summarize_all(pairs, enabled=cfg.summarize, model=cfg.model, language=cfg.language)

    all_chosen = [p for p, _ in pairs]
    must_read = sorted(all_chosen, key=lambda p: p.score, reverse=True)[:cfg.must_read]
    md = render(chosen, cfg.topics, must_read, stats,
                (now - timedelta(days=cfg.days), now), topic_of, cfg.language)

    out_dir = Path(cfg.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{now:%Y-%m-%d}.md"
    out.write_text(md, encoding="utf-8")
    (out_dir / "latest.md").write_text(md, encoding="utf-8")
    log.info("wrote %s (%d papers)", out, len(all_chosen))

    if not args.dry_run:
        state.mark([p.uid for p in all_chosen], now.date())
        state.prune(now.date())
        state.save()
    return out


def list_presets() -> None:
    by_field: dict[str, list[tuple[str, dict]]] = {}
    for key, p in load_presets().items():
        by_field.setdefault(p.get("field", "Other"), []).append((key, p))
    for fld, items in by_field.items():
        print(f"\n{fld}")
        for key, p in items:
            src = p.get("source", "arxiv")
            print(f"  {key:<24} {p['name']}  [{src}: {', '.join(p['categories'])}]")


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
    sub.add_parser("presets", help="list built-in topic presets")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO,
                        format="%(levelname)s %(message)s")
    if args.cmd == "run":
        run(args)
    elif args.cmd == "presets":
        list_presets()


if __name__ == "__main__":
    main()
