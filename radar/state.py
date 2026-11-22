"""Remember which papers were already recommended, so digests do not repeat.

Stored as a small JSON file ({uid: "YYYY-MM-DD"}) so it diffs nicely in git.
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
            raw = json.loads(self.path.read_text(encoding="utf-8"))
            # v0.1 stored bare arXiv ids; v0.2 prefixes the source ("arxiv:...")
            self.seen = {(k if ":" in k else f"arxiv:{k}"): v for k, v in raw.items()}

    def is_seen(self, uid: str) -> bool:
        return uid in self.seen

    def mark(self, uids: list[str], day: date) -> None:
        for u in uids:
            self.seen.setdefault(u, day.isoformat())

    def prune(self, today: date, keep_days: int = 120) -> None:
        cutoff = (today - timedelta(days=keep_days)).isoformat()
        self.seen = {k: v for k, v in self.seen.items() if v >= cutoff}

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.seen, indent=1, sort_keys=True) + "\n",
                             encoding="utf-8")
