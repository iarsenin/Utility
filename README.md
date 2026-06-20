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

## Quick Start

Run the initial toy models:

```bash
python3 scripts/run_toy_models.py
```

The script writes:

- `results/toy_model_report.md`
- `results/tables/endogenous_taste_summary.csv`
- `results/tables/indirect_evolution_summary.csv`

## Current Status

This is bootstrap version 0.1. The repo currently contains:

- a first axiomatic frame for endogenous preferences,
- a literature map with canonical and current entry points,
- a project plan and progress ledger,
- two initial model families:
  - algorithmic preference drift with Darwinian selection,
  - indirect evolutionary Prisoner's Dilemma with mutable social preferences.
