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

### Novelty Check

Added `docs/08_novelty_check_v1.md`.

Preliminary conclusion:

- Not novel: endogenous preferences, recommender feedback loops, engagement-welfare divergence, AI preference manipulation, or welfare trouble under endogenous preferences.
- Potentially novel: a mathematical economics model in which a platform chooses the preference-transition kernel `K_m`, producing a four-way split between platform value, final subjective utility, initial-preference welfare, and material/fitness welfare.
- Closest current threats: Kleinberg-Mullainathan-Raghavan on engagement optimization, Jiang et al. on recommender feedback loops, and Khosrowi-Beck on recommender welfare foundations.

### Fast Preference Limit Pass

Added `docs/09_fast_preference_limit.md`, `src/utility_endogenous/fast_limit.py`, and `scripts/run_fast_limit.py`.

Preliminary conclusion:

- This direction is more fundamental than the platform-only framing.
- Let preference adaptation occur on timescale `T` and take `T -> 0`. If the fast preference subsystem has a unique attracting branch `theta = Phi(z, m)`, utility is replaced by the critical manifold of preference adaptation.
- Darwinian selection over preference states disappears in the unique-attractor limit; selection can only act on slow objects such as adaptation rules, institutions, biological resistance, or population size.
- Material Nash equilibrium need not survive. The surviving Nash object is best response to the fast-adapted preference state, not necessarily to material payoffs.
- Final-preference welfare is too weak in this limit because a path can create the preferences that endorse it.

Numerical readout:

- Strong taste adaptation has fast attractor `theta ~= 0.9615`; the finite AI-speed simulation converges to the same value.
- Selection strength from `0.20` to `5.00` leaves that fast attractor unchanged, while realized fitness falls.
- In the Prisoner's Dilemma model, fast prosocial adaptation yields full cooperation even though cooperation is not material Nash.
- In the platform model, the limit depends on transition-cost scaling: steady penalties vanish after the boundary layer, while boundary-layer penalties can block capture.

### Timescale And Survival Correction

Added `docs/10_timescales_and_survival.md`, `src/utility_endogenous/timescale_variants.py`, and `scripts/run_timescale_variants.py`.

Correction:

- Nash equilibrium is a fixed-point method, not an object that survives or fails. The material-payoff Nash prediction is invariant only when fast preference closure preserves the material best-response correspondence.
- Darwinian selection is an update operator, not a conclusion. In the `T_pref -> 0` limit, it acts on whatever remains heterogeneous after fast closure: populations, adaptation laws, institutions, or resistance to adaptation.
- We should not assume institutions or population are slower than preferences. Their speeds should be estimated or varied.

New numerical readout:

- Fixed exposure `m = 0.05` induces `theta = 0.50` and survives.
- Fixed exposure `m = 0.80` induces `theta ~= 0.94` and goes extinct.
- Myopic institutions select exposure around `m = 0.645`, induce `theta ~= 0.928`, and go extinct under all tested speed orderings.
- Survival-aware institutions select `m = 0.030`, induce `theta = 0.375`, and survive.
- The answer to "what survives?" can be "none" if all admissible institutions induce negative long-run growth after fast preference closure.

### Article Draft v0

Added `paper/article_draft_v0.md`.
Added `paper/article_draft_v0_math.md` as the preferred reading copy with
Markdown/LaTeX display equations.
Added `paper/article_draft_v0_codex.md` as the Codex-app reading copy with
flowing paragraphs and Unicode equation blocks.

Updated `paper/article_draft_v0_codex.md` to reader-facing draft v0.2.
This version expands the article prose, introduces the model intuition before
the equations, replaces slash-style derivatives with dot notation, and displays
key equations in boxed Unicode blocks for easier reading in Codex.

Updated the Codex draft again to v0.3 after visual review. Removed the
box-drawing equation frames because Codex displayed the right border as a
distracting pipe-like character. Formula displays now use plain quote blocks
with no side borders.

Purpose:

- Give a single readable manuscript for comments.
- Reframe the project around the fast-preference singular limit rather than the platform-only model.
- Keep theorem candidates clearly separated from simulation results.
- Preserve the correction that Nash equilibrium and Darwinian selection are methods/operators; what changes is the state space on which they operate.

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
- Map the exact difference from Kleinberg, Mullainathan, and Raghavan's engagement-optimization model.
- Prove the fast-preference singular-limit theorem before committing to the platform-specific paper spine.
- Extend the long-run survival model to allow competition among institutional regimes and empirically estimated timescale priors.

### Open Questions

- What is the right welfare criterion: initial preferences, long-run preferences, meta-preferences, biological fitness, or constitutional constraints?
- Should "preference autonomy" be modeled as a constraint on the transition kernel `K`?
- Can we derive a clean impossibility theorem without importing psychology?
