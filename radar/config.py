"""Load config.yaml, expanding topic presets from radar/presets.yaml."""

from __future__ import annotations

from dataclasses import dataclass, field, fields
from pathlib import Path

import yaml

PRESETS_PATH = Path(__file__).with_name("presets.yaml")
LANGUAGES = ("en", "zh")
SOURCES = ("arxiv", "biorxiv", "medrxiv")


@dataclass
class Topic:
    name: str                      # display name, e.g. "Probability"
    slug: str                      # short id, e.g. "probability"
    categories: list[str]          # arXiv categories, or bioRxiv/medRxiv subject areas
    interest: str                  # free-text description used for ranking (English works best)
    source: str = "arxiv"          # "arxiv", "biorxiv" or "medrxiv"
    keywords: list[str] = field(default_factory=list)   # filter + ranking boost
    seed_ids: list[str] = field(default_factory=list)   # arXiv ids / bioRxiv DOIs you liked
    primary_only: bool = False     # arXiv: keep only papers whose primary category is listed
    top_k: int = 3
    name_zh: str = ""
    field: str = ""                # e.g. "Mathematics"; only used for documentation

    def display_name(self, language: str) -> str:
        return self.name_zh if language == "zh" and self.name_zh else self.name


@dataclass
class Config:
    topics: list[Topic]
    language: str = "en"
    days: int = 7
    overlap_days: int = 3          # extra lookback so late-announced papers are not missed
    max_per_topic: int = 600       # cap on papers fetched per topic
    min_score: float = 0.03        # below this, a paper is not worth recommending
    must_read: int = 3
    top_k_per_topic: int | None = None   # if set, overrides every topic's top_k
    include_revisions: bool = False      # bioRxiv/medRxiv: also show new versions of old preprints
    summarize: bool = True
    model: str = "claude-haiku-5-5"
    output_dir: str = "docs/digests"     # daily Markdown digests (readable on GitHub)
    site_dir: str | None = "docs"        # the website; its data goes to <site_dir>/data
    state_path: str = "state/seen.json"
    archive_path: str = "state/archive.jsonl"
    archive_days: int = 90               # how long recommended papers are kept
    feed_days: int = 30                  # how far back each topic's feed goes on the website
    site_title: str = "Research Radar"
    supabase_url: str = ""               # optional login; see README "Accounts"
    supabase_anon_key: str = ""          # public by design; access is limited by row-level security


def load_presets() -> dict[str, dict]:
    return yaml.safe_load(PRESETS_PATH.read_text(encoding="utf-8"))


_TOPIC_FIELDS = {f.name for f in fields(Topic)}


def resolve_topic(item, presets: dict[str, dict]) -> Topic:
    """A topic entry can be a preset key, a preset with overrides, or a full definition."""
    if isinstance(item, str):
        item = {"preset": item}
    if not isinstance(item, dict):
        raise ValueError(f"cannot read topic entry {item!r}")

    item = dict(item)
    key = item.pop("preset", None)
    data: dict = {}
    if key is not None:
        if key not in presets:
            raise ValueError(f"unknown preset {key!r}; available: {', '.join(sorted(presets))}")
        data = {"slug": key, **presets[key]}
    data.update(item)

    unknown = set(data) - _TOPIC_FIELDS
    if unknown:
        raise ValueError(f"topic {data.get('slug', '?')!r}: unknown field(s) {sorted(unknown)}")
    topic = Topic(**data)
    if not topic.categories:
        raise ValueError(f"topic {topic.slug!r} has no categories")
    if topic.source not in SOURCES:
        raise ValueError(f"topic {topic.slug!r}: source must be one of {SOURCES}")
    return topic


def load_config(path: str | Path) -> Config:
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    items = raw.pop("topics", None)
    if not items:
        raise ValueError("config must list at least one topic")

    presets = load_presets()
    topics = [resolve_topic(it, presets) for it in items]
    slugs = [t.slug for t in topics]
    dupes = {s for s in slugs if slugs.count(s) > 1}
    if dupes:
        raise ValueError(f"duplicate topic slug(s): {sorted(dupes)}")

    cfg = Config(topics=topics, **raw)
    if cfg.language not in LANGUAGES:
        raise ValueError(f"language must be one of {LANGUAGES}")
    if cfg.top_k_per_topic is not None:
        for t in cfg.topics:
            t.top_k = cfg.top_k_per_topic
    return cfg
