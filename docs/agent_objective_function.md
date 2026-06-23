# Agent Objective Function For Article Editing

## Primary Objective

Produce a mathematically rigorous article that can be followed by a highly
educated reader who is not already a specialist in Nash equilibrium, singular
perturbation, or evolutionary preference theory.

The article should be readable without becoming informal, and rigorous without
becoming opaque.

## Reader Model

Assume the reader is intelligent and comfortable with abstract reasoning, but
does not know the paper's notation and should not be asked to infer it.

The reader may know what utility, equilibrium, and welfare mean in ordinary
economic language, but may not know:

- mixed strategies;
- best-response correspondences;
- closure laws;
- boundary-layer arguments;
- singular limits;
- indirect evolutionary preference models;
- post-closure admissibility.

## Hard Requirements

1. State the model in plain words before formal notation.
2. State the main results in plain words before theorem labels.
3. Number every displayed formula.
4. Introduce every symbol before the first displayed formula in which it appears.
5. Never use shorthand such as "fixed-\(E\), fixed-\(\ell\)" without explaining
   that \(E\) is the slow environment and \(\ell\) is the preference-formation
   or closure law being held constant during the fast preference adjustment.
6. Keep Nash equilibrium described as a method or consistency condition, not as
   a welfare conclusion.
7. Keep mixed best-response invariance described as a strong sufficient
   condition for Nash-set agreement, not as a necessary condition.
8. Keep platform material-loss claims conditional on proxy/material
   misalignment on the feasible rule set.
9. Keep welfare language criterion-explicit: final preferences, initial
   preferences, material payoff, and transition-law evaluation are distinct.
10. Do not over-correct by removing mathematical content, weakening theorem
    statements, or replacing formal claims with impressionistic prose.

## Editing Sequence

Each cycle should check the draft in this order:

1. Setup: can a reader state the model after reading the abstract and first
   page?
2. Notation: is each symbol introduced before it appears in a display?
3. Results: are theorem implications stated in plain language before and after
   the formal block?
4. Rigor: did the prose accidentally overstate a sufficient condition,
   simulation result, or welfare interpretation?
5. Rendering: do formula numbers, equations, tables, and theorem boxes render
   cleanly in HTML after MathJax loads?

## Role-Specific Objective Functions

### Modeller / Rigor Agent

Preserve the mathematics while making assumptions explicit. Check especially
that:

- \(E\) is introduced as the slow economic environment before it appears;
- \(\ell\) is introduced as the preference-formation or closure law before it
  appears;
- \(H\), \(\dot\theta\), \(T_\theta\), \(NE(\Gamma)\), and best responses are
  introduced before their first display;
- Proposition 1 remains sufficient, not necessary;
- Proposition 3 remains a feasible-set proxy/material alignment result;
- simulations are described as audits or stress tests, not empirical estimates.

### Writer / Reader Agent

Maximize reader comprehension subject to mathematical accuracy. The article
should tell the reader, in ordinary language, what the model is doing before it
asks the reader to parse a formal display. Every abstract-level result should
answer: what is the object, what changes, what survives, and what does not
follow.

The writer may simplify sentences but must not simplify theorem claims into
false claims.

### Editor / Production Agent

Make the document readable as a published article. Check sequence, definitions,
formula numbering, visual display, and unwanted residue from earlier drafts.

The editor should reject:

- unexplained shorthand such as "fixed-\(E\)" or "fixed-\(\ell\)";
- formula boxes with unbalanced delimiters or duplicate numbering;
- paragraphs that argue against an earlier draft instead of stating the current
  model;
- jargon before definition, especially "boundary layer," "closure-equivalence
  class," and "mixed best-response correspondence."
