"""Render the weekly digest as Markdown."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .config import Topic
from .i18n import STRINGS
from .models import Paper


@dataclass
class TopicStats:
    fetched: int = 0
    new: int = 0
    error: str = ""


def _authors(names: list[str], s: dict, n: int = 3) -> str:
    # bioRxiv writes "Smith, J."; use ";" between authors so the list stays readable
    sep = "; " if any("," in a for a in names) else ", "
    return sep.join(names) if len(names) <= n else sep.join(names[:n]) + s["et_al"]


def _entry(p: Paper, s: dict) -> str:
    summ = p.summary or {}
    c = s["colon"]
    lines = [
        f"### [{p.title}]({p.url})",
        f"*{_authors(p.authors, s)}* · `{p.primary_category}` · {p.label}"
        f" · {s['relevance']} {p.score:.2f}",
        "",
        f"- **{s['one_liner']}**{c}{summ.get('one_liner', '')}"
        + ("" if summ.get("ai") else s["fallback"]),
    ]
    if summ.get("why"):
        lines.append(f"- **{s['why']}**{c}{summ['why']}")
    if summ.get("background") or summ.get("difficulty"):
        diff = f" · {s['difficulty']}{c}{summ['difficulty']}" if summ.get("difficulty") else ""
        lines.append(f"- **{s['background']}**{c}{summ.get('background', '')}{diff}")
    if p.matched_keywords:
        lines.append(f"- {s['keywords']}{c}" + s["list_sep"].join(p.matched_keywords))
    lines += ["", f"<details><summary>{s['abstract']}</summary>", "", p.abstract, "",
              "</details>", ""]
    return "\n".join(lines)


def render(chosen: dict[str, list[Paper]], topics: list[Topic], must_read: list[Paper],
           stats: dict[str, TopicStats], window: tuple[datetime, datetime],
           topic_of: dict[str, str], language: str = "en") -> str:
    s = STRINGS[language]
    start, end = window
    out = [
        "# " + s["title"].format(date=f"{end:%Y-%m-%d}"),
        "",
        s["coverage"].format(start=f"{start:%Y-%m-%d}", end=f"{end:%Y-%m-%d}"),
        "",
        s["note"],
        "",
        f"## {s['must_read']}",
        "",
    ]
    if must_read:
        for p in must_read:
            one = (p.summary or {}).get("one_liner", "")
            out.append(f"- **[{p.title}]({p.url})** ({topic_of.get(p.uid, '')}){s['colon']}{one}")
    else:
        out.append(s["no_must_read"])
    out.append("")

    for t in topics:
        out += [f"## {t.display_name(language)}", ""]
        st = stats.get(t.slug, TopicStats())
        if st.error:
            out += [s["failed"].format(error=st.error), ""]
            continue
        papers = chosen.get(t.slug, [])
        if not papers:
            out += [s["nothing"], ""]
            continue
        out += [_entry(p, s) for p in papers]

    out += [f"## {s['stats']}", "", s["stats_header"], "|---|---|---|---|"]
    for t in topics:
        st = stats.get(t.slug, TopicStats())
        out.append(f"| {t.display_name(language)} | {st.fetched} | {st.new} | "
                   f"{len(chosen.get(t.slug, []))} |")
    out.append("")
    return "\n".join(out)
