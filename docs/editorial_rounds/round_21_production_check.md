# Round 21 Production Check

## Visual QA

Rendered `paper/geb_submission_v1.html` through the local server at
`http://127.0.0.1:8765/paper/geb_submission_v1.html` and captured screenshots
after MathJax completed.

Screenshots:

- `results/figures/geb_submission_v1_round21_qa_top.png`
- `results/figures/geb_submission_v1_round21_qa_intro_formula_number.png`
- `results/figures/geb_submission_v1_round21_qa_model_formula_numbers.png`
- `results/figures/geb_submission_v1_round21_qa_material_scalar.png`
- `results/figures/geb_submission_v1_round21_qa_nash.png`

## Rendering Findings

- Formula boxes display visible right-side numbers.
- The first formal display is introduced as Equation (1) for a fixed slow
  environment \(E\).
- The material benchmark and scalar material evaluation formulas render cleanly
  as Equations (6) and (7), with no stray delimiters.
- The expected-payoff and best-response equations render cleanly as Equations
  (8) and (9).

## Source Validation

- `paper/geb_submission_v1.html` parses with Python's `HTMLParser`.
- There are 15 `.equation` blocks and 15 equation labels.
- There are 15 source display-math openings and 15 source display-math closings.
- MathJax display tagging is set to `tags: 'none'`; CSS counters are the single
  visible numbering system.
- Rendered text has no `fixed-E` or `fixed-l` residue.
