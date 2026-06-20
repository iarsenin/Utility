# Project Plan

## Working Title

Endogenous Utility in Algorithmic Economies: Preference Dynamics, Selection, and Welfare Failure

## Central Claim

The exogeneity of preferences is no longer a harmless approximation when preference-updating technologies operate at social-media or AI speed. Welfare, equilibrium, and Pareto efficiency must be defined over extended paths that include preference states and preference-transition technologies.

## Research Questions

1. What axioms replace static utility representation when preferences are state variables?
2. What are the smallest models where endogenous preferences change equilibrium conclusions?
3. When does selection favor preference types that maximize survival, engagement, status, imitation, or reproduction?
4. Can subjective utility rise while biological or material fitness falls?
5. What becomes of Pareto efficiency when the allocation mechanism can alter tastes?
6. Which empirical observables could distinguish slow cultural preference drift from AI-accelerated preference control?

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

Output: `docs/02_axioms_v0.md`.

### 3. Models

Start with two families:

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

Target a theory-forward paper with a provocative applied motivation:

1. Introduction: why exogenous preferences may fail at AI speed.
2. Literature and conceptual gap.
3. Dynamic endogenous-preference axioms.
4. Toy models showing welfare and equilibrium reversals.
5. Richer platform-selection model.
6. Welfare implications and impossibility/proposition section.
7. Empirical strategy.

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

### Milestone 2: First Formal Note

- Convert axioms into proposition-ready notation.
- Prove a simple "preference laundering" result: if utilities can be altered cheaply enough, final-preference Pareto comparisons are not invariant.
- Prove a timescale result: if preference plasticity dominates fitness selection, population mean taste can move opposite to Darwinian fitness gradient.

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

The first publishable paper should not merely argue that preferences are endogenous. That is already known. The sharper contribution is:

```text
AI and social-media systems act as fast, strategic preference-transition technologies.
```

The formal model should therefore focus on:

- local utility representation,
- a preference transition kernel `K_m`,
- material or Darwinian fitness `F`,
- platform or institutional policy `m`,
- welfare comparisons over allocation-preference paths.
