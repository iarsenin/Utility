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

### Current Conjectures

1. If preference-transition technology is fast relative to biological or material selection, current subjective welfare can rise while fitness falls.
2. Pareto comparisons over allocations alone are ill-defined when allocations alter the preferences used to evaluate them.
3. A Nash equilibrium of actions is not enough. In an endogenous-preference economy, equilibrium must include the preference-transition policy or institution.
4. Platform objectives can become an alternative selection criterion, creating a conflict between survival fitness and engagement fitness.

### Next Actions

- Prove or falsify the timescale-dominance proposition in `docs/06_formal_research_plan.md`.
- Implement `models/platform_preference_control.md`.
- Create phase diagrams for plasticity, selection strength, platform bias, and exposure cost.
- Begin a formal note for the preference-laundering theorem.

### Open Questions

- What is the right welfare criterion: initial preferences, long-run preferences, meta-preferences, biological fitness, or constitutional constraints?
- Should "preference autonomy" be modeled as a constraint on the transition kernel `K`?
- Can we derive a clean impossibility theorem without importing psychology?
