# Endogenous Utility Research Program

This repository develops a mathematical economics research project around a simple provocation:

> What if utility functions are not quasi-fixed objects, but fast-moving state variables shaped by institutions, social media, AI systems, and evolutionary selection?

Classical consumer and welfare theory often treats preferences as exogenous or slow moving. This project asks what changes when the preference map itself is endogenous, manipulable, and selected by fitness-like forces. The first target is not a finished theorem, but a disciplined research machine: axioms, model families, simulations, literature notes, and a reproducible progress ledger.

## Research Spine

The current paper studies dynamic economies where each agent has a preference
state and a material capacity stock, not merely a fixed utility function:

```text
state_t = (material_capacity_t, beliefs_t, preference_state_t, institutions_t)
```

Agents maximize current subjective utility, while preference states evolve
through exposure, habit, imitation, recommender systems, institutions, and AI.
The choices made under those subjective payoffs then change slower material
capacities such as health, solvency, social skill, fertility agency, learning,
trust, and institutional continuity. The key separation is:

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
- `results/figures/legacy/platform_inversion_heatmap.svg`
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

Run the current material-feedback model:

```bash
python3 scripts/run_material_feedback_analysis.py
python3 scripts/build_material_feedback_article.py
```

The scripts write:

- `results/material_feedback_report.md`
- `results/tables/material_feedback_*.csv`
- `results/figures/material_feedback_*.svg`
- `paper/when_preferences_move_faster_than_equilibrium_v1.html`

## Current Status

The live manuscript direction is now the material-capacity feedback paper:

- `paper/when_preferences_move_faster_than_equilibrium_v1.html`

The paper keeps the fast-preference limit and Nash equilibrium discipline, but
the main object is now a feedback loop:

```text
fast subjective payoff formation
-> Nash or choice under subjective payoff
-> slow material capacity
-> future subjective payoff formation
```

The older GEB, finite-game, and fashion drafts remain in `paper/` as source
history. They should not be treated as the live frame unless explicitly revived.

## Research Planning Docs

Start here for the current research direction:

- `paper/when_preferences_move_faster_than_equilibrium_v1.html`
- `docs/13_material_feedback_pivot.md`
- `models/material_capacity_feedback.md`
- `results/material_feedback_report.md`
- `docs/agent_rounds/combined_round_1_modeller.md`
- `docs/agent_rounds/combined_round_2_literature.md`
- `docs/agent_rounds/combined_round_3_writer.md`
- `docs/agent_rounds/combined_round_4_editor.md`
- `docs/agent_rounds/combined_round_5_production.md`
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

Current research decision: treat platform-controlled preference transitions as
one application of a broader material-feedback program. The next proof target
is a rigorous singular-limit theorem for fast subjective payoff formation
coupled to slow capacity dynamics, with institutional and population speeds
treated as estimable parameters rather than assumptions.
