# Novelty Check v1

## Bottom Line

The current result is **not novel** if stated as:

```text
preferences are endogenous
```

or:

```text
recommender systems can influence behavior and preferences
```

Both claims are already well represented in economics, recommender-systems research, behavioral welfare, and AI-safety-adjacent work.

The current result still looks **potentially novel** if stated narrowly as:

```text
A platform-controlled preference-transition kernel can generate a welfare trilemma:
final-preference satisfaction and platform value rise while initial-preference welfare
and material/fitness welfare fall.
```

This is a preliminary web and primary-source pass, not a substitute for a
database-complete EconLit/Google Scholar review. It is strong enough to guide the
next model iteration and weak enough that any paper draft should still include a
formal related-work audit before claiming novelty.

The defensible contribution is therefore not a discovery that preferences move. It is a mathematical economics synthesis that combines:

1. local utility representation;
2. endogenous preference-transition technology `K_m`;
3. platform choice of `m`;
4. subjective utility distinct from material or Darwinian fitness;
5. welfare comparison across initial preferences, final preferences, meta-preferences, and fitness.

## Already Established

### Endogenous Preferences

This is an old and serious literature.

- Stigler and Becker model apparent taste change through stable deep preferences and consumption capital.
- Bowles reviews how institutions affect preferences.
- Bisin and Verdier model cultural transmission and population dynamics of preference traits.
- Dekel, Ely, and Yilankaya endogenize preferences through the indirect evolutionary approach: subjective preferences determine behavior, while objective payoffs determine fitness.
- Bernheim et al. model chosen preferences or worldviews.
- Hayashi models layers of meta-preferences and investment in future preferences.

Implication: the paper must not pitch endogenous preferences as the novel claim.

### Recommender Systems Influence Preferences

This is also established.

- Adomavicius et al. provide experimental evidence that recommender ratings can anchor constructed preferences.
- Jiang et al. model degenerate feedback loops in recommender systems.
- Ashton and Franklin argue that AI/ML systems can blur whether they have learned preferences or taught users to behave in ways that maximize the system objective.
- Franklin et al. call for a broader "Preference Science" around AI-induced preference change.
- Recommender-systems dynamics work treats preferences and recommendations as a feedback system.

Implication: the paper should cite this as motivation and not claim the feedback-loop idea as original.

### Engagement Optimization Can Lower Welfare

Kleinberg, Mullainathan, and Raghavan are very close. They model inconsistent preferences and engagement optimization, showing that increasing engagement need not increase user welfare.

Implication: the paper must differentiate itself from "engagement is not welfare." Our distinction should be:

```text
not just inconsistent current preferences,
but endogenous transition of the future utility function itself.
```

Their platform chooses locations on a content manifold and can move engagement in
directions that lower welfare. Our model must instead put the preference state in
the transition law itself:

```text
theta_{t+1} ~ K_m(. | theta_t, a_t, x_t)
```

If we cannot prove a result that uses this transition law essentially, the paper
collapses into a variant of their engagement-welfare result.

### AI/Social Media Platform Political Economy

Acemoglu, Ozdaglar, and Siderius model AI-powered social media business models and polarization channels. Platform incentives to maximize engagement and monetize targeting are already central in that literature.

Implication: platform objective functions and engagement incentives are not novel by themselves.

### Preference Laundering And Welfare With Endogenous Preferences

Behavioral welfare and philosophy/economics already discuss preference laundering, true preferences, fuzzy preferences, and problems of welfare assessment when preferences are endogenous.

Implication: the paper must be precise about what is being added: a transition-kernel/equilibrium model with platform choice and material fitness, not merely a philosophical warning.

Khosrowi and Beck's 2026 recommender-systems paper is an especially close
normative warning sign. They argue that recommender-systems research lacks a
coherent account of welfare-relevant preferences and that engagement, preference
satisfaction, and welfare can come apart. This is not our theorem, but it means a
purely conceptual "engagement is not welfare" framing is already occupied.

## Closest Overlap Matrix

| Literature | What It Already Has | What We Need To Add |
| --- | --- | --- |
| Stigler-Becker, Bowles, Bisin-Verdier, Bernheim, Hayashi | Preferences respond to experience, institutions, culture, worldviews, and investment. | A platform or AI system as an optimizing controller of a within-life preference-transition technology. |
| Dekel-Ely-Yilankaya, Ely-Yilankaya | Subjective preferences govern behavior; objective payoffs/fitness govern selection. | A third force: platform-selected preference mutation fast enough to dominate material selection. |
| Adomavicius et al. | Recommender ratings can anchor constructed consumer preferences experimentally. | Dynamic equilibrium and welfare comparison across initial, final, and fitness criteria. |
| Jiang et al. | Recommender-user feedback can generate degenerate dynamics, echo chambers, and filter bubbles. | A mathematical economics welfare theorem rather than primarily a recommender-dynamics result. |
| Franklin et al.; Ashton and Franklin | AI systems can change preferences; meta-preferences matter. | A formal platform-control model with tractable comparative statics. |
| Kleinberg-Mullainathan-Raghavan | Engagement optimization can reduce welfare under inconsistent preferences. | Endogenous future utility functions, not only inconsistent current preferences or unobserved welfare. |
| Khosrowi-Beck | Recommender systems lack a coherent normative foundation for welfare-relevant preferences. | A positive model and theorem explaining one mechanism by which the normative problem arises. |

## What Still Looks Distinctive

### 1. The `K_m` Object

The clean mathematical object is:

```text
theta_{t+1} ~ K_m(. | theta_t, a_t, x_t)
```

where the platform chooses `m`. Much recommender literature studies feedback loops or inferred preferences; much economics literature studies endogenous preferences; fewer papers place a platform-chosen preference-transition kernel directly into a welfare/equilibrium model.

### 2. The Four-Way Welfare Split

Our current simulation compares:

- platform objective;
- local/final subjective utility;
- initial-preference welfare;
- material/fitness welfare.

The distinct claim is that these can systematically diverge in a platform equilibrium.

### 3. Fitness-Utility Inversion Under Platform Control

The indirect evolutionary literature separates subjective preference from objective fitness, but generally does not add AI-speed platform-controlled within-life preference mutation.

Our stronger result is:

```text
selection alone moves toward the fitness-favored state;
platform-controlled transition can reverse that direction;
the reversal is chosen by the platform, not imposed exogenously.
```

### 4. Guardrail Comparative Static

The calibrated guardrail result matters because it turns the model from a one-note harm story into a policy model:

```text
weak autonomy penalties do little;
stronger transition penalties can prevent preference capture.
```

This can become an analytical threshold result.

## Novelty Risk

High-risk overlaps:

1. Kleinberg, Mullainathan, and Raghavan: engagement optimization versus welfare.
2. Ashton and Franklin / Franklin et al.: AI systems changing preferences and the need for meta-preferences.
3. Jiang et al. and recommender feedback-loop literature: dynamic feedback and homogenization.
4. Bowles / Bisin-Verdier / Dekel-Ely-Yilankaya: endogenous and evolutionary preferences.
5. Khosrowi and Beck / behavioral welfare literature: recommender systems and endogenous preferences make welfare analysis difficult.

The paper survives only if it is mathematically sharper than a conceptual synthesis.

## Recommended Positioning

Do not title or pitch the paper as:

```text
Endogenous Utility
```

That is too broad and invites the obvious objection that the literature already exists.

Better:

```text
Platform-Controlled Preference Transitions
```

or:

```text
Endogenous Utility at AI Speed
```

Precise contribution sentence:

> I model algorithmic platforms as choosing a preference-transition technology. In equilibrium, the platform can move the distribution of utility functions toward states that increase engagement and final-preference satisfaction while lowering initial-preference welfare and material fitness. The result links endogenous preference theory, indirect evolutionary preferences, and recommender feedback loops in a single welfare framework.

## Paper-Worthiness Assessment

Current status: promising but not yet proven.

What is already established:

- preferences can be endogenous;
- platforms optimize engagement;
- engagement is not necessarily welfare;
- recommenders can manipulate or amplify preferences;
- welfare with endogenous preferences is difficult.

What may be publishable:

- a clean theorem showing platform-chosen `K_m` creates a welfare trilemma;
- a threshold result for when platform drift dominates material selection;
- a regulatory comparative static showing when transition-cost or autonomy constraints prevent capture.

## Next Literature Tasks

1. Read Kleinberg, Mullainathan, and Raghavan carefully and map exact differences.
2. Read Jiang et al. and later feedback-loop papers for dynamic-homogenization theorems.
3. Search for "platform endogenous preferences" and "preference manipulation economics platform" in EconLit/Google Scholar.
4. Add a formal related-work section that admits overlaps before stating the narrower contribution.
5. Replace "fitness" language with "material payoff" in economics sections unless the model is explicitly evolutionary.
