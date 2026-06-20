# Model Inventory

## Model A: Algorithmic Taste Drift With Selection

Purpose: show how a standard consumption model changes when a taste parameter is a state variable.

Baseline utility:

```text
U(o, h; theta) = theta log(o) + (1 - theta) log(h)
```

where:

- `o` is online/artificial consumption,
- `h` is offline/human/social consumption,
- `theta in [0,1]` is taste for the online good.

With prices and income normalized to one:

```text
o*(theta) = theta
h*(theta) = 1 - theta
```

Endogenous preference law:

```text
theta_{t+1} = theta_t
  + eta [ algorithmic_field(theta_t, M_t) (1 - theta_t)
          - offline_anchor theta_t ]
```

Selection:

```text
population share(theta) grows with F(theta)
```

where high `theta` may reduce biological or social fitness even as it increases attention revenue.

## Model B: Indirect Evolutionary Prisoner's Dilemma

Purpose: rerun a standard indirect evolutionary model with mutable social preferences.

Material payoffs are the standard Prisoner's Dilemma:

```text
        C      D
C     3,3    0,5
D     5,0    1,1
```

Subjective utility type:

```text
U_i = pi_i + lambda_i pi_j + norm_bonus * 1{C}
```

where `lambda_i` is altruism or social preference. Agents choose actions from subjective utility. Types reproduce by material payoff. Institutions or algorithms can move `lambda_i`.

## Model C: Platform Preference-Control Game

Purpose: make AI/social-media mechanism explicit.

Actors:

- users with current preference state `theta`,
- a platform choosing exposure policy `m(theta)`,
- possible regulator or constitutional constraint on admissible `K`.

Platform objective:

```text
max_m E[attention(theta, m)] - cost(m)
```

User objective:

```text
max_a U(a, theta)
```

Population transition:

```text
mu_{t+1} = T(mu_t, m)
```

This is the next model to implement after the bootstrap.

## Model D: Overlapping-Generations Preference Transmission

Purpose: connect to cultural evolution.

Preference states are transmitted through parents, peers, teachers, media, and algorithms. AI enters as a high-bandwidth socialization technology.

Candidate law:

```text
theta_child = alpha theta_parent
            + beta theta_peer
            + gamma theta_algorithm
            + epsilon
```

The key comparative static is `gamma / generation_length`.

## Model E: Generic Finite-Game Fast Closure

Purpose: provide the core theorem route for the `T_P -> 0` limit without
building in a one-dimensional survival frontier.

Material game:

```text
pi_i(a; E, ell)
```

Fast preference closure:

```text
theta_ell^star(E)
```

Subjective game:

```text
Gamma_ell^star(E)
  = <N, {A_i}, {U_i(.; theta_{i,ell}^star(E), E, ell)}>
```

Reduced equilibrium:

```text
sigma_ell(E) in NE(Gamma_ell^star(E))
```

Material Nash predictions are invariant only when:

```text
BR_star(x_-i; E, ell) = BR_pi(x_-i; E, ell)
for every mixed opponent profile x_-i.
```

Status: promoted to the main theorem route after the model-selection audit in
`docs/11_model_selection_audit.md`. Platform control should be treated as the
main application of this finite-game core. The current article uses an explicit
equilibrium selector `sigma_ell(E)` and material evaluator `G_ell(E)` to handle
mixed equilibria and material comparison after closure.
