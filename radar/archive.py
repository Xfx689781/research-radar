"""A running archive of every recommended paper, with its summary.

Topic pages and feeds are rebuilt from this file on every run, so each topic
page can show the last few weeks of papers, not just today's.
Stored as JSON Lines (one paper per line), which diffs nicely in git.
"""

from __future__ import annotations

import json
from dataclasses import fields
from datetime import date, datetime, timedelta
from pathlib import Path

from .models import Paper

_KEEP = ("uid", "source", "label", "title", "authors", "abstract", "primary_category",
         "categories", "url", "pdf_url", "version", "score", "summary")


def to_record(paper: Paper, topic_slug: str, day: date) -> dict:
    rec = {k: getattr(paper, k) for k in _KEEP}
    rec["published"] = paper.published.isoformat()
    rec["topic"] = topic_slug
    rec["date"] = day.isoformat()
    return rec


def to_paper(rec: dict) -> Paper:
    names = {f.name for f in fields(Paper)}
    data = {k: v for k, v in rec.items() if k in names}
    data["published"] = datetime.fromisoformat(rec["published"])
    return Paper(**data)


class Archive:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.records: list[dict] = []
        if self.path.exists():
            for line in self.path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    self.records.append(json.loads(line))

    def add(self, papers_by_topic: dict[str, list[Paper]], day: date) -> None:
        # a re-run on the same day replaces that day's entries
        self.records = [r for r in self.records if r["date"] != day.isoformat()]
        for slug, papers in papers_by_topic.items():
            self.records += [to_record(p, slug, day) for p in papers]

    def prune(self, today: date, keep_days: int) -> None:
        cutoff = (today - timedelta(days=keep_days)).isoformat()
        self.records = [r for r in self.records if r["date"] >= cutoff]

    def for_topic(self, slug: str, since: date | None = None) -> list[dict]:
        """Records of one topic, newest day first, best score first within a day."""
        rs = [r for r in self.records if r["topic"] == slug
              and (since is None or r["date"] >= since.isoformat())]
        return sorted(rs, key=lambda r: (r["date"], r.get("score", 0)), reverse=True)

    def count_on(self, slug: str, day: date) -> int:
        return sum(1 for r in self.records if r["topic"] == slug and r["date"] == day.isoformat())

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        lines = [json.dumps(r, ensure_ascii=False, sort_keys=True) for r in self.records]
        self.path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
