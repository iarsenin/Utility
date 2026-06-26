# Research Synthesis v1

## Executive Claim

The publishable version of this project should not say "economics ignored endogenous preferences." It did not. The sharper claim is:

> Existing endogenous-preference economics usually treats preference change as habit formation, cultural transmission, self-chosen worldview adoption, or evolutionary selection. AI and social-media platforms introduce a faster object: a deliberately optimized preference-transition technology.

The paper should therefore model preferences as state variables with an endogenous transition law. The transition law can be selected by institutions, platforms, or AI systems whose objective differs from both current subjective utility and biological or material fitness.

## What The Literature Already Gives Us

### 1. Utility Is A Representation, Not An Origin Story

Classical consumer theory asks when a preference relation can be represented by a utility function. Debreu-style representation results and revealed-preference theory treat utility as a summary of choice-consistency restrictions, not as a causal account of where taste comes from.

Useful baseline:

```text
preference relation over X -> utility representation u: X -> R
```

This project changes the primitive:

```text
preference-state process over Theta -> local utility u(., theta_t)
```

The implication is subtle: there can be perfectly rational local choice at each date and still no fixed global utility function over ordinary consumption bundles.

### 2. Stigler-Becker Is The Foil

Stigler and Becker's "De Gustibus" program argues that much apparent taste change can be modeled as stable preferences plus changing shadow prices, skills, or consumption capital. Their music example and addiction logic are exactly the kind of state-dependence we can reuse.

Their move:

```text
stable deep utility + changing consumption capital -> changing observed demand
```

Our move:

```text
preference-transition technology + changing consumption capital -> changing local utility map
```

The paper should explicitly respect Stigler-Becker. We do not need to deny their framework. We can say AI shifts the empirical burden: if the "consumption capital" stock can be targeted and optimized in real time, then the distinction between stable deep utility and endogenous local utility becomes welfare-relevant.

### 3. Habit, Addiction, And Time Preference Are Proto-Models

Ryder-Heal, Becker-Murphy, Becker-Mulligan, Rozen, and related habit/addiction work already model state variables that affect preferences over time. These are strong ancestors for the formal model.

Their common structure:

```text
state_{t+1} = law(state_t, consumption_t)
u_t = u(consumption_t, state_t)
```

Our addition:

```text
state_{t+1} = law(state_t, consumption_t, exposure_t, platform_policy_t)
```

The new object is not habit alone. It is an optimized, data-driven state transition.

### 4. Cultural Transmission Gives Population Dynamics

Bowles and Bisin-Verdier already place preference traits inside institutional and cultural dynamics. This literature is central because it treats preferences as socially transmitted and not merely individually learned.

Canonical dynamic:

```text
parental/peer/institutional socialization -> population distribution of traits
```

Our modification:

```text
algorithmic/AI socialization -> high-frequency population distribution of traits
```

The empirical and theoretical wedge is timescale. Cultural transmission is usually intergenerational or slowly institutional. Social-media and AI exposure can operate daily or continuously.

### 5. Indirect Evolutionary Preferences Give The Fitness Split

Dekel, Ely, and Yilankaya are foundational for the split we need:

```text
subjective preferences determine behavior
objective payoffs determine fitness
fitness determines preference-type growth
```

This is the cleanest route to the project's Darwinian/Nash foundation. The current repo's Prisoner's Dilemma model is a deliberately small descendant of this line.

The new contribution is within-life mutation:

```text
subjective preferences -> behavior -> objective payoff -> replication
plus
AI exposure -> preference mutation before replication
```

That second line lets preference drift outrun selection. This is where the bizarre results become plausible.

### 6. Meta-Preferences Are The Normative Escape Hatch

Bernheim et al.'s chosen-preferences model and Hayashi's meta-preference representation matter because they formalize endorsement of preference change. Without such a layer, a platform can first create a preference and then cite the satisfied preference as welfare evidence.

For this project:

```text
theta_t ranks outcomes
M_t ranks transitions theta_t -> theta_{t+1}
```

The welfare section should not pick a single criterion immediately. It should show that initial preferences, final preferences, meta-preferences, and fitness can rank the same path differently.

### 7. Recommender Systems Supply The Modern Shock

The recommender-systems literature emphasizes feedback loops: recommendations affect behavior, behavior affects inferred preferences, inferred preferences affect future recommendations. The AI-safety literature adds that learning preferences and changing preferences can become empirically entangled.

Economically, this is a transition-kernel problem:

```text
K_m(d theta' | theta, action, exposure)
```

where `m` is a platform or AI policy. If `m` is chosen to maximize engagement, then preference change is not merely endogenous. It is strategic.

## The Gap

The project should target the intersection of four literatures:

1. Utility representation and revealed preference.
2. Endogenous preference formation through habit, culture, and self-choice.
3. Indirect evolutionary models where preference types are selected by fitness.
4. Algorithmic recommender systems and AI preference manipulation.

The gap is a unified welfare and equilibrium framework for:

```text
fast preference transitions + strategic platform control + Darwinian/material selection
```

## Main Research Bet

The first paper should try to prove three things:

1. **Equilibrium Enlargement**: action profiles are not enough; an equilibrium must include the induced preference-transition law.
2. **Pareto Fragility**: final-preference Pareto criteria become weak or manipulable when the mechanism can alter preferences.
3. **Fitness-Utility Inversion**: subjective utility and platform engagement can rise while material or reproductive fitness falls, if preference plasticity is faster than selection.

## What Counts As A Good Strange Result

A result is worth preserving if it has this form:

```text
Under standard local rationality and explicit transition laws,
the economy converges to a state that is locally welfare-improving
but globally fitness-destroying or autonomy-destroying.
```

The point is not to moralize against technology. The point is to show that standard welfare language cannot classify such a path without additional axioms.

## Working Thesis

Utility should be modeled as a locally represented preference-state process:

```text
U_t = U(., theta_t)
theta_{t+1} ~ K_m(. | theta_t, a_t, x_t)
```

The economic primitive is no longer `U`. It is:

```text
(Theta, U, K, F, M)
```

where `M` is the space of institutional or algorithmic policies that shape `K`, and `F` is the material or Darwinian criterion that may select among preference states.
