# research-radar

A daily research feed for curious readers. Readers open the website, choose the fields they care about (as many as they like, changeable at any time), and every day they see the newest papers in those fields, each explained in plain words by Claude.

**Open the site:** https://xfx689781.github.io/research-radar/

Behind the site, a GitHub Actions job runs every morning: it pulls new papers from **arXiv**, **bioRxiv** and **medRxiv** for 24 topics across mathematics, physics, computer science and AI, chemistry, biology and economics, picks the most relevant papers per topic, asks Claude for summaries, and publishes them.

```
arXiv / bioRxiv / medRxiv ──► fetch per topic ──► skip papers already recommended
   ──► rank (TF-IDF similarity to each topic + keyword bonus) ──► top papers per topic
   ──► Claude summary in plain words ──► docs/data/*.json ──► website (GitHub Pages)
```

Each paper gets:

- **In plain words**: the problem and the result, for readers from other fields
- **In one sentence**: what the paper does, for specialists
- **Why it matters**, **background needed** and a difficulty level
- a link to the paper and its original abstract

## For readers

1. Open the site and pick your topics.
2. Come back any day; your feed shows the latest papers in your topics. Use the chips to look at one topic at a time, and **Edit topics** to change your choice.
3. Your choice is saved in your browser. If the site has accounts turned on, **Sign in** with your email to keep your topics on every device.

## Run your own copy in 10 minutes

1. Click **Use this template → Create a new repository**.
2. Edit `config.yaml`: keep or remove topics, or add your own (see below).
3. **AI summaries.** Create an API key at [console.anthropic.com](https://console.anthropic.com) (it needs a small amount of prepaid credit), then in your repository go to **Settings → Secrets and variables → Actions → New repository secret**, name it `ANTHROPIC_API_KEY` and paste the key. Never put the key in a file. Without it, the site still works but shows only the first sentence of each abstract.
4. **Website.** **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main`, folder `/docs` → Save.** Your site will be at `https://<your-username>.github.io/<repository-name>/`.
5. **First run.** **Actions → research-digest → Run workflow.** After that it runs every day by itself.
6. Optional: **accounts**, see below.

If the commit step fails with a permission error, go to **Settings → Actions → General → Workflow permissions** and select **Read and write permissions**.

**Cost.** Summaries use `claude-haiku-5-5` and only the abstract of each selected paper: with 24 topics and up to 3 papers each, at most 72 short requests a day (fewer on quiet days). See Anthropic's pricing page for current rates, and set a spending limit in the console. Lower `top_k_per_topic` or remove topics to spend less. GitHub Actions and Pages are free for public repositories.

## Accounts (optional)

Without accounts, each reader's topics are stored in their browser. To let readers sign in by email and keep their topics on every device, connect a free [Supabase](https://supabase.com) project:

1. Create a project at supabase.com.
2. **SQL Editor → New query**, paste the contents of `supabase/schema.sql`, **Run**. This creates the `preferences` table with row-level security, so every reader can only read and change their own row.
3. **Authentication → Sign In / Providers**: make sure **Email** is enabled.
4. **Authentication → URL Configuration**: set **Site URL** to your site's address (e.g. `https://xfx689781.github.io/research-radar/`) and add the same address under **Redirect URLs**.
5. **Project Settings → API** (or **Data API**): copy the **Project URL** and the **anon / publishable** key into `config.yaml` as `supabase_url` and `supabase_anon_key`, commit, and run the workflow once.

The anon key is meant to be public; row-level security is what protects each reader's data. Never put the `service_role` key anywhere in this repository.

Supabase's built-in email service only sends a few sign-in emails per hour, which is fine for a handful of readers. For more, connect your own SMTP provider under **Authentication → Emails**.

## Choosing topics

List the built-in presets:

```bash
python -m radar presets
```

| Field | Presets |
|---|---|
| Mathematics | `probability`, `statistics-theory`, `differential-geometry`, `pde`, `harmonic-analysis`, `complex-analysis`, `combinatorics`, `math-physics`, `optimization-control` |
| Computer science and AI | `ml-theory`, `interpretability`, `ai4math`, `embodied-ai` |
| Physics | `theoretical-physics`, `quantum` |
| Chemistry | `chemistry`, `ml-for-molecules` |
| Biology | `biology` (bioRxiv), `neuroscience` (bioRxiv), `quantitative-biology` (arXiv), `epidemiology` (medRxiv) |
| Economics | `economics`, `game-theory`, `quantitative-finance` |

Every topic listed in `config.yaml` is fetched daily and offered to readers on the site. Each entry can be a preset, a preset with changes, or your own:

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
- `top_k_per_topic`: papers per topic per day. `feed_days`: how far back the site shows papers.
- **Weekly instead of daily:** set `days: 7` and change the cron line in `.github/workflows/digest.yml` to `"51 12 * * 0"` (Sundays).

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

pytest -q                                                     # tests, no network needed
python -m radar run --offline tests/fixtures                  # try it on test data (writes to offline-output/)
python -m radar run --no-summary                              # real run, no AI summaries
ANTHROPIC_API_KEY=... python -m radar run                     # real run with summaries
```

A real run writes the site data (`docs/data/`), a Markdown digest of the day (`docs/digests/<date>.md`, handy for reading on GitHub) and the archive of recommended papers (`state/archive.jsonl`). It takes several minutes because the APIs ask clients to pause between requests.

To look at the website locally: `python -m http.server -d docs 8000` and open http://localhost:8000.

## How ranking works

For each topic, the `interest` text is split at commas into short facets (for example `geometric flows`, `Lie groups`). A paper's score is

$$
\text{score}(p) = \max_{f} \cos\big(\text{tfidf}(p), \text{tfidf}(f)\big) + \min\big(0.24,\ 0.08 \times \#\text{matched keywords}\big)
$$

The maximum over facets matters: compared with the whole interest text at once, a paper about one facet would look only weakly similar. The score measures how close the **wording** is, not how good a paper is.

Other details:

- A paper listed in several topics goes only to the topic where it scores highest.
- Running twice on the same day (for example after adding the API key) redoes that day's selection instead of skipping it.
- Each run looks back `days + overlap_days` days, since papers appear with a delay; `state/seen.json` makes sure nothing is recommended twice.
- Highlights are chosen by z-score within each topic, so topics with keywords (which score higher in absolute terms) do not crowd out the others.
- For bioRxiv and medRxiv, only first versions count as new; set `include_revisions: true` to also see updated preprints.

## Project layout

```
radar/
  sources/arxiv.py     arXiv API query and Atom parsing (standard library only)
  sources/biorxiv.py   bioRxiv / medRxiv API
  rank.py              scoring and cross-topic de-duplication
  summarize.py         Claude summaries, with a fallback when no key is set
  digest.py            daily Markdown digest
  archive.py           every recommended paper with its summary (state/archive.jsonl)
  site.py              JSON data for the website
  presets.yaml         built-in topics
  i18n.py              English and Chinese text
config.yaml            your topics and settings
docs/index.html        the website: topic picker, personal feed, optional sign-in
docs/data/             data the website reads, rebuilt every run
supabase/schema.sql    table and security rules for optional accounts
tests/                 unit tests and invented test data (not real papers)
.github/workflows/digest.yml   the daily schedule
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
- [ ] A daily email to each signed-in reader with their topics.
- [ ] RSS feed per topic.
- [ ] Check AI summaries for numbers or claims that are not in the abstract.

## Acknowledgements

Thank you to arXiv for use of its open access interoperability. Paper metadata comes from the [arXiv API](https://info.arxiv.org/help/api/) and the [bioRxiv/medRxiv API](https://api.biorxiv.org/); please follow their terms of use and keep the request delays.

## License

MIT. See `LICENSE`.
