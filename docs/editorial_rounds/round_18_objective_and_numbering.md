# Round 18 Objective And Formula Numbering

## Objective Update

The editorial objective was tightened after the draft still left a highly
educated non-specialist reader guessing at notation. The new hard requirements
are recorded in `docs/agent_objective_function.md`.

The key change is simple: define before formalizing. In particular, the draft
must introduce \(E\), \(\ell\), \(\theta\), \(H\), \(NE(\Gamma)\), best
responses, and material evaluation before asking the reader to parse displayed
formulas.

## Manuscript Edits

- Added visible CSS equation numbers to every `.equation` display in
  `paper/geb_submission_v1.html`.
- Changed MathJax display tagging to `tags: 'none'` so CSS counters are the
  single equation-numbering system.
- Rewrote the abstract language around \(E\), \(\ell\), \(\theta_\ell^\star(E)\),
  \(\Gamma_\ell^\star(E)\), Nash sets, and mixed best-response invariance.
- Expanded the introduction glossary to include the slow environment, action
  profiles, settled preference state, Nash set, and scalar material value.
- Added explicit prose around the first display, now referenced as Equation (1).

## Guardrails

- Nash equilibrium remains a consistency condition.
- Material payoff remains separate from subjective utility.
- Preference change alone is not called material loss.
- Mixed best-response invariance remains a strong sufficient condition, not a
  necessary condition for every fixed game.
