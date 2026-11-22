"""Optional: short summaries written by Claude, based only on the abstract.

If ANTHROPIC_API_KEY is not set (or the `anthropic` package is missing), the
digest still works: it falls back to the first sentence of the abstract.
"""

from __future__ import annotations

import json
import logging
import os
import re

from .i18n import DIFFICULTIES, SYSTEM_PROMPT, USER_PROMPT
from .models import Paper

log = logging.getLogger(__name__)


def first_sentence(text: str, limit: int = 300) -> str:
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    s = m.group(1) if m else text
    return s if len(s) <= limit else s[:limit].rstrip() + "…"


def fallback_summary(paper: Paper) -> dict:
    return {"one_liner": first_sentence(paper.abstract), "plain": "", "why": "",
            "background": "", "difficulty": "", "ai": False}


def parse_summary(text: str, language: str = "en") -> dict:
    """Extract the JSON object from the model's reply and validate it."""
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end <= start:
        raise ValueError("no JSON object in reply")
    data = json.loads(text[start:end + 1])
    out = {k: str(data.get(k, "")).strip()
           for k in ("one_liner", "plain", "why", "background", "difficulty")}
    if not out["one_liner"]:
        raise ValueError("empty one_liner")
    if out["difficulty"].lower() not in {d.lower() for d in DIFFICULTIES[language]}:
        out["difficulty"] = ""
    out["ai"] = True
    return out


def summarize_all(papers_with_topic: list[tuple[Paper, str]], enabled: bool, model: str,
                  language: str = "en") -> None:
    """Fill paper.summary for each (paper, topic_name) pair, in place."""
    client = None
    if enabled and os.environ.get("ANTHROPIC_API_KEY"):
        try:
            import anthropic
            client = anthropic.Anthropic()
        except ImportError:
            log.warning("`anthropic` package not installed; using abstract fallback")
    elif enabled:
        log.info("ANTHROPIC_API_KEY not set; using abstract fallback")

    for paper, topic_name in papers_with_topic:
        if client is None:
            paper.summary = fallback_summary(paper)
            continue
        try:
            msg = client.messages.create(
                model=model,
                max_tokens=900,
                system=SYSTEM_PROMPT[language],
                messages=[{"role": "user", "content": USER_PROMPT[language].format(
                    topic=topic_name, title=paper.title, abstract=paper.abstract)}],
            )
            text = "".join(getattr(b, "text", "") for b in msg.content)
            paper.summary = parse_summary(text, language)
        except Exception as exc:  # one bad reply should not break the digest
            log.warning("summary failed for %s: %s", paper.uid, exc)
            paper.summary = fallback_summary(paper)
