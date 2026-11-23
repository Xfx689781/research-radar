"""News from RSS 2.0 and Atom feeds (company blogs, tech news sites).

Only what a feed publishes for syndication is used: the headline, the link, the
date and a short teaser (HTML stripped, cut to TEASER_CHARS). The AI summary is
written from that teaser; readers follow the link for the full article.
"""

from __future__ import annotations

import hashlib
import html
import logging
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from urllib.parse import urlparse

from ..models import Paper
from .http import get_text

log = logging.getLogger(__name__)

ATOM = "{http://www.w3.org/2005/Atom}"
TEASER_CHARS = 600


def clean_text(raw: str, limit: int = TEASER_CHARS) -> str:
    """HTML to plain text, shortened at a word boundary."""
    text = re.sub(r"<(script|style)\b.*?</\1>", " ", raw or "", flags=re.S | re.I)
    text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    text = " ".join(text.split())
    if len(text) > limit:
        text = text[:limit].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return text


def parse_date(s: str) -> datetime | None:
    s = (s or "").strip()
    if not s:
        return None
    try:
        d = parsedate_to_datetime(s)                       # RSS: "Fri, 20 Nov 2026 10:00:00 GMT"
    except (TypeError, ValueError):
        try:
            d = datetime.fromisoformat(s.replace("Z", "+00:00"))   # Atom: ISO 8601
        except ValueError:
            return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def _text(el: ET.Element | None) -> str:
    return (el.text or "").strip() if el is not None else ""


def parse_feed(xml_text: str, feed_url: str = "") -> list[Paper]:
    text = xml_text.lstrip("\ufeff \r\n\t")
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        raise ValueError(f"{exc}; response starts {text[:80]!r}") from exc
    host = urlparse(feed_url).netloc.removeprefix("www.")
    items = []
    if root.tag == f"{ATOM}feed":                         # Atom
        site = _text(root.find(f"{ATOM}title")) or host
        for e in root.findall(f"{ATOM}entry"):
            link = next((l.get("href", "") for l in e.findall(f"{ATOM}link")
                         if l.get("rel", "alternate") == "alternate"), "")
            items.append((_text(e.find(f"{ATOM}title")), link,
                          _text(e.find(f"{ATOM}published")) or _text(e.find(f"{ATOM}updated")),
                          _text(e.find(f"{ATOM}summary")) or _text(e.find(f"{ATOM}content")),
                          [a.findtext(f"{ATOM}name", "") for a in e.findall(f"{ATOM}author")]))
    else:                                                 # RSS 2.0
        channel = root.find("channel")
        if channel is None:
            raise ValueError("not an RSS or Atom feed")
        site = _text(channel.find("title")) or host
        for it in channel.findall("item"):
            creator = it.find("{http://purl.org/dc/elements/1.1/}creator")
            items.append((_text(it.find("title")), _text(it.find("link")),
                          _text(it.find("pubDate")), _text(it.find("description")),
                          [_text(creator)] if creator is not None else []))

    site = clean_text(site, 60)
    papers = []
    for title, link, date_s, teaser, authors in items:
        published = parse_date(date_s)
        if not (title and link.startswith("https://") and published):
            continue
        papers.append(Paper(
            uid="news:" + hashlib.sha1(link.encode()).hexdigest()[:16],
            source="rss",
            label=site,
            title=clean_text(title, 300),
            authors=[a for a in authors if a],
            abstract=clean_text(teaser),
            primary_category=host,
            categories=[host],
            published=published,
            url=link,
        ))
    return papers


def search(feeds: list[str], keywords: list[str], start: datetime, end: datetime) -> list[Paper]:
    """Items from all feeds published in [start, end]. A broken feed is skipped, not fatal."""
    from ..models import matched_keywords

    out: dict[str, Paper] = {}
    for url in feeds:
        try:
            items = parse_feed(get_text(url, retries=2), url)
        except Exception as exc:
            log.warning("feed %s failed: %s", url, exc)
            continue
        for p in items:
            if start <= p.published <= end and (not keywords or matched_keywords(p, keywords)):
                out.setdefault(p.uid, p)
        log.info("  %s: %d items in window", urlparse(url).netloc, sum(
            1 for p in items if start <= p.published <= end))
    return list(out.values())
