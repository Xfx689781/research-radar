"""Short summaries written by Claude, based only on the abstract (or news teaser).

The model answers through a forced tool call, so the reply arrives as structured
fields rather than free text that has to be parsed.

If ANTHROPIC_API_KEY is not set (or the `anthropic` package is missing), the
digest still works: it falls back to the first sentence of the abstract.
"""

from __future__ import annotations

import json
import logging
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor

from .i18n import DIFFICULTIES, KIND, SYSTEM_PROMPT, USER_PROMPT
from .models import Paper

log = logging.getLogger(__name__)

WORKERS = 4
ATTEMPTS = 3
FIELDS = ("one_liner", "plain", "why", "background", "difficulty")


def tool_spec(language: str) -> dict:
    text = {"type": "string"}
    return {
        "name": "record_summary",
        "description": "Record the brief for one paper or news item.",
        "input_schema": {
            "type": "object",
            "properties": {
                "one_liner": text, "plain": text, "why": text, "background": text,
                "difficulty": {"type": "string", "enum": list(DIFFICULTIES[language])},
            },
            "required": list(FIELDS),
        },
    }


def first_sentence(text: str, limit: int = 300) -> str:
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    s = m.group(1) if m else text
    return s if len(s) <= limit else s[:limit].rstrip() + "…"


def fallback_summary(paper: Paper) -> dict:
    return {"one_liner": first_sentence(paper.abstract), "plain": "", "why": "",
            "background": "", "difficulty": "", "ai": False}


def validate_summary(data: dict, language: str = "en") -> dict:
    out = {k: str(data.get(k, "") or "").strip() for k in FIELDS}
    if not out["one_liner"] and not out["plain"]:
        raise ValueError("empty summary")
    if out["difficulty"].lower() not in {d.lower() for d in DIFFICULTIES[language]}:
        out["difficulty"] = ""
    out["ai"] = True
    return out


def parse_summary(text: str, language: str = "en") -> dict:
    """Fallback for a plain-text reply: extract a JSON object and validate it."""
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end <= start:
        raise ValueError("no JSON object in reply")
    return validate_summary(json.loads(text[start:end + 1]), language)


def summary_from_message(msg, language: str) -> dict:
    for block in msg.content:
        if getattr(block, "type", "") == "tool_use":
            return validate_summary(dict(block.input), language)
    text = "".join(getattr(b, "text", "") or "" for b in msg.content)
    try:
        return parse_summary(text, language)
    except Exception as exc:
        raise ValueError(f"{exc}; stop_reason={getattr(msg, 'stop_reason', '?')}; "
                         f"reply starts {text[:120]!r}") from exc


def summarize_all(papers_with_topic: list[tuple[Paper, str]], enabled: bool, model: str,
                  language: str = "en", deadline: float | None = None) -> None:
    """Fill paper.summary for each (paper, topic_name) pair, in place.

    deadline is a time.monotonic() value: once it passes, the remaining items get the
    plain fallback instead of an AI summary, so the run always finishes and saves its
    work. Items without an AI summary are picked up again by later runs.
    """
    client = None
    if enabled and os.environ.get("ANTHROPIC_API_KEY"):
        try:
            import anthropic
            client = anthropic.Anthropic(max_retries=4)
        except ImportError:
            log.warning("`anthropic` package not installed; using abstract fallback")
    elif enabled:
        log.info("ANTHROPIC_API_KEY not set; using abstract fallback")

    if client is None:
        for paper, _ in papers_with_topic:
            paper.summary = fallback_summary(paper)
        return

    tool = tool_spec(language)

    def one(paper: Paper, topic_name: str) -> None:
        if deadline is not None and time.monotonic() > deadline:
            paper.summary = fallback_summary(paper)
            return
        kind = KIND[language]["news" if paper.source == "rss" else "paper"]
        prompt = USER_PROMPT[language].format(topic=topic_name, kind=kind, title=paper.title,
                                              abstract=paper.abstract or "(no text available)")
        for attempt in range(1, ATTEMPTS + 1):
            try:
                msg = client.messages.create(
                    model=model, max_tokens=1200, system=SYSTEM_PROMPT[language],
                    tools=[tool], tool_choice={"type": "tool", "name": tool["name"]},
                    messages=[{"role": "user", "content": prompt}])
                paper.summary = summary_from_message(msg, language)
                return
            except Exception as exc:  # one bad reply should not break the digest
                if attempt == ATTEMPTS:
                    log.warning("summary failed for %s: %s", paper.uid, exc)
                time.sleep(2 * attempt)
        paper.summary = fallback_summary(paper)

    # A few requests at a time: much faster than one by one, gentle on rate limits.
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        list(pool.map(lambda pt: one(*pt), papers_with_topic))
    ok = sum(1 for p, _ in papers_with_topic if p.summary.get("ai"))
    log.info("AI summaries: %d of %d", ok, len(papers_with_topic))
