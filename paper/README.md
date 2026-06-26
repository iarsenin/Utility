# Paper Artifacts

The live manuscript is:

- `when_preferences_move_faster_than_equilibrium_v1.html`

Current title:

- **When Preferences Decouple From Fitness**

The filename is retained for continuity. The article is generated from:

- `scripts/build_material_feedback_article.py`

## Current Manuscript Frame

The current paper centers material-capacity feedback:

```text
fast subjective payoff formation
-> coherent choice or Nash equilibrium
-> slow material-capacity change
-> future payoff formation
-> competition among preference-forming rules
```

The main text is narrative-first. Formal definitions, propositions, proofs,
empirical equations, calibrations, and audit tables belong in the appendices.

## Current QA Rule

For every reader-facing article update:

1. regenerate the HTML from source;
2. open it in the target browser;
3. inspect the rendered page;
4. save a screenshot under `results/figures/`;
5. record the screenshot in `PROGRESS.md` when the update is substantive.

## Archived Drafts

Older HTML, Markdown, and PDF drafts in this folder are retained as project
history. They include fast-limit, GEB-facing, working-paper, fashion/meme, and
combined-manuscript variants. They should not be treated as live guidance
unless explicitly revived.

Important older artifacts:

- `archive/article_draft_v0*`: early fast-preference-limit drafts.
- `archive/venue_strategy.md`: older venue notes; update before relying on it.
- `working_paper_v1.html`: broad working-paper version before the
  material-capacity reset.
- `geb_submission_v1.html`: earlier GEB-facing finite-game version.
- `fashion_meme_closure_presentation.html`: separate mechanism exploration.
- `combined_fast_preference_closure_v1.html`: prior combined manuscript.

## Local Rendering

The current manuscript loads MathJax locally from
`vendor/mathjax/es5/tex-chtml.js`. It should render as either a local file or
through the local HTTP server. If the browser shows stale content, reload the
tab.
