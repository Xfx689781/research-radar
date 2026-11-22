"""Optional: short Chinese summaries written by Claude, based only on the abstract.

If ANTHROPIC_API_KEY is not set (or the `anthropic` package is missing), the
digest still works: it falls back to the first sentence of the abstract.
"""

from __future__ import annotations

import json
import logging
import os
import re

from .arxiv_client import Paper

log = logging.getLogger(__name__)

DIFFICULTIES = {"入门", "中等", "研究级"}

SYSTEM = (
    "你是一位帮数学系本科生筛选论文的研究助理。只根据给出的标题和摘要写，"
    "不要编造摘要里没有的结论、数字、方法或作者信息；摘要信息不足时如实说明。"
    "用中文写，专业术语保留英文原词。语气克制，不要夸大论文的意义。"
)

PROMPT = """方向：{topic}
标题：{title}
摘要：{abstract}

只输出一个 JSON 对象，不要输出其他文字。字段：
- "one_liner": 一句话说明这篇论文做了什么
- "why": 2 到 3 句，为什么值得关注、可能和哪些方向有联系（不确定就说不确定）
- "background": 读懂核心思想需要的数学背景（简短列举）
- "difficulty": "入门"、"中等"、"研究级" 三者之一
"""


def first_sentence(text: str, limit: int = 300) -> str:
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    s = m.group(1) if m else text
    return s if len(s) <= limit else s[:limit].rstrip() + "…"


def fallback_summary(paper: Paper) -> dict:
    return {"one_liner": first_sentence(paper.abstract), "why": "", "background": "",
            "difficulty": "", "ai": False}


def parse_summary(text: str) -> dict:
    """Extract the JSON object from the model's reply and validate it."""
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end <= start:
        raise ValueError("no JSON object in reply")
    data = json.loads(text[start:end + 1])
    out = {k: str(data.get(k, "")).strip() for k in ("one_liner", "why", "background", "difficulty")}
    if not out["one_liner"]:
        raise ValueError("empty one_liner")
    if out["difficulty"] not in DIFFICULTIES:
        out["difficulty"] = ""
    out["ai"] = True
    return out


def summarize_all(papers_with_topic: list[tuple[Paper, str]], enabled: bool, model: str) -> None:
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
                max_tokens=700,
                system=SYSTEM,
                messages=[{"role": "user", "content": PROMPT.format(
                    topic=topic_name, title=paper.title, abstract=paper.abstract)}],
            )
            text = "".join(getattr(b, "text", "") for b in msg.content)
            paper.summary = parse_summary(text)
        except Exception as exc:  # one bad reply should not break the digest
            log.warning("summary failed for %s: %s", paper.arxiv_id, exc)
            paper.summary = fallback_summary(paper)
