"""Which daily jobs have already been done today (state/runs.json).

The workflow is scheduled several times a day in case GitHub skips a run.
This file lets later runs see that the digest was already built, or the email
already sent, and do nothing instead of repeating it.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path


class RunLog:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.data: dict[str, str] = {}
        if self.path.exists():
            self.data = json.loads(self.path.read_text(encoding="utf-8"))

    def done(self, job: str, day: date) -> bool:
        return self.data.get(job) == day.isoformat()

    def mark(self, job: str, day: date) -> None:
        self.data[job] = day.isoformat()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, indent=1, sort_keys=True) + "\n", encoding="utf-8")
