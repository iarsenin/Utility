# Self-Correction And Competition

This note records the current correction and selection results.

## Question

Does the model contain an automatic self-correcting mechanism, or can a
low-capacity trap persist even when deterioration is visible?

## Result 1: Current-Movement Signals Are Weak

The tested signal reports whether material capacity is improving or
deteriorating right now. In the scalar diagnostic, this signal changes
adjustment speeds and local slopes, but it does not move the interior
steady-state capacities. At a steady state, current movement is zero, so the
signal is silent exactly where it would need to remove the trap.

Interpretation: warning, discomfort, regret, or current pain can matter, but
they are not a general automatic correction mechanism in the minimal model.

## Result 2: Capacity-Level Feedback Can Repair

A different channel depends on the level of material capacity itself. If higher
capacity makes the substitute less attractive strongly enough, the low-capacity
trap can disappear in the diagnostic calibration.

Interpretation: durable correction requires a force that changes the capacity
path, not only a warning about current movement.

## Result 3: Competition Selects Its Score

Competition is represented as a share dynamic over preference-forming rules,
with a separate equation for absolute material scale. This separates relative
victory from absolute survival.

In the two-rule diagnostic:

- Material-viability competition selects the capacity-preserving bridge and
  total scale rises.
- Engagement-proxy competition selects the high-engagement sink and total scale
  falls.

Interpretation: Darwinian language is useful only after the competitive score
is named. Competition can select attention, revenue, reproduction,
institutional persistence, or material viability. These are not the same object.

## Article Consequence

The paper should not sound like advice. It should map mechanisms:

- which forces move capacity paths;
- when a low trap persists;
- which score governs selection;
- whether relative success and absolute survival diverge.

## Reproducible Outputs

Run:

```bash
python3 scripts/run_self_correction_analysis.py
```

Outputs:

- `results/self_correction_report.md`
- `results/tables/self_correction_material_signal_roots.csv`
- `results/tables/self_correction_stock_feedback_roots.csv`
- `results/tables/self_correction_competition_summary.csv`
- `results/figures/self_correction_channels.svg`
- `results/figures/competition_selection_channels.svg`
