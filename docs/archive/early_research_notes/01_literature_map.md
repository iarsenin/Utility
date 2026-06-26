# Literature Map

## 1. Classical Baseline

The standard utility-function move is representational: impose consistency axioms on preferences, then prove that a utility function exists. This makes utility a compact summary of preference ordering rather than a causal object.

Main anchor points:

- expected utility: von Neumann and Morgenstern,
- subjective expected utility: Savage,
- revealed preference: Samuelson, Houthakker, Afriat, Varian,
- general equilibrium and welfare: Debreu, Arrow, welfare theorems.

The usual move is not "preferences never change"; rather, the analyst often treats preference change as slow, external, or outside the allocative mechanism. This project attacks that separation.

## 2. Endogenous Preferences

Bowles is the natural starting point: institutions, markets, and other allocation mechanisms can shape values and motives. Bernheim's agenda frames the problem directly: what determines preferences?

Useful distinction:

- **parametric endogeneity**: a taste parameter changes with experience, culture, or exposure;
- **strategic endogeneity**: preference types affect strategic behavior and are selected because of payoff consequences;
- **technological endogeneity**: an actor, such as a platform or AI agent, chooses interventions that alter the transition law for preferences;
- **normative endogeneity**: the welfare criterion itself depends on the preference path.

## 3. Evolution of Preferences

The indirect evolutionary approach separates subjective utility from material fitness. Agents choose actions according to preferences, but preference types reproduce according to material payoff. Dekel, Ely, and Yilankaya connect stable preference distributions to Nash equilibrium properties under observability assumptions.

This gives the project a rigorous base:

```text
preference type -> subjective best response -> material payoff -> type replication
```

The new contribution is to add fast within-life preference plasticity:

```text
preference type_t -> exposure/institution/AI -> preference type_{t+1}
```

This means selection is no longer only across types. Preferences become a controlled state variable.

## 4. Dynamic Choice and Meta-Preferences

Chosen-preference and meta-preference models are crucial because they provide a formal way to ask whether a person endorses future taste changes. Without meta-preferences, a platform can create the tastes it later satisfies.

Key modeling object:

```text
M(theta_t, theta_{t+1})
```

where `M` ranks preference transitions, not just consumption bundles.

## 5. Recommender Systems and AI

Recommender systems estimate preferences, but iterative personalization can also change them. AI increases the relevant state dimension:

- content can be personalized,
- persuasion can be conversational,
- the system can adapt in real time,
- preference drift can become both measured and optimized.

Economically, this converts preferences from primitives into partly engineered capital goods.

## 6. Gap This Project Targets

Existing literatures cover endogenous preferences, cultural evolution, dynamic choice, and recommender manipulation. The gap is an axiomatic welfare-and-equilibrium frame for the AI-speed case:

```text
allocation mechanism + preference-transition technology + selection criterion
```

The project will be successful if it produces even one clean theorem showing that a familiar welfare or equilibrium conclusion reverses once `K(theta' | theta, action, institution)` is endogenous.

## 7. Current Source-Grounded Synthesis

See `docs/05_research_synthesis_v1.md` for the current research synthesis and `references/literature_matrix.md` for the working source map. The core positioning is:

```text
not endogenous preferences alone,
but fast, strategic, platform-controlled preference transition.
```
