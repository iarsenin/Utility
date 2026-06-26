# Puzzle Bridge Edit Chain

Date: 2026-06-26

Manuscript: `paper/when_preferences_move_faster_than_equilibrium_v1.html`

## Objective

Make clear how the Nash, selection, and social-feedback results help answer the preference-capacity puzzles. If the framework could not carry that burden, the edit chain was instructed to stop and recommend stronger formal work.

## Round 1: Editor

Verdict: Go, with revisions.

Main finding: the framework can carry the paper, but the draft made readers infer the mapping too often. The editor recommended an explicit bridge connecting each puzzle family to the formal levers:

- Nash: local rationality inside induced wants.
- Selection: the durable empirical object shifts toward taste-forming systems when initial tastes are overwritten.
- Social feedback: persistence and branch shifts.

Edits made:

- Added an early Section 1 paragraph giving the three-question order: what forms the want, what equilibrium follows, and what evaluator judges the result.
- Renamed Section 2 to "Ten Preference-Capacity Puzzles."
- Added a bridge paragraph explaining when the Nash/selection framework adds something beyond a descriptive list.
- Added a mapping table, "How the formal results read the puzzles."

## Round 2: Writer

Verdict: the bridge should be explicit but not overbearing.

Edits made:

- Added theorem-level sentences to the fertility, social-capacity, reward-loop, and politics result boxes.
- Tightened the taxonomy so crime fear, economic mood, and alliance trust are subcases of civic reference-point dynamics rather than extra uncounted puzzles.

## Round 3: Scientist

Verdict: Go, with tightening.

Main cautions:

- The selection theorem shows indistinguishability within settling-equivalence classes; selection over institutions/rules requires an additional replication or evolutionary layer.
- The social-feedback threshold is proved for the specified contraction and mean-field models, not for every norm or meme.
- Proxy alignment gives a sufficient no-loss condition and a two-rule loss construction; harm requires rule selection and a named material evaluator.

Edits made:

- Replaced "material harm follows" with "material harm can follow from proxy maximization over rules that are misaligned with the named material evaluator."
- Rewrote the selection-row claim to emphasize settling-equivalence and empirical target shift.
- Rewrote the social-feedback claim as a result of the specifications below, with the domain-approximation condition stated.

## Round 4: Writer/Editor

Verdict: Pass.

Remaining issue: the AI companion table blurred platform proxy and material evaluator.

Edits made:

- Changed the table heading from "Long-run evaluator" to "Selection criterion."
- Labeled replacement design criteria as platform proxy.
- Labeled scaffolding design criteria as material evaluator.
- Reworded the politics result box so Nash explains individual consistency after anger, fear, or humiliation enters the payoff.

## Final Judgment

The framework does not need a revamp at this stage. The contribution is best framed as a conditional diagnostic framework:

1. Fast preference formation creates the payoff table.
2. Nash tests whether induced wants change strategic behavior.
3. Social feedback explains persistence in the specified threshold models.
4. Selection identifies what later evidence can still distinguish after initial tastes are overwritten.
5. Proxy alignment determines when preference formation repairs or worsens the named material evaluator.

## Second Four-Round Chain: Nash/Selection Bridge Clarity

Date: 2026-06-26

Objective: Re-check whether the Nash/Darwin/selection framework actually helps answer the puzzles, rather than merely decorating them with formulas. The instruction was to stop and report if the framework did not carry the burden.

### Round 1: Editor

Verdict: Pass with revision.

Finding: the bridge was present but needed to be stated earlier and more plainly. The article should admit examples only when they specify the preference-forming rule, induced payoff or best-response change, material evaluator, and evidence that would make fixed preferences sufficient.

Edits made:

- Rewrote the Section 1 admission test for applications.
- Compressed the opening of Section 2 so the puzzle table is explicitly diagnostic rather than a loose list.
- Reframed "What the math adds" as a bridge from puzzles to formal claims.

### Round 2: Scientist

Verdict: Go, with precision changes.

Finding: the framework is viable, but the language had to avoid overclaiming. Nash is used after preferences settle; it is not a convergence claim. Selection indistinguishability holds for post-adjustment rules that observe only the induced game, material evaluator, and slow environment.

Edits made:

- Changed the abstract to say behavior is analyzed through Nash equilibrium after preferences settle.
- Replaced broad "later behavior cannot tell" language with the formal observability condition.
- Replaced "sharp predictions" with "concrete empirical tests."
- Tightened the Nash invariance, social-feedback, and selection target rows.

### Round 3: Narrator

Verdict: Pass.

Finding: the framework contribution is clear enough to keep editing, but some theorem-level wording was too heavy in the reader-facing path.

Edits made:

- Rewrote the abstract selection result in plainer language while retaining the observability restriction.
- Replaced "boundary condition" with "evidence that would show that a fixed-preference account is enough."
- Added a reversibility test to the appearance/lookmaxxing discussion.
- Added a conditional diplomatic-drift prediction to the politics and international spillovers section.
- Recast the social-feedback paragraph so it ends with the practical implication: test reversibility before choosing policy scale.

### Round 4: Final Editor/Writer

Verdict: Pass; no structural revamp needed.

Finding: the paper now repeatedly separates induced utility, Nash consistency, material evaluation, and selection over preference-forming systems. Remaining issues were polish: reduce loaded phrasing and do not ask Nash to explain individual consistency where ordinary maximization is enough.

Edits made:

- Replaced "manufactured wants" with "induced wants."
- Replaced "selection remains a survival method" with "selection remains a way to ask what persists."
- Changed "taste-shaping systems" to "preference-forming systems."
- Softened AI companion wording from "infinite patience" to "effectively unlimited patience."
- Clarified the demographic result: ordinary maximization explains individual delay, and Nash applies where partner-market choices interact.
- Softened the identity-loop warning and made the international prediction explicitly conditional.

### Verification Notes

- `git diff --check` passed.
- Internal anchor check passed: 55 IDs, no duplicates, no missing hash links.
- Equation containers: 15. Figure blocks: 4. Theorem blocks: 11.
- Display-math delimiters are balanced.
- HTML Tidy on this machine is old enough to misclassify HTML5 tags such as `main`, `header`, and `section`; the custom structural checks did not find unbalanced main tags.
- Browser reload/screenshot was attempted through the in-app browser, but the browser security policy blocked visiting the localhost URL during this pass. No workaround was used.
