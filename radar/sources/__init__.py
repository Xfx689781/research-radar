"""Paper sources. Each topic in the config picks one source."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from ..models import Paper, matched_keywords
from . import arxiv, biorxiv, rss

SOURCES = ("arxiv", "biorxiv", "medrxiv", "rss")


def fetch(topic, start: datetime, end: datetime, max_results: int) -> list[Paper]:
    """All new papers for a topic between start and end."""
    if topic.source == "arxiv":
        query = arxiv.build_query(topic.categories, topic.keywords, start, end)
        return arxiv.search(query, max_results=max_results)
    if topic.source == "rss":
        return rss.search(topic.feeds, topic.keywords, start, end)[:max_results]
    return biorxiv.search(topic.source, topic.categories, topic.keywords,
                          start.date(), end.date(), max_results=max_results)


def fetch_seeds(topic) -> list[Paper]:
    """Papers the user listed as examples of what they like."""
    if not topic.seed_ids or topic.source == "rss":
        return []
    if topic.source == "arxiv":
        return arxiv.fetch_by_ids(topic.seed_ids)
    return biorxiv.fetch_by_dois(topic.source, topic.seed_ids)


# ---------------------------------------------------------------- offline mode

def load_offline(directory: str | Path) -> dict[str, list[Paper]]:
    """Read saved responses (arxiv.xml, biorxiv.json, medrxiv.json, rss.xml) from a folder."""
    d = Path(directory)
    out: dict[str, list[Paper]] = {s: [] for s in SOURCES}
    if (d / "arxiv.xml").exists():
        out["arxiv"] = arxiv.parse_feed((d / "arxiv.xml").read_text(encoding="utf-8"))
    for server in ("biorxiv", "medrxiv"):
        f = d / f"{server}.json"
        if f.exists():
            data = json.loads(f.read_text(encoding="utf-8"))
            out[server] = biorxiv.latest_versions(biorxiv.parse_collection(data, server))
    out["rss"] = []
    if (d / "rss.xml").exists():
        out["rss"] = rss.parse_feed((d / "rss.xml").read_text(encoding="utf-8"),
                                    "https://news.example.org/feed")
    return out


def offline_candidates(topic, offline: dict[str, list[Paper]]) -> list[Paper]:
    """Mimic the server-side filters on saved data."""
    papers = offline.get(topic.source, [])
    if topic.source == "rss":
        return [p for p in papers if not topic.keywords or matched_keywords(p, topic.keywords)]
    if topic.source == "arxiv":
        papers = [p for p in papers if set(p.categories) & set(topic.categories)]
        if topic.keywords:
            papers = [p for p in papers if matched_keywords(p, topic.keywords)]
        return papers
    return biorxiv.filter_papers(papers, topic.categories, topic.keywords)
