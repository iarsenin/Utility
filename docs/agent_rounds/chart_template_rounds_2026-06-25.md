# Chart Template And Appendix QA Rounds

Date: 2026-06-25

Manuscript: `paper/when_preferences_move_faster_than_equilibrium_v1.html`

## Objective

Bring Appendix C charts and presentation up to a professional publication standard while preserving the paper's notation, formula numbering, table numbering, and reader-friendly narrative style.

## Agent Loop 1

Scientist review:

- Confirmed that the chart redesign should not change the underlying simulations or reported rates.
- Found that the legacy finite-game SVG was not automatically refreshed when the current SVG was regenerated.
- Asked for the network multiplier to state explicitly that the displayed calculation is the zero-taste benchmark where \(D=I\).

Editor review:

- Found that the appendix referred to a mean-field hysteresis figure without embedding the figure in the current manuscript.
- Found clipped y-axis labels in two charts.
- Flagged the old platform heatmap as not production-ready if presented as part of the current chart set.
- Asked for a visible cue on mobile tables.

Fixes:

- Added a shared SVG style module with a warm paper background, red editorial rule, and semantic teal/amber/blue/red palette.
- Embedded the mean-field hysteresis chart in Appendix C.
- Moved axis labels and regenerated the affected charts.
- Added the zero-taste \(D=I\) explanation in Appendix C and the network chart subtitle.
- Made the old platform heatmap a legacy exploratory output.

## Agent Loop 2

Scientist review:

- Passed equation numbering, theorem/proof ordering, and cross-reference logic.
- Confirmed the current and legacy finite-game SVGs are identical compatibility copies.
- Confirmed the \(D=I\) specialization is scoped to the zero-taste benchmark and does not alter the general formula.

Editor review:

- Confirmed embedded Appendix C figures are visually coherent and consistent.
- Required that old internal language not appear in figure-facing text.
- Required an explicit mobile affordance for horizontally scrollable tables.

Fixes:

- Replaced chart-facing "audit" titles and footers with "check" language.
- Added mobile-only table guidance and a right-edge inset shadow for wide tables.
- Saved browser-rendered QA screenshots for the article top, Appendix C chart region, finite-game section, and mobile table behavior.

## Validation

- Python syntax passed for updated scripts and chart modules.
- HTML parse check passed with no missing assets, missing anchors, duplicate ids, or open tags.
- Current manuscript counts: 14 sections, 4 figures, 7 tables, 15 numbered equations, 11 formal boxes.
- SVG rasterization passed for all current Appendix C figures.
- Current and legacy finite-game SVGs match byte-for-byte after regeneration.
