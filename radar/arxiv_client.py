"""Minimal client for the official arXiv API (https://info.arxiv.org/help/api/).

Only the standard library is used, so this module is easy to read end to end.
arXiv asks API users to wait about 3 seconds between requests; we respect that.
"""

from __future__ import annotations

import logging
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime

log = logging.getLogger(__name__)

API_URL = "https://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"
USER_AGENT = "research-radar/0.1 (personal research digest)"

_ID_RE = re.compile(r"abs/(?P<id>.+?)(?P<version>v\d+)?$")


@dataclass
class Paper:
    arxiv_id: str                  # without version, e.g. "2611.01234" or "math/0601001"
    version: str                   # e.g. "v2"
    title: str
    authors: list[str]
    abstract: str
    primary_category: str
    categories: list[str]
    published: datetime
    updated: datetime
    url: str
    pdf_url: str = ""
    # filled in later by the pipeline
    score: float = 0.0
    matched_keywords: list[str] = field(default_factory=list)
    summary: dict = field(default_factory=dict)

    @property
    def text(self) -> str:
        return f"{self.title}. {self.abstract}"


class ArxivError(RuntimeError):
    pass


# ---------------------------------------------------------------- query building

def _term(keyword: str) -> str:
    """Match a keyword in the title or the abstract. Phrases are quoted."""
    k = keyword.replace('"', "")
    k = f'"{k}"' if " " in k or "-" in k else k
    return f"ti:{k} OR abs:{k}"


def build_query(categories: list[str], keywords: list[str],
                start: datetime, end: datetime) -> str:
    """Build an arXiv search_query string.

    Example: (cat:math.PR) AND submittedDate:[202611150000 TO 202611222359]
    """
    if not categories:
        raise ValueError("need at least one category")
    q = "(" + " OR ".join(f"cat:{c}" for c in categories) + ")"
    if keywords:
        q += " AND (" + " OR ".join(_term(k) for k in keywords) + ")"
    q += f" AND submittedDate:[{start:%Y%m%d%H%M} TO {end:%Y%m%d%H%M}]"
    return q


# ---------------------------------------------------------------- parsing

def _text(el: ET.Element | None) -> str:
    return " ".join((el.text or "").split()) if el is not None else ""


def _date(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def parse_feed(xml_text: str) -> list[Paper]:
    """Turn an arXiv Atom feed into a list of Paper objects."""
    root = ET.fromstring(xml_text)
    papers = []
    for entry in root.findall(f"{ATOM}entry"):
        raw_id = _text(entry.find(f"{ATOM}id"))
        if "api/errors" in raw_id:
            raise ArxivError(_text(entry.find(f"{ATOM}summary")) or "arXiv API error")

        m = _ID_RE.search(raw_id)
        if not m:
            log.warning("skipping entry with unexpected id %r", raw_id)
            continue

        pdf_url = ""
        url = raw_id
        for link in entry.findall(f"{ATOM}link"):
            if link.get("title") == "pdf":
                pdf_url = link.get("href", "")
            elif link.get("rel") == "alternate":
                url = link.get("href", url)

        primary = entry.find(f"{ARXIV}primary_category")
        categories = [c.get("term", "") for c in entry.findall(f"{ATOM}category")]

        papers.append(Paper(
            arxiv_id=m.group("id"),
            version=m.group("version") or "",
            title=_text(entry.find(f"{ATOM}title")),
            authors=[_text(a.find(f"{ATOM}name")) for a in entry.findall(f"{ATOM}author")],
            abstract=_text(entry.find(f"{ATOM}summary")),
            primary_category=primary.get("term", "") if primary is not None else
                             (categories[0] if categories else ""),
            categories=[c for c in categories if c],
            published=_date(_text(entry.find(f"{ATOM}published"))),
            updated=_date(_text(entry.find(f"{ATOM}updated"))),
            url=url.replace("http://", "https://", 1),
            pdf_url=pdf_url.replace("http://", "https://", 1),
        ))
    return papers


# ---------------------------------------------------------------- fetching

def _get(params: dict, retries: int = 3, timeout: int = 60) -> str:
    url = API_URL + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8")
        except Exception as exc:  # network hiccups are common; back off and retry
            if attempt == retries:
                raise
            wait = 5 * attempt
            log.warning("arXiv request failed (%s); retrying in %ss", exc, wait)
            time.sleep(wait)
    raise AssertionError("unreachable")


def search(query: str, max_results: int = 600, page_size: int = 200,
           delay: float = 3.0) -> list[Paper]:
    """Run a search, following pages until max_results or the end of results."""
    papers: list[Paper] = []
    start = 0
    while start < max_results:
        n = min(page_size, max_results - start)
        xml_text = _get({
            "search_query": query,
            "start": start,
            "max_results": n,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        })
        page = parse_feed(xml_text)
        papers.extend(page)
        log.info("  fetched %d (total %d)", len(page), len(papers))
        if len(page) < n:
            break
        start += n
        time.sleep(delay)
    return papers


def fetch_by_ids(ids: list[str], delay: float = 3.0) -> list[Paper]:
    """Fetch specific papers, e.g. the seed papers that describe your taste."""
    if not ids:
        return []
    time.sleep(delay)
    return parse_feed(_get({"id_list": ",".join(ids), "max_results": len(ids)}))
