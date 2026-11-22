from argparse import Namespace
from datetime import date, datetime, timezone
from pathlib import Path

import pytest
import yaml

from radar.__main__ import run
from radar.arxiv_client import ArxivError, build_query, parse_feed
from radar.config import Topic
from radar.rank import assign_unique, matched_keywords, score_papers
from radar.state import SeenState
from radar.summarize import fallback_summary, parse_summary

FIXTURE = Path(__file__).parent / "fixtures" / "sample_feed.xml"


@pytest.fixture
def papers():
    return parse_feed(FIXTURE.read_text(encoding="utf-8"))


def by_id(papers, i):
    return next(p for p in papers if p.arxiv_id == i)


# ---------------------------------------------------------------- arxiv client

def test_parse_feed(papers):
    assert len(papers) == 5
    p = by_id(papers, "2611.00001")
    assert p.version == "v2"
    assert p.title == "[TEST] Propagation of chaos for mean-field Langevin dynamics"
    assert p.authors == ["Test Author A", "Test Author B"]
    assert p.primary_category == "math.PR"
    assert p.categories == ["math.PR", "stat.ML"]
    assert p.url.startswith("https://")
    assert p.pdf_url == "https://arxiv.org/pdf/2611.00001v2"
    assert p.published == datetime(2026, 11, 17, 18, tzinfo=timezone.utc)


def test_old_style_id(papers):
    p = by_id(papers, "math/0601001")
    assert p.version == "v1"


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


# ---------------------------------------------------------------- ranking

def make_topic(**kw):
    base = dict(name="ML 理论", slug="ml", categories=["cs.LG"],
                interest="PAC-Bayes generalization bounds and sample complexity of neural networks",
                keywords=["PAC-Bayes", "generalization bound"], top_k=2)
    base.update(kw)
    return Topic(**base)


def test_relevant_paper_ranks_first(papers):
    ranked = score_papers(papers, make_topic())
    assert ranked[0].arxiv_id == "2611.00002"
    assert ranked[0].matched_keywords == ["PAC-Bayes", "generalization bound"]
    assert ranked[0].score > by_id(ranked, "2611.00003").score


def test_keyword_is_whole_word(papers):
    gpu = by_id(papers, "2611.00003")           # abstract contains "clean"
    lean = by_id(papers, "2611.00004")
    assert matched_keywords(gpu, ["Lean"]) == []
    assert matched_keywords(lean, ["Lean"]) == ["Lean"]


def test_scores_are_per_topic(papers):
    a = score_papers(papers, make_topic())
    b = score_papers(papers, make_topic(interest="Ricci flow curvature surfaces", keywords=[]))
    # same paper, different topics, independent scores
    assert by_id(a, "math/0601001").score != by_id(b, "math/0601001").score


def test_assign_unique_no_duplicates(papers):
    ml = score_papers(papers, make_topic())
    prob = score_papers(papers, make_topic(slug="prob", interest="mean-field Langevin propagation of chaos",
                                           keywords=[]))
    chosen = assign_unique({"ml": ml, "prob": prob}, {"ml": 2, "prob": 2}, min_score=0.05)
    ids = [p.arxiv_id for ps in chosen.values() for p in ps]
    assert len(ids) == len(set(ids))
    assert "2611.00002" in [p.arxiv_id for p in chosen["ml"]]
    assert "2611.00001" in [p.arxiv_id for p in chosen["prob"]]
    assert all(len(ps) <= 2 for ps in chosen.values())


# ---------------------------------------------------------------- state and summaries

def test_state_roundtrip(tmp_path):
    path = tmp_path / "seen.json"
    s = SeenState(path)
    s.mark(["a", "b"], date(2026, 1, 1))
    s.mark(["c"], date(2026, 11, 1))
    s.prune(date(2026, 11, 22), keep_days=120)
    s.save()
    s2 = SeenState(path)
    assert not s2.is_seen("a") and s2.is_seen("c")


def test_parse_summary_accepts_wrapped_json():
    reply = 'Sure:\n{"one_liner": "证明了一个界", "why": "w", "background": "测度论", "difficulty": "中等"}'
    out = parse_summary(reply)
    assert out["one_liner"] == "证明了一个界" and out["difficulty"] == "中等" and out["ai"]


def test_parse_summary_rejects_bad_reply():
    with pytest.raises(ValueError):
        parse_summary("no json here")
    assert parse_summary('{"one_liner": "x", "difficulty": "超难"}')["difficulty"] == ""


def test_fallback_summary_uses_first_sentence(papers):
    s = fallback_summary(by_id(papers, "2611.00002"))
    assert s["one_liner"].startswith("We derive non-vacuous PAC-Bayes")
    assert s["one_liner"].endswith(".") and not s["ai"]


# ---------------------------------------------------------------- end to end

def test_offline_run(tmp_path, monkeypatch):
    cfg = yaml.safe_load((Path(__file__).parents[1] / "config.yaml").read_text(encoding="utf-8"))
    cfg["output_dir"] = str(tmp_path / "digests")
    cfg["state_path"] = str(tmp_path / "state" / "seen.json")
    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(cfg, allow_unicode=True), encoding="utf-8")
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)

    args = Namespace(config=str(cfg_path), no_summary=False, offline=str(FIXTURE), dry_run=False)
    out = run(args)
    md = out.read_text(encoding="utf-8")

    assert "## 本周必读" in md
    for name in ["ML 理论", "概率", "微分几何", "AI4Math", "复分析"]:
        assert f"## {name}" in md
    assert "2611.00002" in md and "2611.00004" in md
    assert "A faster GPU kernel" not in md           # no theory keywords: filtered out
    assert md.count("### [[TEST] Propagation of chaos") == 1   # cross-listed, shown once
    assert "## 复分析\n\n本周无重点。" in md

    # second run: everything already recommended, so nothing repeats
    md2 = run(args).read_text(encoding="utf-8")
    assert "2611.00002" not in md2.split("## 抓取统计")[0]


def test_summarize_with_fake_client(papers, monkeypatch):
    """The AI path, with a fake `anthropic` module so no network or key is needed."""
    import sys
    import types

    from radar.summarize import summarize_all

    class FakeMessages:
        def create(self, **kw):
            assert "PAC-Bayes" in kw["messages"][0]["content"]
            block = types.SimpleNamespace(type="text", text=
                '{"one_liner": "给出非平凡的 PAC-Bayes 界", "why": "w", '
                '"background": "概率论", "difficulty": "研究级"}')
            return types.SimpleNamespace(content=[block])

    fake = types.ModuleType("anthropic")
    fake.Anthropic = lambda: types.SimpleNamespace(messages=FakeMessages())
    monkeypatch.setitem(sys.modules, "anthropic", fake)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")

    p = by_id(papers, "2611.00002")
    summarize_all([(p, "ML 理论")], enabled=True, model="test-model")
    assert p.summary["ai"] and p.summary["difficulty"] == "研究级"
