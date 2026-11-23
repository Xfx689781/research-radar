"""Daily email: send each subscribed reader today's papers in their topics.

Readers opt in on the website (signed in, "Email me these every morning"),
which stores email_daily = true in the Supabase `preferences` table.

This job needs, as GitHub Actions secrets (all optional; without them it does nothing):
  SUPABASE_SECRET_KEY   Supabase secret key (or legacy service_role key), to read subscribers
  SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD   any SMTP account, e.g. Gmail + app password
  MAIL_FROM             optional sender, defaults to SMTP_USER
"""

from __future__ import annotations

import html
import json
import logging
import os
import smtplib
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date
from email.message import EmailMessage

from .archive import Archive
from .config import Config

log = logging.getLogger(__name__)


@dataclass
class SmtpSettings:
    host: str
    port: int
    user: str
    password: str
    sender: str

    @classmethod
    def from_env(cls) -> "SmtpSettings | None":
        host, user, pw = (os.environ.get(k, "").strip() for k in ("SMTP_HOST", "SMTP_USER", "SMTP_PASSWORD"))
        if not (host and user and pw):
            return None
        port = int(os.environ.get("SMTP_PORT", "465") or 465)
        return cls(host, port, user, pw, os.environ.get("MAIL_FROM", "").strip() or user)


def _jwt_role(key: str) -> str:
    """The role inside a legacy JWT key ('anon' or 'service_role'); '' if not a JWT."""
    try:
        import base64
        part = key.split(".")[1]
        return json.loads(base64.urlsafe_b64decode(part + "=" * (-len(part) % 4))).get("role", "")
    except Exception:
        return ""


def fetch_subscribers(supabase_url: str, key: str) -> list[dict]:
    """Rows with email_daily = true, read with the secret key (bypasses row-level security).

    If the database does not have the unsubscribe_token column yet (supabase/schema.sql
    not re-run), the emails still go out, just without the one-click unsubscribe link.
    """
    headers = {"apikey": key, "Accept": "application/json"}
    if not key.startswith("sb_"):          # legacy JWT keys also go in the Authorization header
        headers["Authorization"] = f"Bearer {key}"

    def get(columns: str) -> list[dict]:
        query = urllib.parse.urlencode({"select": columns, "email_daily": "eq.true"})
        req = urllib.request.Request(f"{supabase_url.rstrip('/')}/rest/v1/preferences?{query}",
                                     headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:      # say why, not just the status code
            detail = exc.read().decode("utf-8", errors="replace")[:300]
            raise RuntimeError(f"Supabase answered {exc.code}: {detail}") from exc

    try:
        rows = get("email,topics,unsubscribe_token")
    except RuntimeError as exc:
        if "unsubscribe_token" not in str(exc):
            raise
        log.warning("the database has no unsubscribe_token column yet; run supabase/schema.sql "
                    "again to add one-click unsubscribe links. Sending without them for now.")
        rows = get("email,topics")
    return [r for r in rows if r.get("email") and r.get("topics")]


def unsubscribe_url(site_url: str, token: str | None) -> str:
    if not (site_url and token):
        return ""
    return f"{site_url.rstrip('/')}/?unsubscribe={urllib.parse.quote(str(token))}"


def build_email(topics: list[str], archive: Archive, cfg: Config, today: date,
                site_url: str, unsubscribe: str = "") -> tuple[str, str, str] | None:
    """(subject, plain text, html) with today's items in these topics, or None if there are none."""
    names = {t.slug: t.display_name(cfg.language) for t in cfg.topics}
    sections = []
    for slug in topics:
        if slug not in names:
            continue
        items = [r for r in archive.for_topic(slug) if r["date"] == today.isoformat()]
        if items:
            sections.append((names[slug], items))
    if not sections:
        return None

    n = sum(len(items) for _, items in sections)
    subject = f"{cfg.site_title}: {n} new for you · {today:%b %d}"

    text = [f"{cfg.site_title} · {today:%A, %B %d}", ""]
    parts = [f'<div style="font-family:system-ui,Arial,sans-serif;max-width:640px;margin:auto;'
             f'color:#1d1f22;line-height:1.5">'
             f'<h1 style="font-family:Georgia,serif;font-size:22px;margin:0 0 4px">{html.escape(cfg.site_title)}</h1>'
             f'<p style="color:#5d636b;margin:0 0 18px">{today:%A, %B %d} · {n} new in your topics</p>']
    for name, items in sections:
        text += [name.upper(), ""]
        parts.append(f'<h2 style="font-size:13px;letter-spacing:.06em;text-transform:uppercase;'
                     f'color:#0f6b5c;margin:26px 0 8px">{html.escape(name)}</h2>')
        for r in items:
            s = r.get("summary") or {}
            blurb = s.get("plain") or s.get("one_liner") or ""
            text += [r["title"], r["url"], blurb, ""]
            parts.append(
                f'<div style="border:1px solid #e6e2da;border-radius:10px;padding:14px 16px;margin:0 0 10px">'
                f'<a href="{html.escape(r["url"], quote=True)}" style="font-family:Georgia,serif;'
                f'font-size:17px;color:#1d1f22;font-weight:600;text-decoration:none">{html.escape(r["title"])}</a>'
                f'<div style="color:#8a9098;font-size:13px;margin:2px 0 8px">{html.escape(r.get("label") or "")}</div>'
                f'<div>{html.escape(blurb)}</div></div>')
    footer = (f"You get this email because you subscribed at {site_url}. "
              f"Change your topics there. Summaries are written by AI and can be wrong.")
    text += ["--", footer]
    if unsubscribe:
        text.append(f"Unsubscribe: {unsubscribe}")
    unsub_html = (f' · <a href="{html.escape(unsubscribe, quote=True)}" style="color:#0f6b5c">Unsubscribe</a>'
                  if unsubscribe else "")
    parts.append(f'<p style="color:#8a9098;font-size:12px;margin-top:26px">'
                 f'<a href="{html.escape(site_url, quote=True)}" style="color:#0f6b5c">Open your feed</a>{unsub_html}<br>'
                 f'{html.escape(footer)}</p></div>')
    return subject, "\n".join(text), "".join(parts)


def send_daily(cfg: Config, archive: Archive, today: date, dry_run: bool = False) -> int | None:
    """Number of emails sent, or None when email is not set up."""
    key = os.environ.get("SUPABASE_SECRET_KEY", "").strip()
    smtp = SmtpSettings.from_env()
    if not (cfg.supabase_url and key):
        log.info("daily email skipped: SUPABASE_SECRET_KEY or supabase_url not set")
        return None
    if not smtp and not dry_run:
        log.info("daily email skipped: SMTP settings not set")
        return None

    if key.startswith(("sb_publishable_", "eyJ")) and "service_role" not in _jwt_role(key):
        log.warning("SUPABASE_SECRET_KEY looks like the public (publishable/anon) key, which "
                    "cannot read other readers' settings. Use the secret key (sb_secret_...).")
    subscribers = fetch_subscribers(cfg.supabase_url, key)
    log.info("daily email: %d subscriber(s)", len(subscribers))
    messages = []
    for sub in subscribers:
        unsub = unsubscribe_url(cfg.site_url, sub.get("unsubscribe_token"))
        built = build_email(sub["topics"], archive, cfg, today, cfg.site_url, unsub)
        if not built:
            continue
        subject, text, body = built
        msg = EmailMessage()
        msg["Subject"], msg["To"] = subject, sub["email"]
        msg["From"] = smtp.sender if smtp else "dry-run@example.org"
        if unsub:                       # mail apps show an "Unsubscribe" button for this
            sender = smtp.sender if smtp else "dry-run@example.org"
            addr = sender.split("<")[-1].rstrip(">").strip()
            msg["List-Unsubscribe"] = f"<{unsub}>, <mailto:{addr}?subject=unsubscribe>"
        msg.set_content(text)
        msg.add_alternative(body, subtype="html")
        messages.append(msg)

    if dry_run:
        for m in messages:
            log.info("would send to %s: %s", m["To"], m["Subject"])
        return len(messages)

    sent = 0
    context = ssl.create_default_context()
    server = (smtplib.SMTP_SSL(smtp.host, smtp.port, context=context, timeout=60) if smtp.port == 465
              else smtplib.SMTP(smtp.host, smtp.port, timeout=60))
    with server:
        if smtp.port != 465:
            server.starttls(context=context)
        server.login(smtp.user, smtp.password)
        for m in messages:
            try:
                server.send_message(m)
                sent += 1
            except smtplib.SMTPException as exc:   # one bad address should not stop the rest
                log.warning("could not email %s: %s", m["To"], exc)
            time.sleep(1)                           # stay well under provider rate limits
    log.info("daily email: sent %d of %d", sent, len(messages))
    return sent
