"""Load and validate config.yaml."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class Topic:
    name: str                      # display name, e.g. "ML 理论"
    slug: str                      # short id, e.g. "ml-theory"
    categories: list[str]          # arXiv categories, e.g. ["stat.ML", "cs.LG"]
    interest: str                  # free-text description used for ranking (English works best)
    keywords: list[str] = field(default_factory=list)   # server-side filter + ranking boost
    seed_ids: list[str] = field(default_factory=list)   # arXiv ids of papers you liked
    top_k: int = 3


@dataclass
class Config:
    topics: list[Topic]
    days: int = 7
    overlap_days: int = 3          # extra lookback so late-announced papers are not missed
    max_per_topic: int = 600       # cap on papers fetched per topic
    min_score: float = 0.05        # below this, a paper is not worth recommending
    must_read: int = 2
    summarize: bool = True
    model: str = "claude-haiku-5-5"
    output_dir: str = "digests"
    state_path: str = "state/seen.json"


def load_config(path: str | Path) -> Config:
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    topics_raw = raw.pop("topics", None)
    if not topics_raw:
        raise ValueError("config must define at least one topic")

    topics = []
    seen_slugs = set()
    for t in topics_raw:
        topic = Topic(**t)
        if not topic.categories:
            raise ValueError(f"topic {topic.slug!r} has no categories")
        if topic.slug in seen_slugs:
            raise ValueError(f"duplicate topic slug {topic.slug!r}")
        seen_slugs.add(topic.slug)
        topics.append(topic)

    return Config(topics=topics, **raw)
