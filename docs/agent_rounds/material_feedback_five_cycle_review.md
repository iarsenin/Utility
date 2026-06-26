# Material Feedback Five-Cycle Review

Date: 2026-06-26.

Draft reviewed:

- `paper/when_preferences_move_faster_than_equilibrium_v1.html`

Core generated artifacts:

- `src/utility_endogenous/material_feedback.py`
- `scripts/run_material_feedback_analysis.py`
- `scripts/build_material_feedback_article.py`
- `results/material_feedback_report.md`

## Cycle 1: Editor -> Scientist -> Narrator -> Writer

Editor found that the abstract introduced too many terms too early, the
capacity/substitute/evaluator triad was scattered, and the tables needed
reader-facing interpretation.

Scientist found the largest formal problems:

- the normalized state space needed boundary treatment;
- comparative statics for `beta` and `rho` were overstated;
- the fast-limit proposition needed stronger assumptions;
- the empirical strategy needed a behavior equation.

Narrator found that dating and alliances were underdeveloped, the examples
needed clearer substitutes and capacities, and the scalar model needed at least
one strategic/Nash application.

Writer changes:

- rewrote the abstract in plainer language;
- added a glossary and "how to read the equations" paragraph;
- added interpretation columns and percentages to tables;
- split migration and alliances;
- added dating, AI companion, and alliance capacity tests;
- added projected boundary dynamics;
- replaced broad comparative statics with conditional derivative statements.

## Cycle 2: Verification Agent -> Writer

Verification found no P1 blockers but flagged:

- the two-basin proposition needed exact conditions;
- the random audit needed parameter ranges and seed;
- "baseline" was used inconsistently;
- `F` was used without definition;
- some application mechanisms were cited as phenomena rather than mechanisms.

Writer changes:

- tightened the two-basin proposition to require exactly three interior
  equilibria in the relevant interval and no attracting boundary state;
- added an audit-design table with seed and parameter ranges;
- consistently named the self-correcting and capacity-trap calibrations;
- defined `F` as the material law of motion and distinguished it from the
  evaluator `G`;
- cited Fenichel for singular-perturbation logic;
- softened fertility and GLP-1 mechanism claims where the source evidence is
  indirect.

## Cycle 3: Scientist Check

Checklist:

- Projected state space is explicit in the model and appendix.
- Audit classification separates interior low-high traps from lower-boundary
  projected states.
- `alpha` is used for baseline repair; action notation remains separate.
- The derivative formulas match the scalar model:

```text
dPhi/dL = -p
dPhi/dz = -L beta p(1-p)
dPhi/drho = L beta K p(1-p)
dPhi/dbeta = -L(q+z-rho K)p(1-p)
```

Outcome: no remaining formal blocker found at this stage.

## Cycle 4: Editor/Narrator Check

Checklist:

- The main text starts with a concrete puzzle before equations.
- The abstract states the result directly: self-correction, threshold trap,
  and lower-boundary/collapse-prone dynamics.
- Each major application names the substitute and material capacity.
- Examples are framed as candidate applications with empirical tests, not as
  proof that one mechanism explains everything.
- Nash equilibrium is presented as a consistency condition, not a welfare
  endorsement.

Outcome: prose is substantially clearer than the previous formula-first draft.
Remaining future improvement: a richer worked strategic example could become a
separate section.

## Cycle 5: Production Check

Commands run:

```bash
python3 scripts/run_material_feedback_analysis.py
python3 scripts/build_material_feedback_article.py
python3 -m compileall -q src scripts
git diff --check
```

Source checks:

- HTML parse passed.
- Citation anchors resolve.
- Article counts: 15 equation boxes, 4 theorem boxes, 3 figures, 4 tables.
- No prominent "closure" residue, "wants" terminology, or self-referential
  "this paper will show" scaffolding remains in the generated article.

Browser note:

- Attempted in-app browser visual QA of the local `file://` article.
- Browser Use rejected the local URL by policy and explicitly prohibited
  workarounds. No screenshot was taken in this cycle.

## Current Verdict

The manuscript is now coherent around a stronger analytical spine:

```text
fast subjective payoff formation
-> induced choice or Nash game
-> slow projected material capacity
-> future payoff formation
```

The result is not yet a final journal submission, but it is now a credible
working-paper draft with a defensible model, reproducible mechanism checks, and
reader-facing applications.

Best next research step: develop one richer strategic application, probably an
appearance arms race, political outrage game, dating-market withdrawal game, or
alliance reliability game, so the Nash component has the same force as the
scalar capacity component.
