"""Daily post to a Discord channel through a webhook.

A Discord channel is shared, so it gets one post for everyone: by default the
day's highlights across all topics, or every item of the topics listed in
config.yaml under discord_topics.

Needs the GitHub Actions secret DISCORD_WEBHOOK_URL (Discord: channel settings
-> Integrations -> Webhooks -> New Webhook -> Copy Webhook URL). Without it,
this step does nothing.
"""

from __future__ import annotations

import json
import logging
import os
import time
import urllib.request
from datetime import date

from .archive import Archive
from .config import Config

log = logging.getLogger(__name__)

EMBEDS_PER_MESSAGE = 10        # Discord's limit
DESCRIPTION_CHARS = 400
COLOR = 0x0F6B5C               # the site's accent colour


def _cut(text: str, n: int) -> str:
    text = " ".join((text or "").split())
    return text if len(text) <= n else text[:n - 1].rsplit(" ", 1)[0] + "…"


def pick_items(cfg: Config, archive: Archive, today: date) -> list[dict]:
    """Today's items to post: chosen topics in full, or the overall highlights."""
    todays = [r for r in archive.records if r["date"] == today.isoformat()]
    if cfg.discord_topics:
        order = {slug: i for i, slug in enumerate(cfg.discord_topics)}
        items = [r for r in todays if r["topic"] in order]
        return sorted(items, key=lambda r: (order[r["topic"]], -r.get("score", 0)))
    # Highlights: the best item of each topic first, then by score, so that one
    # busy topic cannot fill the whole post.
    best: dict[str, dict] = {}
    for r in sorted(todays, key=lambda r: -r.get("score", 0)):
        best.setdefault(r["topic"], r)
    return sorted(best.values(), key=lambda r: -r.get("score", 0))[:cfg.discord_highlights]


def build_messages(items: list[dict], cfg: Config, today: date) -> list[dict]:
    names = {t.slug: t.display_name(cfg.language) for t in cfg.topics}
    embeds = []
    for r in items:
        s = r.get("summary") or {}
        embeds.append({
            "title": _cut(r["title"], 250),
            "url": r["url"],
            "description": _cut(s.get("plain") or s.get("one_liner") or "", DESCRIPTION_CHARS),
            "footer": {"text": _cut(f"{names.get(r['topic'], r['topic'])} · {r.get('label', '')}", 200)},
            "color": COLOR,
        })
    what = "papers and news" if cfg.discord_topics else "highlights"
    intro = f"**{cfg.site_title} · {today:%A, %B %d}**: {len(items)} {what}"
    if cfg.site_url:
        intro += f". Pick your own topics: <{cfg.site_url}>"
    messages = []
    for i in range(0, len(embeds), EMBEDS_PER_MESSAGE):
        msg = {"embeds": embeds[i:i + EMBEDS_PER_MESSAGE],
               "allowed_mentions": {"parse": []}}   # never ping anyone
        if i == 0:
            msg["content"] = intro
        messages.append(msg)
    return messages


def _post(url: str, payload: dict) -> None:
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), method="POST",
                                 headers={"Content-Type": "application/json",
                                          "User-Agent": "research-radar"})
    with urllib.request.urlopen(req, timeout=30):
        pass


def post_daily(cfg: Config, archive: Archive, today: date, dry_run: bool = False) -> int:
    url = os.environ.get("DISCORD_WEBHOOK_URL", "").strip()
    if not url and not dry_run:
        log.info("Discord skipped: DISCORD_WEBHOOK_URL not set")
        return 0
    items = pick_items(cfg, archive, today)
    if not items:
        log.info("Discord: nothing new today")
        return 0
    messages = build_messages(items, cfg, today)
    if dry_run:
        log.info("would post %d Discord message(s) with %d items", len(messages), len(items))
        return len(messages)
    for i, m in enumerate(messages):
        if i:
            time.sleep(1.5)            # stay under the webhook rate limit
        _post(url, m)
    log.info("Discord: posted %d item(s) in %d message(s)", len(items), len(messages))
    return len(messages)
