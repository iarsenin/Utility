# Narrative Appendix Rewrite Agent Rounds

Date: 2026-06-26

## Objective

Rewrite `paper/when_preferences_move_faster_than_equilibrium_v1.html` so the
main text is readable as a narrative article for educated non-specialists while
retaining a rigorous formal appendix for experts.

Main requirements:

- no displayed formulas, theorem boxes, proofs, or empirical equations in the
  main text;
- all formal machinery in appendices;
- only the most salient charts in the main body;
- real-world examples framed as testable mappings, not completed explanations;
- real recheck of math and conclusions after recent model changes.

## Review Agents

- Scientist: exact, skeptical, and focused on whether formal claims match
  equations, simulations, and proofs.
- Editor: journal editor focused on clarity, sequence, vocabulary, and reader
  patience.
- Narrator: concrete narrative reviewer focused on whether the formal results
  illuminate real puzzles.

## Cycle Summary

### Cycle 1

Main feedback:

- move all displayed equations and theorem/proof language out of the main body;
- keep only salient figures up front;
- make bridge versus sink the reader-facing story;
- keep current-drift, capacity feedback, and competition claims scoped to the
  model.

Implemented:

- moved formal equations, empirical equations, proofs, calibration tables, and
  audit tables into appendices;
- kept three main figures: threshold paths, self-correction channels, and
  competition selection channels.

### Cycle 2

Main feedback:

- remove leftover math-book language and inline notation from the main text;
- make AI companionship a running example;
- add real-world vignettes for sports betting, GLP-1 medicines, and political
  outrage;
- tighten overclaims around current-drift and competition.

Implemented:

- removed visible main-body math;
- added plain-language results and examples;
- distinguished relative prevalence from absolute survival.

### Cycle 3

Main feedback:

- pass on structure and narrative;
- replace specialist language such as `scalar diagnostic`, `root pattern`, and
  `vector field` in the main text;
- define material viability in plain language;
- split dense examples.

Implemented:

- changed main text to `one-capacity example`;
- rewrote correction and competition captions;
- split candidate-domain vignettes and expanded the positive GLP-1 bridge/sink
  case.

### Cycle 4

Main feedback:

- pass with final precision edits;
- state that the current-drift theorem concerns interior steady states;
- soften "objective force only if";
- avoid early specialist phrasing in the abstract.

Implemented:

- revised abstract;
- changed the appendix proposition title to "Current deterioration does not move
  interior steady states";
- rewrote Nash section in plainer language.

### Cycle 5

Final gate:

- Scientist: PASS, no blocking math or conclusion issues.
- Editor: PASS, no blocking readability/style issues.
- Narrator: PASS.

## Verification

Commands run:

```text
python3 scripts/run_material_feedback_analysis.py
python3 scripts/run_self_correction_analysis.py
python3 scripts/build_material_feedback_article.py
python3 -m compileall -q src scripts
git diff --check
```

HTML structural check:

- missing references: none;
- unused references: none;
- main displayed equations: 0;
- main theorem boxes: 0;
- visible main inline math: none;
- figures: 5 total, 3 in main;
- tables: 6 total, 1 in main;
- template placeholders: 0.

Independent numeric audit:

- current-drift roots match baseline roots up to `1.192e-10` at the largest
  tested signal strength;
- stock-feedback channel removes the low trap at about `rho = 3.1` on the grid;
- material-viability competition selects the bridge and recovers total scale;
- engagement-proxy competition selects the sink while total scale falls.

## Current Manuscript Shape

Main text:

- abstract;
- puzzle in plain words;
- model in words;
- plain-language results with three figures;
- Nash equilibrium and competition;
- AI companions and loneliness as flagship example;
- candidate domains and empirical strategy;
- relation to economics literature;
- implications and conclusion.

Appendices:

- Appendix A: general formal model;
- Appendix B: scalar capacity model and propositions;
- Appendix C: numerical diagnostics and tables;
- Appendix D: empirical specification.
