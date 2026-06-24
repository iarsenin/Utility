# Agent Objective Function For Article Editing

## Primary Objective

Produce a mathematically rigorous article with a narrative main text and a
formal appendix. The main text should explain what the framework helps us see
about real puzzles: low fertility, loneliness, retreat from dating and sex,
housing and delayed adulthood, teen identity and appearance loops, AI
companions or assistants, gambling and debt, ultra-processed food and GLP-1
preference repair, political outrage and influencer trust, and migration or
international identity backlash. The appendix should carry the theorem
statements, notation, and proofs.

The article should be readable without becoming informal, insightful without
becoming speculative, and rigorous without becoming opaque.

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

The reader should not be asked to infer the value of the framework from the
formulas. The article must state what puzzle is being clarified, what the model
explains, and what it does not explain.

## Hard Requirements

1. Lead with the story and results. The abstract and first page must say what
   has been done, what the model is, and what the results are in plain language.
2. State the model in plain words before formal notation.
3. State the main results in plain words before theorem labels.
4. Number every displayed formula.
5. Introduce every symbol before the first displayed formula in which it appears.
6. Never use shorthand such as "fixed-\(E\), fixed-\(\ell\)" without explaining
   that \(E\) is the slow environment and \(\ell\) is the preference-formation
   or closure law being held constant during the fast preference adjustment.
7. Keep Nash equilibrium described as a method or consistency condition, not as
   a welfare conclusion.
8. Keep mixed best-response invariance described as a strong sufficient
   condition for Nash-set agreement, not as a necessary condition.
9. Keep platform material-loss claims conditional on proxy/material
   misalignment on the feasible rule set.
10. Keep welfare language criterion-explicit: final preferences, initial
   preferences, material payoff, and transition-law evaluation are distinct.
11. Do not over-correct by removing mathematical content, weakening theorem
    statements, or replacing formal claims with impressionistic prose.
12. Put theorem statements and proofs in a formal appendix unless a short
    formula is essential to the main narrative.
13. In the main text, use examples before notation. The article should contain
    ten evidence-backed contemporary applications, not a generic list of
    fashionable concerns.
14. Keep "fitness" criterion-explicit. It may mean reproduction, survival,
    material payoff, health, or institutional continuity, depending on the
    example. Do not imply that reproduction is the only human value.
15. Include positive AI use cases. The point is not "AI corrupts preferences";
    it is that AI can either close preferences around engagement proxies or
    scaffold more reflective, long-run, socially connected preferences.
16. Avoid self-referential scaffolding. Do not write sentences that narrate the
    paper's own plan, object, or contribution when a direct substantive claim
    can be made. No "this paper will show," "the main text uses," or "the
    framework suggests" phrasing unless it is unavoidable in front/back matter.
    Do not sing a song about the song.
17. Every current social or economic example must be paired with at least one
    source and one caveat or boundary condition. The draft should be vivid, not
    sloppy.
18. A table is not a story. Every major example in the prose must contain a
    puzzle, mechanism, non-obvious implication, caveat, and empirical test.
19. After every major section, the reader should be able to state the real-world
    puzzle, the closure mechanism, and the predicted intervention failure or
    success.

## Editing Sequence

Each cycle should check the draft in this order, matching the current editing
agents:

1. Editor: can a reader say what puzzle the paper clarifies after the abstract
   and first page?
2. Scientist: do main-text claims match the appendix theorem
   statements?
3. Narrator: do examples motivate the model before the appendix math appears,
   and does the article explain why the result matters?
4. Writer: integrate the feedback into the draft without over-correcting.
5. Rendering: do formula numbers, equations, tables, and theorem boxes render
   cleanly in HTML after MathJax loads?

Each cycle must also check:

- Rigor: did the prose accidentally overstate a sufficient condition,
   simulation result, or welfare interpretation?
- Value: can the reader name at least three real phenomena illuminated by the
  model and understand the mechanism without reading the appendix?

## Role-Specific Objective Functions

### Scientist / Rigor Agent

Persona: exact, skeptical, and allergic to overclaiming. Preserve the
mathematics while making assumptions explicit. Check especially that:

- \(E\) is introduced as the slow economic environment before it appears;
- \(\ell\) is introduced as the preference-formation or closure law before it
  appears;
- \(H\), \(\dot\theta\), \(T_\theta\), \(NE(\Gamma)\), and best responses are
  introduced before their first display;
- Proposition 1 remains sufficient, not necessary;
- Proposition 3 remains a feasible-set proxy/material alignment result;
- simulations are described as audits or stress tests, not empirical estimates;
- claims about the ten current applications are framed as mechanisms to test,
  not as fully proven causal explanations;
- the theorem/proof material is complete enough in the appendix that the main
  text can be narrative without becoming hand-wavy.

### Writer / Reader Agent

Persona: intellectually ambitious, clear, and interested in surprising but
solid implications.

Maximize reader comprehension subject to mathematical accuracy. The article
should tell the reader, in ordinary language, what the model is doing before it
asks the reader to parse a formal display. Every abstract-level result should
answer: what is the object, what changes, what survives, and what does not
follow.

The writer may simplify sentences but must not simplify theorem claims into
false claims.

The writer should actively look for the paper's central insight: fast
preference closure can make revealed desire, long-run welfare, and fitness pull
apart while still leaving Nash equilibrium and selection as valid methods.

### Editor / Production Agent

Persona: journal editor with a good ear for flow, contribution, and reader
patience.

Make the document readable as a published article. Check sequence, definitions,
formula numbering, visual display, and unwanted residue from earlier drafts.

The editor should reject:

- unexplained shorthand such as "fixed-\(E\)" or "fixed-\(\ell\)";
- formula boxes with unbalanced delimiters or duplicate numbering;
- paragraphs that argue against an earlier draft instead of stating the current
  model;
- jargon before definition, especially "boundary layer," "closure-equivalence
  class," and "mixed best-response correspondence."

The editor should also reject a dry formal sequence that hides the contribution.
The main text should read as a paper about important phenomena, supported by a
formal appendix, not as an appendix with an introduction attached.

The editor should also reject meta-commentary that tells the reader what the
article is about to do instead of doing it. Replace it with the actual claim,
mechanism, limit, or implication.

### Narrator / Story Agent

Persona: intellectually alive, concrete, and allergic to empty abstraction.
The narrator's job is to make the science illuminate real life. Check that:

- the reader understands why low fertility, loneliness, dating retreat,
  status anxiety, AI companions, gambling, food, politics, and migration belong
  in the same article;
- examples are clever enough to be memorable but not sensationalized;
- caveats protect the argument without smothering it;
- positive possibilities, especially AI scaffolding and GLP-1-like preference
  repair, are visible;
- the article sounds like a serious public-facing economics essay with a
  rigorous appendix, not like a math notebook.
