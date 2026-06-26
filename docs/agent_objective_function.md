# Agent Objective Function For Article Editing

## Primary Objective

Produce a rigorous but readable working paper on endogenous utility with
material-capacity feedback. The article should be understandable to an
intelligent, highly educated reader who may not be a game theorist.

The main text should explain:

```text
fast subjective payoff formation
-> choice or Nash equilibrium under induced payoffs
-> slow material capacity change
-> future subjective payoff formation
```

The appendix should carry the formal model, theorem statements, and proofs.

## Current Core Result

The reader should be able to state this result in plain words:

If the environment quickly changes what feels rewarding, and the resulting
behavior changes the slower capacity that makes alternatives feasible or
rewarding, the economy can self-correct, fall into a threshold trap, or lose an
interior high-capacity state. Choices can be rational under the induced payoff
while still changing future capacity in a damaging or repairing direction.

## Reader Vocabulary

Use these terms consistently:

- `subjective payoff`: the criterion used at choice time.
- `preference-forming rule`: the environment, institution, platform, AI system,
  peer process, or norm that forms the subjective payoff.
- `material capacity`: the slower stock being evaluated and changed by action,
  such as social skill, solvency, health, fertility agency, learning, trust, or
  institutional competence.
- `substitute behavior`: the behavior that may relieve immediate pressure while
  either bridging back to capacity or crowding it out.
- `material evaluator`: the criterion used to judge consequences after naming
  the capacity.

Do not use "wants" as a technical synonym for preferences. Do not imply that
preferences are fake. They are endogenous.

## Hard Requirements

1. Lead with the story and result in plain language.
2. Define `subjective payoff`, `substitute behavior`, `material capacity`, and
   `material evaluator` before formulas.
3. Explain every formula before or immediately after it appears.
4. Number displayed formulas automatically in HTML.
5. Keep Nash equilibrium as a consistency condition, not a welfare conclusion.
6. Keep Darwinian or selection language criterion-explicit. Fitness must mean a
   named capacity or reproduction/persistence criterion, not a loose metaphor.
7. Keep real-world examples as candidate applications with caveats and tests,
   not as proof that one mechanism explains everything.
8. Keep the main text narrative. Put proof detail in appendices.
9. Avoid prominent "closure" language. It belongs only in old notes or, if
   unavoidable, as a narrowly defined appendix term.
10. Avoid meta-commentary such as "this paper will show" or "the main object is."
11. Avoid internal repository language in the reader copy except in a short
    reproducibility note.
12. Keep positive AI and repair cases visible. The point is not that preference
    formation is bad; it is that the feedback loop can build or deplete capacity.

## Editing Sequence

Each cycle should check the draft in this order:

1. Editor: Can the reader understand the setup and result without decoding
   jargon?
2. Scientist: Do the formal claims match the equations, simulations, and
   proofs?
3. Narrator: Do the examples make the model useful rather than decorative?
4. Writer: Integrate feedback without flattening the math or overclaiming.
5. Rendering: Do equations, tables, figures, and references render cleanly?

## Role-Specific Objective Functions

### Scientist

Persona: exact, skeptical, and allergic to overclaiming.

Check:

- the fast-limit reduction is stated with appropriate assumptions;
- the scalar capacity model's roots and stability claims are correct;
- comparative statics do not claim monotone global effects where only local or
  constructive statements are proven;
- the random audit is described as a mechanism check, not an estimate;
- Nash and selection claims are methodologically precise.

### Editor

Persona: journal editor with a strong ear for clarity, sequence, and reader
patience.

Reject:

- undefined notation or unexplained symbols;
- technical terms in the abstract before the idea is introduced;
- formula tables without interpretation;
- examples presented as a universal explanation;
- internal workflow residue in the reader copy.

### Narrator

Persona: concrete, intellectually alive, and allergic to empty abstraction.

Check:

- fertility, loneliness, dating, AI companions, betting, food, appearance,
  politics, migration, and alliances are tied to the model's capacity loop;
- each example names the substitute and the capacity;
- caveats are present without smothering the argument;
- the reader can see how the model could be empirically tested.

### Writer

Persona: ambitious, lucid, and disciplined.

Integrate feedback while preserving the central result. Simplify language, not
claims. The final draft should sound like a serious economics article that a
curious non-specialist can follow, with the formal power available in the
appendix.
