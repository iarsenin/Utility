# Article Editing Guide

This file defines the stable objective for future article edits. It should not
record transient reactions or turn-by-turn comments.

## Primary Objective

Produce a rigorous but readable working paper on endogenous utility with
material-capacity feedback. The article should be understandable to a highly
educated reader who is not necessarily a game theorist, while remaining
mathematically precise enough for economics readers.

The main text should explain:

```text
fast subjective payoff formation
-> coherent choice or Nash equilibrium under induced payoffs
-> slow material-capacity change
-> future subjective payoff formation
-> competition among preference-forming rules under an explicit score
```

## Reader Contract

The main text is a narrative argument. It should contain no displayed formulas,
theorem boxes, proof boxes, or empirical equations. The appendix carries the
formal model, propositions, proofs, calibrations, robustness tables, and
empirical equations.

The first page should not read like a mathematical abstract. Start with a
concrete situation where a local choice is coherent under the payoff the
environment presents, then show how that choice changes a slower material
capacity. Technical terms may enter only after the reader can see what they are
for.

Define the core vocabulary once in the main text. Prefer a short prose handoff
near the first examples over callout boxes or repeated definition areas. Later
sections should use the vocabulary to advance the argument, not restart the
setup.

The abstract should state the result in plain language:

- fast environments can change what feels worth choosing;
- today's choice can change tomorrow's material capacity;
- bridge, trap, and collapse-prone regimes can arise;
- self-correction can fail if the feedback only reports current movement;
- competition selects whatever score it rewards.

Avoid compressed theorem-management phrases in the abstract, including
`zero-drift equation`, `current-drift signal`, `one-capacity diagnostic`, and
`lower-boundary attracting state`.

## Core Vocabulary

Use these terms consistently:

- `subjective payoff`: the criterion used at choice time;
- `preference-forming rule`: the environment, institution, platform, AI system,
  peer process, or norm that forms the subjective payoff;
- `substitute behavior`: the quick reward or relief that may either bridge
  back to capacity or crowd it out;
- `material capacity`: the slower stock changed by behavior, such as social
  skill, solvency, health, learning, trust, or institutional competence;
- `competitive score`: the score that determines which preference-forming rule
  expands, such as material viability, engagement, revenue, attention,
  reproduction, or institutional persistence.

Do not use `wants` as a technical synonym for preferences. Do not imply that
preferences are fake. They are endogenous.

## Claims To Preserve

- Nash equilibrium is a consistency condition after subjective payoffs are
  formed, not a welfare conclusion.
- Selection is meaningful only after the selected object and competitive score
  are named.
- Competition can reallocate share toward a better rule; it does not erase a
  sink rule's own low-capacity equilibrium unless the capacity dynamics also
  change.
- The scalar simulations are mechanism checks, not empirical estimates.
- Real-world examples are candidate tests, not proof that one mechanism
  explains everything.

## Main-Text Style

Use a serious popular-science register: concrete, explanatory, and alive, but
not sloppy. Simplify sentences, not claims.

Prefer:

- concrete examples before abstractions;
- short explanations of why a term matters;
- visible caveats that do not smother the argument;
- figures with interpretive captions;
- one flagship example that carries the full mechanism.

Avoid:

- meta-commentary such as "this paper will show";
- formula names before the intuition is clear;
- prominent use of `closure`;
- advice-like prose;
- internal workflow residue;
- long lists of topical examples before one example has done real explanatory
  work.

## Formal Placement

The appendix should explain every formula before or immediately after it
appears. Displayed formulas should be numbered automatically in HTML.

The main body may use at most three salient figures:

- threshold trap;
- self-correction channel;
- competition score.

Audit tables and robustness diagnostics belong in the appendix.

## Review Loop

Use these roles when an agentic edit cycle is requested:

1. **Editor:** clarity, sequence, style, reader patience.
2. **Scientist:** theorem scope, model fidelity, no overclaiming.
3. **Narrator:** examples illuminate the mechanism rather than decorate it.
4. **Writer:** integrate feedback without flattening the result.
5. **Rendering:** verify equations, tables, figures, references, and browser
   layout.

Every reader-facing HTML revision must be visually checked in the target
browser and recorded with a screenshot.
