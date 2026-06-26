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
-> competition among preference-forming rules under an explicit metric
```

The main text should be a narrative argument with no displayed formulas and no
theorem or proof boxes. The appendix should carry the formal model, theorem
statements, proofs, empirical equations, calibration tables, and numerical
audit tables. The main text may use only a small number of salient figures that
teach the argument directly.

The main text should use a Scientific American style: concrete, explanatory,
and alive, but not stripped of technical content. Short sentences are useful
when they clarify; technical terms are useful when they are introduced before
they are used. Avoid academic scaffolding when a direct claim will do, but do
not hide the actual result. Terms such as `interior steady state`, `threshold`,
`scalar model`, and `competitive score` may appear in the main body when the
sentence explains what they mean.

## Current Core Result

The reader should be able to state this result in plain words:

If the environment quickly changes what feels rewarding, and the resulting
behavior changes the slower capacity that makes alternatives feasible or
rewarding, the economy can self-correct, fall into a threshold trap, or enter a
collapse-prone lower-boundary region in the scalar diagnostics. Choices can be
rational under the induced payoff while still changing future capacity in a
damaging or repairing direction.

The current revision adds the objective correction result:

- An instantaneous current-drift signal alone does not move interior
  steady-state capacities in the one-capacity model, because the signal is zero
  at interior steady states.
- A sufficiently strong level-of-capacity channel can change the number and
  location of long-run states and remove a low-capacity trap in the diagnostic
  calibration.
- Competition preserves capacity when the competitive score ranks the
  capacity-preserving rule above the sink. Material viability is one aligned
  score; engagement or another proxy can select a sink while absolute material
  mass falls.

## Reader Vocabulary

Use these terms consistently:

- `subjective payoff`: the criterion used at choice time.
- `preference-forming rule`: the environment, institution, platform, AI system,
  peer process, or norm that forms the subjective payoff.
- `material capacity`: the slower stock being evaluated and changed by action,
  such as social skill, solvency, health, metabolic resilience, learning, trust, or
  institutional competence.
- `substitute behavior`: the behavior that may relieve immediate pressure while
  either bridging back to capacity or crowding it out.
- `material outcome metric`: the plain-language term in the main text for the
  criterion used to judge consequences after naming the capacity.
- `material evaluator`: the formal appendix term for the material outcome
  metric.
- `competitive score`: the score that determines which preference-forming rule
  expands under competition. It may be material viability, engagement, revenue,
  attention, reproduction, solvency, or institutional persistence. Always name
  it.

Do not use "wants" as a technical synonym for preferences. Do not imply that
preferences are fake. They are endogenous.

## Hard Requirements

1. Lead with the story and result in plain language.
2. Define `subjective payoff`, `substitute behavior`, `material capacity`, and
   `material outcome metric` in the main text before any formal appendix.
3. Keep displayed formulas, theorem statements, proofs, and empirical equations
   out of the main text; put them in appendices.
4. Explain every appendix formula before or immediately after it appears.
5. Number displayed formulas automatically in HTML.
6. Keep Nash equilibrium as a consistency condition, not a welfare conclusion.
7. Keep Darwinian or selection language criterion-explicit. Fitness must mean a
   named capacity or reproduction/persistence criterion, not a loose metaphor.
8. Keep real-world examples as candidate applications with caveats and tests,
   not as proof that one mechanism explains everything.
9. Keep the main text narrative. Put proof detail in appendices.
10. Avoid prominent "closure" language. It belongs only in old notes or, if
   unavoidable, as a narrowly defined appendix term.
11. Avoid meta-commentary such as "this paper will show" or "the main object is."
12. Avoid internal repository language in the reader copy except in a short
    reproducibility note.
13. Keep positive AI and repair cases visible. The point is not that preference
    formation is bad; it is that the feedback loop can build or deplete capacity.
14. Distinguish formal theorem, constructive calibration, random audit, and
    empirical conjecture.
15. Avoid advice-like prose. State implications as changes in capacity paths,
    measurable capacity changes, or falsifiable predictions.
16. Use one flagship application to carry the full mechanism before listing
    candidate domains.
17. Keep the bridge/sink distinction visible: a bridge rule rebuilds the named
    material capacity, while a sink wins the induced payoff game and depletes
    the capacity that would make exit feasible.
18. Keep at most three salient charts in the main body: threshold trap,
    correction channel, and competition score. Put audit figures and tables in
    appendices.
19. In the main text, use the memorable result names `Bridge`, `Trap`,
    `Collapse`, `Alarm`, and `Selection`, but pair them with the technical
    claim they summarize.
20. Captions should be short and interpretive. They should tell the reader what
    the figure says, not restate the formal model.
21. The abstract must include enough technical detail to state the result:
    fast-settled subjective payoff, slow material capacity, the scalar
    bridge/trap/collapse regimes, the current-drift warning limitation, and the
    dependence of Darwinian selection on the competitive score. Do this in
    prose, without symbolic formulas in the abstract.

## Editing Sequence

Each cycle should check the draft in this order:

1. Editor: Does the prose read like serious popular science rather than either
   a math monograph or a motivational essay?
2. Scientist: Do the formal claims match the equations, simulations, and
   proofs?
3. Narrator: Do the examples make the model useful rather than decorative?
4. Writer: Integrate feedback without flattening the math, adding prescriptions,
   or overclaiming.
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
- competition claims distinguish relative prevalence from absolute survival;
- the selected metric is not conflated with objective material welfare.

### Editor

Persona: journal editor with a strong ear for clarity, sequence, and reader
patience.

Reject:

- undefined notation or unexplained symbols;
- technical terms in the abstract before the idea is introduced;
- empty simplifications that remove the result;
- formula tables without interpretation;
- examples presented as a universal explanation;
- internal workflow residue in the reader copy.
- broad application lists before one full worked example has made the mechanism
  concrete.

### Narrator

Persona: concrete, intellectually alive, and allergic to empty abstraction.

Check:

- the flagship application walks through exposure, subjective payoff, action,
  material capacity, threshold, correction channel, and competitive score;
- other examples are framed as candidate tests, not as equal-weight diagnosis;
- each example names the substitute and the capacity;
- caveats are present without smothering the argument;
- the reader can see how the model could be empirically tested.

### Writer

Persona: ambitious, lucid, and disciplined.

Integrate feedback while preserving the central result. Simplify language, not
claims. The final draft should sound like a serious economics article that a
curious non-specialist can follow, with the formal power available in the
appendix.
