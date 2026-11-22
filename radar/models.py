"""The Paper record shared by all sources."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Paper:
    uid: str                       # unique across sources, e.g. "arxiv:2611.01234"
    source: str                    # "arxiv", "biorxiv" or "medrxiv"
    label: str                     # human-readable id, e.g. "arXiv:2611.01234v2"
    title: str
    authors: list[str]
    abstract: str
    primary_category: str
    categories: list[str]
    published: datetime
    url: str
    pdf_url: str = ""
    version: int = 0
    # filled in later by the pipeline
    score: float = 0.0
    matched_keywords: list[str] = field(default_factory=list)
    summary: dict = field(default_factory=dict)

    @property
    def text(self) -> str:
        return f"{self.title}. {self.abstract}"


def matched_keywords(paper: Paper, keywords: list[str]) -> list[str]:
    """Keywords that appear as whole words (so "Lean" does not match "clean")."""
    text = paper.text.lower()
    return [k for k in keywords
            if re.search(r"(?<!\w)" + re.escape(k.lower()) + r"(?!\w)", text)]
