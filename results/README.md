# Results

This directory contains generated reports, figures, and tables. Treat these as
evidence artifacts, not active writing instructions.

## Current Core Outputs

Run:

```bash
python3 scripts/run_material_feedback_analysis.py
python3 scripts/run_self_correction_analysis.py
python3 scripts/build_material_feedback_article.py
```

Current core generated files:

- `material_feedback_report.md`
- `self_correction_report.md`
- `tables/material_feedback_equilibria.csv`
- `tables/material_feedback_paths.csv`
- `tables/material_feedback_parameter_audit.csv`
- `tables/material_feedback_regime_grid.csv`
- `tables/self_correction_*.csv`
- `figures/material_feedback_loop.svg`
- `figures/material_feedback_regime_map.svg`
- `figures/material_feedback_phase.svg`
- `figures/material_feedback_paths.svg`
- `figures/material_feedback_audit.svg`
- `figures/self_correction_channels.svg`
- `figures/competition_selection_channels.svg`

## Evidence Standard

- Material-feedback and self-correction outputs are mechanism checks, not
  empirical estimates.
- Random audits show how often a qualitative regime appears in a sampled
  parameter class; they do not estimate population frequencies.
- WDI outputs are diagnostic associations and timescale measures, not causal
  evidence of platform-induced preference formation.
- Fashion/meme outputs show criticality, amplification, and hysteresis in a
  stylized settling rule, not estimates for a specific platform.
- Toy and early iteration outputs are retained for source history.

## Figure Use

The current manuscript's main body should use only the salient production
figures:

- mechanism loop figure: fast substitute share and slow capacity drift;
- regime map: damage and repair movements across bridge/trap/collapse regions;
- competition selection figure: bridge share and carrier mass under alternative
  scores.

Time-path, phase-line, audit, and robustness figures belong in appendices unless
a later manuscript explicitly changes that design.

## Legacy Artifacts

Legacy exploratory figures are retained under `figures/legacy/` or as older
named files in `results/figures/`. Use them for provenance only unless a model
or paper section explicitly revives them.
