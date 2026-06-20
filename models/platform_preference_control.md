# Platform Preference-Control Model

## Purpose

This is the first "not so toy" model. It makes the social-media or AI actor explicit.

## Agents

There is a continuum of users with preference state:

```text
theta in [0, 1]
```

Interpretation:

- `theta = 0`: offline/human/social orientation.
- `theta = 1`: online/artificial/platform-mediated orientation.

Users choose consumption or attention allocation:

```text
a in [0, 1]
```

where `a` is time or expenditure directed to the platform-mediated good.

## User Utility

```text
u(a; theta) = theta log(a) + (1 - theta) log(1 - a)
```

The myopic best response is:

```text
a*(theta) = theta
```

## Platform Policy

The platform chooses exposure intensity:

```text
m in [0, m_bar]
```

or a state-contingent policy:

```text
m: [0, 1] -> [0, m_bar]
```

## Preference Transition

```text
theta' = theta + eta[m(theta)(1 - theta) - c theta] + epsilon
```

where:

- `eta` is preference plasticity,
- `c` is the offline anchor,
- `epsilon` is mutation/noise.

## Platform Objective

Candidate baseline:

```text
Pi(m, mu) = integral [a*(theta') + rho predictability(mu')] mu(d theta) - C(m)
```

Predictability can be proxied by negative entropy:

```text
predictability(mu) = -H(mu)
```

The platform may prefer a concentrated distribution even if users do not initially prefer concentration.

## Fitness

```text
F(theta) = exp(-s theta^2)
```

or a richer form:

```text
F(theta) = exp(s_0(1 - theta) - s_1 theta^2)
```

## Expected Result

If engagement returns to `theta` and predictability exceed the cost of exposure, the platform's optimal `m` pushes the population toward high `theta`. If `F` declines in high `theta`, then:

```text
Delta platform value > 0
Delta subjective local value >= 0
Delta fitness < 0
```

This is the cleanest place to formalize the paper's "satisfied by preferences it produced" mechanism.

## Next Implementation

1. Add `src/utility_endogenous/platform_control.py`.
2. Solve platform policy on a grid.
3. Produce phase diagrams for:
   - plasticity `eta`,
   - selection strength `s`,
   - exposure cost,
   - predictability return `rho`.
