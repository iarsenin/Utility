# Combined Round 5: Production

Date: 2026-06-23

Role: production editor, formula and rendering sanity.

Target: `paper/combined_fast_preference_closure_v1.html`

## Checks

1. HTML parsing should pass with Python's `HTMLParser`.
2. Raw less-than signs inside MathJax should be escaped as `&lt;`.
3. Equation boxes should be centered, numbered, and horizontally scrollable on narrow screens.
4. Figure and table numbering should remain coherent after insertion of the social-feedback material.
5. The final draft should be opened in a browser and visually checked with screenshots before handoff.

## Integrated Or Pending Actions

- HTML parse passed during editing.
- Raw less-than searches for `<B_c`, `< z`, `<0`, `<1`, `B_c-h<`, and `|h|<` returned clean.
- Figure and table numbering was updated after the merge.
- Browser screenshot QA remains the final verification step after all edits.
