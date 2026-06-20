# Endogenous Utility Research Program

This repository develops a mathematical economics research project around a simple provocation:

> What if utility functions are not quasi-fixed objects, but fast-moving state variables shaped by institutions, social media, AI systems, and evolutionary selection?

Classical consumer and welfare theory often treats preferences as exogenous or slow moving. This project asks what changes when the preference map itself is endogenous, manipulable, and selected by fitness-like forces. The first target is not a finished theorem, but a disciplined research machine: axioms, model families, simulations, literature notes, and a reproducible progress ledger.

## Research Spine

The project studies dynamic economies where each agent has a preference state, not merely a utility function:

```text
state_t = (resources_t, beliefs_t, preference_state_t, institutions_t)
```

Agents maximize current subjective utility, while preference states evolve through exposure, habit, imitation, recommender systems, institutions, and selection. The key separation is:

```text
subjective utility != biological/material fitness != platform objective
```

That separation is where the strange results should live.

## Repository Layout

- `docs/`: literature map, axioms, methodology, and project plans.
- `models/`: model-specific mathematical notes.
- `src/utility_endogenous/`: simulation and model code.
- `scripts/`: reproducible entry points.
- `data/`: raw and processed data placeholders.
- `results/`: generated reports, figures, and tables.
- `references/`: bibliography notes and paper summaries.
- `notebooks/`: exploratory notebooks, when needed.
- `paper/`: readable article drafts assembled from the research program.

## Quick Start

Run the initial toy models:

```bash
python3 scripts/run_toy_models.py
```

The script writes:

- `results/toy_model_report.md`
- `results/tables/endogenous_taste_summary.csv`
- `results/tables/indirect_evolution_summary.csv`

Run the three-iteration research sprint:

```bash
python3 scripts/run_research_iterations.py
```

The script writes:

- `results/research_iteration_report.md`
- `results/figures/platform_inversion_heatmap.svg`
- `results/tables/iteration_*.csv`

Run the fast preference limit experiment:

```bash
python3 scripts/run_fast_limit.py
```

The script writes:

- `results/fast_preference_limit_report.md`
- `results/tables/fast_limit_*.csv`

Run the timescale/survival variants:

```bash
python3 scripts/run_timescale_variants.py
```

The script writes:

- `results/timescale_variant_report.md`
- `results/tables/timescale_*.csv`

## Current Status

This is bootstrap version 0.1. The repo currently contains:

- a first axiomatic frame for endogenous preferences,
- a literature map with canonical and current entry points,
- a project plan and progress ledger,
- two initial model families:
  - algorithmic preference drift with Darwinian selection,
  - indirect evolutionary Prisoner's Dilemma with mutable social preferences.

## Research Planning Docs

Start here for the current research direction:

- `paper/article_draft_v0.html`
- `paper/article_draft_v0_codex.md`
- `paper/article_draft_v0_math.md`
- `paper/article_draft_v0.md`
- `docs/05_research_synthesis_v1.md`
- `docs/06_formal_research_plan.md`
- `docs/07_paper_outline_v1.md`
- `docs/08_novelty_check_v1.md`
- `docs/09_fast_preference_limit.md`
- `docs/10_timescales_and_survival.md`
- `docs/11_model_selection_audit.md`
- `references/literature_matrix.md`

Next model specs:

- `models/platform_preference_control.md`
- `models/revealed_preference_with_drift.md`

Current research decision: treat platform-controlled preference transitions as one application of the broader fast-preference-limit program. The next proof target is a singular-limit theorem for utility functions that adapt instantly, with institution and population speeds treated as estimable parameters rather than assumptions.
