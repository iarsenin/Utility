# Paper Outline v1

Status note: this outline predates the fast-preference-limit pass in
`docs/09_fast_preference_limit.md`. Platform-controlled preference transition
remains important, but it should now be treated as an application of a broader
singular-limit framework rather than as the only candidate spine.

## Working Title

Endogenous Utility at AI Speed: Preference Dynamics, Platform Control, and Welfare Failure

## One-Paragraph Abstract

Economic models often treat utility functions as fixed primitives or as slow-moving products of habit, culture, or evolution. This paper studies economies in which utility is a local representation of a preference state that evolves under a transition law shaped by institutions and algorithmic systems. Agents maximize current subjective utility, while preference states are selected by material fitness and can also be shifted by a platform that maximizes engagement. The model shows that standard equilibrium and welfare objects are incomplete: a Nash equilibrium of actions need not be dynamically stable, final-preference Pareto comparisons can be manipulated by preference-changing mechanisms, and subjective utility can rise while material or biological fitness falls. The results motivate an expanded welfare domain over allocation-preference paths and a distinction between satisfying preferences and producing the preferences later satisfied.

## Section 1: Introduction

Core argument:

- Economists have long known preferences can be endogenous.
- The new issue is not endogeneity per se; it is speed, measurement, and control.
- Social media and AI systems make preference change part of the allocation mechanism.
- Welfare analysis over allocations alone can become circular.

Opening example:

```text
A platform learns that a user engages more when her tastes become narrower, more intense,
and more predictable. It can then recommend content that changes the future preference state
used to measure consumer surplus.
```

## Section 2: Literature

Organize around five strands:

1. Utility representation and revealed preference.
2. Stable-taste economics and consumption capital.
3. Habit, addiction, and endogenous time preference.
4. Cultural transmission and indirect evolutionary preference formation.
5. Meta-preferences, behavioral welfare, and recommender systems.

Emphasize:

```text
This paper adds an institution-controlled transition kernel K_m.
```

## Section 3: Axiomatic Environment

Define:

```text
(X, A, Theta, U, K, F, M)
```

Key axioms:

- local utility representation;
- Markovian preference-state transition;
- local subjective maximization;
- material or Darwinian selection;
- platform or institutional policy;
- welfare over extended paths.

Deliverable:

```text
Definition: Endogenous-preference economy.
Definition: Endogenous-preference equilibrium.
Proposition: Static model is the degenerate-K special case.
```

## Updated Research Decision

After three implementation iterations, the paper should center on platform-controlled preference transition. The one-dimensional taste model and the indirect evolutionary Prisoner's Dilemma remain in the paper, but as benchmark/proposition sections rather than the main contribution.

The current strongest result is:

```text
A platform that optimizes engagement and predictability chooses a preference-transition
policy that shifts the population toward platform-oriented tastes. In broad parameter
regions this raises platform value while lowering material fitness and the initial self's
evaluation of the induced allocation.
```

The simulation version appears in `results/research_iteration_report.md`; the next step is to prove the threshold condition analytically.

## Section 4: Benchmark 1, One-Dimensional Taste Drift

Use the online/offline model:

```text
u(o, h; theta) = theta log(o) + (1 - theta) log(h)
```

Preference transition:

```text
theta' = theta + eta[b_m(theta)(1 - theta) - c theta]
```

Fitness:

```text
F(theta) decreasing for high theta
```

Main result:

```text
For sufficiently high eta or platform bias, the population converges toward high theta
even when fitness is lower there.
```

This is the "fitness-utility inversion" section.

Iteration result:

```text
35/42 sweep cells show the fitness-utility inversion criterion.
```

Role in paper: transparent theorem candidate, not the centerpiece.

## Section 5: Benchmark 2, Indirect Evolutionary Game With Preference Mutation

Start from Prisoner's Dilemma or a generic symmetric game.

Subjective utility:

```text
u_i(a_i, a_j; lambda_i) = pi_i(a_i, a_j) + lambda_i pi_j(a_i, a_j)
```

Selection:

```text
types with higher pi_i grow
```

Mutation:

```text
lambda' ~ K_m(. | lambda)
```

Main result:

```text
The dynamic stability of an action outcome depends on the preference-transition law,
not only on Nash equilibrium of the material game.
```

Iteration result:

```text
12/36 sweep cells produce high-cooperation reversal.
```

Role in paper: bridge to indirect evolutionary preference theory.

## Section 6: Main Model, Platform Control

Introduce platform objective:

```text
Pi(m, mu) = engagement(m, mu) - cost(m)
```

Candidate engagement forms:

- higher time-on-platform when `theta` is high;
- higher predictability when `mu` is concentrated;
- higher monetization when preferences are intense.

Main result:

```text
The platform may optimally choose a transition law that increases current subjective
satisfaction and engagement while lowering material fitness or preference autonomy.
```

Iteration result:

```text
49/108 sweep cells show platform inversion: taste capture,
fitness loss, and initial-preference loss.
```

Policy comparative static:

```text
A weak autonomy penalty barely changes exposure, but a calibrated guardrail
prevents capture in the current model.
```

This section should receive the most formal attention.

## Section 7: Welfare

Show the welfare conflict:

```text
initial preference ranking != final preference ranking != meta-preference ranking != fitness ranking
```

Candidate proposition:

```text
Ex post Pareto efficiency is not invariant to preference-transition technologies.
```

Additional simulation-backed trilemma:

```text
no platform: fitness can improve while initial-preference value falls;
unregulated platform: platform value rises while fitness and initial-preference value fall;
guardrail: moderate intervention can preserve initial-preference value and fitness.
```

Policy interpretation:

- A regulator cannot rely only on "users choose it."
- A ban cannot rely only on "final users dislike alternatives."
- The missing object is admissible preference transition.

## Section 8: Empirical Implications

Observable predictions:

- fast taste drift should correlate with exposure intensity;
- drift should align with platform incentives;
- local revealed preference should look rational while longer panels violate stable-preference restrictions;
- interventions changing feed policy should alter future choice elasticities, not just current choices.

Possible empirical hooks:

- social-media deactivation experiments;
- algorithmic versus chronological feed experiments;
- large-scale recommender RCTs;
- public time-use and relationship formation data;
- cosmetic/body-image investment as a high-salience domain.

## Section 9: Conclusion

Close with:

```text
The welfare theorem for an algorithmic economy cannot be stated only over allocations.
It must also restrict the technologies that produce the utility functions used to evaluate those allocations.
```

## Target Venues

Ambitious theory/economics targets:

- Journal of Economic Theory
- Theoretical Economics
- Games and Economic Behavior
- Journal of Economic Behavior and Organization

Broader, provocative targets if framed with AI/social-media motivation:

- Journal of Economic Perspectives style article, though original theory may not fit
- Economics and Philosophy
- Philosophy and Technology
- AI and Society

The research should be written first for a theory seminar, then adapted outward.
