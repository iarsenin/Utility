# Model Selection Audit

This note records durable lessons from earlier model comparisons. It is not the
current paper spine.

## Durable Lesson

The project should not claim that fast endogenous preferences automatically
produce collapse or welfare loss. The result depends on how induced subjective
payoffs connect to material capacity and on whether the competitive score is
aligned with material viability.

## Model Families Assessed

| Model family | Durable use | Limitation |
| --- | --- | --- |
| One-dimensional taste drift | Exposition of fast preference movement. | Too easy to make harm automatic through monotone assumptions. |
| Indirect evolutionary Prisoner's Dilemma | Link to evolutionary preference literature. | Familiar result space; not enough novelty by itself. |
| Platform preference control | Useful application of proxy misalignment. | Can collapse into "engagement is not welfare" without capacity feedback. |
| Generic finite-game fast settling | Good formal background for Nash invariance. | Too abstract to carry the current reader-facing paper alone. |
| Material-capacity feedback | Current paper core. | Scalar version is a diagnostic model, not an empirical estimate. |

## What Survived Into The Current Paper

- Keep Nash equilibrium as a consistency condition after subjective payoffs are
  formed.
- Separate subjective payoff, material outcome, and competitive score.
- Use platform or recommender systems as examples of preference-forming rules,
  not as the whole theory.
- Avoid making harm automatic; identify alignment and feedback conditions.

## What Was Demoted

The finite-game singular-limit route is no longer the main manuscript frame.
It remains useful in the appendix and in future theory work, especially for
best-response invariance and selection-target claims.

The current paper instead leads with material capacity because it better
connects endogenous preferences to measurable consequences: social skill,
solvency, health, trust, learning, and institutional competence.

## Reproducible Audit

Earlier model-selection diagnostics can still be run with:

```bash
python3 scripts/run_model_selection_audit.py
python3 scripts/run_model_selection_sensitivity.py
```

Outputs:

- `results/model_selection_audit_report.md`
- `results/model_selection_sensitivity_report.md`
- `results/tables/model_selection_*.csv`
- `results/figures/model_selection_*.svg`

Treat these as background diagnostics unless a future paper revives the
finite-game route.
