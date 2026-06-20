# Fast Preference Limit Report

## Mathematical Limit

Let slow economic state be `z` and preference state be `theta`. The extreme case is:

```text
T d theta / dt = G(theta, z, a, m)
d z / dt = H(z, theta, a, m)
a in BR(theta, z, m)
```

Taking `T -> 0` forces the system onto the critical set:

```text
G(theta, z, a, m) = 0
```

If the fast subsystem has a unique attracting branch `theta = Phi(z, m)`,
the slow economy becomes:

```text
d z / dt = H(z, Phi(z, m), BR(Phi(z, m), z, m), m)
```

Preferences no longer behave like a slowly selected trait. They behave like an
instantaneous state constraint.

## Cross-Model Numerical Readout

### Taste Drift

| scenario | finite_final_theta | fast_limit_theta | finite_final_fitness | fast_limit_fitness | selection_can_move_preferences |
| --- | --- | --- | --- | --- | --- |
| no_fast_preference_law | 0.0140 |  | 2.7340 |  | True |
| weak_algorithmic_adaptation | 0.1946 | 0.6051 | 2.2498 | 1.3417 | False |
| strong_algorithmic_adaptation | 0.9614 | 0.9615 | 0.7900 | 0.7899 | False |

In the strong-adaptation case the finite model already approaches the singular
attractor: finite theta `0.9614`,
fast-limit theta `0.9615`.

### Selection Invariance

| scenario | fast_limit_theta | fast_limit_fitness | note |
| --- | --- | --- | --- |
| selection_invariance_s0.20 | 0.9615 | 0.9460 | Same fast attractor across selection strengths; only realized fitness changes. |
| selection_invariance_s0.60 | 0.9615 | 0.8467 | Same fast attractor across selection strengths; only realized fitness changes. |
| selection_invariance_s1.00 | 0.9615 | 0.7577 | Same fast attractor across selection strengths; only realized fitness changes. |
| selection_invariance_s1.80 | 0.9615 | 0.6069 | Same fast attractor across selection strengths; only realized fitness changes. |
| selection_invariance_s3.20 | 0.9615 | 0.4116 | Same fast attractor across selection strengths; only realized fitness changes. |
| selection_invariance_s5.00 | 0.9615 | 0.2498 | Same fast attractor across selection strengths; only realized fitness changes. |

The fast attractor is invariant to selection strength in this model because
selection acts on the slow population distribution after the fast taste state
has already collapsed. Selection changes realized fitness, not the preference
state.

### Indirect Evolutionary Prisoner's Dilemma

| scenario | finite_final_lambda | fast_limit_lambda | finite_final_cooperation | fast_limit_cooperation | material_nash |
| --- | --- | --- | --- | --- | --- |
| fixed_preferences_selection_only | 0.0804 |  | 0.0004 |  |  |
| prosocial_institution | 1.0827 | 1.1000 | 1.0000 | 1.0000 | False |
| conflict_algorithm | -0.2497 | -0.2500 | 0.0000 | 0 | True |
| knife_edge_mixed_fast_preference | 0.3403 | 0.3800 | 0.2745 | 0.3792 | False |

Fast prosocial adaptation gives cooperation `1.0000`.
Fast conflict adaptation gives cooperation `0`.
Thus the material Nash prediction survives only when the fast preference
attractor itself points to material self-interest.

### Platform Control

| scenario | penalty_case | fast_limit_exposure | fast_limit_theta | fast_limit_fitness | fast_limit_platform_value | autonomy_penalty |
| --- | --- | --- | --- | --- | --- | --- |
| no_platform_selection_benchmark | steady | 0.0000 | 0.0000 | 3.0042 | 0.2000 | 0.0000 |
| no_platform_selection_benchmark | boundary_layer | 0.0000 | 0.0000 | 3.0042 | 0.2000 | 0.1325 |
| myopic_platform_low_cost | steady | 0.8000 | 0.9412 | 0.6851 | 1.1656 | 0.0000 |
| myopic_platform_low_cost | boundary_layer | 0.8000 | 0.9412 | 0.6851 | 1.1656 | 0.3594 |
| platform_with_calibrated_guardrail | steady | 0.8000 | 0.9412 | 0.6851 | 1.1656 | 0.0000 |
| platform_with_calibrated_guardrail | boundary_layer | 0.0500 | 0.5000 | 1.5296 | -4.1179 | 0.0325 |

In the steady fast limit, transition penalties vanish after the boundary layer.
The low-cost platform chooses exposure `0.8000`
and pushes theta to `0.9412`.
If autonomy is charged on the boundary-layer jump itself, the calibrated
guardrail chooses exposure `0.0500`.

## Candidate Invariant Results

1. **Attractor Replacement**: with a unique fast preference attractor, utility
   is no longer a primitive or a selected type; it is the graph of a fast
   response map `Phi(z, m)`.
2. **Darwinian Selection Loses Its Preference Target**: selection can change
   population size or select adaptation rules, but it cannot select among
   preference types that are instantly reset by the fast law.
3. **Material Nash Need Not Survive**: actions are Nash only with respect to
   instantaneous adapted preferences. They need not be Nash in the material
   payoff game.
4. **Ex Post Welfare Becomes Fragile**: if final preferences adapt to the
   reached state, final-preference Pareto comparisons can validate the path
   that produced those preferences.
5. **Only Meta-Objects Survive**: invariant welfare/equilibrium claims must be
   stated over adaptation laws, admissible transition kernels, initial or
   meta-preferences, material fitness, or constitutional constraints.

## Research Verdict

This limit is more fundamental than the platform-specific model. The platform
case becomes one application of a broader singular-limit theorem: when utility
adapts infinitely fast, economics on fixed utility functions is replaced by
economics on the critical manifold of preference adaptation.
