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
        assert t.name and t.interest and t.categories and t.field
    fields = {p["field"] for p in presets.values()}
    assert {"Chemistry", "Biology", "Economics"} <= fields


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
            block = types.SimpleNamespace(text='{"one_liner": "A PAC-Bayes bound", "plain": "p", "why": "w", '
                                               '"background": "probability", "difficulty": "intermediate"}')
            return types.SimpleNamespace(content=[block])

    fake = types.ModuleType("anthropic")
    fake.Anthropic = lambda: types.SimpleNamespace(messages=FakeMessages())
    monkeypatch.setitem(sys.modules, "anthropic", fake)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")

    p = by_uid(papers, "arxiv:2611.00002")
    summarize_all([(p, "ML theory")], enabled=True, model="test-model", language="en")
    assert p.summary["ai"] and p.summary["difficulty"] == "intermediate" and p.summary["plain"] == "p"
    assert "Field: ML theory" in seen["messages"][0]["content"]


# ---------------------------------------------------------------- end to end

def write_config(tmp_path, **overrides):
    cfg = yaml.safe_load((REPO / "config.yaml").read_text(encoding="utf-8"))
    cfg.update(output_dir=str(tmp_path / "docs" / "digests"), site_dir=str(tmp_path / "docs"),
               state_path=str(tmp_path / "state" / "seen.json"), **overrides)
    path = tmp_path / "config.yaml"
    path.write_text(yaml.safe_dump(cfg, allow_unicode=True), encoding="utf-8")
    return path


def test_offline_run_english(tmp_path, monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    args = Namespace(config=str(write_config(tmp_path)), no_summary=False,
                     offline=str(FIXTURES), dry_run=False, keep_paths=True)
    md = run(args).read_text(encoding="utf-8")

    assert "# Research digest" in md and "## Highlights" in md
    for name in ["Machine learning theory", "Chemistry and materials",
                 "Computational and systems biology", "Economics"]:
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
    # website home page
    index = (tmp_path / "docs" / "index.md").read_text(encoding="utf-8")
    assert index.startswith("# Research Radar")
    assert "](digests/" in index and "## All digests" in index

    # second run: everything already recommended, so nothing repeats
    md2 = run(args).read_text(encoding="utf-8")
    assert "2611.00002" not in md2.split("## Fetch statistics")[0]


def test_offline_run_chinese(tmp_path, monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    args = Namespace(config=str(write_config(tmp_path, language="zh")), no_summary=True,
                     offline=str(FIXTURES), dry_run=True, keep_paths=True)
    md = run(args).read_text(encoding="utf-8")
    assert "# 研究进展简报" in md and "## 化学与材料" in md and "## 复分析\n\n这次无重点。" in md


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
    assert {t.top_k for t in cfg.topics} == {1}


def test_index_lists_digests_newest_first(tmp_path):
    from radar.site import build_index
    d = tmp_path / "docs" / "digests"
    d.mkdir(parents=True)
    for name in ["2026-11-20.md", "2026-11-22.md", "latest.md"]:
        (d / name).write_text("x")
    cfg = load_config(REPO / "config.yaml")
    index = build_index(tmp_path / "docs", d, cfg.topics[:2], [], {}, 0).read_text()
    assert index.index("2026-11-22") < index.index("2026-11-20")
    assert "latest.md" not in index.split("## All digests")[1]
