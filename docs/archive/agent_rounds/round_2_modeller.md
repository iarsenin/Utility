# Round 2 Modeller Review

Date: 2026-06-20

Scope: read-only review of `paper/article_v1.html`, the model-selection audit,
the WDI empirical pipeline, and generated tables/figures. I did not edit the
article, code, data, tables, or figures.

## Bottom Line

The paper's central conditional claim is scientifically sound: fast preference
closure changes the subjective game; material harm is not implied by speed
alone and depends on alignment between the preference-generating operator and
material evaluation. The finite-game audit and WDI diagnostic are useful support
devices if framed as diagnostics, not proofs.

Before publication, the manuscript needs sharper theorem assumptions, tighter
notation for the empirical regression, and clearer captions for mixed-metric
figures. No fatal contradiction appeared in the generated tables I checked.

## Must-Fix Before Publication

1. **Theorem 1 is currently a reduction lemma, not a full singular-perturbation
   theorem.** The statement fixes `(E,I)` and assumes a unique globally
   attracting fixed point of `T_theta dot theta_i = F_i(theta_i;E,I)`. That is
   enough for a pointwise closure claim after an initial layer. It is not enough
   for a general singular-limit theorem with moving slow variables. Either:
   add compactness/smoothness, uniform attraction, continuity of
   `theta^star(E,I)`, and a slow law for `(E,I)`, or rename this as a fast
   closure/reduction lemma for fixed slow states.

2. **Preference dynamics are written as player-separable.** The formal dynamic
   uses `F_i(theta_i;E,I)`, but platform and social mechanisms may produce
   coupled preference states. If the theorem is meant to cover the generic
   finite-game route, write the fast subsystem as
   `T_theta dot theta = F(theta;E,I)` with a unique attracting vector
   `theta^star(E,I)`. The current separable form is acceptable only as a
   simplifying assumption.

3. **Proposition 2's converse is under-specified.** The sufficient direction is
   correct: identical best-response correspondences imply identical Nash sets.
   The converse is false for a single fixed game because best responses can
   differ off equilibrium while Nash sets coincide. The manuscript says
   "robust equality across perturbations," which is the right idea, but it must
   be formalized: define the perturbation class or state only the sufficient
   condition plus a generic/off-path warning.

4. **Proposition 4 needs tie discipline.** If `V` and `G` rank all feasible
   environments in the same strict order, proxy maximizers are material
   maximizers. With weak rankings or ties, `G(I^V)=G(I^G)` need not hold for
   arbitrary selections from `argmax V`. State one of: strict ordinal
   equivalence, `argmax V subset argmax G`, or tie-breaking that selects a
   material maximizer.

5. **Proposition 5 is too vague as a theorem.** "Sufficiently rich
   preference-state space" and "ranked differently by initial preferences,
   final preferences, material payoff, and path/meta-preference criteria" need
   a constructive example or formal assumptions. Otherwise demote it to a
   proposition-by-example or an observation about welfare-domain
   non-invariance.

6. **The empirical regression notation must define the horizon exactly.** In
   `src/utility_endogenous/empirical_wdi.py`, the response is computed from
   `t-1` to `t+h` and divided by `h+1`. Thus table horizon `h=0` is a one-year
   annualized change from `t-1` to `t`, not a zero-length contemporaneous
   response. The manuscript equation should explicitly define
   `Delta_h y_ct = (y_c,t+h - y_c,t-1)/(h+1)` or the log analogue.

7. **Scale the internet-change regressor in notation.** The code uses
   `(I_ct - I_c,t-1)/10`, so the coefficient is per 10 percentage-point jump.
   The equation should use a named scaled regressor, e.g.
   `dI10_ct = (I_ct - I_c,t-1)/10`, rather than plain `Delta I_ct`.

8. **Do not imply country fixed effects.** The WDI fit includes lag controls,
   year fixed effects, and country-clustered standard errors, but no country
   fixed effects. Calling it a first-difference panel diagnostic is acceptable
   because the dependent variable is differenced, but any claim that country
   levels are fully absorbed should be avoided.

9. **Figure 1 mixes metrics in one bar chart.** The first two bars display
   equilibrium-shift rates; the proxy bars display material-loss rates. This is
   defensible only if the caption says so explicitly, or the figure is split
   into two panels. The table is clearer than the figure.

## Sound Components

- The strategic irrelevance condition
  `U_i = alpha_i(a_-i) + beta_i pi_i`, `beta_i > 0`, correctly preserves
  conditional own-action rankings and hence best responses.
- The finite-game audit's neutral-control result is a valid sanity check:
  strategically irrelevant perturbations preserve best responses and selected
  equilibria in the implementation.
- The proxy audit supports the paper's conditional message. The aligned route
  has a low material-loss rate (`0.0432`), independent is intermediate
  (`0.5758`), and misaligned is high (`0.9706`). This is exactly the discipline
  the theory needs.
- The WDI coverage table is internally consistent with the manuscript:
  internet, mobile, GDP, life expectancy, and fertility run through 2024 in the
  pull; suicide mortality runs through 2021.
- The manuscript already gives the necessary identification warning: WDI
  aggregates do not observe preference states and the empirical section is not a
  causal platform estimate.

## Empirical Limits To State More Sharply

- The 10-90 traversal metric is based on each country's own observed range, not
  an invariant structural timescale. It is sensitive to endpoints, volatility,
  and crises.
- Internet gap half-life excludes declining annual pairs and late observations
  with less than five percentage points of remaining gap. The reported `19.70`
  years is conditional on usable rising annual pairs.
- Suicide mortality should not be used as a slow-state benchmark. The manuscript
  already notes volatility; keep that caveat wherever Figure 2 is discussed.
- The regression estimates are associations conditional on controls. Endogenous
  rollout, country-specific trends, policy shocks, wars, health shocks, and
  measurement changes remain first-order threats.
- Figure 3 uses separate vertical scales by outcome. This is fine, but the
  caption should warn that visual heights are not comparable across panels.
- Normal-approximation confidence intervals are acceptable for a diagnostic
  with many country clusters, but publication text should not overemphasize
  p-values.

## Nice-To-Have Improvements

- Add a short formal definition of a "closure law" and of the material evaluator
  `G_l`, including how `G_l` is selected when `NE(Gamma_l^star)` is
  multi-valued.
- State explicitly that ordinal preservation of own-action rankings is the
  general invariance condition; the affine formula is a convenient sufficient
  condition.
- Add a small constructive welfare example for Proposition 5 with two
  transitions and two terminal preference states.
- Report the full WDI alignment table in an appendix or linked CSV note, since
  the article table shows selected horizons while the figure includes
  `0,1,3,5`.
- Add sensitivity checks for WDI fits: region/income strata, country trends, and
  excluding crisis years such as 2020-2021.
- In the model-selection audit, label the equilibrium metric as "selected
  equilibrium distribution shift" rather than "Nash-set shift"; the code uses a
  pure-equilibrium selection convention and an L1 distance threshold.

## Concrete Equation Edits Recommended

Replace the empirical equation block with a version that defines the implemented
variables:

```text
dI10_ct = (I_ct - I_c,t-1) / 10

Delta_h y_ct =
  [Y_c,t+h - Y_c,t-1] / (h+1)
```

with `Y=log GDPpc` for GDP and `Y=y` for level outcomes. Then estimate:

```text
Delta_h y_ct = alpha + beta dI10_ct + gamma_1 I_c,t-1
             + gamma_2 log GDPpc_c,t-1 + gamma_3 y_c,t-1
             + lambda_t + error_ct.
```

For the GDP outcome, omit `gamma_3 y_c,t-1` because it is the same variable as
`log GDPpc_c,t-1`.

## Publication Readiness Judgment

The article is promising and mostly disciplined. The theory should be published
only after theorem statements are made commensurate with their assumptions. The
empirical section is suitable as a diagnostic appendix or motivating section,
provided the horizon notation, non-causal language, and figure captions are
tightened.
