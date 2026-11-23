"""Minimal client for the official arXiv API (https://info.arxiv.org/help/api/).

Only the standard library is used, so this module is easy to read end to end.
arXiv asks API users to wait about 3 seconds between requests; we respect that.
"""

from __future__ import annotations

import logging
import re
import time
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

from ..models import Paper
from .http import get_text

log = logging.getLogger(__name__)

API_URL = "https://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"
DELAY = 3.0

_ID_RE = re.compile(r"abs/(?P<id>.+?)(?:v(?P<version>\d+))?$")


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
        arxiv_id, version = m.group("id"), int(m.group("version") or 0)

        pdf_url = ""
        url = raw_id
        for link in entry.findall(f"{ATOM}link"):
            if link.get("title") == "pdf":
                pdf_url = link.get("href", "")
            elif link.get("rel") == "alternate":
                url = link.get("href", url)

        primary = entry.find(f"{ARXIV}primary_category")
        categories = [c.get("term", "") for c in entry.findall(f"{ATOM}category")]
        categories = [c for c in categories if c]

        papers.append(Paper(
            uid=f"arxiv:{arxiv_id}",
            source="arxiv",
            label=f"arXiv:{arxiv_id}" + (f"v{version}" if version else ""),
            title=_text(entry.find(f"{ATOM}title")),
            authors=[_text(a.find(f"{ATOM}name")) for a in entry.findall(f"{ATOM}author")],
            abstract=_text(entry.find(f"{ATOM}summary")),
            primary_category=primary.get("term", "") if primary is not None else
                             (categories[0] if categories else ""),
            categories=categories,
            published=_date(_text(entry.find(f"{ATOM}published"))),
            url=url.replace("http://", "https://", 1),
            pdf_url=pdf_url.replace("http://", "https://", 1),
            version=version,
        ))
    return papers


# ---------------------------------------------------------------- fetching

def search(query: str, max_results: int = 600, page_size: int = 200) -> list[Paper]:
    """Run a search, following pages until max_results or the end of results."""
    papers: list[Paper] = []
    start = 0
    while start < max_results:
        n = min(page_size, max_results - start)
        params = {"search_query": query, "start": start, "max_results": n,
                  "sortBy": "submittedDate", "sortOrder": "descending"}
        page = parse_feed(get_text(API_URL + "?" + urllib.parse.urlencode(params)))
        papers.extend(page)
        log.info("  fetched %d (total %d)", len(page), len(papers))
        if len(page) < n:
            break
        start += n
        time.sleep(DELAY)
    return papers


def fetch_by_ids(ids: list[str]) -> list[Paper]:
    """Fetch specific papers, e.g. the seed papers that describe your taste."""
    if not ids:
        return []
    time.sleep(DELAY)
    params = {"id_list": ",".join(ids), "max_results": len(ids)}
    return parse_feed(get_text(API_URL + "?" + urllib.parse.urlencode(params)))


# ---------------------------------------------------------------- daily RSS listings
#
# arXiv's RSS feeds list one day's announcements, and one URL can combine many
# categories (https://rss.arxiv.org/rss/math.PR+math.AP). For daily runs this
# replaces one paged API query per topic with a handful of requests, which keeps
# us clear of the API's rate limit. Feeds are empty on weekends.

RSS_URL = "https://rss.arxiv.org/rss/"
RSS_CHUNK = 15                 # categories per request
DC = "{http://purl.org/dc/elements/1.1/}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"
_GUID_RE = re.compile(r"(?:oai:arXiv\.org:)?(?P<id>.+?)(?:v(?P<version>\d+))?$")
NEW_TYPES = {"new", "cross"}   # skip "replace": an older paper's new version


def parse_rss(xml_text: str) -> list[Paper]:
    root = ET.fromstring(xml_text.lstrip("﻿ \r\n\t"))
    channel = root.find("channel")
    papers = []
    for it in (channel.findall("item") if channel is not None else []):
        kind = (it.findtext(f"{ARXIV_NS}announce_type") or "new").strip()
        if kind not in NEW_TYPES:
            continue
        m = _GUID_RE.match((it.findtext("guid") or "").strip())
        link = (it.findtext("link") or "").strip()
        if not m or not link:
            continue
        arxiv_id, version = m.group("id"), int(m.group("version") or 1)
        desc = " ".join((it.findtext("description") or "").split())
        abstract = desc.split("Abstract:", 1)[1].strip() if "Abstract:" in desc else desc
        categories = [c.text.strip() for c in it.findall("category") if c.text]
        creators = (it.findtext(f"{DC}creator") or "").replace(" and ", ", ")
        try:
            published = parsedate_to_datetime(it.findtext("pubDate") or "")
        except (TypeError, ValueError):
            published = datetime.now(timezone.utc)
        papers.append(Paper(
            uid=f"arxiv:{arxiv_id}",
            source="arxiv",
            label=f"arXiv:{arxiv_id}v{version}",
            title=" ".join((it.findtext("title") or "").split()),
            authors=[a.strip() for a in creators.split(",") if a.strip()],
            abstract=abstract,
            primary_category=categories[0] if categories else "",
            categories=categories,
            published=published,
            url=link.replace("http://", "https://", 1),
            pdf_url=link.replace("http://", "https://", 1).replace("/abs/", "/pdf/"),
            version=version,
        ))
    return papers


def fetch_rss(categories: list[str]) -> list[Paper]:
    """Today's new and cross-listed papers in these categories, de-duplicated."""
    cats = sorted(set(categories))
    out: dict[str, Paper] = {}
    for i in range(0, len(cats), RSS_CHUNK):
        if i:
            time.sleep(DELAY)
        chunk = cats[i:i + RSS_CHUNK]
        for p in parse_rss(get_text(RSS_URL + "+".join(chunk))):
            out.setdefault(p.uid, p)
        log.info("  arXiv RSS %s…: %d papers so far", chunk[0], len(out))
    return list(out.values())
