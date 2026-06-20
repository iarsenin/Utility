# Progress Ledger

## 2026-06-20

### Completed

- Created Drive-backed repository at `/Users/igor/My Drive/git/Utility`.
- Connected local working copy to `https://github.com/iarsenin/Utility.git`.
- Created initial project structure.
- Drafted first research plan, literature map, axioms, and model inventory.
- Implemented dependency-free simulations for:
  - endogenous taste drift under algorithmic exposure and Darwinian selection,
  - indirect evolutionary Prisoner's Dilemma with mutable social preferences.
- Ran the bootstrap simulations and generated first outputs in `results/`.

### First Simulation Readout

- Slow cultural drift moves mean online/artificial taste from about `0.35` to `0.06`; fitness rises.
- AI-speed preference capture moves mean online/artificial taste from about `0.35` to `0.96`; fitness falls.
- Even when selection against high online orientation is made much stronger, the chosen high-persuasion parameters still move the population near `0.96`; this is a useful stress case, not a proof.
- In the Prisoner's Dilemma model, prosocial preference drift restores near-full cooperation; conflict-oriented drift collapses cooperation.

### Research Planning Pass

- Added `docs/05_research_synthesis_v1.md`.
- Added `docs/06_formal_research_plan.md`.
- Added `docs/07_paper_outline_v1.md`.
- Added `references/literature_matrix.md` and `references/bibliography.bib`.
- Added model specs for:
  - platform preference control,
  - revealed preference with drifting tastes.

### Source-Grounded Finding

The literature already has endogenous preferences through consumption capital, habit, addiction, time preference, cultural transmission, indirect evolution, chosen preferences, and meta-preferences. The novel wedge is not "preferences can change." It is:

```text
algorithmic and AI systems can optimize the preference-transition kernel K_m
at a much faster timescale than culture or biological selection.
```

### Three-Iteration Research Sprint

Completed three major iterations in `scripts/run_research_iterations.py`.

Iteration 1: one-dimensional taste drift.

- Benchmark reproduced: with degenerate `K`, mean taste is stable; with selection only, taste moves toward the fitness-favored offline state.
- Endogenous modification: AI-speed transition pushes mean online/artificial taste from about `0.35` to `0.96` while fitness falls.
- Verdict: useful theorem candidate, too reduced-form to carry the paper.

Iteration 2: indirect evolutionary Prisoner's Dilemma.

- Benchmark reproduced: material payoff selection pushes cooperation nearly to zero.
- Endogenous modification: preference mutation toward prosocial types restores cooperation; mutation toward conflict collapses it.
- Verdict: strong bridge to the literature, not novel enough unless platform incentives choose the mutation law.

Iteration 3: platform preference control.

- Benchmark reproduced: no-platform selection increases fitness but can move taste away from the initial optimum.
- Endogenous modification: a myopic platform chooses exposure, raising mean online/artificial taste from about `0.35` to `0.79` while fitness falls by about `1.02`.
- Parameter sweep: `49/108` platform cells show taste capture, fitness loss, and initial-preference loss.
- Guardrail result: a calibrated autonomy penalty prevents capture and improves fitness; a weak penalty barely changes platform behavior.
- Verdict: this is the first paper's core candidate.

### Current Conjectures

1. If preference-transition technology is fast relative to biological or material selection, current subjective welfare can rise while fitness falls.
2. Pareto comparisons over allocations alone are ill-defined when allocations alter the preferences used to evaluate them.
3. A Nash equilibrium of actions is not enough. In an endogenous-preference economy, equilibrium must include the preference-transition policy or institution.
4. Platform objectives can become an alternative selection criterion, creating a conflict between survival fitness and engagement fitness.

### Next Actions

- Prove the timescale-dominance proposition in `docs/06_formal_research_plan.md`.
- Derive the platform-control first-order or threshold condition.
- Replace the myopic platform with a forward-looking platform or regulator.
- Tighten welfare language around initial preferences, final preferences, meta-preferences, and fitness.
- Begin a formal note for the preference-laundering theorem.

### Open Questions

- What is the right welfare criterion: initial preferences, long-run preferences, meta-preferences, biological fitness, or constitutional constraints?
- Should "preference autonomy" be modeled as a constraint on the transition kernel `K`?
- Can we derive a clean impossibility theorem without importing psychology?
