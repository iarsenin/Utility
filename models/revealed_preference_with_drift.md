# Revealed Preference With Drifting Tastes

## Purpose

This model connects the theory to observable choice data. Standard revealed-preference tests ask whether a finite dataset can be rationalized by one stable preference relation. Here we ask whether it can be rationalized by a bounded sequence of local preferences.

## Standard Data

Observed:

```text
{(p_t, x_t)}_{t=1}^T
```

where `p_t` are prices and `x_t` are chosen bundles.

Standard revealed preference asks whether there exists `u` such that:

```text
x_t in argmax {u(x): p_t x <= p_t x_t}
```

## Endogenous-Preference Version

Let:

```text
u_t(x) = u(x; theta_t)
```

and impose bounded drift:

```text
theta_{t+1} in Gamma(theta_t, exposure_t)
```

The revealed-preference question becomes:

```text
Does there exist a theta path satisfying Gamma
such that every observed choice is locally utility-maximizing?
```

## Why This Matters

If `Gamma` is unrestricted, almost any finite dataset can be rationalized by changing preferences. If `Gamma` is too restrictive, the model collapses back to stable preferences.

The empirical content is in the transition restriction.

## Candidate Definition: K-GARP

A dataset satisfies `K-GARP` if there exists a preference-state path `{theta_t}` such that:

1. each choice satisfies the local revealed-preference inequalities for `u(., theta_t)`;
2. each transition is feasible under `K` or `Gamma`;
3. exposure variables explain transition direction better than price/budget changes alone.

## Expected Result

The project can show a trilemma:

```text
unrestricted preference drift -> no empirical content
fixed preferences -> too rigid for algorithmic environments
bounded transition laws -> testable middle ground
```

This may become an applied/theory follow-up paper.
