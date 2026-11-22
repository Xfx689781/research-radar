"""Render the weekly digest as Markdown."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .arxiv_client import Paper
from .config import Topic


@dataclass
class TopicStats:
    fetched: int = 0
    new: int = 0
    error: str = ""


def _authors(names: list[str], n: int = 3) -> str:
    return ", ".join(names) if len(names) <= n else ", ".join(names[:n]) + " 等"


def _entry(p: Paper) -> str:
    s = p.summary or {}
    lines = [
        f"### [{p.title}]({p.url})",
        f"*{_authors(p.authors)}* · `{p.primary_category}` · arXiv:{p.arxiv_id}{p.version}"
        f" · 相关度 {p.score:.2f}",
        "",
        f"- **一句话**：{s.get('one_liner', '')}" + ("" if s.get("ai") else "（摘要首句，未生成 AI 摘要）"),
    ]
    if s.get("why"):
        lines.append(f"- **为什么值得看**：{s['why']}")
    if s.get("background") or s.get("difficulty"):
        bg = s.get("background", "")
        diff = f" · 难度：{s['difficulty']}" if s.get("difficulty") else ""
        lines.append(f"- **需要的背景**：{bg}{diff}")
    if p.matched_keywords:
        lines.append("- 命中关键词：" + "、".join(p.matched_keywords))
    lines += ["", "<details><summary>原始摘要</summary>", "", p.abstract, "", "</details>", ""]
    return "\n".join(lines)


def render(chosen: dict[str, list[Paper]], topics: list[Topic], must_read: list[Paper],
           stats: dict[str, TopicStats], window: tuple[datetime, datetime],
           topic_of: dict[str, str]) -> str:
    start, end = window
    out = [
        f"# 研究进展简报 · {end:%Y-%m-%d}",
        "",
        f"覆盖 arXiv 提交时间约 {start:%Y-%m-%d} 至 {end:%Y-%m-%d}（UTC）。",
        "",
        "> 相关度 = 和你的兴趣描述的 TF-IDF 余弦相似度 + 关键词加权。"
        "它只衡量文字上像不像你关心的东西，不代表论文质量。AI 摘要只依据论文摘要写成，读原文前请自己核对。",
        "",
        "## 本周必读",
        "",
    ]
    if must_read:
        for p in must_read:
            one = (p.summary or {}).get("one_liner", "")
            out.append(f"- **[{p.title}]({p.url})**（{topic_of.get(p.arxiv_id, '')}）：{one}")
    else:
        out.append("本周没有达到推荐门槛的论文。")
    out.append("")

    for t in topics:
        out += [f"## {t.name}", ""]
        st = stats.get(t.slug, TopicStats())
        if st.error:
            out += [f"⚠️ 抓取失败：{st.error}", ""]
            continue
        papers = chosen.get(t.slug, [])
        if not papers:
            out += ["本周无重点。", ""]
            continue
        out += [_entry(p) for p in papers]

    out += ["## 抓取统计", "", "| 方向 | 抓到 | 新论文 | 入选 |", "|---|---|---|---|"]
    for t in topics:
        st = stats.get(t.slug, TopicStats())
        n = len(chosen.get(t.slug, []))
        out.append(f"| {t.name} | {st.fetched} | {st.new} | {n} |")
    out.append("")
    return "\n".join(out)
