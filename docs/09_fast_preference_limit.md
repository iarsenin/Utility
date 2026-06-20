# Fast Preference Limit

## Motivation

This note deliberately backs away from the platform-specific framing. The
mathematical question is:

```text
What remains of Nash equilibrium, Darwinian selection, and welfare when utility
functions adapt infinitely fast?
```

Let `T` be the preference-adaptation timescale. The limit of interest is:

```text
T -> 0
```

relative to the timescale of resources, population turnover, institutions, and
biological or material selection.

## Literature Position

This is related to, but not the same as, several established literatures.

### Indirect Evolutionary Preferences

Ely and Yilankaya, Dekel, Ely, and Yilankaya, Heifetz-Shannon-Spiegel, and
Sandholm study preferences as traits selected by material payoffs. The standard
logic is:

```text
subjective preferences -> behavior -> material payoff -> preference-type growth
```

Sandholm's two-speed model is especially close because behavior adjusts quickly
while natural selection slowly reshapes preference distributions. Our proposed
limit is different:

```text
preference adaptation is itself fast
```

If preferences are instantly reset by experience, institutions, or an adaptive
utility law, then Darwinian selection may no longer act on preferences directly.
It acts on slower objects: adaptation rules, institutions, platform policies,
biological types that resist adaptation, or population size.

### Adaptive Utility

Robson, Whitehead, and Robalino model real-time adaptation of utility under
limited discriminative capacity. This is relevant because utility is treated as
an adaptive coding device rather than as a fixed taste primitive.

### Adaptive Preferences And Welfare

Von Weizsaecker's adaptive-preferences program asks when welfare economics can
survive endogenous preferences. The useful connection is acyclicity: if
preference adaptation generates non-circular improvement paths, one can recover
a quasi-utility over paths. If not, final preferences alone are not enough.

### Singular Perturbation Theory

The mathematical template is a slow-fast system:

```text
T d theta / dt = G(theta, z, a, m)
d z / dt = H(z, theta, a, m)
a in BR(theta, z, m)
```

where:

- `theta` is the preference state;
- `z` is the slow economic or population state;
- `a` is an action or Nash profile induced by current preferences;
- `m` is an institution, environment, or platform rule.

The limit `T -> 0` imposes:

```text
G(theta, z, a, m) = 0
```

If this critical set has a unique attracting branch:

```text
theta = Phi(z, m)
```

then the reduced economy is:

```text
d z / dt = H(z, Phi(z, m), BR(Phi(z, m), z, m), m)
```

That is the central reduction.

## Limit Axioms

### Axiom F1: Fast Preference Closure

For each slow state `(z, m)`, the fast preference subsystem has an attracting
invariant set:

```text
A(z, m) = {theta : G(theta, z, BR(theta, z, m), m) = 0}
```

### Axiom F2: Local Choice Still Holds

At each instant, agents choose actions that are locally optimal under their
current preference state:

```text
a in BR(theta, z, m)
```

This preserves Nash-style reasoning, but only on the fast-adapted preference
state.

### Axiom F3: Slow Selection Acts After Fast Closure

Material or Darwinian selection evaluates the action induced by the fast
preference state:

```text
fitness = F(z, Phi(z, m), BR(Phi(z, m), z, m), m)
```

Selection does not get to choose among preference states if the fast subsystem
has already collapsed them to `Phi(z, m)`.

### Axiom F4: Welfare Domain Must Include the Transition Law

Because final preferences are produced by the path, welfare cannot be a function
only of final allocations and final preferences. The welfare domain must include
at least:

```text
(z_t, theta_t, m_t, K_t, a_t)_{t >= 0}
```

## Candidate Results

### Result 1: Attractor Replacement

If `A(z, m)` is a singleton `Phi(z, m)` and globally attracting, utility is no
longer a primitive state variable in the slow economy. It is replaced by the
fast-response map:

```text
U_t(.) = U(.; Phi(z_t, m_t))
```

This result is invariant to the specific cardinal form of `U`, as long as local
choices are represented by a preference state and the fast subsystem is
contractive.

### Result 2: Darwinian Selection Loses Its Preference Target

In the ordinary indirect evolutionary approach, preference types survive because
they induce fitness-improving behavior. In the fast limit with a unique
attractor, all types are reset to the same adapted preference state before slow
selection acts.

Therefore:

```text
selection over theta disappears
```

and is replaced by:

```text
selection over adaptation laws, institutions, or biological resistance to adaptation
```

This is the most interesting extreme conclusion so far.

### Result 3: Material Nash Need Not Survive

In the material Prisoner's Dilemma, universal defection is the Nash prediction.
But if preferences adapt instantly to a prosocial state, the action profile can
be cooperative even though cooperation is not a Nash equilibrium of the material
payoff game.

What survives is weaker:

```text
actions are Nash with respect to fast-adapted preferences
```

not:

```text
actions are Nash with respect to material payoffs
```

### Result 4: Final-Preference Pareto Becomes Too Weak

If preferences instantly adapt to the reached state, then a path can create the
preferences that later endorse it. Final-preference welfare can therefore become
path-validating.

The invariant welfare objects are instead:

- initial preferences;
- meta-preferences over preference changes;
- material or biological fitness;
- constitutional constraints on admissible transition laws;
- welfare over whole allocation-preference paths.

### Result 5: Multi-Attractor Cases Become Basin Economics

If the fast subsystem has multiple attractors:

```text
A(z, m) = {theta_1, ..., theta_k}
```

then the slow economy is not summarized by one utility function. It becomes a
basin-selection problem. Small changes in institutions or initial conditions can
move the economy to different preference manifolds.

This is likely where discontinuities, hysteresis, and "rapid social change"
enter.

### Result 6: Cyclic Fast Preferences Destroy Static Utility

If the fast subsystem has a limit cycle or chaotic invariant measure rather than
a fixed attractor, then the slow economy sees:

```text
theta ~ invariant_measure(z, m)
```

not a stable utility function. In that case, expected behavior over the fast
cycle may be well-defined while instantaneous welfare is not.

## Numerical Readout From Current Models

The script:

```bash
python3 scripts/run_fast_limit.py
```

writes:

- `results/fast_preference_limit_report.md`
- `results/tables/fast_limit_taste.csv`
- `results/tables/fast_limit_social.csv`
- `results/tables/fast_limit_platform.csv`

Main findings:

- Strong taste adaptation has fast attractor `theta ~= 0.9615`; the finite
  AI-speed model already converges to the same value.
- Varying selection strength from `0.20` to `5.00` leaves the fast attractor
  unchanged; only realized fitness changes.
- In the Prisoner's Dilemma model, fast prosocial adaptation produces full
  cooperation, while fast conflict adaptation produces defection.
- In the platform model, the fast-limit result depends critically on how
  autonomy or transition cost scales:
  - if only steady-state transition costs matter, transition penalties vanish
    after the boundary layer;
  - if the boundary-layer jump itself is penalized, strong guardrails can block
    capture;
  - if speed-squared costs scale as `1/T`, any nonzero instantaneous jump has
    infinite cost, making preferences effectively rigid.

## Research Repositioning

The platform-control model should now be treated as one application of a more
general singular-limit program.

Better first-paper spine:

```text
The Singular Limit of Endogenous Utility
```

or:

```text
When Utility Adapts Faster Than Selection
```

Possible core theorem:

```text
In an endogenous-preference economy with a globally attracting fast preference
subsystem, the slow equilibrium is determined by the critical manifold of
preference adaptation. Darwinian selection over preference states and material
Nash equilibrium survive only under additional invariance conditions.
```

The next technical target is to prove this theorem cleanly for a finite action
game with continuous one-dimensional preference state, then extend to
multi-attractor and platform-controlled cases.
