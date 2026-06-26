# Material-Capacity Feedback Model

## Purpose

This is the current core model for the working paper. It replaces the earlier
fast-settling-only emphasis with a closed feedback loop:

```text
fast subjective payoff formation -> choice/equilibrium -> slow material capacity -> future payoff formation
```

The model keeps endogenous preferences tied to material consequences.
Preference-forming environments shape current payoffs; choices under those
payoffs change material capacity; material capacity then affects future payoff
formation.

## Variables

- `K`: material capacity, normalized to `[0, 1]`. Its interpretation depends on
  the application: social skill, solvency, metabolic health, fertility agency,
  institutional trust, learning capacity, or demographic continuity.
- `p`: fast-settled share or probability of a substitute behavior.
- `z`: exposure or inducement from platforms, peers, institutions, advertising,
  or AI systems.
- `q`: baseline pull of the substitute.
- `beta`: sensitivity of the subjective payoff to the field.
- `rho`: protective effect of material capacity on subjective payoff formation.
- `L`: material damage or crowding-out effect from substitute behavior.
- `alpha`, `r`, `d`: baseline repair, practice-based repair, and decay.

## Scalar Normal Form

```text
p(K,z) = logistic(beta * (q + z - rho K))
```

```text
Kdot = alpha + r K^2 (1 - K) - d K - L p(K,z)
```

The repair term is deliberately nonlinear. Repair is weak when capacity is
near zero, stronger at intermediate capacity, and limited near the upper bound.
The normalized state is interpreted as a projected dynamic on `[0,1]`: when the
unprojected drift points below zero or above one, the boundary is a feasible
boundary state. This allows the model to distinguish:

- self-correction;
- threshold traps;
- collapse-prone movement to a lower boundary state.

## Main Result

If the reduced vector field has three simple roots:

```text
K_L < K_U < K_H
```

with negative slope at `K_L` and `K_H` and positive slope at `K_U`, then the
system has two stable capacity states separated by an unstable threshold.

Interpretation:

- Below `K_U`, low capacity makes the substitute attractive, and the substitute
  prevents repair.
- Above `K_U`, capacity makes the substitute less attractive, and capacity
  rebuilds.
- A repair intervention can work by moving the state across the threshold or by
  shifting the vector field upward so the low basin disappears.
- Stronger damage can also produce a lower-boundary state rather than a clean
  two-interior-basin trap.

## Self-Correction And Competition Extension

The model has two correction channels.

First, a current material-drift signal can enter subjective payoff formation:

```text
p_chi(K) = logistic(beta * (q + z - rho K + chi * Phi_chi(K)))
Phi_chi(K) = alpha + r K^2(1 - K) - d K - L p_chi(K)
```

This looks like reality pushing back, but it does not move the steady-state
capacities. At any steady state `Phi_chi(K) = 0`, so the current-drift signal is
zero exactly where it would need to remove the trap. It can damp slopes and
adjustment speeds, but it is not a general self-correction mechanism.

Second, competition among preference-forming rules is modeled by a replicator
layer:

```text
sdot_l = omega * s_l * (S_l - sum_r s_r S_r)
Ndot = N * sum_r s_r g_r
```

Here `s_l` is the prevalence of rule `l`, `S_l` is the operative competitive
score, `g_l` is material growth, `omega` is competition intensity, and `N` is
absolute population, capital, or institutional scale. This separates relative
victory from absolute survival.

Key implication:

- If `S_l` is material viability and tracks `g_l`, competition can shift
  prevalence toward the capacity-preserving rule.
- If `S_l` is an engagement proxy, competition can select a high-engagement sink
  while absolute material mass falls.
- If all available rules have negative material growth, Darwinian competition
  can still produce disappearance rather than convergence to a fitter taste.

## Literature Position

The model draws from:

- Grossman health capital;
- Becker and Murphy rational addiction;
- Bowles endogenous preferences;
- Bisin and Verdier cultural transmission;
- Koszegi and Rabin reference-dependent preferences;
- Genicot and Ray aspirations;
- Brock and Durlauf social interactions;
- Arthur increasing returns and lock-in;
- recommender-system feedback loops;
- randomized social-media exposure/deactivation evidence.

The contribution is the timing discipline: fast subjective payoff formation,
ordinary Nash equilibrium after payoff formation, and slow material capacity
feedback.

## Reproducible Outputs

Run:

```bash
python3 scripts/run_material_feedback_analysis.py
python3 scripts/run_self_correction_analysis.py
python3 scripts/build_material_feedback_article.py
```

Generated outputs:

- `results/material_feedback_report.md`
- `results/tables/material_feedback_equilibria.csv`
- `results/tables/material_feedback_paths.csv`
- `results/tables/material_feedback_parameter_audit.csv`
- `results/figures/material_feedback_phase.svg`
- `results/figures/material_feedback_paths.svg`
- `results/figures/material_feedback_audit.svg`
- `results/self_correction_report.md`
- `results/tables/self_correction_*.csv`
- `results/figures/self_correction_channels.svg`
- `results/figures/competition_selection_channels.svg`
- `paper/when_preferences_move_faster_than_equilibrium_v1.html`

## Evidence Standard

The scalar simulation is a mechanism check, not an empirical estimate. Any
applied claim must name:

1. the material capacity;
2. the substitute behavior;
3. the preference-forming exposure;
4. a measure of capacity change;
5. an identification strategy that separates feedback from fixed heterogeneity
   and ordinary constraints.
