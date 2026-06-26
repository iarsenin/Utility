# Project Plan

## Working Title

When Preferences Move Faster Than Equilibrium: Endogenous Utility And
Material-Capacity Feedback

## Central Claim

The exogeneity of preferences is no longer a harmless approximation when
preference-updating technologies operate at social-media or AI speed and when
choices made under induced subjective payoffs change slower material
capacities. Welfare, equilibrium, and selection must be defined over paths that
include preference states, preference-forming rules, actions, and material
capacity stocks.

## Research Questions

1. What axioms replace static utility representation when preferences are state variables?
2. What are the smallest models where endogenous preferences change equilibrium conclusions?
3. When does selection favor rules that reproduce material capacity rather
   than rules that maximize engagement, status, imitation, or immediate
   subjective payoff?
4. When can choices be locally rational under induced subjective payoffs while
   depleting health, solvency, fertility agency, social skill, learning, trust,
   or institutions?
5. What becomes of Pareto efficiency when the allocation mechanism can alter
   the payoff criteria used to evaluate allocations?
6. Which empirical observables distinguish stable preferences, reversible
   influence, threshold traps, and collapse-prone capacity feedback?

## Workstreams

### 1. Literature

Build a structured map across:

- revealed preference and utility representation,
- endogenous preferences and cultural transmission,
- indirect evolutionary approach,
- dynamic choice and meta-preferences,
- recommender systems and preference manipulation,
- welfare economics under adaptive preferences.

Output: `docs/01_literature_map.md` and paper notes in `references/`.

### 2. Axioms

Develop an axiomatic system where the primitive is a dynamic preference process:

```text
(X, Theta, A, M, K, F, U)
```

where `Theta` is the preference-state space, `K` is the preference transition kernel, `F` is material or Darwinian fitness, and `U` is current subjective utility.

Current revision: reserve `K` in the manuscript for material capacity. Use
`C` or `P` for preference-transition maps if needed. This avoids overloading the
central variable in the new model.

Output: `docs/02_axioms_v0.md`.

### 3. Models

Current core model:

- material-capacity feedback:

```text
p(K,z) = logistic(beta * (q + z - rho K))
Kdot = a + r K^2(1 - K) - d K - L p(K,z)
```

This model classifies self-correction, threshold traps, and collapse-prone
feedback. It is implemented in `src/utility_endogenous/material_feedback.py`.

Legacy and supporting model families:

- A consumption model where the Cobb-Douglas weight is endogenous and algorithmically shifted.
- An indirect evolutionary game where social preferences are selected by material payoff while institutions mutate preference types.

Then extend to:

- platform-agent games,
- overlapping-generations cultural transmission,
- Bayesian persuasion / recommender-control models,
- empirical calibrations using public social-media, fertility, time-use, and consumption proxies.

Output: `models/`, `src/`, and `results/`.

### 4. Results

For every iteration:

- define model primitives,
- state the exogenous-preference benchmark,
- modify the axioms,
- run simulations or prove comparative statics,
- document whether the result is robust, fragile, or bizarre-but-solid.

Output: `PROGRESS.md` plus generated files under `results/`.

### 5. Paper

Target a reader-facing but rigorous working paper:

1. Plain-language puzzle: rational choice inside induced subjective payoffs.
2. Material-capacity feedback model.
3. Analytical classification: self-correction, threshold trap, collapse-prone
   feedback.
4. Real-world applications and tests.
5. Empirical strategy.
6. Nash equilibrium and material selection.
7. Formal appendix.

## Near-Term Milestones

### Milestone 0: Bootstrap

- Create repository structure.
- Write first axioms and literature map.
- Run initial toy simulations.
- Commit and push to GitHub.

Status: complete.

### Milestone 1: Research Plan v1

- Produce source-grounded research synthesis.
- Write formal model hierarchy.
- Identify theorem candidates.
- Write first paper outline.
- Build a literature matrix and bibliography seed.

Status: complete as of `docs/05_research_synthesis_v1.md`, `docs/06_formal_research_plan.md`, and `docs/07_paper_outline_v1.md`.

### Milestone 2: Material Feedback Formal Note

- Convert the material-capacity feedback model into proposition-ready notation.
- Prove the fast-limit reduction from preference dynamics to the slow capacity
  law under a selected attracting preference branch.
- Prove the one-dimensional two-basin trap result.
- State comparative statics for repair, substitute damage, sensitivity,
  exposure, and capacity protection.

Status: first version implemented in
`models/material_capacity_feedback.md`,
`src/utility_endogenous/material_feedback.py`, and
`paper/when_preferences_move_faster_than_equilibrium_v1.html`.

### Milestone 3: Model Deepening

- Add a platform objective and solve for Markov-perfect or stationary equilibria.
- Compare welfare under biological fitness, current subjective utility, and meta-preference criteria.

### Milestone 4: Empirical Anchors

- Identify datasets and proxies for rapid preference movement:
  - time-use,
  - fertility and relationship formation,
  - cosmetic procedure uptake,
  - teen mental health and online engagement,
  - recommender-system exposure experiments.

## Operating Rules

- Every model gets a markdown spec in `models/`.
- Every script writes reproducible output to `results/`.
- Every iteration updates `PROGRESS.md`.
- Claims are tagged as `conjecture`, `simulation`, `proposition`, or `empirical hypothesis`.
- Strange conclusions are allowed, but only if the assumptions are explicit.

## Current Research Bet

The first publishable paper should not merely argue that preferences are
endogenous. That is already known. The sharper contribution is:

```text
fast preference formation can create material-capacity feedback loops
```

The formal model should therefore focus on:

- local subjective payoff formation;
- the induced subjective game and Nash equilibrium;
- material capacity dynamics;
- selection over rules, institutions, and designs;
- empirical tests that identify capacity feedback rather than merely
  preference drift.
