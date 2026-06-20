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

### Current Conjectures

1. If preference-transition technology is fast relative to biological or material selection, current subjective welfare can rise while fitness falls.
2. Pareto comparisons over allocations alone are ill-defined when allocations alter the preferences used to evaluate them.
3. A Nash equilibrium of actions is not enough. In an endogenous-preference economy, equilibrium must include the preference-transition policy or institution.
4. Platform objectives can become an alternative selection criterion, creating a conflict between survival fitness and engagement fitness.

### Next Actions

- Inspect first simulation outputs for knife-edge assumptions.
- Add proposition sketches to `docs/02_axioms_v0.md`.
- Add richer platform-agent model with platform best response.
- Create a BibTeX file once the core reference list stabilizes.

### Open Questions

- What is the right welfare criterion: initial preferences, long-run preferences, meta-preferences, biological fitness, or constitutional constraints?
- Should "preference autonomy" be modeled as a constraint on the transition kernel `K`?
- Can we derive a clean impossibility theorem without importing psychology?
