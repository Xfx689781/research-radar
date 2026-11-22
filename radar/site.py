"""Export the data the web app reads (docs/data/*.json).

The website is a single static page (docs/index.html). Each run writes:

  data/topics.json          every topic: name, field, description, papers added today
  data/topics/<slug>.json   one topic's recent papers with their summaries
  data/site.json            public site settings (title, optional login settings)

The page loads topics.json, lets the reader pick topics, then loads only the
files of the topics they picked.
"""

from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path

from .archive import Archive
from .config import Config

PAPER_FIELDS = ("uid", "title", "url", "authors", "label", "primary_category", "date",
                "summary", "abstract", "source")


def _write(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def export_site(site_dir: Path, cfg: Config, archive: Archive, today: date) -> list[Path]:
    data_dir = site_dir / "data"
    since = today - timedelta(days=cfg.feed_days)
    written = []

    fields: list[str] = []
    topics = []
    for t in cfg.topics:
        fld = t.field or "Other"
        if fld not in fields:
            fields.append(fld)
        topics.append({
            "slug": t.slug,
            "name": t.display_name(cfg.language),
            "field": fld,
            "description": " ".join(t.interest.split()),
            "source": t.source,
            "categories": t.categories,
            "new_today": archive.count_on(t.slug, today),
        })

        papers = [{k: r.get(k) for k in PAPER_FIELDS} for r in archive.for_topic(t.slug, since)]
        path = data_dir / "topics" / f"{t.slug}.json"
        _write(path, {"slug": t.slug, "updated": today.isoformat(), "papers": papers})
        written.append(path)

    index = data_dir / "topics.json"
    _write(index, {"updated": today.isoformat(), "language": cfg.language,
                   "fields": fields, "topics": topics})
    settings = data_dir / "site.json"
    _write(settings, {"title": cfg.site_title,
                      "supabase_url": cfg.supabase_url,
                      "supabase_anon_key": cfg.supabase_anon_key})
    return [index, settings, *written]
