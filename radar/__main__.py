"""Command line entry point.

    python -m radar run                    # fetch, rank, summarize, write digest
    python -m radar run --no-summary       # skip the AI summaries
    python -m radar run --offline FEED.xml --dry-run   # test without network
"""

from __future__ import annotations

import argparse
import logging
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from .arxiv_client import Paper, build_query, fetch_by_ids, parse_feed, search
from .config import Config, Topic, load_config
from .digest import TopicStats, render
from .rank import assign_unique, matched_keywords, score_papers
from .state import SeenState
from .summarize import summarize_all

log = logging.getLogger("radar")


def candidates_for(topic: Topic, cfg: Config, start: datetime, end: datetime,
                   offline: list[Paper] | None) -> list[Paper]:
    if offline is not None:
        # mimic the server-side filter: category match, plus a keyword if any are set
        ps = [p for p in offline if set(p.categories) & set(topic.categories)]
        if topic.keywords:
            ps = [p for p in ps if matched_keywords(p, topic.keywords)]
        return ps
    query = build_query(topic.categories, topic.keywords, start, end)
    log.info("[%s] %s", topic.slug, query)
    return search(query, max_results=cfg.max_per_topic)


def run(args: argparse.Namespace) -> Path:
    cfg = load_config(args.config)
    if args.no_summary:
        cfg.summarize = False

    now = datetime.now(timezone.utc)
    # Look back a few extra days: arXiv announces papers with a delay, so a paper
    # submitted just before last week's run may only have appeared afterwards.
    # The seen-state makes sure nothing is recommended twice.
    start = now - timedelta(days=cfg.days + cfg.overlap_days)
    state = SeenState(cfg.state_path)
    offline = parse_feed(Path(args.offline).read_text(encoding="utf-8")) if args.offline else None

    ranked: dict[str, list[Paper]] = {}
    stats: dict[str, TopicStats] = {}
    for i, topic in enumerate(cfg.topics):
        st = stats[topic.slug] = TopicStats()
        try:
            if i and offline is None:
                time.sleep(3)  # be polite to the arXiv API
            cands = candidates_for(topic, cfg, start, now, offline)
            new = [p for p in cands if not state.is_seen(p.arxiv_id)]
            seeds = fetch_by_ids(topic.seed_ids) if topic.seed_ids and offline is None else []
            ranked[topic.slug] = score_papers(new, topic, [s.text for s in seeds])
            st.fetched, st.new = len(cands), len(new)
        except Exception as exc:  # one failing topic should not kill the digest
            log.error("[%s] failed: %s", topic.slug, exc)
            st.error = str(exc)
            ranked[topic.slug] = []

    chosen = assign_unique(ranked, {t.slug: t.top_k for t in cfg.topics}, cfg.min_score)
    name_of = {t.slug: t.name for t in cfg.topics}
    pairs = [(p, name_of[slug]) for slug, ps in chosen.items() for p in ps]
    topic_of = {p.arxiv_id: name for p, name in pairs}

    summarize_all(pairs, enabled=cfg.summarize, model=cfg.model)

    all_chosen = [p for p, _ in pairs]
    must_read = sorted(all_chosen, key=lambda p: p.score, reverse=True)[:cfg.must_read]
    md = render(chosen, cfg.topics, must_read, stats,
                (now - timedelta(days=cfg.days), now), topic_of)

    out_dir = Path(cfg.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{now:%Y-%m-%d}.md"
    out.write_text(md, encoding="utf-8")
    (out_dir / "latest.md").write_text(md, encoding="utf-8")
    log.info("wrote %s (%d papers)", out, len(all_chosen))

    if not args.dry_run:
        state.mark([p.arxiv_id for p in all_chosen], now.date())
        state.prune(now.date())
        state.save()
    return out


def main() -> None:
    parser = argparse.ArgumentParser(prog="radar", description="Weekly arXiv research digest")
    sub = parser.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="build this week's digest")
    r.add_argument("--config", default="config.yaml")
    r.add_argument("--no-summary", action="store_true", help="skip AI summaries")
    r.add_argument("--offline", metavar="FEED.xml", help="read papers from a saved arXiv feed")
    r.add_argument("--dry-run", action="store_true", help="do not update state/seen.json")
    r.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO,
                        format="%(levelname)s %(message)s")
    if args.cmd == "run":
        run(args)


if __name__ == "__main__":
    main()
