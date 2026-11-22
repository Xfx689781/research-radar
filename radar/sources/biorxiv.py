"""Client for the bioRxiv / medRxiv API (https://api.biorxiv.org).

Most biology (and much of chemistry-adjacent life science) is posted on bioRxiv,
not arXiv, so biology topics can use this source instead.

Endpoint used:  /details/{server}/{YYYY-MM-DD}/{YYYY-MM-DD}/{cursor}?category=...
Each call returns up to 100 records plus a "messages" block with the total count.
"""

from __future__ import annotations

import logging
import time
import urllib.parse
from datetime import date, datetime, timezone

from ..models import Paper, matched_keywords
from .http import get_json

log = logging.getLogger(__name__)

API_URL = "https://api.biorxiv.org"
DELAY = 1.0
MAX_REQUESTS_PER_CATEGORY = 60     # safety cap: 60 x 100 records
SERVER_LABEL = {"biorxiv": "bioRxiv", "medrxiv": "medRxiv"}


def normalize_category(c: str) -> str:
    """bioRxiv writes "cell biology"; the query string uses "cell_biology"."""
    return c.strip().lower().replace("_", " ")


def _date(s: str) -> datetime:
    try:
        return datetime.fromisoformat(s).replace(tzinfo=timezone.utc)
    except ValueError:
        return datetime(1970, 1, 1, tzinfo=timezone.utc)


def parse_collection(data: dict, server: str) -> list[Paper]:
    """Turn one API response into Paper objects."""
    papers = []
    for it in data.get("collection") or []:
        doi = str(it.get("doi", "")).strip()
        if not doi:
            continue
        try:
            version = int(it.get("version") or 0)
        except (TypeError, ValueError):
            version = 0
        category = str(it.get("category", "")).strip()
        url = (f"https://www.{server}.org/content/{doi}v{version}" if version
               else f"https://doi.org/{doi}")
        papers.append(Paper(
            uid=f"{server}:{doi}",
            source=server,
            label=f"{SERVER_LABEL.get(server, server)} doi:{doi}" + (f" v{version}" if version else ""),
            title=" ".join(str(it.get("title", "")).split()),
            authors=[a.strip() for a in str(it.get("authors", "")).split(";") if a.strip()],
            abstract=" ".join(str(it.get("abstract", "")).split()),
            primary_category=category,
            categories=[category] if category else [],
            published=_date(str(it.get("date", ""))),
            url=url,
            version=version,
        ))
    return papers


def latest_versions(papers: list[Paper]) -> list[Paper]:
    """The same preprint can appear once per version; keep the newest."""
    best: dict[str, Paper] = {}
    for p in papers:
        if p.uid not in best or p.version > best[p.uid].version:
            best[p.uid] = p
    return list(best.values())


def filter_papers(papers: list[Paper], categories: list[str], keywords: list[str]) -> list[Paper]:
    wanted = {normalize_category(c) for c in categories}
    out = [p for p in papers if not wanted or normalize_category(p.primary_category) in wanted]
    if keywords:
        out = [p for p in out if matched_keywords(p, keywords)]
    return out


def search(server: str, categories: list[str], keywords: list[str],
           start: date, end: date, max_results: int = 600) -> list[Paper]:
    """Fetch preprints posted between start and end in the given categories.

    The category is passed to the API, and the results are also filtered here,
    so the output is correct even if the API ignores the parameter.
    """
    collected: list[Paper] = []
    for cat in categories or [""]:
        cursor = 0
        for _ in range(MAX_REQUESTS_PER_CATEGORY):
            url = f"{API_URL}/details/{server}/{start:%Y-%m-%d}/{end:%Y-%m-%d}/{cursor}"
            if cat:
                url += "?" + urllib.parse.urlencode(
                    {"category": normalize_category(cat).replace(" ", "_")})
            data = get_json(url)
            batch = data.get("collection") or []
            collected.extend(filter_papers(parse_collection(data, server), [cat] if cat else [], keywords))
            try:
                total = int((data.get("messages") or [{}])[0].get("total", 0) or 0)
            except (TypeError, ValueError):
                total = 0
            cursor += len(batch)
            log.info("  %s/%s: %d of %d", server, cat or "all", cursor, total)
            if not batch or cursor >= total or len(collected) >= max_results:
                break
            time.sleep(DELAY)
    return latest_versions(collected)[:max_results]


def fetch_by_dois(server: str, dois: list[str]) -> list[Paper]:
    """Fetch seed preprints by DOI."""
    papers = []
    for doi in dois:
        time.sleep(DELAY)
        papers += parse_collection(get_json(f"{API_URL}/details/{server}/{doi}"), server)
    return latest_versions(papers)
