"""Rank papers by how well they match a topic's interest profile.

v0.1 uses TF-IDF + cosine similarity against short "facets" of the interest
text, plus a small boost for explicit keywords.
It is simple, fast, needs no GPU, and every score can be explained.
(Upgrading to sentence embeddings is a good next step: see README.)
"""

from __future__ import annotations

import re
from dataclasses import replace

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .config import Topic
from .models import Paper, matched_keywords

KEYWORD_BOOST = 0.08
MAX_BOOST = 0.24


_TOKEN = re.compile(r"[a-z][a-z0-9\-]+")


def _singular(word: str) -> str:
    """Crude plural stripping so "flows" matches "flow" and "bounds" matches "bound".

    It is applied to profile and papers alike, so a wrong cut ("process" -> "proces")
    does no harm: both sides are cut the same way.
    """
    if len(word) > 4 and word.endswith("ies"):
        return word[:-3] + "y"
    if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def analyze(text: str) -> list[str]:
    """Tokens and bigrams, lowercased, stop words removed, plurals stripped."""
    toks = [_singular(t) for t in _TOKEN.findall(text.lower()) if t not in ENGLISH_STOP_WORDS]
    return toks + [f"{a} {b}" for a, b in zip(toks, toks[1:])]


def interest_facets(topic: Topic, seed_texts: list[str] | None = None) -> list[str]:
    """Split the interest text into short facets, e.g. "geometric flows".

    A long profile dilutes cosine similarity: a paper about one facet looks only
    weakly similar to the whole list. Scoring against each facet separately and
    taking the best match fixes that.
    """
    facets = [f.strip() for f in re.split(r"[,;:.\n]", topic.interest) if f.strip()]
    return [topic.interest, *facets, *(seed_texts or [])]


def score_papers(papers: list[Paper], topic: Topic,
                 seed_texts: list[str] | None = None) -> list[Paper]:
    """Set paper.score for each paper and return them sorted, best first.

    score = max over facets of cos(paper, facet) + keyword boost, where the
    facets are the whole interest text, each comma-separated part of it, and
    the abstract of each seed paper.
    """
    if not papers:
        return []
    # Work on copies: the same paper may be scored for several topics,
    # and each topic needs its own score.
    papers = [replace(p) for p in papers]

    facets = interest_facets(topic, seed_texts)
    vectorizer = TfidfVectorizer(analyzer=analyze, sublinear_tf=True)
    matrix = vectorizer.fit_transform(facets + [p.text for p in papers])
    sims = cosine_similarity(matrix[len(facets):], matrix[:len(facets)]).max(axis=1)

    for paper, sim in zip(papers, sims):
        hits = matched_keywords(paper, topic.keywords)
        paper.matched_keywords = hits
        paper.score = float(sim) + min(MAX_BOOST, KEYWORD_BOOST * len(hits))

    # How unusual is this paper within its own topic? Raw scores are not comparable
    # across topics (topics with keywords score higher), z-scores are.
    scores = [p.score for p in papers]
    mean = sum(scores) / len(scores)
    std = (sum((s - mean) ** 2 for s in scores) / len(scores)) ** 0.5
    for paper in papers:
        paper.zscore = (paper.score - mean) / std if std > 0 else 0.0

    return sorted(papers, key=lambda p: p.score, reverse=True)


def assign_unique(ranked: dict[str, list[Paper]], top_k: dict[str, int],
                  min_score: float) -> dict[str, list[Paper]]:
    """Pick the top papers per topic so that no paper appears twice.

    A paper cross-listed in several topics goes to the topic where it scores
    highest. Greedy over all (score, topic, paper) triples, best first.
    """
    triples = [(p.score, slug, p) for slug, ps in ranked.items() for p in ps]
    triples.sort(key=lambda t: t[0], reverse=True)

    chosen: dict[str, list[Paper]] = {slug: [] for slug in ranked}
    used: set[str] = set()
    for score, slug, paper in triples:
        if score < min_score or paper.uid in used:
            continue
        if len(chosen[slug]) >= top_k[slug]:
            continue
        chosen[slug].append(paper)
        used.add(paper.uid)
    return chosen
