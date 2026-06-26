# Round 2 Writer Review

Date: 2026-06-20

Scope: read-only review of `paper/article_v1.html` after the Modeller fixes and
`docs/agent_rounds/round_2_modeller.md`. I did not edit the article, code,
data, figures, or results.

## Bottom Line

The manuscript now has the right intellectual spine: finite-game fast closure is
the theorem route, platform control is the application, and the scalar taste
model is only exposition. The central idea is serious and publishable if the
paper keeps saying one thing sharply:

```text
In the fast-preference limit, utility moves from the primitive side of the
model to the closure side of the model.
```

The remaining writer problem is not lack of discipline. It is excess
defensiveness and note-like sequencing. The draft often pauses to explain what
it is not claiming before it has made the reader feel why the positive claim is
powerful. The next revision should make the paper feel less like a careful
repository report and more like a mathematical economics article with a
disturbing implication.

## Narrative Logic

The article's current logic is basically sound:

```text
fast preference dynamic
-> induced subjective game
-> Nash object shift
-> selection target shift
-> platform proxy alignment
-> welfare non-invariance
```

That chain should remain. The main narrative weakness is that the empirical WDI
section arrives before the conceptual synthesis table. This interrupts the
paper at the moment when the reader needs the theory to crystallize.

Recommended section order:

1. Introduction
2. Related work and distinction
3. Environment
4. Fast preference closure
5. Nash equilibrium after closure
6. Finite-game audit
7. Selection after closure
8. Platform control as application
9. Scalar taste exposition
10. Welfare when preferences are produced
11. What is invariant?
12. Empirical diagnostic and measurement agenda
13. Limitations and extensions
14. Conclusion

The "What Is Invariant?" table is the conceptual center and should appear before
the empirical diagnostic. The WDI material is useful, but it should not be the
bridge from welfare to conclusion. The bridge should be the invariant/non-
invariant synthesis.

## Novelty

The novelty is now clearer than in v0, but it can be stated with more nerve. The
paper should not lead with "endogenous preferences" or "platforms affect
welfare." The distinct contribution is the timescale reversal relative to
indirect evolutionary preference theory.

Suggested novelty sentence:

```text
The paper's contribution is to reverse the usual timing of indirect evolutionary
preference models: subjective preferences do not first persist as types and
then face material selection; in the singular limit they close before selection
acts, so the selected objects are the laws and institutions that generate
preferences.
```

This is more novel than "engagement is not welfare" and more specific than
"utility is endogenous." It also explains why the paper belongs near
finite-game preference evolution rather than only in recommender-system policy.

The platform application should then be introduced as the modern institutional
case where the closure law is not anonymous:

```text
The platform case matters because the closure map may be chosen by an optimizing
institution rather than inherited from habit, culture, or biology.
```

That sentence gives the application its own reason to exist.

## Overcautious Passages

The article is appropriately careful, but it sometimes sounds apologetic. There
are too many local disclaimers:

- "This paper does not claim..."
- "The lemma is intentionally spare..."
- "The formal conclusion should be modest..."
- "This is not a full welfare theory..."
- "This is not a causal estimate..."
- "The model does not prove..."

Each caveat is individually defensible. Together they flatten the prose. Move
most caveats into the limitations section and replace local apologies with
positive discipline.

Example replacement in Section 4:

Current tone:

```text
The lemma is intentionally spare. It does not say that the closed preference
state is good, rational, autonomous, welfare maximizing, or materially adaptive.
```

Better:

```text
The lemma is a closure result, not a welfare result. It identifies the payoff
object that agents optimize after fast adjustment; whether that object is
materially adaptive or normatively acceptable is a separate question.
```

Example replacement in Section 10:

Current tone:

```text
The formal conclusion should be modest.
```

Better:

```text
The formal conclusion is a non-invariance result.
```

That is still careful, but it sounds like a theorem rather than an apology.

## Overbroad Passages

The conclusion currently says:

```text
Harm follows when the preference-generating operator is independent of or
misaligned with material welfare, and when the resulting closure changes the
reduced game.
```

"Follows" is too strong, especially for independence. The audit shows harm
becomes common under independent proxies in the simulated route; it does not
prove harm from independence alone.

Recommended replacement:

```text
Material harm is not a theorem of speed alone. It becomes possible, and in the
audit common, when the preference-generating operator is independent of or
misaligned with the material evaluator and the resulting closure changes
best-response behavior.
```

The WDI language also needs a narrower claim. The article says alignment is
measurable and should not be assumed. True, but WDI does not measure alignment
between platform preference-generation and material welfare. It measures
macro-level associations between digital adoption proxies and material or
demographic outcomes.

Recommended replacement:

```text
The WDI exercise does not measure platform-induced preference closure. It shows
how the paper's alignment question can be disciplined empirically: exposure
proxies, outcome proxies, and their relative timescales can be measured rather
than assumed.
```

## Dry Or Confusing Places

### Abstract

The abstract is accurate but overpacked. It reads like a compressed checklist.
It should foreground the conceptual result before listing all machinery.

Suggested replacement abstract:

```text
Economic models usually treat utility as an input to choice. This paper studies
the opposite limiting case: a preference state adapts so quickly that, before
the rest of the economy moves, utility has already been produced by the
environment. In finite games with subjective utility distinct from material
payoff, the limit T_theta -> 0 pins preferences to a fast attracting branch
theta^star(E,I). The induced object is a reduced subjective game. Nash
equilibrium still applies, but to that game rather than automatically to the
material-payoff game. Material selection still applies, but to the adaptation
laws, institutions, resistance parameters, or induced systems that remain
heterogeneous after closure. The paper gives a best-response invariance
condition, a selection-target-shift result, and a platform-control application
in which material loss depends on the alignment between the preference-
generating proxy and the material evaluator. The point is not that fast
endogenous preferences mechanically cause harm. It is that they move utility
from the primitive side of the model to the object being generated inside the
model.
```

This is longer than a journal abstract may ultimately be, but it has a cleaner
arc than the current paragraph.

### Introduction

The introduction has a good first paragraph and a good clock argument. It needs
one vivid paragraph before the formal question, otherwise the "digital and
AI-mediated environments" sentence is too generic.

Insert after the second paragraph:

```text
A recommender system is the clean contemporary example. It does not only solve
a static prediction problem of the form "what does this user want now?" It can
choose the sequence of exposures that changes what the user will want next. If
the future preference state is then treated as ordinary revealed preference,
the mechanism has helped produce the standard by which it is judged.
```

This gives readers the unsettling application early without making the theorem
platform-specific.

### Related Work

Section 2 is correct but list-like. It needs a closing paragraph that names the
paper's wedge.

Add:

```text
The wedge is therefore not endogeneity, feedback, or welfare ambiguity by
itself. It is the singular timing: preference adjustment occurs before the
equilibrium and selection operators are applied. That timing turns familiar
ingredients into a different reduced game.
```

### Environment

Section 3 is clean but dry. Add one paragraph after the subjective/material
payoff equation to anchor the split.

Suggested paragraph:

```text
The distinction is easiest to read in evolutionary language but does not depend
on biology. A player may maximize the utility representation currently encoded
by theta_i, while the outside evaluator records profit, health, output,
retention, fertility, exit, or survival. The model's work begins precisely when
these two objects are not silently identified.
```

### Finite-Game Audit

The audit is useful but still feels like a repository report. Avoid "The
repository implements this check" in the article body.

Replacement:

```text
To check that the argument is not driven by the scalar application, I use a
finite-game audit: 5,000 random two-player, two-action games are generated for
each route, and fast preference closure is represented as a payoff
transformation.
```

Also rename "Finite-Game Audit" to one of:

- "A Finite-Game Stress Test"
- "Non-Neutral Closure In Random Games"
- "A Stress Test: Neutral, Aligned, And Misaligned Closure"

"Audit" is useful in internal notes, but "stress test" reads more like an
article.

### Platform Section

The opening "The platform application is now straightforward" undersells the
most interesting application. Replace it.

Suggested replacement:

```text
The platform case gives the closure map an institutional owner. An ordinary
environment may shape preferences incidentally; a platform can optimize over
the transition environment itself.
```

Then continue with the formal `I -> theta^star -> NE -> (V,G)` chain.

The last paragraph of Section 8 is strong. It should be made more central:

```text
The application is not just "engagement is not welfare."
```

Keep that sentence. It is the right defensive wall against the closest
literature.

### Scalar Model

Section 9 is correctly demoted but too small. As written, it is almost only
three equations and a warning. Either add a figure or make it an explicitly
optional "toy map" subsection.

Concrete improvement:

```text
This example should do one job: show why fast closure can create a survival
frontier. It should not be asked to carry the general result.
```

If the article keeps the scalar section in the main text, add one sentence of
interpretation after `p^star(s)`:

```text
The institution does not choose the agent's action directly. It chooses the
exposure environment that pins the preference state from which the action is
chosen.
```

That sentence ties the toy model back to the platform logic.

### Welfare Section

The welfare section is the most conceptually important application after
platform control, but it is currently too schematic. The six-item list is useful
as a map, not as prose. Add a miniature example in words before the formal
observation.

Suggested paragraph:

```text
Consider an agent who initially prefers an allocation that preserves outside
options. A transition law then induces a preference for a more absorbing
allocation and the agent chooses it. Ex post satisfaction is real in the model:
the final utility representation really does rank the absorbing allocation
higher. The welfare problem is that the mechanism being evaluated helped create
the preference that now endorses it.
```

This makes "preference laundering" legible without using inflammatory language.

### Empirical Diagnostic

This section is valuable but too detailed for the main narrative. The equations
are now technically improved, but they slow the article. For a serious theory
article, the WDI section should be shorter in the main text and fuller in an
appendix.

Recommendation:

- Keep one paragraph on timescale measurement.
- Keep Figure 2 if visually strong.
- Keep one paragraph on the alignment regression and one compact table.
- Move detailed definitions of `dI10`, horizon construction, and the full
  regression to an empirical appendix or note.

If the section stays in the main text, retitle it:

```text
Empirical Discipline: Timescales And Alignment
```

"Diagnostic" is honest but sounds auxiliary. The section's role is to show that
the theory points to measurable quantities.

## Serious Article Versus Notes

The draft still contains some phrases that reveal its repo origin. Replace or
remove:

- "The repository implements..."
- "generated from the Utility project repository..."
- "The WDI pipeline uses..."
- "writes figures and tables..."
- "The implemented regressor..."

These are fine in documentation, not in the article. In the article, say "I
estimate," "the diagnostic uses," or "the analysis uses."

The theorem numbering also feels provisional:

```text
Lemma 1, Proposition 2, Theorem 3, Proposition 4, Observation 5
```

For a paper, use a clean sequence and make the hierarchy meaningful:

- Lemma 1: Fast closure
- Proposition 1: Nash invariance
- Proposition 2: Generic non-neutral closure
- Theorem 1: Selection target shift
- Proposition 3: Proxy alignment
- Observation 1: Welfare non-invariance

Alternatively, call all formal statements "Propositions" except the selection
target shift. The current numbering makes the reader feel the draft grew from
notes.

The proof sketches are good for a reader draft, but for submission either move
sketches into a proof block with complete arguments or mark the whole document
as an expository draft. A serious article can still have intuition after each
proposition, but the proof apparatus should look intentional.

## Replacement Sentences To Use

### Central Thesis

```text
When preferences adapt on the fastest clock, utility is no longer the primitive
that closes the model; it is the object closed by the model.
```

Use this in the abstract, introduction, and conclusion. It is the paper's best
sentence.

### Contribution Paragraph

```text
The contribution is a singular-limit analysis of finite games with subjective
utility distinct from material payoff. In the limit, a fast attracting
preference branch induces the game in which agents optimize. Nash equilibrium
is then computed in that induced subjective game, while material selection
evaluates the consequences and selects among the adaptation laws or institutions
that remain heterogeneous after closure.
```

### Platform Wedge

```text
The platform case matters because the closure law can be chosen. A platform
need not merely reveal or satisfy preferences; it can optimize the environment
that produces the preference state under which later satisfaction is measured.
```

### Alignment Claim

```text
Fast closure is the general object shift. Material loss is the conditional
alignment result.
```

### Welfare Claim

```text
Final-preference satisfaction remains a fact about the induced utility
representation. What fails is its invariance as a welfare criterion when the
same mechanism helped induce that representation.
```

### Empirical Transition

```text
The empirical implication is not that macro internet adoption identifies
platform-induced utility change. It is that the theory names two measurable
objects: relative adjustment speeds and the alignment between exposure proxies
and material outcomes.
```

### Conclusion Replacement

```text
The limit is unsettling for a precise reason. It does not say that every fast
preference system is harmful. It says that once preferences close before
equilibrium and selection are evaluated, the analyst cannot treat utility as an
unchanged primitive. The reduced game, the selected object, and the welfare
domain have all moved.
```

## Specific Revision Plan

1. Move "What Is Invariant?" before the empirical diagnostic.
2. Rewrite the abstract around the object shift, not around a list of sections.
3. Add one concrete recommender paragraph to the introduction.
4. Add a related-work closing paragraph that says the wedge is singular timing.
5. Rename "Finite-Game Audit" to "Finite-Game Stress Test" and remove repo
   language.
6. Strengthen the platform opening so the application feels central, not
   mechanical.
7. Add a short prose welfare example before Observation 5.
8. Shorten or appendicize the WDI equations in the main article.
9. Clean theorem numbering so the formal architecture looks deliberate.
10. Move repeated caveats into Limitations and replace local disclaimers with
    positive, bounded claims.

## Final Judgment

The paper is no longer just notes; it has the bones of a serious article. The
next writing pass should make those bones visible. The strongest version is not
"platforms may be bad" and not "preferences are endogenous." It is:

```text
The singular limit changes the object of economic analysis.
```

Everything else should be organized as a consequence of that sentence.
