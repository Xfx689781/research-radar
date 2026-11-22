"""Build the home page of the GitHub Pages site (docs/index.md).

GitHub Pages turns every Markdown file under docs/ into a web page, so the
digests themselves need no extra work; this module only writes the front page
with the latest highlights and links to every past digest.
"""

from __future__ import annotations

import os
from pathlib import Path

from .config import Topic
from .digest import LIQUID_CLOSE, LIQUID_OPEN
from .i18n import STRINGS
from .models import Paper


def digest_files(digest_dir: Path) -> list[Path]:
    """Dated digests, newest first (latest.md is a copy and is skipped)."""
    return sorted((p for p in digest_dir.glob("????-??-??.md")), reverse=True)


def build_index(site_dir: Path, digest_dir: Path, topics: list[Topic], highlights: list[Paper],
                topic_of: dict[str, str], n_papers: int, language: str = "en") -> Path:
    s = STRINGS[language]
    files = digest_files(digest_dir)
    rel = Path(os.path.relpath(digest_dir, site_dir)).as_posix()

    out = [f"# {s['site_title']}", LIQUID_OPEN, "", s["site_intro"], ""]
    if files:
        latest = files[0]
        out += [f"## {s['latest']}: [{latest.stem}]({rel}/{latest.name})", "",
                f"{n_papers} {s['papers']}", ""]
        for p in highlights:
            summ = p.summary or {}
            text = summ.get("plain") or summ.get("one_liner", "")
            out.append(f"- **[{p.title}]({p.url})** ({topic_of.get(p.uid, '')}){s['colon']}{text}")
        out.append("")

    out += [f"## {s['topics']}", "", s["list_sep"].join(t.display_name(language) for t in topics), ""]
    out += [f"## {s['archive']}", ""]
    out += [f"- [{f.stem}]({rel}/{f.name})" for f in files]
    out += ["", LIQUID_CLOSE, ""]

    site_dir.mkdir(parents=True, exist_ok=True)
    index = site_dir / "index.md"
    index.write_text("\n".join(out), encoding="utf-8")
    return index
