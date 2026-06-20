# When Utility Adapts Faster Than Selection

## A Singular-Limit Approach To Endogenous Preferences

Draft v0.1
Project: Endogenous Utility Research Program
Status: working draft for internal reading and comments

## Abstract

Economic theory usually treats utility functions as primitive, fixed, or slow
moving relative to the allocation problem under study. This paper asks what
happens at the opposite extreme. Suppose preference states adapt on a timescale
$T_{\mathrm{pref}}$, and take the singular limit $T_{\mathrm{pref}}\to 0$ relative to other economic,
institutional, and population processes. In that limit, preferences are not
slowly selected traits. They are fast state variables pinned to an attracting
manifold of the preference-adaptation system. Nash equilibrium and Darwinian
selection remain valid mathematical operators, but the state space on which they
operate changes. Nash fixed points are computed in the reduced game induced by
fast-adapted preferences, and material or Darwinian selection acts only on
variables that remain heterogeneous after fast closure: populations, adaptation
laws, institutions, or resistance to adaptation. The result is a sharp
separation between local subjective rationality, material payoff, final
preference satisfaction, and long-run survival. In calibrated toy models,
myopic institutions can induce preference attractors that are locally
satisfying and engagement-maximizing but produce negative long-run growth and
eventual extinction. Survival-aware institutions choose different adaptation
laws and survive. The paper argues that welfare analysis with fast endogenous
utility must be stated over allocation-preference paths, admissible transition
kernels, or meta-preferences, not final preferences alone.

## 1. Introduction

The standard consumer problem begins after tastes have been specified. A
preference relation or utility function is assumed, agents optimize, and the
analyst studies allocation, equilibrium, and welfare. Economics has never been
naive about preference change. Habits, addiction, cultural transmission,
endogenous time preference, socialization, and indirect evolutionary
preferences all appear in established literatures. The usual modeling choice is
not that tastes literally never change. It is that, for the problem at hand,
they can be treated as primitives or slow-moving state variables.

That separation is becoming harder to defend. Digital platforms, recommender
systems, social media feeds, and AI-mediated environments do not merely allocate
goods to fixed tastes. They observe behavior, select environments, alter
attention, and change future behavior. Whether this is called persuasion,
habit, addiction, personalization, social learning, or preference manipulation,
the important mathematical point is that the utility function may itself be a
fast state variable inside the allocation mechanism.

This paper studies the extreme logical case. Let $\theta_t$ denote the preference
state that locally represents an agent's utility function. Let $z_t$ denote
other economic, social, demographic, or material state variables. Suppose
preference adaptation occurs on timescale $T_{\mathrm{pref}}$. What happens as:

$$
T_{\mathrm{pref}} \to 0?
$$

The question is not whether Nash equilibrium "survives." Nash equilibrium is a
fixed-point method. Nor is the question whether Darwinian selection "survives."
Selection is an update operator. The question is what these operators are
applied to after preference states have adjusted infinitely fast.

The central answer is a singular reduction. If the fast preference subsystem has
a unique attracting branch:

$$
\theta = \Phi(z,m)
$$

where $m$ is an institution, platform rule, social environment, or adaptation
law, then the economy no longer evolves with $\theta$ as an independent slow
state. Instead, utility is evaluated on the fast-adapted manifold:

$$
U_t(\cdot)=U(\cdot;\Phi(z_t,m_t)).
$$

Actions are best responses in the reduced preference game, not necessarily in
the material payoff game. Selection acts on the post-closure system: population
shares, institutional regimes, adaptation laws, or the entire induced economy.
If every admissible regime induces negative long-run material growth, the
answer to the Darwinian question "what survives?" can be: nothing.

The paper makes five claims.

First, in the $T_{\mathrm{pref}}\to 0$ limit with a unique attracting preference manifold,
utility is replaced by a fast-response map. Utility is not a primitive and not a
slowly selected trait. It is the graph of the adaptation mechanism.

Second, Nash remains the equilibrium method, but the relevant game changes. A
profile can be Nash with respect to fast-adapted preferences while failing to be
Nash with respect to material payoffs. The material Nash prediction is invariant
only when fast preference closure preserves the material best-response
correspondence.

Third, Darwinian selection remains the selection method, but the selected object
changes. If all agents governed by a common adaptation law are instantly reset
to the same preference state, selection over preference states becomes
degenerate. Selection can still operate over adaptation laws, institutions,
populations, or resistance to adaptation.

Fourth, final-preference welfare is fragile. If a mechanism can first produce a
preference and then satisfy it, ex post preference satisfaction can validate the
path that generated the preference. Welfare analysis must include initial
preferences, meta-preferences, material fitness, constitutional constraints on
transition laws, or welfare over full allocation-preference paths.

Fifth, timescale ordering should not be assumed. This draft fixes only
$T_{\mathrm{pref}}\to 0$. The speeds of institutions, algorithms, action adjustment,
culture, and population dynamics should be estimated or varied. In the toy
models below, myopic institutions induce preference states that maximize
engagement but generate negative population growth under every tested speed
ordering. Survival-aware institutions choose lower exposure and survive.

The argument is intentionally stark. The point is not to claim that real
preferences are literally infinitely adaptable. The point is to use the limit as
a mathematical microscope. Extreme cases expose which concepts are invariant and
which concepts are artifacts of treating preferences as fixed.

## 2. Relation To Existing Literature

The claim that preferences are endogenous is not new. Stigler and Becker
famously argued that apparent taste change can often be modeled through stable
underlying preferences and changing consumption capital. Becker and Murphy
modeled rational addiction. Becker and Mulligan studied endogenous time
preference. Rozen gave foundations for intrinsic habit formation. Bowles
surveyed how markets and institutions shape preferences. Bisin and Verdier
developed cultural transmission models in which preference traits evolve through
family and socialization. Bernheim, Braghieri, Martinez-Marquina, and Zuckerman
modeled chosen preferences or worldviews. Hayashi develops a theory of
meta-preferences and investment in future preferences.

This paper is closest to the indirect evolutionary preference literature. Ely
and Yilankaya, Dekel, Ely, and Yilankaya, Heifetz, Shannon, and Spiegel, and
Sandholm study economies in which agents act according to subjective
preferences, while material payoff determines evolutionary success. Sandholm's
two-speed model is especially important. In his model, behavior adjusts quickly
while natural selection slowly reshapes the distribution of preferences. The
present paper changes the location of the fast variable. Preference adaptation
itself is fast. This alters the object of selection. Instead of selection
sorting slowly inherited preference types, selection may sort adaptation laws or
institutional regimes after preference states have already closed onto a fast
manifold.

There is also a related literature on adaptive utility. Robson, Whitehead, and
Robalino model utility as an adaptive coding device under limited discriminative
capacity. Sadowski and Sarver use adaptive preferences to explain non-expected
utility and ambiguity aversion. Von Weizsaecker asks when welfare economics can
be recovered under adaptive preferences. These papers matter because they do
not treat utility as a fixed object. The present draft adds an explicit
singular-limit perspective and asks what happens when adaptation is faster than
the equilibrium and selection problems being studied.

The recommender-systems and AI literatures provide the motivating environment.
Adomavicius, Bockstedt, Curley, and Zhang show experimentally that recommender
ratings can anchor constructed preferences. Jiang, Chiappa, Lattimore, Gyorgy,
and Kohli study degenerate feedback loops in recommender systems. Ashton and
Franklin, and Franklin, Ashton, Gorman, and Armstrong, argue that AI systems can
change preferences and that meta-preferences are needed to evaluate such
changes. Kleinberg, Mullainathan, and Raghavan show that engagement
optimization can diverge from user welfare when preferences are inconsistent.
Khosrowi and Beck argue that recommender systems lack a coherent normative
foundation for welfare-relevant preferences. Acemoglu, Ozdaglar, and Siderius
model AI and social media from a political economy perspective.

The present draft should not claim priority over these broad insights. It does
not discover endogenous preferences, recommender feedback, or the
engagement-welfare gap. The contribution, if it survives proof and further
literature review, is narrower: a singular-limit model in which infinitely fast
preference adaptation changes the state space of Nash equilibrium, Darwinian
selection, and welfare analysis.

Finally, the formal method is related to singular perturbation theory,
especially Fenichel-style reductions of slow-fast systems. The proof strategy is
not to invent a new mathematical apparatus, but to import the right one into
endogenous-utility economics.

## 3. General Environment

Time may be continuous or discrete. The continuous-time notation is clearer for
the limit. Let:

$$
\theta_t \in \Theta
$$

be the preference state. A utility representation is:

$$
U(x,a;\theta_t),
$$

where $x$ is an allocation or consequence and $a$ is an action. Let:

$$
z_t \in Z
$$

collect non-preference economic states: resources, demographic state,
population size, technology, social capital, or other material variables. Let:

$$
m_t \in M
$$

be an institution, algorithm, platform policy, cultural environment, or
adaptation law.

Agents choose actions according to current subjective preferences. In a game,
this means:

$$
a_t \in BR(\theta_t,z_t,m_t).
$$

The material or survival payoff need not equal subjective utility. Write:

$$
F(z_t,\theta_t,a_t,m_t)
$$

for the material growth, survival, reproductive, or objective payoff criterion.

Preference adaptation is:

$$
T_{\mathrm{pref}}\frac{d\theta}{dt}=G(\theta,z,a,m).
$$

Other state variables evolve according to:

$$
\frac{dz}{dt}=H(z,\theta,a,m).
$$

Institutional or algorithmic rules may also evolve:

$$
T_m\frac{dm}{dt}=R(m,z,\theta,a).
$$

Population or survival dynamics may evolve at another speed:

$$
T_{\mathrm{pop}}\frac{dn}{dt}=n\,g(z,\theta,a,m).
$$

The key modeling discipline is that only $T_{\mathrm{pref}}$ is sent to zero. The other
timescales are not assumed. They are parameters, and in empirical work they
should be estimated or bounded.

The full system is therefore:

$$
\begin{aligned}
T_{\mathrm{pref}}\frac{d\theta}{dt} &= G(\theta,z,a,m),\\
\frac{dz}{dt} &= H(z,\theta,a,m),\\
T_m\frac{dm}{dt} &= R(m,z,\theta,a),\\
T_{\mathrm{pop}}\frac{dn}{dt} &= n\,g(z,\theta,a,m),\\
a &\in BR(\theta,z,m).
\end{aligned}
$$

Taking $T_{\mathrm{pref}}\to 0$ gives the fast-closure condition:

$$
G(\theta,z,BR(\theta,z,m),m)=0.
$$

Define the fast attracting set:

$$
A(z,m)=\{\theta: G(\theta,z,BR(\theta,z,m),m)=0\}.
$$

When $A(z,m)$ is a singleton and globally attracting, write:

$$
\theta=\Phi(z,m).
$$

The reduced economy is:

$$
\begin{aligned}
\frac{dz}{dt} &= H(z,\Phi(z,m),BR(\Phi(z,m),z,m),m),\\
T_m\frac{dm}{dt} &= R(m,z,\Phi(z,m),BR(\Phi(z,m),z,m)),\\
T_{\mathrm{pop}}\frac{dn}{dt} &= n\,g(z,\Phi(z,m),BR(\Phi(z,m),z,m),m).
\end{aligned}
$$

This is the core reduction.

## 4. Equilibrium And Selection In The Fast Limit

### 4.1 Nash Object Shift

Nash equilibrium is a fixed-point concept. It remains available. What changes
is the game to which the fixed-point concept is applied.

Let $\pi_i(a,z,m)$ be the material payoff of player $i$. Let
$U_i(a,z,\theta_i,m)$ be subjective utility. A material-payoff Nash
equilibrium satisfies:

$$
a_i \in \operatorname*{arg\,max}_{b}\; \pi_i(b,a_{-i},z,m).
$$

A fast-adapted preference Nash equilibrium satisfies:

$$
a_i \in \operatorname*{arg\,max}_{b}\; U_i(b,a_{-i},z,\Phi_i(z,m),m).
$$

These two objects coincide only under an invariance condition:

$$
\operatorname*{arg\,max}_{b} U_i(b,a_{-i},z,\Phi_i(z,m),m)
=
\operatorname*{arg\,max}_{b} \pi_i(b,a_{-i},z,m).
$$

for every player and relevant state. When the condition fails, the equilibrium
method remains Nash, but the equilibrium prediction differs.

This is not a failure of game theory. It is a warning against silently switching
between subjective utility and material payoff. If agents maximize subjective
utility but selection evaluates material payoff, the relevant Nash object is
subjective. The relevant survival object is material.

### 4.2 Selection Target Shift

In the indirect evolutionary approach, preference types can be selected because
different preferences induce different behavior and hence different material
payoffs. In symbols:

$$
\theta \longmapsto a(\theta) \longmapsto F(\theta,a(\theta)).
$$

The fast limit changes this chain. If all agents share the same adaptation law
and the fast subsystem has a unique attracting branch:

$$
\theta=\Phi(z,m),
$$

then inherited variation in $\theta$ is erased before selection operates.
Selection over preference states becomes degenerate. Selection instead acts on
whatever remains heterogeneous:

$$
j \longmapsto \Phi_j(z,m) \longmapsto g_j(z,\Phi_j(z,m),m).
$$

The selected object is not necessarily a utility function. It may be an
institution, a recommendation policy, a cultural transmission rule, a biological
resistance parameter, or an entire economic system.

This has an uncomfortable implication. If every admissible adaptation law
induces negative long-run growth:

$$
g_j(z,\Phi_j(z,m),m)<0 \quad \forall j,
$$

then selection does not rescue the system by finding a better preference type.
The system goes extinct, exits, collapses, or is replaced by an external regime.
The answer to "which preferences survive?" can be "none," because preferences
are not the surviving object.

### 4.3 Welfare Object Shift

Final preferences are dangerous welfare evidence when preferences are produced
by the path being evaluated. A mechanism can move the agent from $\theta_0$ to
$\theta_1$, allocate $x_1$, and then point to the fact that $\theta_1$ endorses
$x_1$.

The welfare domain must therefore include more than final allocations and final
preferences. Candidate welfare objects include:

$$
(z_t,\theta_t,m_t,K_t,a_t)_{t\ge 0},
$$

initial preferences, meta-preferences, material growth, biological survival,
or constitutional restrictions on admissible preference transitions.

This is not merely philosophical. In the toy models below, the same path can be
ranked positively by final subjective preferences and negatively by material
growth.

## 5. The One-Dimensional Taste Model

The simplest model has a preference state:

$$
\theta \in [0,1],
$$

where $\theta=0$ represents an offline or embodied good and $\theta=1$
represents an online or artificial good. Given current $\theta$, the agent solves
a Cobb-Douglas attention problem:

$$
\max_a\; \theta\log a + (1-\theta)\log(1-a),
$$

so:

$$
a^*(\theta)=\theta.
$$

Preference adaptation is:

$$
\dot{\theta}=\operatorname{exposure}(\theta,m)(1-\theta)-\operatorname{anchor}\,\theta.
$$

In the fast limit, $\theta$ satisfies:

$$
\operatorname{exposure}(\theta,m)(1-\theta)=\operatorname{anchor}\,\theta.
$$

In the fixed-exposure version:

$$
\theta=\frac{m}{m+\operatorname{anchor}}.
$$

Material growth is assumed to decline at high $\theta$:

$$
g(\theta)=\text{baseline}+\text{offline growth}(1-\theta)-\text{high-theta penalty}\,\theta^2.
$$

This is not a claim about a literal biological mechanism. It is a reduced-form
way to represent the possibility that preferences over artificial or
platform-mediated goods may be locally satisfying while reducing material
resilience, reproduction, social capital, or survival.

The fixed-rule survival frontier is immediate:

$$
\operatorname{survival} \iff g\left(\frac{m}{m+\operatorname{anchor}}\right)\ge 0.
$$

In the current calibration, the largest grid-tested exposure with nonnegative
growth is:

$$
m=0.05.
$$

That exposure induces:

$$
\begin{aligned}
\theta &= 0.50,\\
g(\theta) &= 0.1325.
\end{aligned}
$$

A high exposure:

$$
m=0.80.
$$

induces:

$$
\begin{aligned}
\theta &\approx 0.9412,\\
g(\theta) &\approx -0.7778.
\end{aligned}
$$

Thus high adapted preference satisfaction can coexist with negative long-run
growth.

## 6. Indirect Evolutionary Prisoner's Dilemma

The second model adapts the indirect evolutionary approach. Players play a
Prisoner's Dilemma. Material payoffs favor defection. Subjective preferences
include a social preference parameter $\lambda$:

$$
U_i=\pi_i+\lambda_i\pi_j+\text{norm bonus}\cdot\mathbf{1}_{\{C\}}.
$$

Material payoff determines growth, but behavior is chosen according to
subjective utility.

In the finite-speed simulations:

- fixed preferences with material selection push cooperation nearly to zero;
- prosocial preference drift restores full cooperation;
- conflict-oriented drift collapses cooperation.

In the fast limit, $\lambda$ is pinned to the adaptation target. If the fast
attractor is prosocial:

$$
\lambda=1.10,
$$

the model yields full cooperation. If the fast attractor is conflict-oriented:

$$
\lambda=-0.25,
$$

the model yields defection.

The lesson is not that Nash disappears. The lesson is that the material
Prisoner's Dilemma and the fast-adapted subjective game have different Nash
objects. Material defection is not invariant to a fast preference map that makes
cooperation subjectively optimal.

## 7. Institutional Timescales And Long-Run Survival

The initial fast-limit model treated institutions and population as slower
variables. That was too restrictive. The corrected approach fixes only:

$$
T_{\mathrm{pref}}\to 0.
$$

Other speeds are explicit:

$$
\frac{T_{\mathrm{algorithm}}}{T_{\mathrm{population}}},\qquad
\frac{T_{\mathrm{action}}}{T_{\mathrm{population}}},\qquad
\frac{T_{\mathrm{culture}}}{T_{\mathrm{population}}}.
$$

The current script tests:

- slow institutions and slow population;
- fast institutions and slow population;
- slow institutions and fast population;
- all-fast myopic institutions;
- all-fast survival-aware institutions;
- fixed-rule survival frontiers.

The myopic institution chooses exposure to maximize:

$$
V_{\mathrm{platform}}=\theta-\text{exposure cost}\,m^2.
$$

The survival-aware institution additionally values material growth:

$$
V_{\mathrm{platform}}=\theta-\text{exposure cost}\,m^2+
\text{survival weight}\,g(\theta).
$$

The current calibration gives:

$$
\begin{aligned}
m_{\mathrm{myopic}} &\approx 0.645,\\
\theta &\approx 0.928,\\
g(\theta) &\approx -0.745.
\end{aligned}
$$

Under all tested speed orderings, myopic institutions eventually go extinct.
The extinction date changes with timescales:

- slow institution, slow population: extinction around period 146;
- fast institution, slow population: extinction around period 125;
- slow institution, fast population: extinction around period 18;
- all-fast myopic: extinction around period 8.

By contrast, the survival-aware institution chooses:

$$
\begin{aligned}
m &= 0.030,\\
\theta &= 0.375,\\
g(\theta) &= 0.316.
\end{aligned}
$$

and survives.

This example is deliberately small, but it clarifies the long-run question. The
Darwinian operator does not ask which current preferences are most satisfying.
It asks which induced systems reproduce, persist, or avoid extinction. When
preferences are fast, the induced system is an adaptation law plus its
preference attractor.

## 8. Empirical Timescales

The theory should not assume that institutions, algorithms, population, or
culture are slower than preference adaptation. Timescales should be measured
when data allow.

A minimal reduced-form estimate uses a measured or latent state $y_t$:

$$
y_{t+1}=\alpha+\rho y_t+\beta\,\operatorname{exposure}_t+\varepsilon_t.
$$

Then:

$$
\begin{aligned}
\operatorname{speed} &= -\frac{\log(\rho)}{\Delta t},\\
\text{half-life} &= \frac{\log 2}{\operatorname{speed}}.
\end{aligned}
$$

This is only a diagnostic. In serious empirical work, observed choices are noisy
proxies for latent preferences. Better approaches include:

- Bayesian state-space discrete-choice models for evolving preference
  parameters;
- latent transition models for type movement;
- random-intercept cross-lagged panel models to separate within-person change
  from stable between-person heterogeneity;
- randomized feed experiments and deactivation experiments to identify exposure
  effects;
- survival or hazard models for population exit, fertility, attrition, or
  institutional collapse.

Allcott, Braghieri, Eichmeyer, and Gentzkow's Facebook deactivation experiment
provides a template for measuring behavior and welfare responses over weeks.
Guess et al.'s algorithmic-feed experiment provides a template for measuring
how feed rules affect activity, exposure, and attitudes. Lachaab, Ansari,
Jedidi, and Trabelsi provide a state-space approach to evolving discrete-choice
preferences. Hamaker, Kuiper, and Grasman, and Mulder and Hamaker, warn that
ordinary cross-lagged panel estimates can confound stable heterogeneity with
within-person dynamics.

For this project, the empirical target is not simply "social media changes
preferences." It is:

> Estimate the relative speeds of preference closure, institutional adaptation,
> behavioral best response, and population or exit dynamics.

Those estimates determine which limiting model is relevant.

## 9. Welfare: Why Final Preferences Are Not Enough

Suppose an agent initially prefers path $A$ to path $B$. A mechanism induces
transition law $K$ that moves the agent to a new preference state under which
$B$ is preferred to $A$. If the analyst evaluates only final preferences, the
mechanism appears welfare-improving. But the conclusion is generated by the
preference transition itself.

This is the preference-laundering problem:

$$
\theta_1\;\text{produced}\;\longrightarrow\;
\theta_1\;\text{satisfied}\;\longrightarrow\;
\theta_1\;\text{cited as welfare evidence}.
$$

The fast limit intensifies the problem because preference transition is not a
slow background process. It is effectively simultaneous with allocation.

Possible welfare criteria:

1. Initial-preference welfare: evaluate the path using $\theta_0$.
2. Final-preference welfare: evaluate each state using the preference present
   at that state.
3. Meta-preference welfare: evaluate whether the transition
   $\theta_0 \to \theta_1$ is endorsed by higher-order preferences.
4. Material or survival welfare: evaluate $g(\theta,z,m)$.
5. Constitutional welfare: restrict admissible transition kernels $K$.
6. Path welfare: evaluate the entire allocation-preference path.

The draft does not yet choose one criterion. The immediate theorem target is
weaker: show that these criteria can rank the same path differently in the fast
preference limit.

## 10. What Is Potentially Novel

The following claims are not novel:

- preferences can be endogenous;
- recommender systems can influence behavior;
- engagement need not equal welfare;
- behavioral welfare is difficult when preferences are endogenous;
- subjective preferences and material payoffs can diverge.

The potentially novel contribution is the combination:

> fast preference closure + Nash object shift + selection target shift +
> long-run survival frontier + welfare non-invariance.

The platform-control model is now best understood as one application. The
broader object is the singular limit of endogenous utility.

The most promising paper title is therefore not:

> Endogenous Utility

which is much too broad. Better candidates:

> When Utility Adapts Faster Than Selection

or:

> The Singular Limit Of Endogenous Preferences

## 11. Theorem Targets

The draft currently contains theorem candidates, not finished proofs. The next
technical step is to prove the following.

### Proposition 1: Fast Preference Closure

Assume the fast subsystem:

$$
T_{\mathrm{pref}}\frac{d\theta}{dt}=G(\theta,z,BR(\theta,z,m),m).
$$

has a globally attracting, normally hyperbolic branch $\theta=\Phi(z,m)$.
Then as $T_{\mathrm{pref}}\to 0$, solutions converge after an initial boundary layer to
the reduced system on the critical manifold:

$$
\theta_t=\Phi(z_t,m_t).
$$

This is a direct singular-perturbation result, but the economic interpretation
is new to the paper.

### Proposition 2: Material Nash Invariance

The Nash equilibrium of the fast-adapted preference game coincides with the
Nash equilibrium of the material payoff game if and only if fast preference
closure preserves the material best-response correspondence.

If:

$$
BR_U(\Phi(z,m),z,m) \ne BR_{\pi}(z,m),
$$

then material Nash predictions are not invariant to fast preference closure.

### Proposition 3: Selection Target Shift

If all individuals share a common fast adaptation law with unique attractor
$\Phi(z,m)$, then selection over initial preference states is degenerate in the
$T_{\mathrm{pref}}\to 0$ limit. If adaptation laws differ by type $j$, selection acts on:

$$
j \longmapsto \Phi_j(z,m) \longmapsto g_j(z,\Phi_j(z,m),m).
$$

The selected object is the adaptation law or institution, not the instantaneous
utility function.

### Proposition 4: Long-Run Survival Frontier

In the one-dimensional fixed-rule model:

$$
\theta=\frac{m}{m+\operatorname{anchor}},
$$

and long-run survival occurs if and only if:

$$
g\left(\frac{m}{m+\operatorname{anchor}}\right)\ge 0.
$$

If the institution chooses $m$ to maximize subjective engagement and the
maximizer lies outside the survival set, the induced system goes extinct.

### Proposition 5: Welfare Non-Invariance

For a sufficiently rich preference state space and transition technology,
there exist two paths `A` and `B` such that:

$$
\begin{aligned}
A &\succ_{\theta_0} B,\\
B &\succ_{\theta_1} A,\\
\operatorname{rank}_g(A) &\ne \operatorname{rank}_g(B).
\end{aligned}
$$

Therefore final-preference Pareto comparisons are not invariant to admissible
preference-transition technologies.

## 12. Discussion

The fast preference limit produces several strange but disciplined conclusions.

First, utility can become too responsive to serve as a stable welfare primitive.
If preferences adapt instantly, then satisfying current preferences may be
cheap: change the preferences and then satisfy them.

Second, material-payoff equilibrium and subjective equilibrium are different
objects. Nash still applies, but one must specify the utility used in the best
response.

Third, selection may not rescue bad preferences. If preferences are reset by
the environment before selection can act on them, selection acts on the
environment or adaptation law. A system can locally optimize itself into
extinction.

Fourth, timescales are empirical. The correct limiting model depends on whether
preference closure, algorithmic update, behavioral response, and population
dynamics operate over seconds, days, months, years, or generations.

Fifth, regulation or constitutional design should be modeled as restrictions on
transition kernels, not only as constraints on allocations. If the allocation
mechanism includes preference formation, Pareto efficiency over allocations is
not enough.

## 13. Conclusion

This draft began from a deliberately extreme premise: utility adapts infinitely
fast. The premise is false literally but useful mathematically. In the singular
limit, the economy is reduced to a preference-adaptation manifold. Nash
equilibrium remains a fixed-point method, but the game is the fast-adapted
preference game. Darwinian selection remains an update operator, but it selects
over whatever variables remain heterogeneous after fast closure. Welfare
analysis cannot rely on final preferences alone.

The next version should prove the reduction theorem, formalize the invariance
condition for material Nash predictions, and sharpen the long-run survival
frontier. If those results are clean, the paper can be positioned as a
mathematical economics account of what remains invariant when utility is no
longer slow.

## References To Integrate

Adomavicius, G., Bockstedt, J. C., Curley, S. P., and Zhang, J. "Do Recommender
Systems Manipulate Consumer Preferences? A Study of Anchoring Effects."
Information Systems Research, 2013.

Allcott, H., Braghieri, L., Eichmeyer, S., and Gentzkow, M. "The Welfare
Effects of Social Media." American Economic Review, 2020.

Ashton, H., and Franklin, M. "Solutions to Preference Manipulation in
Recommender Systems Require Knowledge of Meta-Preferences." arXiv, 2022.

Becker, G. S., and Murphy, K. M. "A Theory of Rational Addiction." Journal of
Political Economy, 1988.

Bernheim, B. D., Braghieri, L., Martinez-Marquina, A., and Zuckerman, D. "A
Theory of Chosen Preferences." American Economic Review, 2021.

Bisin, A., and Verdier, T. "The Economics of Cultural Transmission and the
Dynamics of Preferences." Journal of Economic Theory, 2001.

Bowles, S. "Endogenous Preferences: The Cultural Consequences of Markets and
Other Economic Institutions." Journal of Economic Literature, 1998.

Dekel, E., Ely, J. C., and Yilankaya, O. "Evolution of Preferences." Review of
Economic Studies, 2007.

Ely, J. C., and Yilankaya, O. "Nash Equilibrium and the Evolution of
Preferences." Journal of Economic Theory, 2001.

Fenichel, N. "Geometric Singular Perturbation Theory for Ordinary Differential
Equations." Journal of Differential Equations, 1979.

Franklin, M., Ashton, H., Gorman, R., and Armstrong, S. "Recognising the
Importance of Preference Change." arXiv, 2022.

Guess, A. M. et al. "How Do Social Media Feed Algorithms Affect Attitudes and
Behavior in an Election Campaign?" Science, 2023.

Hamaker, E. L., Kuiper, R. M., and Grasman, R. P. P. P. "A Critique of the
Cross-Lagged Panel Model." Psychological Methods, 2015.

Heifetz, A., Shannon, C., and Spiegel, Y. "The Dynamic Evolution of
Preferences." Economic Theory, 2007.

Jiang, R., Chiappa, S., Lattimore, T., Gyorgy, A., and Kohli, P. "Degenerate
Feedback Loops in Recommender Systems." AIES, 2019.

Khosrowi, D., and Beck, L. "Like It or Not: Recommender Systems Lack a Coherent
Normative Foundation." FAccT, forthcoming.

Kleinberg, J., Mullainathan, S., and Raghavan, M. "The Challenge of
Understanding What Users Want: Inconsistent Preferences and Engagement
Optimization." Management Science, 2024.

Lachaab, M., Ansari, A., Jedidi, K., and Trabelsi, A. "Modeling Preference
Evolution in Discrete Choice Models: A Bayesian State-Space Approach."
Quantitative Marketing and Economics, 2006.

Robson, A. J., Whitehead, L. A., and Robalino, N. "Adaptive Utility." Journal
of Economic Behavior and Organization, 2023.

Sandholm, W. H. "Preference Evolution, Two-Speed Dynamics, and Rapid Social
Change." Review of Economic Dynamics, 2001.

Stigler, G. J., and Becker, G. S. "De Gustibus Non Est Disputandum." American
Economic Review, 1977.

von Weizsaecker, C. C. "Freedom, Wealth and Adaptive Preferences." Working
paper, 2013.
