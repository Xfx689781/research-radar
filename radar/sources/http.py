"""Tiny HTTP helper with retries, shared by all sources."""

from __future__ import annotations

import json
import logging
import time
import urllib.request

log = logging.getLogger(__name__)

USER_AGENT = "research-radar/0.2 (+https://github.com/Xfx689781/research-radar)"


def get_text(url: str, retries: int = 3, timeout: int = 60) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8")
        except Exception as exc:  # network hiccups are common; back off and retry
            if attempt == retries:
                raise
            wait = 5 * attempt
            log.warning("request failed (%s); retrying in %ss", exc, wait)
            time.sleep(wait)
    raise AssertionError("unreachable")


def get_json(url: str) -> dict:
    return json.loads(get_text(url))
