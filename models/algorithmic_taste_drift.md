# Algorithmic Taste Drift With Darwinian Selection

## Benchmark

The exogenous-preference benchmark is a one-period consumption problem:

```text
max_{o,h} theta log(o) + (1 - theta) log(h)
s.t. o + h = 1
```

where `theta` is fixed. The solution is:

```text
o* = theta
h* = 1 - theta
```

## Endogenous Modification

Let `theta` evolve. In the bootstrap simulation:

```text
theta' = theta + eta [A(theta; M) (1 - theta) - B theta]
```

where:

- `A(theta; M)` is the algorithmic field pushing taste toward online/artificial goods,
- `B` is the offline anchor,
- `eta` is the plasticity speed.

Population mass is updated by fitness:

```text
mu'(theta') proportional to K(theta' | theta) F(theta) mu(theta)
```

## Interpretation

This is intentionally stark. It asks whether a fast preference-transition technology can overpower a slower fitness penalty. If yes, the economy can move toward high subjective satisfaction with low biological or social viability.

## Simulation Output

Run:

```bash
python3 scripts/run_toy_models.py
```

Then inspect:

- `results/tables/endogenous_taste_summary.csv`
- `results/toy_model_report.md`
