# Endogenous Utility Research Program

This repository develops a mathematical economics paper on endogenous utility:
preferences are treated as state variables shaped by social, institutional, and
technological environments, not as fixed primitives.

The live paper is:

- [When Preferences Decouple From Fitness](paper/when_preferences_move_faster_than_equilibrium_v1.html)

The current model studies a feedback loop:

```text
fast subjective payoff formation
-> coherent choice or Nash equilibrium under the induced payoff
-> slow material-capacity change
-> future subjective payoff formation
-> competition among preference-forming rules under a named score
```

The key distinction is:

```text
subjective payoff != material capacity != competitive score
```

Choices can be rational under the subjective payoff while still building or
depleting future capacity. Competition can correct the system only when the
operative competitive score rewards capacity-preserving rules.

## Start Here

Use these files as the current project memory:

- `PROGRESS.md`: compact state of the project, active result, next work.
- `PROJECT_PLAN.md`: research plan and milestone map.
- `docs/agent_objective_function.md`: article-writing and editing rules.
- `models/material_capacity_feedback.md`: mathematical model note.
- `paper/README.md`: manuscript status and reader-facing artifacts.
- `results/README.md`: generated output map and evidence standard.

Historical round logs and older progress ledgers are archived under
`docs/archive/`. They preserve provenance but are not active instructions.

## Live Research Claim

The paper does not claim that endogenous preferences are new. The contribution
is a timing-and-selection claim:

1. Payoffs can be formed quickly by platforms, peers, institutions, AI systems,
   markets, and norms.
2. Agents may then choose coherently under those induced payoffs.
3. The chosen behavior can change a slower material capacity such as social
   skill, solvency, health, trust, learning, or institutional competence.
4. Preference-forming rules then compete under a score that may or may not
   align with material viability.

The minimal scalar model yields bridge, trap, and collapse-prone regimes. The
self-correction result says that a signal based only on current improvement or
decline can change adjustment speed without changing the long-run states of the
minimal model. Durable correction requires a force that changes the capacity
path, or competition whose score rewards capacity-preserving rules.

## Repository Layout

- `docs/`: active research notes, project memory, and archived review logs.
- `models/`: mathematical model specifications.
- `src/utility_endogenous/`: executable model code.
- `scripts/`: reproducible analysis and article-building entry points.
- `results/`: generated reports, figures, and tables.
- `paper/`: reader-facing drafts and current HTML manuscript.
- `references/`: literature notes and bibliography material.
- `data/`, `notebooks/`: data and exploratory workspace.

## Reproduce The Current Paper

Run:

```bash
python3 scripts/run_material_feedback_analysis.py
python3 scripts/run_self_correction_analysis.py
python3 scripts/build_material_feedback_article.py
```

The main output is:

- `paper/when_preferences_move_faster_than_equilibrium_v1.html`

Core generated diagnostics are:

- `results/material_feedback_report.md`
- `results/self_correction_report.md`
- `results/figures/material_feedback_paths.svg`
- `results/figures/self_correction_channels.svg`
- `results/figures/competition_selection_channels.svg`

## Evidence Standard

Generated simulations are mechanism checks unless explicitly identified as
estimates. Applied claims should name:

1. the payoff-forming exposure;
2. the substitute behavior;
3. the material capacity;
4. the capacity outcome measure;
5. the competitive score;
6. the identification strategy.

## Article QA Rule

Every reader-facing article update must be generated from source, opened in the
target browser, and visually checked with a screenshot before it is reported as
ready.
