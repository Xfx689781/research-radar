import json
import sys
import types
from argparse import Namespace
from datetime import date, datetime, timezone
from pathlib import Path

import pytest
import yaml

from radar import sources
from radar.__main__ import run
from radar.config import Topic, load_config, load_presets, resolve_topic
from radar.models import matched_keywords
from radar.rank import assign_unique, score_papers
from radar.sources import biorxiv
from radar.sources.arxiv import ArxivError, build_query, parse_feed
from radar.state import SeenState
from radar.summarize import fallback_summary, parse_summary, summarize_all

FIXTURES = Path(__file__).parent / "fixtures"
REPO = Path(__file__).parents[1]


@pytest.fixture
def papers():
    return parse_feed((FIXTURES / "arxiv.xml").read_text(encoding="utf-8"))


@pytest.fixture
def bio():
    data = json.loads((FIXTURES / "biorxiv.json").read_text(encoding="utf-8"))
    return biorxiv.parse_collection(data, "biorxiv")


def by_uid(papers, uid):
    return next(p for p in papers if p.uid == uid)


# ---------------------------------------------------------------- arXiv

def test_parse_feed(papers):
    assert len(papers) == 7
    p = by_uid(papers, "arxiv:2611.00001")
    assert p.label == "arXiv:2611.00001v2" and p.version == 2
    assert p.title == "[TEST] Propagation of chaos for mean-field Langevin dynamics"
    assert p.authors == ["Test Author A", "Test Author B"]
    assert p.primary_category == "math.PR"
    assert p.categories == ["math.PR", "stat.ML"]
    assert p.url.startswith("https://")
    assert p.pdf_url == "https://arxiv.org/pdf/2611.00001v2"
    assert p.published == datetime(2026, 11, 17, 18, tzinfo=timezone.utc)


def test_old_style_id(papers):
    assert by_uid(papers, "arxiv:math/0601001").version == 1


def test_error_feed_raises():
    err = """<feed xmlns="http://www.w3.org/2005/Atom"><entry>
      <id>http://arxiv.org/api/errors#bad</id><title>Error</title>
      <summary>malformed query</summary></entry></feed>"""
    with pytest.raises(ArxivError, match="malformed"):
        parse_feed(err)


def test_build_query():
    q = build_query(["math.PR", "stat.ML"], ["PAC-Bayes", "minimax"],
                    datetime(2026, 11, 15), datetime(2026, 11, 22, 23, 59))
    assert q.startswith("(cat:math.PR OR cat:stat.ML) AND (")
    assert 'ti:"PAC-Bayes" OR abs:"PAC-Bayes"' in q
    assert "ti:minimax OR abs:minimax" in q
    assert q.endswith("submittedDate:[202611150000 TO 202611222359]")


# ---------------------------------------------------------------- bioRxiv

def test_biorxiv_parse_and_latest_version(bio):
    latest = biorxiv.latest_versions(bio)
    assert len(latest) == 3
    p = by_uid(latest, "biorxiv:10.1101/2026.11.18.000001")
    assert p.version == 2 and "Version 2" in p.abstract
    assert p.url == "https://www.biorxiv.org/content/10.1101/2026.11.18.000001v2"
    assert p.label == "bioRxiv doi:10.1101/2026.11.18.000001 v2"
    assert p.authors == ["Tester, A.", "Tester, B."]


def test_biorxiv_category_filter(bio):
    kept = biorxiv.filter_papers(bio, ["Cell_Biology"], [])
    assert {p.primary_category for p in kept} == {"cell biology"}


def test_biorxiv_search_pages_and_filters(monkeypatch):
    """Two pages from a fake API; the cell-biology record is filtered out client-side."""
    page1 = {"messages": [{"total": 3}], "collection": [
        {"doi": "10.1/a", "version": "1", "category": "bioinformatics", "title": "A",
         "abstract": "x", "date": "2026-11-20"},
        {"doi": "10.1/b", "version": "1", "category": "cell biology", "title": "B",
         "abstract": "x", "date": "2026-11-20"}]}
    page2 = {"messages": [{"total": 3}], "collection": [
        {"doi": "10.1/c", "version": "1", "category": "bioinformatics", "title": "C",
         "abstract": "x", "date": "2026-11-21"}]}
    urls = []

    def fake_get_json(url):
        urls.append(url)
        return page1 if "/0?" in url else page2

    monkeypatch.setattr(biorxiv, "get_json", fake_get_json)
    monkeypatch.setattr(biorxiv, "DELAY", 0)
    out = biorxiv.search("biorxiv", ["bioinformatics"], [], date(2026, 11, 15), date(2026, 11, 22))
    assert sorted(p.uid for p in out) == ["biorxiv:10.1/a", "biorxiv:10.1/c"]
    assert urls[0].endswith("/details/biorxiv/2026-11-15/2026-11-22/0?category=bioinformatics")
    assert "/2?" in urls[1]


# ---------------------------------------------------------------- config and presets

def test_presets_are_valid():
    presets = load_presets()
    for key in presets:
        t = resolve_topic(key, presets)
        assert t.name and t.interest and (t.categories or t.feeds) and t.field
    fields = {p["field"] for p in presets.values()}
    assert {"Mathematics", "Statistics", "Computer science and AI", "Physics", "Astronomy",
            "Chemistry and materials", "Biology", "Medicine and health",
            "Economics and finance", "Engineering"} == fields


def test_preset_override_and_custom():
    presets = load_presets()
    t = resolve_topic({"preset": "probability", "top_k": 7}, presets)
    assert t.slug == "probability" and t.top_k == 7
    c = resolve_topic({"name": "Number theory", "slug": "nt", "categories": ["math.NT"],
                       "interest": "modular forms"}, presets)
    assert c.source == "arxiv"
    with pytest.raises(ValueError, match="unknown preset"):
        resolve_topic("not-a-preset", presets)
    with pytest.raises(ValueError, match="unknown field"):
        resolve_topic({"preset": "probability", "topk": 3}, presets)


def test_repo_config_loads():
    cfg = load_config(REPO / "config.yaml")
    slugs = [t.slug for t in cfg.topics]
    assert {"chemistry", "biology", "economics"} <= set(slugs)
    assert cfg.language == "en"


# ---------------------------------------------------------------- ranking

def make_topic(**kw):
    base = dict(name="ML theory", slug="ml", categories=["cs.LG"],
                interest="PAC-Bayes generalization bounds and sample complexity of neural networks",
                keywords=["PAC-Bayes", "generalization bound"], top_k=2)
    base.update(kw)
    return Topic(**base)


def test_relevant_paper_ranks_first(papers):
    ranked = score_papers(papers, make_topic())
    assert ranked[0].uid == "arxiv:2611.00002"
    assert ranked[0].matched_keywords == ["PAC-Bayes", "generalization bound"]
    assert ranked[0].score > by_uid(ranked, "arxiv:2611.00003").score


def test_keyword_is_whole_word(papers):
    assert matched_keywords(by_uid(papers, "arxiv:2611.00003"), ["Lean"]) == []   # "clean"
    assert matched_keywords(by_uid(papers, "arxiv:2611.00004"), ["Lean"]) == ["Lean"]


def test_scores_are_per_topic(papers):
    a = score_papers(papers, make_topic())
    b = score_papers(papers, make_topic(interest="Ricci flow curvature surfaces", keywords=[]))
    assert by_uid(a, "arxiv:math/0601001").score != by_uid(b, "arxiv:math/0601001").score


def test_assign_unique_no_duplicates(papers):
    ml = score_papers(papers, make_topic())
    prob = score_papers(papers, make_topic(slug="prob", interest="mean-field Langevin propagation of chaos",
                                           keywords=[]))
    chosen = assign_unique({"ml": ml, "prob": prob}, {"ml": 2, "prob": 2}, min_score=0.05)
    uids = [p.uid for ps in chosen.values() for p in ps]
    assert len(uids) == len(set(uids))
    assert "arxiv:2611.00002" in [p.uid for p in chosen["ml"]]
    assert "arxiv:2611.00001" in [p.uid for p in chosen["prob"]]


# ---------------------------------------------------------------- state and summaries

def test_state_roundtrip_and_v01_compat(tmp_path):
    path = tmp_path / "seen.json"
    path.write_text(json.dumps({"2611.00009": "2026-11-20"}))   # v0.1 format
    s = SeenState(path)
    assert s.is_seen("arxiv:2611.00009")
    s.mark(["a:1"], date(2026, 1, 1))
    s.prune(date(2026, 11, 22), keep_days=120)
    s.save()
    s2 = SeenState(path)
    assert not s2.is_seen("a:1") and s2.is_seen("arxiv:2611.00009")


@pytest.mark.parametrize("lang,diff", [("en", "research-level"), ("zh", "研究级")])
def test_parse_summary(lang, diff):
    reply = 'Sure:\n{"one_liner": "x", "why": "w", "background": "b", "difficulty": "%s"}' % diff
    out = parse_summary(reply, lang)
    assert out["difficulty"] == diff and out["ai"]
    assert parse_summary('{"one_liner": "x", "difficulty": "super hard"}', lang)["difficulty"] == ""
    with pytest.raises(ValueError):
        parse_summary("no json here", lang)


def test_fallback_summary_uses_first_sentence(papers):
    s = fallback_summary(by_uid(papers, "arxiv:2611.00002"))
    assert s["one_liner"].startswith("We derive non-vacuous PAC-Bayes")
    assert s["one_liner"].endswith(".") and not s["ai"]


def test_summarize_with_fake_client(papers, monkeypatch):
    """The AI path, with a fake `anthropic` module so no network or key is needed."""
    seen = {}

    class FakeMessages:
        def create(self, **kw):
            seen.update(kw)
            block = types.SimpleNamespace(type="tool_use", name="record_summary", input={
                "one_liner": "A PAC-Bayes bound", "plain": "p", "why": "w",
                "background": "probability", "difficulty": "intermediate"})
            return types.SimpleNamespace(content=[block], stop_reason="tool_use")

    fake = types.ModuleType("anthropic")
    fake.Anthropic = lambda **kw: types.SimpleNamespace(messages=FakeMessages())
    monkeypatch.setitem(sys.modules, "anthropic", fake)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")

    p = by_uid(papers, "arxiv:2611.00002")
    summarize_all([(p, "ML theory")], enabled=True, model="test-model", language="en")
    assert p.summary["ai"] and p.summary["difficulty"] == "intermediate" and p.summary["plain"] == "p"
    assert "Field: ML theory" in seen["messages"][0]["content"]
    assert seen["tool_choice"] == {"type": "tool", "name": "record_summary"}
    assert seen["tools"][0]["input_schema"]["properties"]["difficulty"]["enum"][-1] == "research-level"


def test_summarize_retries_then_falls_back(papers, monkeypatch):
    calls = []

    class Flaky:
        def create(self, **kw):
            calls.append(1)
            if len(calls) < 2:
                raise RuntimeError("overloaded")
            return types.SimpleNamespace(content=[types.SimpleNamespace(type="text", text="sorry")],
                                         stop_reason="end_turn")

    fake = types.ModuleType("anthropic")
    fake.Anthropic = lambda **kw: types.SimpleNamespace(messages=Flaky())
    monkeypatch.setitem(sys.modules, "anthropic", fake)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    monkeypatch.setattr("radar.summarize.time.sleep", lambda s: None)
    p = by_uid(papers, "arxiv:2611.00002")
    summarize_all([(p, "ML theory")], enabled=True, model="m")
    assert len(calls) == 3 and p.summary["ai"] is False     # 3 attempts, then the fallback


# ---------------------------------------------------------------- end to end

def write_config(tmp_path, **overrides):
    cfg = yaml.safe_load((REPO / "config.yaml").read_text(encoding="utf-8"))
    cfg.update(output_dir=str(tmp_path / "docs" / "digests"), site_dir=str(tmp_path / "docs"),
               state_path=str(tmp_path / "state" / "seen.json"),
               archive_path=str(tmp_path / "state" / "archive.jsonl"), **overrides)
    path = tmp_path / "config.yaml"
    path.write_text(yaml.safe_dump(cfg, allow_unicode=True), encoding="utf-8")
    return path


def test_offline_run_english(tmp_path, monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    args = Namespace(config=str(write_config(tmp_path)), no_summary=False,
                     offline=str(FIXTURES), dry_run=False, keep_paths=True)
    md = run(args).read_text(encoding="utf-8")

    assert "# Research digest" in md and "## Highlights" in md
    for name in ["Machine learning theory", "Chemical physics",
                 "Computational and systems biology", "Econometrics and applied economics"]:
        assert f"## {name}" in md
    assert "arXiv:2611.00005v1" in md                       # chemistry
    assert "arXiv:2611.00006v1" in md                       # economics
    assert "bioRxiv doi:10.1101/2026.11.20.000003 v1" in md  # biology (first versions only)
    assert "2026.11.18.000001" not in md                    # a revised preprint is skipped
    assert "Mitochondrial fission" not in md                # cell biology: not a chosen category
    assert "A faster GPU kernel" not in md                  # no theory keywords
    assert md.count("### [[TEST] Propagation of chaos") == 1
    assert "## Complex analysis\n\nNothing notable this time." in md
    # Liquid guard so GitHub Pages does not choke on "{{" in abstracts
    assert md.splitlines()[1] == "<!-- {% raw %} -->" and md.rstrip().endswith("<!-- {% endraw %} -->")
    # website data
    data = tmp_path / "docs" / "data"
    index = json.loads((data / "topics.json").read_text(encoding="utf-8"))
    slugs = [t["slug"] for t in index["topics"]]
    assert "harmonic-analysis" in slugs and "economics" in slugs and "biology" in slugs
    assert index["fields"][0] == "Mathematics" and "Chemistry and materials" in index["fields"]
    ml = json.loads((data / "topics" / "ml-theory.json").read_text(encoding="utf-8"))
    assert [p["uid"] for p in ml["papers"]][0] == "arxiv:2611.00002"
    assert ml["papers"][0]["summary"]["one_liner"].startswith("We derive")
    assert next(t for t in index["topics"] if t["slug"] == "ml-theory")["new_today"] == len(ml["papers"])
    sitemap = (tmp_path / "docs" / "sitemap.xml").read_text(encoding="utf-8")
    assert "<loc>https://xfx689781.github.io/research-radar/</loc>" in sitemap
    site = json.loads((data / "site.json").read_text(encoding="utf-8"))
    assert site["title"] == "Research Radar" and set(site) == {"title", "supabase_url", "supabase_anon_key"}

    # a second run the same day redoes today's selection (e.g. after adding an API key)
    md2 = run(args).read_text(encoding="utf-8")
    assert "2611.00002" in md2
    archive = (tmp_path / "state" / "archive.jsonl").read_text(encoding="utf-8").splitlines()
    assert len(archive) == len(set(json.loads(l)["uid"] for l in archive))   # no duplicates


def test_offline_run_chinese(tmp_path, monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    args = Namespace(config=str(write_config(tmp_path, language="zh")), no_summary=True,
                     offline=str(FIXTURES), dry_run=True, keep_paths=True)
    md = run(args).read_text(encoding="utf-8")
    assert "# 研究进展简报" in md and "## 化学物理" in md and "## 复分析\n\n这次无重点。" in md


def test_offline_sources_helper():
    off = sources.load_offline(FIXTURES)
    assert len(off["arxiv"]) == 7 and len(off["biorxiv"]) == 3 and off["medrxiv"] == []


def test_include_revisions(tmp_path, monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    args = Namespace(config=str(write_config(tmp_path, include_revisions=True)), no_summary=True,
                     offline=str(FIXTURES), dry_run=True, keep_paths=True)
    md = run(args).read_text(encoding="utf-8")
    assert "bioRxiv doi:10.1101/2026.11.18.000001 v2" in md


def test_zscores_are_standardized(papers):
    ranked = score_papers(papers, make_topic())
    z = [p.zscore for p in ranked]
    assert abs(sum(z)) < 1e-9 and z[0] == max(z) > 0


def test_top_k_per_topic_override(tmp_path):
    cfg = load_config(write_config(tmp_path, top_k_per_topic=1))
    assert {t.top_k for t in cfg.topics if t.slug != "ai-news"} == {1}


def test_seen_papers_are_skipped_on_later_days(tmp_path, papers):
    path = tmp_path / "seen.json"
    s = SeenState(path)
    s.mark(["arxiv:2611.00002"], date(2026, 11, 21))
    s.forget_day(date(2026, 11, 22))          # forgetting today keeps yesterday's marks
    assert s.is_seen("arxiv:2611.00002")
    s.forget_day(date(2026, 11, 21))
    assert not s.is_seen("arxiv:2611.00002")


def test_archive_roundtrip(tmp_path, papers):
    from radar.archive import Archive, to_paper
    a = Archive(tmp_path / "a.jsonl")
    p = papers[0]
    p.summary = {"one_liner": "x", "ai": True}
    a.add({"prob": [p]}, date(2026, 11, 20))
    a.add({"prob": [papers[1]]}, date(2026, 11, 22))
    a.add({"prob": [papers[2]]}, date(2026, 11, 22))   # same day: replaces that day's entries
    a.prune(date(2026, 11, 22), keep_days=30)
    a.save()
    b = Archive(tmp_path / "a.jsonl")
    recs = b.for_topic("prob")
    assert [r["uid"] for r in recs] == [papers[2].uid, p.uid]
    assert b.count_on("prob", date(2026, 11, 22)) == 1
    back = to_paper(recs[1])
    assert back.title == p.title and back.summary["one_liner"] == "x"
    a.prune(date(2027, 1, 1), keep_days=30)
    assert a.records == []


def test_primary_only_drops_cross_lists(tmp_path, monkeypatch):
    """With primary_only, a math.PR paper cross-listed to stat.ML is not an ML-theory paper."""
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    cfg_path = write_config(tmp_path)
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    cfg["topics"] = [{"preset": "ml-theory", "primary_only": True}, "probability"]
    cfg_path.write_text(yaml.safe_dump(cfg), encoding="utf-8")
    args = Namespace(config=str(cfg_path), no_summary=True, offline=str(FIXTURES),
                     dry_run=True, keep_paths=True)
    md = run(args).read_text(encoding="utf-8")
    ml = md.split("## Machine learning theory")[1].split("## Probability")[0]
    assert "2611.00002" in ml and "2611.00001" not in ml   # 00001 is primary math.PR


@pytest.mark.parametrize("raw,norm", [("Cell_Biology", "cell biology"),
                                      ("Infectious Diseases (except HIV/AIDS)", "infectious diseases"),
                                      ("  systems   biology ", "systems biology")])
def test_category_normalization(raw, norm):
    assert biorxiv.normalize_category(raw) == norm


def test_biorxiv_falls_back_when_category_unknown(monkeypatch):
    """If the API returns nothing for a category name, scan the window once and filter."""
    every = {"messages": [{"total": 2}], "collection": [
        {"doi": "10.1/x", "version": "1", "category": "Infectious Diseases (except HIV/AIDS)",
         "title": "X", "abstract": "a", "date": "2026-11-20"},
        {"doi": "10.1/y", "version": "1", "category": "oncology", "title": "Y",
         "abstract": "a", "date": "2026-11-20"}]}
    calls = []

    def fake_get_json(url):
        calls.append(url)
        return {"messages": [{"total": 0}], "collection": []} if "category=" in url else every

    monkeypatch.setattr(biorxiv, "get_json", fake_get_json)
    monkeypatch.setattr(biorxiv, "DELAY", 0)
    biorxiv._ALL.clear()
    out = biorxiv.search("medrxiv", ["infectious diseases"], [], date(2026, 11, 15), date(2026, 11, 22))
    assert [p.uid for p in out] == ["medrxiv:10.1/x"]
    out2 = biorxiv.search("medrxiv", ["oncology"], [], date(2026, 11, 15), date(2026, 11, 22))
    assert [p.uid for p in out2] == ["medrxiv:10.1/y"]
    assert sum("category=" not in u for u in calls) == 1     # the full scan happened only once


# ---------------------------------------------------------------- news (RSS)

def test_rss_parse_and_clean():
    from radar.sources import rss
    items = rss.parse_feed((FIXTURES / "rss.xml").read_text(encoding="utf-8"),
                           "https://news.example.org/feed")
    assert len(items) == 2                                     # the http:// item is skipped
    first = items[0]
    assert first.source == "rss" and first.uid.startswith("news:")
    assert first.label == "Example AI News" and first.authors == ["Test Reporter"]
    assert first.abstract == "The lab says the new model uses a mixture of experts & a longer context window."
    assert first.published == datetime(2026, 11, 20, 10, tzinfo=timezone.utc)


def test_atom_parse():
    from radar.sources import rss
    atom = """<feed xmlns="http://www.w3.org/2005/Atom"><title>Lab blog</title>
      <entry><title>Hello</title><link href="https://lab.example.org/hello"/>
      <published>2026-11-21T09:00:00Z</published><summary>Short teaser.</summary>
      <author><name>A. Writer</name></author></entry></feed>"""
    [p] = rss.parse_feed(atom, "https://lab.example.org/atom")
    assert p.title == "Hello" and p.url == "https://lab.example.org/hello" and p.authors == ["A. Writer"]


def test_rss_search_window_and_bad_feed(monkeypatch):
    from radar.sources import rss
    good = (FIXTURES / "rss.xml").read_text(encoding="utf-8")

    def fake_get(url, retries=2):
        if "broken" in url:
            raise OSError("down")
        return good

    monkeypatch.setattr(rss, "get_text", fake_get)
    out = rss.search(["https://broken.example.org/feed", "https://news.example.org/feed"], [],
                     datetime(2026, 11, 20, tzinfo=timezone.utc), datetime(2026, 11, 22, tzinfo=timezone.utc))
    assert [p.title for p in out] == ["[TEST] Example Lab releases an open-weight mixture-of-experts language model"]


def test_ai_news_topic_in_offline_run(tmp_path, monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    args = Namespace(config=str(write_config(tmp_path)), no_summary=True, offline=str(FIXTURES),
                     dry_run=True, keep_paths=True)
    md = run(args).read_text(encoding="utf-8")
    news = md.split("## AI industry news")[1].split("\n## ")[0]
    assert "mixture-of-experts" in news and "Example AI News" in news
    data = json.loads((tmp_path / "docs" / "data" / "topics" / "ai-news.json").read_text())
    assert data["papers"][0]["source"] == "rss"


def test_topic_top_k_beats_global_default(tmp_path):
    cfg = load_config(write_config(tmp_path, top_k_per_topic=2))
    k = {t.slug: t.top_k for t in cfg.topics}
    assert k["ai-news"] == 5 and k["probability"] == 2


def test_rss_topic_needs_feeds():
    with pytest.raises(ValueError, match="no feeds"):
        resolve_topic({"name": "N", "slug": "n", "source": "rss", "interest": "x"}, load_presets())


def test_rate_limit_waits_longer():
    import urllib.error
    from radar.sources.http import wait_seconds
    e429 = urllib.error.HTTPError("u", 429, "Too Many", {}, None)
    assert wait_seconds(e429, 1) == 20 and wait_seconds(e429, 3) == 60
    assert wait_seconds(OSError("x"), 2) == 10


# ---------------------------------------------------------------- backfill

def test_backfill_spreads_papers_over_days(tmp_path, monkeypatch):
    """With --backfill, each paper lands on the morning after it was posted."""
    import radar.__main__ as main_mod

    class FixedDate(datetime):
        @classmethod
        def now(cls, tz=None):
            return datetime(2026, 11, 22, 13, 0, tzinfo=timezone.utc)

    monkeypatch.setattr(main_mod, "datetime", FixedDate)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    args = Namespace(config=str(write_config(tmp_path)), no_summary=True, offline=str(FIXTURES),
                     dry_run=False, keep_paths=True, backfill=7)
    run(args)
    from radar.archive import Archive
    a = Archive(tmp_path / "state" / "archive.jsonl")
    day = {r["uid"]: r["date"] for r in a.records}
    assert day["arxiv:2611.00001"] == "2026-11-18"     # posted Nov 17
    assert day["arxiv:2611.00002"] == "2026-11-20"     # posted Nov 19
    assert day["arxiv:2611.00006"] == "2026-11-22"     # posted Nov 21
    assert len(set(day.values())) >= 3


# ---------------------------------------------------------------- daily email

def test_build_email(tmp_path, papers):
    from radar.archive import Archive
    from radar.mailer import build_email
    cfg = load_config(write_config(tmp_path))
    a = Archive(tmp_path / "a.jsonl")
    p = by_uid(papers, "arxiv:2611.00002")
    p.summary = {"plain": "Big networks <b>generalize</b>.", "ai": True}
    a.add({"ml-theory": [p]}, date(2026, 11, 22))
    subject, text, body = build_email(["ml-theory", "probability", "gone"], a, cfg,
                                      date(2026, 11, 22), "https://site.example/")
    assert "1 new" in subject and p.url in text
    assert "&lt;b&gt;generalize&lt;/b&gt;" in body and "<b>generalize" not in body   # escaped
    assert "MACHINE LEARNING THEORY" in text and "Unsubscribe" not in text   # no token, no link
    _, text2, body2 = build_email(["ml-theory"], a, cfg, date(2026, 11, 22), "https://site.example/",
                                  "https://site.example/?unsubscribe=abc")
    assert "Unsubscribe: https://site.example/?unsubscribe=abc" in text2 and "?unsubscribe=abc" in body2
    assert build_email(["probability"], a, cfg, date(2026, 11, 22), "x") is None


def test_send_daily_with_fake_services(tmp_path, papers, monkeypatch):
    import radar.mailer as mailer
    from radar.archive import Archive
    cfg = load_config(write_config(tmp_path, supabase_url="https://db.example.co"))
    a = Archive(tmp_path / "a.jsonl")
    a.add({"ml-theory": [by_uid(papers, "arxiv:2611.00002")]}, date(2026, 11, 22))

    monkeypatch.setattr(mailer, "fetch_subscribers", lambda url, key: [
        {"email": "a@example.org", "topics": ["ml-theory"], "unsubscribe_token": "tok-1"},
        {"email": "b@example.org", "topics": ["probability"]}])          # nothing today for b
    sent = []

    class FakeSMTP:
        def __init__(self, *a, **k): pass
        def __enter__(self): return self
        def __exit__(self, *a): return False
        def login(self, u, p): sent.append(("login", u))
        def send_message(self, m):
            sent.append(("to", m["To"]))
            assert "unsubscribe=tok-1" in m["List-Unsubscribe"] and "mailto:me@example.org" in m["List-Unsubscribe"]

    monkeypatch.setattr(mailer.smtplib, "SMTP_SSL", FakeSMTP)
    monkeypatch.setattr(mailer.time, "sleep", lambda s: None)
    for k, v in {"SUPABASE_SECRET_KEY": "sb_secret_x", "SMTP_HOST": "smtp.example.org",
                 "SMTP_USER": "me@example.org", "SMTP_PASSWORD": "pw"}.items():
        monkeypatch.setenv(k, v)
    assert mailer.send_daily(cfg, a, date(2026, 11, 22)) == 1
    assert sent == [("login", "me@example.org"), ("to", "a@example.org")]


def test_send_daily_skips_without_secrets(tmp_path, monkeypatch):
    import radar.mailer as mailer
    from radar.archive import Archive
    for k in ("SUPABASE_SECRET_KEY", "SMTP_HOST", "SMTP_USER", "SMTP_PASSWORD"):
        monkeypatch.delenv(k, raising=False)
    cfg = load_config(write_config(tmp_path))
    assert mailer.send_daily(cfg, Archive(tmp_path / "x.jsonl"), date(2026, 11, 22)) is None


# ---------------------------------------------------------------- time budget and healing

def fake_anthropic(monkeypatch, calls):
    class M:
        def create(self, **kw):
            calls.append(kw["messages"][0]["content"])
            return types.SimpleNamespace(stop_reason="tool_use", content=[types.SimpleNamespace(
                type="tool_use", input={"one_liner": "o", "plain": "p", "why": "w",
                                        "background": "b", "difficulty": "intermediate"})])
    fake = types.ModuleType("anthropic")
    fake.Anthropic = lambda **kw: types.SimpleNamespace(messages=M())
    monkeypatch.setitem(sys.modules, "anthropic", fake)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")


def test_deadline_stops_new_summaries(papers, monkeypatch):
    import time as _time
    calls = []
    fake_anthropic(monkeypatch, calls)
    summarize_all([(p, "T") for p in papers[:3]], enabled=True, model="m",
                  deadline=_time.monotonic() - 1)                  # already past
    assert calls == [] and all(not p.summary["ai"] for p in papers[:3])


def test_heal_archive_fills_missing_summaries(tmp_path, papers, monkeypatch):
    from radar.__main__ import heal_archive
    from radar.archive import Archive
    calls = []
    fake_anthropic(monkeypatch, calls)
    cfg = load_config(write_config(tmp_path))
    a = Archive(tmp_path / "a.jsonl")
    old, done = papers[0], papers[1]
    old.summary = {"one_liner": "x", "ai": False}
    done.summary = {"one_liner": "y", "ai": True}
    a.add({"probability": [old], "ml-theory": [done]}, date(2026, 11, 20))
    n = heal_archive(a, cfg, {"probability": "Probability", "ml-theory": "ML"}, deadline=None)
    assert n == 1 and len(calls) == 1
    rec = next(r for r in a.records if r["uid"] == old.uid)
    assert rec["summary"]["ai"] and rec["summary"]["plain"] == "p"


# ---------------------------------------------------------------- arXiv daily listings (RSS)

def test_parse_arxiv_rss():
    from radar.sources.arxiv import parse_rss
    ps = parse_rss((FIXTURES / "arxiv_rss.xml").read_text(encoding="utf-8"))
    assert [p.uid for p in ps] == ["arxiv:2611.90001", "arxiv:2611.90002"]   # "replace" skipped
    p = ps[0]
    assert p.label == "arXiv:2611.90001v1" and p.version == 1
    assert p.abstract.startswith("We study the mean-field limit")
    assert p.authors == ["Test Author A", "Test Author B"]
    assert p.primary_category == "math.PR" and p.categories == ["math.PR", "cs.LG"]
    assert p.pdf_url == "https://arxiv.org/pdf/2611.90001"


def test_daily_arxiv_uses_few_requests(monkeypatch):
    from radar.sources import arxiv
    body = (FIXTURES / "arxiv_rss.xml").read_text(encoding="utf-8")
    urls = []
    monkeypatch.setattr(arxiv, "get_text", lambda url: urls.append(url) or body)
    monkeypatch.setattr(arxiv, "DELAY", 0)
    cfg = load_config(REPO / "config.yaml")
    n = sources.load_arxiv_today(cfg.topics)
    try:
        cats = {c for t in cfg.topics if t.source == "arxiv" for c in t.categories}
        assert len(urls) == -(-len(cats) // arxiv.RSS_CHUNK)          # ceil(categories / chunk)
        assert all(u.startswith("https://rss.arxiv.org/rss/") for u in urls)
        assert n == 2                                                  # de-duplicated across chunks
        ml = next(t for t in cfg.topics if t.slug == "ml-theory")
        prob = next(t for t in cfg.topics if t.slug == "probability")
        assert not sources.uses_network(ml)
        assert [p.uid for p in sources.fetch(ml, None, None, 600)] == ["arxiv:2611.90001"]  # keyword match
        assert [p.uid for p in sources.fetch(prob, None, None, 600)] == ["arxiv:2611.90001"]
    finally:
        sources.clear_arxiv_today()
    assert sources.uses_network(ml)


def test_http_handles_gzip_and_bom(monkeypatch):
    import gzip as _gzip
    from radar.sources import http

    class Resp:
        headers = {"Content-Encoding": "gzip"}
        def __enter__(self): return self
        def __exit__(self, *a): return False
        def read(self): return _gzip.compress("﻿<rss/>".encode("utf-8"))

    monkeypatch.setattr(http.urllib.request, "urlopen", lambda req, timeout: Resp())
    assert http.get_text("https://example.org/feed") == "<rss/>"


# ---------------------------------------------------------------- Discord

def _archive_with(tmp_path, papers, day=date(2026, 11, 22)):
    from radar.archive import Archive
    a = Archive(tmp_path / "a.jsonl")
    ps = []
    for i, p in enumerate(papers):
        p.score = 1.0 - i / 100
        p.summary = {"plain": f"plain {i}", "ai": True}
        ps.append(p)
    a.add({"ml-theory": ps[:4], "probability": ps[4:5], "ai-news": ps[5:]}, day)
    return a


def test_discord_highlights_one_per_topic_first(tmp_path, papers):
    from radar.discord import pick_items
    cfg = load_config(write_config(tmp_path))
    a = _archive_with(tmp_path, papers)
    items = pick_items(cfg, a, date(2026, 11, 22))
    assert len({r["topic"] for r in items}) == len(items)     # no topic twice in highlights
    cfg.discord_topics = ["probability", "ml-theory"]
    items = pick_items(cfg, a, date(2026, 11, 22))
    assert [r["topic"] for r in items] == ["probability"] + ["ml-theory"] * 4


def test_discord_messages_and_posting(tmp_path, papers, monkeypatch):
    import radar.discord as discord
    cfg = load_config(write_config(tmp_path))
    items = [{"title": f"T{i}", "url": f"https://x/{i}", "topic": "ml-theory", "label": "arXiv:1",
              "summary": {"plain": "word " * 200}} for i in range(12)]
    msgs = discord.build_messages(items, cfg, date(2026, 11, 22))
    assert [len(m["embeds"]) for m in msgs] == [10, 2]
    assert msgs[0]["content"].startswith("**Research Radar") and "content" not in msgs[1]
    assert all(m["allowed_mentions"] == {"parse": []} for m in msgs)
    assert len(msgs[0]["embeds"][0]["description"]) <= discord.DESCRIPTION_CHARS

    posted = []
    monkeypatch.setattr(discord, "_post", lambda url, payload: posted.append((url, payload)))
    monkeypatch.setattr(discord.time, "sleep", lambda s: None)
    monkeypatch.delenv("DISCORD_WEBHOOK_URL", raising=False)
    a = _archive_with(tmp_path, papers)
    assert discord.post_daily(cfg, a, date(2026, 11, 22)) is None and posted == []   # no secret: skip
    monkeypatch.setenv("DISCORD_WEBHOOK_URL", "https://discord.example/webhook")
    assert discord.post_daily(cfg, a, date(2026, 11, 22)) == 1
    assert posted[0][0] == "https://discord.example/webhook"
    assert discord.post_daily(cfg, a, date(2026, 11, 23)) == 0                    # nothing that day


# ---------------------------------------------------------------- once-a-day guards

def test_skip_if_done(tmp_path, monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    cfg_path = write_config(tmp_path, runs_path=str(tmp_path / "state" / "runs.json"))
    args = Namespace(config=str(cfg_path), no_summary=True, offline=str(FIXTURES), dry_run=False,
                     keep_paths=True, skip_if_done=True)
    assert run(args) is not None                 # first run of the day builds
    assert run(args) is None                     # a later scheduled run skips
    args.skip_if_done = False
    assert run(args) is not None                 # a manual run still rebuilds


def test_notify_sends_once_a_day_and_retries_failures(tmp_path, monkeypatch):
    import radar.__main__ as main_mod
    cfg_path = write_config(tmp_path, runs_path=str(tmp_path / "runs.json"))
    calls = {"email": 0, "discord": 0}
    outcome = {"email": "fail", "discord": None}

    def fake_email(cfg, archive, today, dry_run):
        calls["email"] += 1
        if outcome["email"] == "fail":
            raise RuntimeError("401")
        return 1

    def fake_discord(cfg, archive, today, dry_run):
        calls["discord"] += 1
        return outcome["discord"]

    monkeypatch.setattr(main_mod, "send_daily", fake_email)
    monkeypatch.setattr(main_mod, "post_daily", fake_discord)
    args = Namespace(cmd="notify", config=str(cfg_path), dry_run=False, force=False)
    assert main_mod.notify(args) is False        # email failed: not marked done
    outcome["email"] = "ok"; outcome["discord"] = 2
    assert main_mod.notify(args) is True         # retried; discord now set up
    assert main_mod.notify(args) is True         # both done today: nothing sent again
    assert calls == {"email": 2, "discord": 2}


def test_fetch_subscribers_without_unsubscribe_column(monkeypatch):
    import io
    import urllib.error
    import radar.mailer as mailer
    seen = []

    class Resp(io.BytesIO):
        def __enter__(self): return self
        def __exit__(self, *a): return False

    def fake_urlopen(req, timeout):
        seen.append(req.full_url)
        if "unsubscribe_token" in req.full_url:
            raise urllib.error.HTTPError(req.full_url, 400, "Bad Request", {}, io.BytesIO(
                b'{"message":"column preferences.unsubscribe_token does not exist"}'))
        return Resp(b'[{"email": "a@example.org", "topics": ["probability"]}, {"email": null, "topics": []}]')

    monkeypatch.setattr(mailer.urllib.request, "urlopen", fake_urlopen)
    rows = mailer.fetch_subscribers("https://db.example.co", "sb_secret_x")
    assert rows == [{"email": "a@example.org", "topics": ["probability"]}] and len(seen) == 2


def test_fetch_subscribers_reports_other_errors(monkeypatch):
    import io
    import urllib.error
    import radar.mailer as mailer

    def fake_urlopen(req, timeout):
        raise urllib.error.HTTPError(req.full_url, 401, "Unauthorized", {}, io.BytesIO(b'{"message":"Invalid API key"}'))

    monkeypatch.setattr(mailer.urllib.request, "urlopen", fake_urlopen)
    with pytest.raises(RuntimeError, match="401.*Invalid API key"):
        mailer.fetch_subscribers("https://db.example.co", "sb_secret_x")
