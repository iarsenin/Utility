# The Singular Limit Of Endogenous Preferences

## When Utility Adapts Faster Than Selection

Codex reading draft v0.4

Status: reader-facing working draft for comments. This is not a final manuscript. It is written to make the argument readable, expose weak points, and give us a concrete object to revise.

Formatting note: this version is optimized for the Codex app Markdown viewer. Equations use mnemonic variable names, Unicode time subscripts, dot notation for time derivatives, and simple display quotes instead of LaTeX or box-drawing characters.

## Abstract

Economic theory usually begins after preferences have been specified. A preference relation or utility function is treated as primitive, exogenous, or at least slow-moving relative to the allocation problem under study. This paper studies the opposite limiting case. Let P be a preference state, let E be the ordinary economic or material state, and let I be an institution, platform rule, cultural environment, or adaptation law. Suppose preferences adapt on timescale Tᴾ and take the singular limit Tᴾ → 0.

> Tᴾ → 0

In that limit, preferences are not slowly selected traits. They are fast state variables pinned to the attracting set of the preference-adaptation system. If the attracting set is a single branch, preferences close onto a map:

> P = P*(E, I)

Nash equilibrium and Darwinian selection do not disappear. They remain valid mathematical operators. What changes is the state space on which they operate. Nash fixed points are computed in the fast-adapted subjective game. Darwinian or material selection acts only on variables that remain heterogeneous after fast preference closure: populations, institutions, adaptation laws, resistance parameters, or whole induced systems. This produces a sharp separation between subjective rationality, material payoff, final preference satisfaction, and long-run survival. In calibrated toy models, myopic institutions can induce preference attractors that are locally satisfying and engagement-maximizing but imply negative long-run growth and extinction. Survival-aware institutions choose different exposure rules and survive. The paper argues that welfare economics with fast endogenous utility must evaluate allocation-preference paths, transition kernels, or meta-preferences, not final preferences alone.

## 1. Introduction

The standard consumer problem starts too late for the question studied here. In the usual formulation, the analyst specifies a preference relation, represents it with a utility function when convenient, lets agents optimize, and studies equilibrium, efficiency, or welfare. This is a powerful abstraction. It is also fragile if the mechanisms allocating goods are also mechanisms that change the preferences used to evaluate those goods.

Economics has never literally required preferences to be frozen forever. Habit formation, addiction, endogenous time preference, cultural transmission, socialization, identity, advertising, status, and indirect evolutionary preferences all appear in established theory. The conventional defense is a timescale defense. Preferences may change, but for many allocation problems they change slowly enough to be treated as primitives, parameters, or background states.

The modern digital environment weakens that defense. Recommender systems and social platforms observe behavior, choose exposure, adapt in real time, and shape future behavior. AI-mediated experiences may make this loop faster and more individualized. The important theoretical point is not any particular psychological claim about one generation or one platform. The point is that a utility function may itself be a fast-moving state variable inside the economic mechanism.

This paper asks a deliberately extreme question: what remains of standard equilibrium, selection, and welfare reasoning if preference adaptation is infinitely fast relative to the rest of the economy?

Let Pₜ denote the preference state that locally represents an agent's utility function at time t. Let Eₜ denote material, demographic, technological, or social states. Let Iₜ denote an institution, algorithm, platform rule, cultural environment, or adaptation law. Preferences adapt according to a dynamic equation. The economy also has action choices, material payoffs, institutional rules, and population dynamics.

The extreme limit is:

> Tᴾ → 0

This limit is false as a literal description of human life. It is useful as a mathematical microscope. Extreme cases expose which concepts are invariant and which concepts were artifacts of treating preferences as slow.

The central result is a reduction. If the fast preference subsystem has a unique attracting branch, then P is no longer an independent slow state. It is pinned to:

> Pₜ = P*(Eₜ, Iₜ)

Utility is then evaluated as:

> Uₜ(·) = U(· ; P*(Eₜ, Iₜ))

Actions are best responses in this reduced subjective game. Material selection evaluates the material consequences of those best responses. Welfare analysis must decide whether to evaluate the path by initial preferences, final preferences, meta-preferences, material growth, constitutional restrictions on preference transitions, or the whole history.

The paper makes five claims.

First, in the fast limit with a unique attracting preference branch, utility is replaced by a fast-response map. Utility is not a primitive and not a slowly selected trait. It is the graph of the adaptation mechanism.

Second, Nash equilibrium remains the equilibrium method, but the relevant game changes. A profile can be Nash with respect to fast-adapted subjective preferences while failing to be Nash with respect to material payoffs. Material Nash predictions are invariant only when fast preference closure preserves the material best-response correspondence.

Third, Darwinian selection remains the selection method, but the selected object changes. If a common adaptation law instantly maps all agents into the same preference state, selection over initial preference states becomes degenerate. Selection can still operate over adaptation laws, institutions, populations, or resistance to adaptation.

Fourth, final-preference welfare is unstable. If a mechanism can first produce a preference and then satisfy it, ex post preference satisfaction can validate the path that created the preference. Welfare analysis must therefore include transition laws, initial preferences, meta-preferences, material fitness, or constitutional restrictions.

Fifth, timescale ordering should be measured or varied rather than assumed. This draft sends only Tᴾ to zero. Institutional speed, algorithmic speed, behavioral adjustment, cultural transmission, and population dynamics remain parameters. In the models below, myopic institutions induce preference attractors that maximize engagement but generate negative growth under all tested speed orderings. Survival-aware institutions choose different rules and survive.

## 2. What Is Already Known

The claim that preferences are endogenous is not new. Stigler and Becker argued that many apparent changes in tastes can be represented by stable deeper preferences and changing consumption capital. Becker and Murphy modeled rational addiction. Becker and Mulligan studied endogenous time preference. Rozen provided foundations for intrinsic habit formation. Bowles surveyed how markets and institutions shape preferences. Bisin and Verdier built cultural transmission models in which preference traits evolve through family and socialization. Bernheim, Braghieri, Martinez-Marquina, and Zuckerman modeled chosen preferences. Hayashi develops welfare analysis with meta-preferences and investment in future preferences.

The closest mathematical economics literature is the indirect evolutionary preference literature. In that tradition, agents act according to subjective preferences, while material payoffs determine evolutionary success. Ely and Yilankaya, Dekel, Ely, and Yilankaya, Heifetz, Shannon, and Spiegel, and Sandholm all study versions of this separation. Sandholm's two-speed model is especially important because behavior adjusts quickly while the distribution of preference types evolves slowly.

This paper changes the location of the fast variable. In the limit studied here, preference adaptation itself is fast. The inherited or current preference state is not the slow object being selected. Instead, it closes onto an attracting map before slower material selection can sort it.

Adaptive utility is another neighboring literature. Robson, Whitehead, and Robalino model utility as an adaptive coding device under limited discriminative capacity. Sadowski and Sarver use adaptive preferences to explain ambiguity and non-expected utility behavior. Von Weizsaecker asks when welfare economics can be recovered under adaptive preferences. These papers matter because they already weaken the fixed-utility premise. The present draft adds a singular-limit question: what does economic theory look like when preference adaptation is faster than the equilibrium or selection process under study?

The recommender-systems and AI literatures provide the motivating environment. Adomavicius, Bockstedt, Curley, and Zhang show experimentally that recommender ratings can anchor constructed preferences. Jiang, Chiappa, Lattimore, Gyorgy, and Kohli study degenerate feedback loops in recommender systems. Ashton and Franklin, and Franklin, Ashton, Gorman, and Armstrong, argue that AI systems can change preferences and that meta-preferences are needed to evaluate such changes. Kleinberg, Mullainathan, and Raghavan show that engagement optimization can diverge from user welfare when preferences are inconsistent. Khosrowi and Beck argue that recommender systems lack a coherent normative foundation for welfare-relevant preferences.

The contribution here, if it survives further proof and literature review, is therefore narrow. It is not "preferences are endogenous." It is the combination of fast preference closure, Nash object shift, selection target shift, survival frontiers, and welfare non-invariance in a single mathematical economics frame.

## 3. The General Environment

This section introduces the model in its most abstract form. The notation is intentionally broad because the point is to identify what changes when utility becomes a state variable.

There are five moving parts. The mnemonic convention is:

- `P`: preferences or tastes;
- `E`: economic and material state;
- `I`: institution or environment;
- `A`: action or action profile;
- `N`: population size or survival mass.

The subscript t means "at time t." In this Codex-readable draft, time is written with Unicode subscripts, as in Pₜ, rather than underscore notation.

The first object is the preference state P. This is not necessarily a complete psychological description. It is the state variable that determines the local utility representation used by the agent.

> Pₜ ∈ PreferenceSpace

The second object is the ordinary economic state E. This can include resources, technology, wealth, demographics, social capital, health, reproductive state, or any other non-preference variable.

> Eₜ ∈ EconomicStateSpace

The third object is the institutional or environmental rule I. This can be a platform policy, recommender algorithm, school, family regime, cultural environment, legal rule, firm strategy, or preference-transition technology.

> Iₜ ∈ InstitutionSpace

The fourth object is the action A. Agents choose actions according to current subjective utility, not necessarily according to material payoff.

> Aₜ ∈ BestResponse(Pₜ, Eₜ, Iₜ)

The fifth object is the population or survival mass N. It records whether the induced system expands, persists, contracts, or exits.

> Nₜ ≥ 0

The utility representation is:

> Uₜ = U(x, Aₜ ; Pₜ)

Material payoff, reproductive success, survival, or objective growth is written separately:

> MaterialPayoffₜ = M(Eₜ, Pₜ, Aₜ, Iₜ)

This separation is the whole point. Subjective utility is what the agent maximizes. Material payoff is what the environment selects.

The dynamic system is:

> Tᴾ · Ṗ = PreferenceChange(P, E, A, I)
> Ė = EconomicChange(E, P, A, I)
> Tᴵ · İ = InstitutionChange(I, E, P, A)
> Tᴺ · Ṅ = N · SurvivalGrowth(E, P, A, I)
> A ∈ BestResponse(P, E, I)

Here Tᴾ is the preference-adaptation timescale, Tᴵ is the institutional timescale, and Tᴺ is the population or survival timescale. The dot over a variable denotes a time derivative. For example, Ṗ is the time derivative of P.

Only Tᴾ is sent to zero. The other speeds are left open. In empirical work they should be estimated, bounded, or varied.

Taking Tᴾ → 0 gives the fast-closure condition:

> PreferenceChange(P, E, BestResponse(P, E, I), I) = 0

Define the fast attracting set:

> Attractor(E, I) = { P : PreferenceChange(P, E, BestResponse(P, E, I), I) = 0 }

When the attracting set is a single stable branch, write:

> P = P*(E, I)

Read P*(E, I) as "the preference state implied by economic state E and institution I after fast adjustment."

The reduced economy is then:

> Ė = EconomicChange(E, P*(E, I), BestResponse(P*(E, I), E, I), I)
> Tᴵ · İ = InstitutionChange(I, E, P*(E, I), BestResponse(P*(E, I), E, I))
> Tᴺ · Ṅ = N · SurvivalGrowth(E, P*(E, I), BestResponse(P*(E, I), E, I), I)

This is the core mathematical object of the paper. The economy is no longer an economy with fixed preferences. It is an economy on a preference-adaptation manifold.

## 4. The Fast-Limit Proposition

The first theorem target is a standard singular-perturbation result with an economic interpretation.

Assume that for each relevant pair (E, I), the fast preference equation has a stable, normally hyperbolic attracting branch P*(E, I). Then as Tᴾ approaches zero, solutions of the full system rapidly approach the branch P = P*(E, I), remain close to it after a short boundary layer, and then evolve according to the reduced system.

In compact form:

> Full economy with P as a state
> ↓ Tᴾ → 0
> Reduced economy with P = P*(E, I)

The economics is more important than the mathematical technique. A utility function is usually treated as a primitive input to choice. In the fast limit it becomes an output of the adaptation system. The agent still maximizes utility, but the utility being maximized is itself pinned by the surrounding environment.

This is why the limit is conceptually sharp. Slow preference change can often be tucked into a state variable. Infinitely fast preference change changes the object being analyzed. It turns utility from a preference primitive into a response function.

## 5. Nash Equilibrium After Fast Closure

It is tempting to say that Nash equilibrium fails in this model. That would be wrong. Nash equilibrium is a fixed-point concept. It remains available. What changes is the game to which the fixed-point concept is applied.

Let Πᵢ be player i's material payoff. Let Uᵢ be player i's subjective utility. A material-payoff Nash equilibrium satisfies:

> Aᵢ ∈ argmaxᵦ Πᵢ(b, A₋ᵢ, E, I)

A fast-adapted subjective Nash equilibrium satisfies:

> Aᵢ ∈ argmaxᵦ Uᵢ(b, A₋ᵢ, E, Pᵢ*(E, I), I)

These coincide only if fast preference closure preserves the material best-response correspondence:

> argmaxᵦ Uᵢ(b, A₋ᵢ, E, Pᵢ*(E, I), I)
> = argmaxᵦ Πᵢ(b, A₋ᵢ, E, I)

When this invariance condition fails, the material Nash prediction is not robust to fast endogenous preferences. That is not a failure of Nash equilibrium. It is a failure to specify which payoff function agents are optimizing.

The clean statement is:

> Nash survives as a method.
> The Nash object changes from Π to U(· ; P*(E, I)).

This distinction matters because many economic arguments silently slide between subjective utility and material payoff. In an endogenous-preference economy, that slide is no longer harmless.

## 6. Darwinian Selection After Fast Closure

Darwinian selection also survives as a method. It is an update operator over whatever entities reproduce, persist, imitate, expand, or avoid exit. The difficult question is not whether selection exists. The question is what selection can still select after preferences adapt infinitely fast.

In the indirect evolutionary preference literature, the usual chain is:

> P → A(P) → material payoff

Different preferences induce different behavior. Different behavior produces different material payoff. Selection changes the distribution of preferences.

The fast limit can erase the first link. If all agents share the same adaptation law and the attracting branch is unique, then initial differences in P vanish before selection evaluates material consequences:

> initial P → P*(E, I) → A(P*) → SurvivalGrowth

Selection over initial preference states becomes degenerate. Selection instead acts on whatever remains heterogeneous:

> adaptation law j → P*ⱼ(E, I) → SurvivalGrowthⱼ(E, P*ⱼ(E, I), I)

The selected object may therefore be an adaptation law, an institution, a recommender policy, a cultural rule, a biological resistance parameter, or a whole induced system. It need not be an instantaneous utility function.

The extreme conclusion is uncomfortable but mathematically straightforward. If every admissible regime induces negative long-run growth after fast closure, then selection does not rescue the system by finding a better preference state:

> SurvivalGrowthⱼ(E, P*ⱼ(E, I), I) < 0 for all j

In that case the Darwinian answer to "which preferences survive?" can be "none." More precisely, no preference-generating regime in the admissible class survives.

## 7. Welfare When Preferences Are Produced

Welfare analysis is where the fast limit bites hardest.

Suppose a mechanism moves an agent from preference state P₀ to preference state P₁. At P₀ the agent prefers path A to path B. At P₁ the agent prefers path B to path A. If the analyst evaluates only final preferences, the mechanism can produce P₁, allocate B, and cite the resulting preference satisfaction as welfare evidence.

The problem is:

> produce P₁ → satisfy P₁
> → cite P₁ as welfare

Call this preference laundering. It is not a claim that final preferences are always illegitimate. It is a claim that final preferences cannot be the only welfare object when the evaluated mechanism helps produce them.

Possible welfare domains include:

1. Initial-preference welfare: evaluate the path using P₀.
2. Final-preference welfare: evaluate each state using the preference present at that state.
3. Meta-preference welfare: ask whether the agent endorses the transition from P₀ to P₁.
4. Material or survival welfare: evaluate SurvivalGrowth(E,P,A,I).
5. Constitutional welfare: restrict admissible preference-transition kernels before evaluating outcomes.
6. Path welfare: evaluate the full sequence of allocations, preferences, institutions, and actions.

The paper does not yet choose one criterion. The immediate theorem target is weaker and cleaner: in the fast preference limit, these criteria can rank the same path differently.

## 8. Model I: A One-Dimensional Taste Economy

The first model is deliberately small. It is not meant to be psychologically complete. It is a minimal laboratory for the fast-closure idea.

There is one scalar preference state p between zero and one. Low p means the agent is oriented toward an offline or embodied good. High p means the agent is oriented toward an online, artificial, or platform-mediated good.

> p = 0: offline/embodied orientation
> p = 1: online/artificial orientation

Given p, the agent allocates attention a between the two goods. The subjective problem is Cobb-Douglas:

> maximize over a: p log(a) + (1 − p) log(1 − a)

The solution is:

> a*(p) = p

The institution chooses exposure intensity s. Exposure pulls p upward; an anchoring force pulls p downward. The preference dynamic is:

> ṗ = ExposureForce(p,s) · (1 − p) − anchor · p

In the fast limit, ṗ = 0. The preference state is pinned by:

> ExposureForce(p,s) · (1 − p) = anchor · p

In the fixed-exposure case, ExposureForce(p,s) = s, so:

> p = s / (s + anchor)

Material growth is assumed to decline when p becomes too high:

> Growth(p) = Baseline + OfflineGrowth · (1 − p)
> − HighPPenalty · p²

This is a reduced-form survival penalty, not a claim about a single biological channel. It represents any long-run cost that rises when attention, social capital, reproduction, physical resilience, or institutional maintenance are displaced by the high-p good.

The survival condition is:

> survival ⇔ Growth(s / (s + anchor)) ≥ 0

The current calibration gives a simple frontier. Low exposure survives:

> s = 0.05
> p = 0.50
> Growth(p) = 0.1325

High exposure does not:

> s = 0.80
> p ≈ 0.9412
> Growth(p) ≈ −0.7778

The point is the separation. The agent's final subjective allocation is internally coherent: a*(p) = p. But the induced state can be materially nonviable. Final preference satisfaction and long-run survival can point in opposite directions.

## 9. Model II: An Indirect Evolutionary Prisoner's Dilemma

The second model connects the project to the indirect evolutionary preference literature. It uses a familiar Prisoner's Dilemma, but separates the payoff agents maximize from the payoff that determines survival.

Players choose cooperation C or defection D. Material payoffs Π have the usual Prisoner's Dilemma ranking: defection is materially tempting. Subjective utility adds a social preference term λ and possibly a norm bonus for cooperation:

> Uᵢ = Πᵢ + λᵢΠⱼ + NormBonus · 1{C}

Agents choose actions according to U. Growth or selection is determined by Π.

This model matters because it shows why "Nash survives" must be stated carefully. In the material game, defection can be the Nash prediction. In the subjective game, if λ or the norm bonus is large enough, cooperation can be a Nash prediction.

In the finite-speed simulations:

- fixed preferences with material selection push cooperation nearly to zero;
- prosocial preference drift restores full cooperation;
- conflict-oriented preference drift collapses cooperation.

In the fast limit, λ is pinned directly to the adaptation target. A prosocial fast attractor gives:

> λ = 1.10

and the model yields cooperation. A conflict-oriented fast attractor gives:

> λ = −0.25

and the model yields defection.

The result is not that game theory stops working. The result is that the material Prisoner's Dilemma and the fast-adapted subjective game are different games. The analyst must say which game is being solved.

## 10. Model III: Institutions, Timescales, And Survival

The third model is the most important for the current paper direction. It asks what survives after preference closure.

The one-dimensional taste model treated exposure intensity s as fixed. Here s is chosen by an institution I. The institution may be a platform, recommender system, school, family regime, cultural authority, firm, or regulator. The model lets us compare myopic institutions with survival-aware institutions.

The only maintained limiting assumption is:

> Tᴾ → 0

Other timescales are varied:

> Tᴵ / Tᴺ    institution speed relative to population speed
> Tᴬ / Tᴺ    action-adjustment speed relative to population speed
> Tᶜ / Tᴺ    cultural speed relative to population speed

A myopic institution chooses exposure to maximize engagement net of exposure cost:

> PlatformValue = p − ExposureCost · s²

A survival-aware institution gives weight to material growth:

> PlatformValue = p − ExposureCost · s²
> + SurvivalWeight · Growth(p)

Under the current calibration, the myopic institution chooses:

> s ≈ 0.645
> p ≈ 0.928
> Growth(p) ≈ −0.745

The result is extinction under every tested speed ordering. The date of extinction changes:

- slow institution, slow population: extinction around period 146;
- fast institution, slow population: extinction around period 125;
- slow institution, fast population: extinction around period 18;
- all-fast myopic institution: extinction around period 8.

The survival-aware institution chooses:

> s = 0.030
> p = 0.375
> Growth(p) = 0.316

and survives.

This is only a toy result, but it is the right kind of toy result. It shows that the Darwinian question is not "which final tastes are most satisfying?" The question is "which preference-generating systems persist?" In the fast limit, the object that survives is an institution-plus-adaptation-law-plus-attractor, not a static utility function.

## 11. Empirical Timescales

The theory should not assume that institutions, algorithms, culture, behavior, or populations are slower than preferences. Those speeds should be measured when possible and varied when not.

A minimal reduced-form estimate starts with an observed or latent state Yₜ:

> Yₜ₊₁ = α + ρYₜ + βExposureₜ + εₜ

The implied speed and half-life are:

> speed = −log(ρ) / Δt
> half-life = log(2)/speed

This is only a diagnostic. Observed choices are noisy proxies for latent preferences, and the same behavior can reflect preference change, belief change, constraint change, or attention change.

Better empirical approaches include:

- Bayesian state-space discrete-choice models for evolving preference parameters;
- latent transition models for movement between types;
- random-intercept cross-lagged panel models that separate stable heterogeneity from within-person change;
- randomized feed experiments and deactivation experiments that identify exposure effects;
- survival or hazard models for exit, fertility, attrition, institutional collapse, or platform abandonment.

Allcott, Braghieri, Eichmeyer, and Gentzkow's Facebook deactivation experiment provides a template for measuring behavior and welfare over weeks. Guess et al.'s algorithmic-feed experiment provides a template for measuring how feed rules affect exposure, activity, and attitudes. Lachaab, Ansari, Jedidi, and Trabelsi provide a state-space approach to evolving discrete-choice preferences. Hamaker, Kuiper, and Grasman, and Mulder and Hamaker, warn that ordinary cross-lagged panel estimates can confuse stable between-person differences with within-person dynamics.

The empirical target for this project is not the vague claim "social media changes preferences." The target is:

> Estimate the relative speeds of preference closure,
> institutional adaptation, behavioral response,
> and population or exit dynamics.

Those estimates determine which limiting model is relevant.

## 12. What The Current Results Say

The simulations so far are not evidence about the real world. They are existence demonstrations and theorem probes. Their value is to reveal which claims can be made cleanly.

The one-dimensional model shows that final preference satisfaction can coexist with negative material growth. The result is not surprising; its value is that it gives a closed-form survival frontier.

The Prisoner's Dilemma model shows that a fast-adapted subjective Nash equilibrium can differ from the material-payoff Nash equilibrium. The result keeps the paper connected to indirect evolutionary preferences while clarifying that the novelty is not cooperation itself.

The institutional model shows that myopic exposure optimization can generate extinction under several timescale orderings, while survival-aware optimization survives. This is the strongest current candidate for the paper's applied spine.

The invariant lesson across all three models is:

> Fast preferences turn utility into a response map.
> Equilibrium is computed after that map closes.
> Selection acts on what remains heterogeneous.
> Welfare cannot rest on final preferences alone.

## 13. What Is Potentially Novel

The following claims are not novel:

- preferences can be endogenous;
- tastes can be shaped by habits, institutions, culture, or technology;
- recommender systems can influence behavior;
- engagement need not equal welfare;
- subjective preferences and material payoffs can diverge;
- welfare is difficult when preferences are endogenous.

The potentially novel contribution is the combined singular-limit structure:

> fast preference closure
> + Nash object shift
> + selection target shift
> + long-run survival frontier
> + welfare non-invariance

This also clarifies the title. "Endogenous Utility" is too broad. Better titles are:

> When Utility Adapts Faster Than Selection
> The Singular Limit Of Endogenous Preferences

## 14. Theorem Targets

The draft currently contains theorem candidates, not finished proofs. The next technical step is to prove or abandon them.

Proposition 1: Fast Preference Closure. If the fast subsystem has a globally attracting, normally hyperbolic branch P = P*(E, I), then as Tᴾ → 0, the full economy converges after a boundary layer to the reduced economy on that branch.

> Pₜ ≈ P*(Eₜ, Iₜ) after closure

Proposition 2: Material Nash Invariance. The Nash equilibria of the fast-adapted subjective game coincide with the Nash equilibria of the material payoff game if and only if fast preference closure preserves the material best-response correspondence.

> BestResponseᵁ(P*(E, I), E, I) = MaterialBestResponse(E, I)

Proposition 3: Selection Target Shift. If all individuals share a common fast adaptation law with unique attractor P*(E, I), then selection over initial preference states is degenerate in the fast limit. If adaptation laws differ by type j, selection acts on:

> j → P*ⱼ(E, I) → SurvivalGrowthⱼ(E, P*ⱼ(E, I), I)

Proposition 4: Long-Run Survival Frontier. In the one-dimensional fixed-rule model, survival occurs if and only if:

> Growth(s / (s + anchor)) ≥ 0

If a myopic institution chooses an exposure outside the survival set, the induced system goes extinct.

Proposition 5: Welfare Non-Invariance. For a sufficiently rich preference state space and transition technology, there exist two paths A and B such that initial-preference welfare, final-preference welfare, meta-preference welfare, and material welfare do not all agree.

> A ≻ under P₀ B
> B ≻ under P₁ A
> SurvivalRank(A) ≠ SurvivalRank(B)

This proposition would formalize the preference-laundering problem.

## 15. Limitations And Risks

The main risk is overclaiming. Endogenous preferences are a large existing literature. The paper should not imply that economists forgot preferences can change. The correct claim is about a specific limiting regime and its consequences for equilibrium, selection, and welfare objects.

The second risk is that the toy models are too easy. A model where exposure increases p and high p reduces growth will naturally generate a survival frontier. The proof burden is to show that the qualitative object shift is invariant across richer models, not to overinterpret a calibration.

The third risk is welfare ambiguity. The draft can show that final preferences are insufficient, but it cannot simply replace them with biological fitness without argument. Material survival is one criterion, not a complete welfare theory. The paper should separate positive survival claims from normative welfare claims.

The fourth risk is empirical identification. Preference change is hard to distinguish from belief change, constraint change, attention change, and measurement error. The empirical section should therefore focus on timescale estimation and model discrimination, not sweeping claims about psychology.

## 16. Conclusion

This draft began with an extreme premise: utility adapts infinitely fast. The premise is not literally true, but the limit is analytically useful. It reveals that once preferences are fast state variables, utility becomes a response map rather than a primitive. Nash equilibrium still applies, but to the fast-adapted subjective game. Darwinian selection still applies, but to the variables that remain heterogeneous after preference closure. Welfare analysis cannot rely on final preferences alone because the mechanism being evaluated may have produced those preferences.

The strongest current version of the paper is not a broad essay on endogenous utility. It is a mathematical economics paper about the singular limit of endogenous preferences. The technical spine is fast closure. The conceptual payoffs are the Nash object shift, the selection target shift, and welfare non-invariance. The applied spine is the survival frontier of preference-generating institutions.

The next version should prove the closure theorem, formalize the Nash invariance condition, sharpen the selection-target proposition, and decide whether the institutional survival model is strong enough to carry the paper.

## References To Integrate

Adomavicius, G., Bockstedt, J. C., Curley, S. P., and Zhang, J. "Do Recommender Systems Manipulate Consumer Preferences? A Study of Anchoring Effects." Information Systems Research, 2013.

Allcott, H., Braghieri, L., Eichmeyer, S., and Gentzkow, M. "The Welfare Effects of Social Media." American Economic Review, 2020.

Ashton, H., and Franklin, M. "Solutions to Preference Manipulation in Recommender Systems Require Knowledge of Meta-Preferences." arXiv, 2022.

Becker, G. S., and Murphy, K. M. "A Theory of Rational Addiction." Journal of Political Economy, 1988.

Becker, G. S., and Mulligan, C. B. "The Endogenous Determination of Time Preference." Quarterly Journal of Economics, 1997.

Bernheim, B. D., Braghieri, L., Martinez-Marquina, A., and Zuckerman, D. "A Theory of Chosen Preferences." American Economic Review, 2021.

Bisin, A., and Verdier, T. "The Economics of Cultural Transmission and the Dynamics of Preferences." Journal of Economic Theory, 2001.

Bowles, S. "Endogenous Preferences: The Cultural Consequences of Markets and Other Economic Institutions." Journal of Economic Literature, 1998.

Dekel, E., Ely, J. C., and Yilankaya, O. "Evolution of Preferences." Review of Economic Studies, 2007.

Ely, J. C., and Yilankaya, O. "Nash Equilibrium and the Evolution of Preferences." Journal of Economic Theory, 2001.

Fenichel, N. "Geometric Singular Perturbation Theory for Ordinary Differential Equations." Journal of Differential Equations, 1979.

Franklin, M., Ashton, H., Gorman, R., and Armstrong, S. "Recognising the Importance of Preference Change." arXiv, 2022.

Guess, A. M. et al. "How Do Social Media Feed Algorithms Affect Attitudes and Behavior in an Election Campaign?" Science, 2023.

Hamaker, E. L., Kuiper, R. M., and Grasman, R. P. P. P. "A Critique of the Cross-Lagged Panel Model." Psychological Methods, 2015.

Hayashi, T. "A Theory of Preferences and Meta-Preferences." working paper.

Heifetz, A., Shannon, C., and Spiegel, Y. "The Dynamic Evolution of Preferences." Economic Theory, 2007.

Jiang, R., Chiappa, S., Lattimore, T., Gyorgy, A., and Kohli, P. "Degenerate Feedback Loops in Recommender Systems." AIES, 2019.

Khosrowi, D., and Beck, L. "Like It or Not: Recommender Systems Lack a Coherent Normative Foundation." FAccT, forthcoming.

Kleinberg, J., Mullainathan, S., and Raghavan, M. "The Challenge of Understanding What Users Want: Inconsistent Preferences and Engagement Optimization." Management Science, 2024.

Lachaab, M., Ansari, A., Jedidi, K., and Trabelsi, A. "Modeling Preference Evolution in Discrete Choice Models: A Bayesian State-Space Approach." Quantitative Marketing and Economics, 2006.

Robson, A. J., Whitehead, L. A., and Robalino, N. "Adaptive Utility." Journal of Economic Behavior and Organization, 2023.

Rozen, K. "Foundations of Intrinsic Habit Formation." Econometrica, 2010.

Sadowski, P., and Sarver, T. "Foundations of Ambiguity in Preferences." working paper.

Sandholm, W. H. "Preference Evolution, Two-Speed Dynamics, and Rapid Social Change." Review of Economic Dynamics, 2001.

Stigler, G. J., and Becker, G. S. "De Gustibus Non Est Disputandum." American Economic Review, 1977.

von Weizsaecker, C. C. "Freedom, Wealth and Adaptive Preferences." Working paper, 2013.
