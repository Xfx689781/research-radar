# research-radar

A personal weekly research digest. Every Sunday it pulls new papers from **arXiv**, **bioRxiv** and **medRxiv** in the topics you choose, ranks them against a plain-English description of your interests, optionally asks Claude for short summaries, and commits a Markdown digest to your repository.

It ships with presets for mathematics, physics, computer science and AI, chemistry, biology and economics, and you can add any topic of your own.

```
arXiv / bioRxiv / medRxiv ──► fetch (categories + optional keywords) ──► skip papers already recommended
   ──► rank (TF-IDF similarity to your interests + keyword bonus) ──► top papers per topic, no duplicates
   ──► (optional) Claude summary ──► digests/YYYY-MM-DD.md
```

## Use it yourself in 5 minutes

1. Click **Use this template → Create a new repository** (public or private).
2. Edit `config.yaml` and choose your topics (see below).
3. Optional, for AI summaries: **Settings → Secrets and variables → Actions → New repository secret**, name `ANTHROPIC_API_KEY`. Without it, each paper shows the first sentence of its abstract instead. Use your own key and never commit it to a file.
4. **Actions → weekly-digest → Run workflow** to get your first digest now. After that it runs every Sunday.

If the commit step fails with a permission error, go to **Settings → Actions → General → Workflow permissions** and select **Read and write permissions**.

## Choosing topics

List the built-in presets:

```bash
python -m radar presets
```

| Field | Presets |
|---|---|
| Mathematics | `probability`, `statistics-theory`, `differential-geometry`, `analysis-pde`, `complex-analysis`, `combinatorics`, `math-physics`, `optimization-control` |
| Computer science and AI | `ml-theory`, `interpretability`, `ai4math`, `embodied-ai` |
| Physics | `theoretical-physics`, `quantum` |
| Chemistry | `chemistry`, `ml-for-molecules` |
| Biology | `biology` (bioRxiv), `neuroscience` (bioRxiv), `quantitative-biology` (arXiv), `epidemiology` (medRxiv) |
| Economics | `economics`, `game-theory`, `quantitative-finance` |

In `config.yaml`, each topic can be a preset, a preset with changes, or your own:

```yaml
topics:
  - probability                      # a preset
  - preset: economics                # a preset with changes
    top_k: 5
    seed_ids: [2410.01234]           # papers you liked sharpen the ranking
  - name: Number theory              # your own topic
    slug: number-theory
    source: arxiv                    # arxiv, biorxiv or medrxiv
    categories: [math.NT]
    keywords: [modular forms, L-functions]   # optional filter
    interest: >
      Analytic number theory, modular forms, L-functions, distribution of primes.
```

- `categories`: arXiv categories ([list](https://arxiv.org/category_taxonomy)) or bioRxiv/medRxiv subject areas such as `cell biology`.
- `interest`: a comma-separated list of specific things you care about, in English. Ranking depends on it most.
- `keywords`: for very large categories such as `cs.LG`, only papers containing at least one keyword are fetched; matches also add a small bonus.
- `language`: `en` or `zh` for the digest text and AI summaries.

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

pytest -q                                                     # tests, no network needed
python -m radar run --offline tests/fixtures --dry-run        # try it on the bundled test data
python -m radar run --no-summary                              # real run, no AI summaries
ANTHROPIC_API_KEY=... python -m radar run                     # real run with summaries
```

The digest is written to `digests/latest.md`. A full run takes a few minutes because the APIs ask clients to pause between requests.

## How ranking works

For each topic, the `interest` text is split at commas into short facets (for example `geometric flows`, `Lie groups`). A paper's score is

$$
\text{score}(p) = \max_{f} \cos\big(\text{tfidf}(p), \text{tfidf}(f)\big) + \min\big(0.24,\ 0.08 \times \#\text{matched keywords}\big)
$$

The maximum over facets matters: compared with the whole interest text at once, a paper about one facet would look only weakly similar. The score measures how close the **wording** is, not how good a paper is.

Other details:

- A paper listed in several topics goes only to the topic where it scores highest.
- Each run looks back `days + overlap_days` days, since papers appear with a delay; `state/seen.json` makes sure nothing is recommended twice.
- For bioRxiv and medRxiv, only the newest version of each preprint is kept.

## Project layout

```
radar/
  sources/arxiv.py     arXiv API query and Atom parsing (standard library only)
  sources/biorxiv.py   bioRxiv / medRxiv API
  rank.py              scoring and cross-topic de-duplication
  summarize.py         optional Claude summaries, with a fallback
  digest.py            Markdown output
  presets.yaml         built-in topics
  i18n.py              English and Chinese text
config.yaml            your topics and settings
tests/                 unit tests and invented test data (not real papers)
.github/workflows/weekly.yml   the weekly schedule
```

## Limitations

- TF-IDF matches words, not meaning: `Ricci flow` and `geometric evolution equation` look unrelated to it.
- Chemistry coverage is limited to arXiv (`physics.chem-ph`, `cond-mat.mtrl-sci`); ChemRxiv is not supported yet.
- Economics uses arXiv's `econ` and `q-fin` categories; NBER and SSRN working papers are not included.
- AI summaries are written from the abstract only and can be wrong or overstated.

## Roadmap

- [ ] Measure ranking quality: label recommendations as useful or not for a few weeks and track precision@k.
- [ ] Try sentence embeddings instead of TF-IDF, and compare precision@k.
- [ ] Learn from feedback: add liked papers to `seed_ids` automatically.
- [ ] More sources: ChemRxiv, NBER, Semantic Scholar citation signals.
- [ ] Email or phone notifications.
- [ ] Check AI summaries for numbers or claims that are not in the abstract.

## Acknowledgements

Thank you to arXiv for use of its open access interoperability. Paper metadata comes from the [arXiv API](https://info.arxiv.org/help/api/) and the [bioRxiv/medRxiv API](https://api.biorxiv.org/); please follow their terms of use and keep the request delays.

## License

MIT. See `LICENSE`.
