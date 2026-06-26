# Material-Capacity Feedback Model

## Purpose

This is the current core model for the working paper. It replaces the
fast-settling-only emphasis with a closed feedback loop:

```text
fast subjective payoff formation -> choice/equilibrium -> slow material capacity -> future payoff formation
```

The model is designed to answer the user's central objection: endogenous
preferences should not be free-floating. They should be shaped by material
outcomes, and material outcomes should be shaped by the choices made under the
induced subjective payoff.

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
