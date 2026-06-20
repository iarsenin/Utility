# Round 5 Modeller Memo

Role: exacting modeller. Layer: formal scope, evidentiary support, hidden assumptions, and one minimal robustness improvement. I did not edit `paper/article_v1.html`.

## Bottom Line

The Pass 4 article repairs the main mixed-strategy notation problem. The finite-game section now uses the theorem-aligned mixed best-response diagnostic and distinguishes it from the weaker pure-endpoint check. That is a real improvement.

The next modelling improvement is not another toy model. It is a sharper formal bridge between the propositions and the computational evidence. The article should add a short corollary after Proposition 1: strategically irrelevant preference changes preserve mixed best responses and hence Nash sets. This turns the neutral control from a simulation detail into an exact benchmark.

I also added a sensitivity audit. It shows that the finite-game message is not a single-parameter artifact, but it also disciplines the claim: strategic closure changes games increasingly with distortion size; exact proxy alignment can shift equilibria while producing zero material loss.

## 1. Additional Formal Claim Or Proof Clarification

### Add Corollary 1: strategically irrelevant closure

The article currently gives strategic irrelevance in prose. It should be promoted to a corollary immediately after Proposition 1.

Suggested statement:

```text
Corollary. Suppose that for every player i there exist beta_i > 0 and
alpha_i(a_-i;E,ell), independent of a_i, such that

U_i(a_i,a_-i;theta_{i,ell}^*(E),E,ell)
  = alpha_i(a_-i;E,ell)
    + beta_i pi_i(a_i,a_-i;E,ell).

Then BR_{i,ell}^*(x_-i;E)=BR_{i,ell}^pi(x_-i;E) for every
x_-i in X_-i, and therefore NE(Gamma_ell^*(E))=NE(Gamma_ell^pi(E)).
```

Proof clarification:

```text
For fixed x_-i, the expected alpha_i term is constant in x_i, while
beta_i > 0 preserves the argmax of expected material payoff.
```

This matters because it proves the neutral control analytically. It also prevents the reader from interpreting "preference changes" as automatically behavior-changing.

### Add Corollary 2 or a sentence after Proposition 2: equilibrium movement is not material loss

The proxy-alignment result should explicitly distinguish two events:

```text
sigma_r(E) changes relative to the material benchmark
```

and

```text
G(r^G)-G(r^V)>0.
```

The sensitivity audit shows that under exact material alignment, equilibrium shifts occur in `0.3647` of games while material loss is `0.0000`. This is an important conceptual point: preference closure can move behavior without lowering the specified material evaluator if the choosing proxy remains aligned with that evaluator.

## 2. Do The Finite-Game Results Support The Central Claims?

Yes, with the right wording.

The stress test supports three claims:

1. Neutral preference motion is a sanity benchmark. It preserves mixed best responses and selected outcomes in the audit.
2. Strategic preference closure generically changes the reduced game. In the main audit, random strategic closure preserves all mixed best-response correspondences in only `0.0762` of games and shifts selected outcomes in `0.5044`.
3. Material harm is conditional on proxy alignment. Material loss is rare when the proxy is close to material welfare (`0.0432`) and common when independent (`0.5758`) or misaligned (`0.9706`).

The stress test does not support stronger claims:

- It does not prove that real platforms are misaligned.
- It does not prove that fast preference closure is usually harmful.
- It does not identify welfare unless the material evaluator is accepted.
- It does not remove dependence on equilibrium-selection conventions.

The new sensitivity audit supports the article's conditional phrasing. Strategic distortion scale results:

```text
scale 0.000: mixed BR invariance 1.0000, equilibrium shift 0.0000
scale 0.125: mixed BR invariance 0.2110, equilibrium shift 0.1087
scale 0.500: mixed BR invariance 0.1403, equilibrium shift 0.3630
scale 1.000: mixed BR invariance 0.0813, equilibrium shift 0.5177
scale 4.000: mixed BR invariance 0.0313, equilibrium shift 0.7153
```

Aligned proxy noise results:

```text
noise 0.000: material loss 0.0000, equilibrium shift 0.3647
noise 0.100: material loss 0.0147
noise 0.250: material loss 0.0470
noise 0.500: material loss 0.1093
noise 1.000: material loss 0.2853
noise 2.000: material loss 0.3990
```

These numbers make the paper more credible because they do not mechanically vindicate the dramatic story. They say: exact alignment protects material value; noisy alignment erodes protection; strategic distortions matter more as they become larger.

## 3. Hidden Assumptions To Name Explicitly

The paper should include a short "Maintained Assumptions" paragraph before Lemma 1 or at the start of the formal model.

Recommended assumptions:

1. Fast stable closure: for each fixed `(E,ell)`, the fast subsystem has a unique attracting fixed point `theta_ell^*(E)`. If there are multiple basins, the object is a closure correspondence, not a function.
2. Boundary-layer timing: `E` and `ell` are fixed during fast adjustment. The paper sends only `T_theta` to zero; it does not assume institutions, population, or algorithms are slower in reality.
3. State-only closure in the main theorem: `H(theta;E,ell)` does not depend on contemporaneous mixed actions. If it does, the reduced object becomes a joint fixed point in preferences and play.
4. Equilibrium selection for scalar evaluation: material comparisons use a selected equilibrium `sigma_ell(E)`. Set-valued Nash statements are selection-free; scalar welfare/material claims are not.
5. Exogenous material evaluator: `M` or `G` is not itself produced by the final preference state. If the evaluator is also endogenous, the welfare section needs a higher-order criterion.
6. Finite active selection set: the replicator equation is over `L_0`, a finite active set of closure laws with shares. Claims over infinite `L` require different existence and measurability assumptions.
7. Random-game audit scope: iid uniform payoffs are a stress test of logical structure, not an empirical distribution of platform environments.

## 4. Minimal Model/Result Improvement Made

I added a sensitivity audit:

- `scripts/run_model_selection_sensitivity.py`
- `results/model_selection_sensitivity_report.md`
- `results/tables/model_selection_sensitivity.csv`
- `results/figures/model_selection_sensitivity.svg`

The audit varies the strategic distortion scale and the noise in an otherwise material-aligned proxy. It materially improves the article because it shows the main results are comparative, not binary:

```text
strategic closure effect grows with distortion scale;
material loss grows as alignment deteriorates;
equilibrium shifts are not identical to material losses.
```

## Concrete Writer Instructions

1. Add the strategically irrelevant closure corollary after Proposition 1, using the expected-payoff proof above.
2. Add one paragraph in Section 6 using the sensitivity audit: "As distortion scale rises, mixed-BR invariance falls and outcome shifts rise; as proxy noise rises, material loss rises from zero." Keep it as robustness, not as a new main theorem.
3. Insert a "Maintained Assumptions" paragraph before Lemma 1. Do not bury unique closure, fixed boundary-layer timing, state-only closure, and equilibrium selection in prose.
4. In the platform section, explicitly say that equilibrium shifts are not necessarily material losses. Exact proxy alignment can move behavior while preserving the material criterion.
5. Keep the WDI section modest. It is empirical discipline and calibration scaffolding, not evidence that platforms produce preferences.

## Verification

- Ran `python3 scripts/run_model_selection_sensitivity.py`.
- Ran `python3 -m compileall -q src scripts`.
- Ran an HTML parser check on `paper/article_v1.html`.
