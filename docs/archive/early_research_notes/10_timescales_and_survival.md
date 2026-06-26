# Timescales And Long-Run Survival

## Correction

Nash equilibrium and Darwinian selection are not conclusions. They are methods
or operators.

The correct question is:

```text
After fast preference closure, what state space do Nash fixed points and
Darwinian selection act on?
```

In the `T_pref -> 0` limit, the preference state is pinned by:

```text
theta = Phi(z, m)
```

when the fast subsystem has a unique attracting branch. Nash equilibrium is then
computed in the reduced game induced by `Phi`, and selection acts on whatever
remains heterogeneous.

## Do Not Assume The Other Clocks

The previous note sometimes spoke as if population and institutions were slower
than preference adaptation. That is only one case. The empirical version should
estimate or bound the following timescales:

```text
T_pref          preference or latent-taste adjustment
T_action        behavioral best-response or learning
T_algorithm     recommendation or institutional-rule update
T_population    demography, survival, entry, exit, fertility, attrition
T_culture       imitation, education, family transmission, norm diffusion
```

The limiting exercise fixes:

```text
T_pref -> 0
```

but leaves the ratios:

```text
T_algorithm / T_population
T_action / T_population
T_culture / T_population
```

as parameters.

## Empirical Estimation

A minimal reduced-form estimate uses a latent or observed state `y_t`:

```text
y_{t+1} = alpha + rho y_t + beta exposure_t + error_t
speed = -log(rho) / Delta t
half_life = log(2) / speed
```

This is only a first pass. Serious empirical work should use:

- state-space discrete-choice models for preference parameters;
- latent transition models for type movement;
- random-intercept panel models to separate within-person change from stable
  heterogeneity;
- event studies or randomized feed/deactivation experiments to identify
  algorithmic exposure effects;
- survival or hazard models for population, exit, fertility, or attrition.

Relevant literature includes Lachaab et al. on Bayesian state-space preference
evolution, Hamaker et al. on random-intercept cross-lagged panel models, Allcott
et al. on social-media deactivation, and Guess et al. on algorithmic-feed
experiments.

## Short, Medium, And Long Run

### Short Run

Preferences close instantly:

```text
theta_t = Phi(z_t, m_t)
```

Local behavior is a Nash or best-response object in the fast-adapted preference
game.

### Medium Run

Institutional and population speeds matter. A myopic institution may change
`m_t` quickly or slowly. Population may respond slowly through fertility or
rapidly through exit, attrition, mortality, or collapse.

No timescale ordering should be assumed here.

### Long Run

The survival question is:

```text
Which adaptation laws or institutions induce nonnegative long-run growth after
fast preference closure?
```

The answer can be:

```text
none
```

If all admissible institutions induce preference attractors with negative
material growth, then the model predicts extinction of the system rather than
selection of a stable preference type.

## Model Variant Results

The script:

```bash
python3 scripts/run_timescale_variants.py
```

tests:

- slow institutions and slow population;
- fast institutions and slow population;
- slow institutions and fast population;
- all-fast myopic institutions;
- all-fast survival-aware institutions;
- fixed-rule survival frontiers.

Current calibration:

- `m = 0.05` induces `theta = 0.50` and survives.
- `m = 0.80` induces `theta ~= 0.94` and goes extinct.
- myopic institutions select exposure around `m = 0.645`, induce
  `theta ~= 0.928`, and go extinct under every tested institution/population
  speed ordering.
- survival-aware institutions select `m = 0.030`, induce `theta = 0.375`, and
  survive.

This is not yet a theorem. It is a useful warning: the long-run object selected
by Darwinian logic may be the adaptation law or institution, not a utility
function.
