# Axioms v0: Dynamic Endogenous Utility

## Primitive Objects

Let:

- `X` be an outcome or consumption space.
- `A_i` be the action set of agent `i`.
- `Theta_i` be the preference-state space of agent `i`.
- `M` be the institutional or media environment.
- `U_i(x, a, theta_i)` be current subjective utility.
- `F_i(x, a, theta, M)` be material, reproductive, or survival fitness.
- `K_i(d theta_i' | theta_i, a_i, a_-i, x, M)` be the preference-transition kernel.

The static utility-function primitive is replaced by:

```text
(U_i, Theta_i, K_i, F_i)
```

## Axiom 1: Local Utility Representation

At each date `t`, conditional on preference state `theta_i,t`, agent `i` has complete and transitive preferences over feasible current acts. Under the usual continuity or expected-utility restrictions, there exists a local utility representation:

```text
U_i,t = U_i(., theta_i,t)
```

The utility function is therefore locally valid but globally moving.

## Axiom 2: Preference-State Transition

Preferences evolve according to a transition kernel:

```text
theta_i,t+1 ~ K_i(. | theta_i,t, a_i,t, a_-i,t, x_t, M_t)
```

The transition law may depend on consumption, peers, institutions, media exposure, AI systems, habits, and shocks.

Static preference theory is the special case:

```text
K_i(theta_i,t+1 = theta_i,t) = 1
```

## Axiom 3: Subjective Choice

Agents choose actions using current subjective preferences:

```text
a_i,t in argmax_{a_i in A_i} E_t[U_i(x_t, a_i, a_-i, theta_i,t)]
```

This axiom preserves ordinary maximization, but only locally.

## Axiom 4: Selection by Fitness

Preference states may be selected by a criterion not identical to current subjective utility. For a population measure `mu_t` over `Theta`, the replicator-mutator form is:

```text
mu_{t+1}(B) =
  integral_Theta K(B | theta, a(theta), M_t) F(theta, a(theta), M_t) mu_t(d theta)
  / integral_Theta F(theta, a(theta), M_t) mu_t(d theta)
```

This separates:

- what agents want,
- what survives,
- what platforms or institutions optimize.

## Axiom 5: Endogenous-Preference Equilibrium

An endogenous-preference equilibrium is a tuple:

```text
(sigma, m, {mu_t}_{t >= 0})
```

such that:

1. agents best respond according to `U(., theta_t)`;
2. institutional or platform policies `m` are optimal for their objective, if such actors exist;
3. the population law `mu_t` evolves under the induced selection-transition operator.

The equilibrium object is not merely a profile of actions. It includes the law of taste change.

## Axiom 6: Extended Welfare Domain

Welfare comparisons must be made over extended paths:

```text
{x_t, a_t, theta_t, M_t}_{t >= 0}
```

not over allocation paths alone.

Without this extension, a mechanism can change the utility functions used to evaluate itself.

## Conjecture 1: Preference Laundering

If a planner or platform can choose `K` at sufficiently low cost, then final-preference Pareto comparisons are not invariant. For many allocations `x` and `y`, one can construct a transition law that makes agents at `theta'` rank `y` over `x`, even if their initial `theta` ranked `x` over `y`.

Implication: Pareto efficiency must be indexed by either initial preferences, admissible preference transitions, meta-preferences, or an external constitutional criterion.

## Conjecture 2: Fitness-Utility Inversion

Suppose `theta` increases current subjective satisfaction from an artificial or online good, but decreases reproductive or material fitness. If the transition speed toward high `theta` exceeds the strength of selection against it, average subjective utility can rise while average fitness falls.

This is the core bizarre-but-solid possibility:

```text
d E[U_t] / dt > 0
and
d E[F_t] / dt < 0
```

## Conjecture 3: Nash Is Incomplete

When preference states are endogenous, a Nash equilibrium of actions can be dynamically unstable because the transition kernel changes the future game. The natural fixed point is a Nash equilibrium of the expanded game where strategies include preference-transition policies.
