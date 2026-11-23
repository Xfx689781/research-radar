"""Tiny HTTP helper with retries, shared by all sources."""

from __future__ import annotations

import json
import logging
import time
import urllib.error
import urllib.request

log = logging.getLogger(__name__)

USER_AGENT = "research-radar/0.6 (+https://github.com/Xfx689781/research-radar)"
RETRIES = 5
SLOW_DOWN = (429, 503)       # "too many requests" / "try again later"


def wait_seconds(exc: Exception, attempt: int) -> float:
    """How long to wait before retrying. Rate limits get much longer pauses."""
    if isinstance(exc, urllib.error.HTTPError) and exc.code in SLOW_DOWN:
        retry_after = exc.headers.get("Retry-After") if exc.headers else None
        if retry_after and retry_after.isdigit():
            return min(int(retry_after), 120)
        return 20 * attempt              # 20, 40, 60, 80 seconds
    return 5 * attempt


def get_text(url: str, retries: int = RETRIES, timeout: int = 60) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as exc:
            if exc.code not in SLOW_DOWN and 400 <= exc.code < 500:
                raise                     # a real client error will not fix itself
            if attempt == retries:
                raise
            wait = wait_seconds(exc, attempt)
        except Exception as exc:          # network hiccups are common; back off and retry
            if attempt == retries:
                raise
            wait = wait_seconds(exc, attempt)
        log.warning("request failed (%s); retrying in %ss", url[:80], wait)
        time.sleep(wait)
    raise AssertionError("unreachable")


def get_json(url: str) -> dict:
    return json.loads(get_text(url))
