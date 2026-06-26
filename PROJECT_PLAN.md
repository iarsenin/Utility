# Project Plan

## Working Title

When Preferences Decouple From Fitness: Endogenous Utility, Material Capacity,
and Strategic Choice

## Core Objective

Develop a rigorous but readable working paper showing how endogenous
preference formation changes economic dynamics when induced subjective payoffs
feed back into slower material capacities.

The paper should be legible to a technically educated reader and defensible to
mathematical economists. The main text should carry the story and result; the
appendix should carry formulas, theorem statements, proofs, and numerical
audits.

## Current Model Spine

```text
preference-forming rule
-> subjective payoff
-> action or Nash equilibrium
-> material capacity
-> future subjective payoff
-> selection among rules under an explicit competitive score
```

The central state variable is material capacity, denoted `K` in the formal
model. Depending on the application, `K` can represent social skill, solvency,
health, metabolic resilience, learning, trust, or institutional competence.

## Main Results To Preserve

- **Bridge:** a substitute can reduce pressure while rebuilding the capacity
  that makes outside options usable.
- **Trap:** low capacity can make the substitute attractive, while substitute
  use keeps capacity low; a threshold separates recovery from persistence in
  the low state.
- **Collapse-prone regime:** stronger damage can pull the capacity stock toward
  a lower boundary in the minimal model.
- **Alarm limitation:** a signal based only on current improvement or decline
  can change adjustment speed without changing the long-run states of the
  minimal capacity model.
- **Selection metric:** competition preserves capacity only when its score
  rewards capacity-preserving rules. Engagement, retention, or attention can
  select a sink while material capacity falls.

## Research Questions

1. Which assumptions are sufficient for the fast-payoff/slow-capacity
   reduction?
2. How general are the bridge, trap, and collapse-prone regimes beyond the
   scalar normal form?
3. What competitive scores align with material viability, and which select
   sinks?
4. Which empirical designs can distinguish stable preferences from endogenous
   payoff formation and capacity feedback?
5. Which applications are strongest as tests rather than anecdotes?

## Active Workstreams

### 1. Formal Model

Keep the scalar capacity model as the main exposition and diagnostic model.
Use the general appendix to state the fast-limit reduction and Nash step.
Future extensions can add vector capacities, stochastic environments, or
explicit platform optimization once the scalar paper is stable.

### 2. Numerical Diagnostics

Maintain reproducible scripts that generate:

- phase-line and path figures for bridge/trap/collapse-prone dynamics;
- current-movement versus capacity-level correction diagnostics;
- competition diagnostics comparing material viability and engagement scores.

### 3. Empirical Strategy

Applications are admissible only when they name exposure, substitute behavior,
material capacity, and competitive score. The strongest current candidates are
AI companions and loneliness, sports betting and solvency, outrage media and
verification capacity, food/GLP-1 and metabolic capacity, and dating retreat
and social capacity.

### 4. Article Development

The article should remain narrative-first:

1. concrete puzzle;
2. mechanism in plain language;
3. bridge/trap/collapse/self-correction/selection results;
4. flagship example;
5. candidate domains and empirical strategy;
6. formal appendix.

Avoid resurrecting the old theorem-first or fast-settling framing as the main
paper. Those ideas are useful background, not the live reader spine.

## Reproducible Commands

```bash
python3 scripts/run_material_feedback_analysis.py
python3 scripts/run_self_correction_analysis.py
python3 scripts/build_material_feedback_article.py
python3 -m compileall -q src scripts
git diff --check
```

## Project Memory Discipline

- Keep `PROGRESS.md` compact and forward-looking.
- Put historical round logs only under `docs/archive/`.
- Do not copy transient edit reactions into active guidance unless they become
  stable editorial rules.
- When a pivot occurs, update the active plan and demote superseded notes.
