"""Remember which papers were already recommended, so digests do not repeat.

Stored as a small JSON file ({arxiv_id: "YYYY-MM-DD"}) so it diffs nicely in git.
"""

from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path


class SeenState:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.seen: dict[str, str] = {}
        if self.path.exists():
            self.seen = json.loads(self.path.read_text(encoding="utf-8"))

    def is_seen(self, arxiv_id: str) -> bool:
        return arxiv_id in self.seen

    def mark(self, arxiv_ids: list[str], day: date) -> None:
        for i in arxiv_ids:
            self.seen.setdefault(i, day.isoformat())

    def prune(self, today: date, keep_days: int = 120) -> None:
        cutoff = (today - timedelta(days=keep_days)).isoformat()
        self.seen = {k: v for k, v in self.seen.items() if v >= cutoff}

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.seen, indent=1, sort_keys=True) + "\n",
                             encoding="utf-8")
