# Timescale Variant Report

## Correction To Language

Nash equilibrium and Darwinian selection are methods/operators fixed
by the model. What changes in the infinite preference-velocity limit
is the state space to which those operators are applied.

Corrected statement:

```text
Nash fixed points are computed after fast preference closure.
Darwinian selection then acts on whatever variables remain heterogeneous:
population shares, adaptation laws, institutions, or biological resistance.
```

## Timescale Identification

Do not assume population or institutions are slower. Treat the speeds as
estimable quantities. For a measured latent state `y_t`, a first-pass
timescale estimate is the AR(1) half-life from:

```text
y_{t+1} = alpha + rho y_t + error_t
speed = -log(rho) / Delta t
half_life = log(2) / speed
```

Better empirical versions should use latent-state, dynamic discrete-choice,
or random-intercept panel models when observed choices are noisy proxies for
preferences.

Illustrative half-life estimates from synthetic paths:

| process | rho | continuous_speed | half_life |
| --- | --- | --- | --- |
| fast_preference_proxy | 0.3980 | 0.9212 | 0.7524 |
| slow_institution_proxy | 0.7809 | 0.2473 | 2.8031 |
| population_proxy | 0.7997 | 0.2235 | 3.1012 |

## Fixed-Rule Survival Frontier

In the instantaneous preference limit, a fixed institutional exposure `m`
induces `theta = m / (m + anchor)`. Long-run survival depends on the
material growth rate at that induced preference state.

The largest grid-tested exposure with nonnegative growth is `0.050`.

| fixed_exposure | theta | material_growth | survives_long_run | platform_flow_value |
| --- | --- | --- | --- | --- |
| 0.0000 | 0.0000 | 0.6700 | True | 0.0000 |
| 0.1250 | 0.7143 | -0.2586 | False | 0.7130 |
| 0.2500 | 0.8333 | -0.5175 | False | 0.8283 |
| 0.3750 | 0.8824 | -0.6328 | False | 0.8711 |
| 0.5000 | 0.9091 | -0.6978 | False | 0.8891 |
| 0.6250 | 0.9259 | -0.7395 | False | 0.8947 |
| 0.7500 | 0.9375 | -0.7685 | False | 0.8925 |
| 0.8750 | 0.9459 | -0.7898 | False | 0.8847 |
| 1.0000 | 0.9524 | -0.8062 | False | 0.8724 |

## Variant Outcomes

| scenario | institution_speed | population_speed | survival_weight | final_exposure | final_theta | mean_tail_growth | extinct_period | survives_long_run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fixed_survival_rule | 0.0000 | 0.2500 | 0.0000 | 0.0500 | 0.5000 | 0.1325 |  | True |
| fixed_capture_rule | 0.0000 | 0.2500 | 0.0000 | 0.8000 | 0.9412 | -0.7778 | 24 | False |
| slow_institution_slow_population_myopic | 0.0200 | 0.0500 | 0.0000 | 0.6138 | 0.9247 | -0.7364 | 146 | False |
| fast_institution_slow_population_myopic | 1.0000 | 0.0500 | 0.0000 | 0.6450 | 0.9281 | -0.7448 | 125 | False |
| slow_institution_fast_population_myopic | 0.0200 | 1.0000 | 0.0000 | 0.2314 | 0.8223 | -0.4923 | 18 | False |
| all_fast_myopic | 1.0000 | 1.0000 | 0.0000 | 0.6450 | 0.9281 | -0.7448 | 8 | False |
| all_fast_survival_aware | 1.0000 | 1.0000 | 0.7500 | 0.0300 | 0.3750 | 0.3161 |  | True |
| slow_institution_survival_aware | 0.0200 | 1.0000 | 0.7500 | 0.0300 | 0.3750 | 0.3160 |  | True |

Key comparison:

- all-fast myopic institutions end at theta `0.9281`
  and extinction period `8`.
- all-fast survival-aware institutions choose a lower exposure, end at
  theta `0.3750`, and survive.

## Interpretation

In the `T_pref -> 0` limit, short-run preferences are pinned by the fast
closure map. Medium-run outcomes depend on the measured speeds of
institutions and population dynamics. Long-run survival is determined by
the growth rate of the whole induced system, not by subjective utility
alone and not by material Nash predictions alone.

Thus the Darwinian question should be phrased as:

```text
Which adaptation laws or institutional regimes induce nonnegative long-run
growth after fast preference closure?
```

The answer can be none. If every admissible institution drives the fast
preference attractor into negative material growth, the model predicts
system extinction rather than a surviving preference type.
