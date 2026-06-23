# Combined Round 8: Editor Production Pass

Date: 2026-06-23

Role objective: protect reader comprehension and publication polish while
avoiding over-correction of the mathematical prose.

## Findings

- "Aligned proxy" risked sounding like the exact alignment condition in
  Proposition 3, even though the simulation route is noisy and approximate.
- "Spinodal" needed a plain-language first mention.
- The fixed-state closure assumption needed sharper wording: slow state and
  law are held fixed, while the fast input path may be specified by the
  experiment.
- The hysteresis caption should distinguish mathematical availability of a
  branch from the realized path's basin of attraction.

## Integrated Changes

- Replaced ambiguous finite-game simulation language with "noisy
  approximately aligned proxy."
- Updated Figure 4 and Table 8 language to preserve the distinction between
  simulated approximate alignment and exact maximizer-set alignment.
- Clarified first use of the fold/spinodal terminology.
- Tightened the fixed-state closure paragraph.
- Rewrote the hysteresis caption so persistence is not described as arbitrary.

## Residual Risk

The manuscript is much more readable in HTML, but the next serious production
step should be a LaTeX conversion with native theorem, equation, figure, and
table counters.
