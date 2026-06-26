# Round 4 Modeller Memo

Role: exacting modeller. Objective: protect the paper from overclaiming and make the formal core harder to misunderstand.

## Bottom Line

The current article has a coherent central object:

```text
closure law ell -> fast preference state theta_ell^*(E)
                 -> reduced subjective game Gamma_ell^*(E)
                 -> Nash set / selection rule sigma_ell(E)
                 -> material evaluator G_ell(E)
```

This is the right backbone. The main correction from this pass is that the computational "best-response invariance" diagnostic was weaker than Proposition 1: it checked agreement at pure opponent actions, while the proposition is stated over all mixed opponent profiles. I added an all-mixed diagnostic to the model-selection audit. The stricter result strengthens the paper: random strategic closure preserves mixed best-response correspondences in only `0.0762` of games, compared with `0.3126` under the old pure-action endpoint check.

## 1. Theorem Statements That Need Sharpening

### Lemma 1: fast closure

Keep the current version as a fixed-slow-state closure lemma. Do not present it as a full singular perturbation theorem for moving slow states.

For a publishable theorem, the moving-state version would need something like:

```text
E in compact set, ell in finite or compact admissible set,
H(theta; E, ell) has a unique globally attracting root theta_ell^*(E),
attraction is uniform in (E, ell),
theta_ell^*(E) is continuous, and the slow state moves on an O(1) clock.
```

Then equilibrium analysis after the boundary layer is conducted in `Gamma_ell^*(E)`. Without these uniformity assumptions, the fixed-state lemma is defensible but intentionally local.

### Proposition 1: Nash invariance

The proposition is formally correct if "best response" means the mixed best-response correspondence for every `x_-i in X_-i`. The article should define expected payoffs explicitly before the proposition:

```text
bar U_i(x_i,x_-i; E,ell)
  = sum_{a in A} x(a) U_i(a; theta_{i,ell}^*(E), E, ell)

bar pi_i(x_i,x_-i; E,ell)
  = sum_{a in A} x(a) pi_i(a; E, ell)
```

Then write `BR_i^*(x_-i;E,ell)` and `BR_i^pi(x_-i;E,ell)` using these expected payoff functions. This avoids ambiguity between pure-action utility notation and mixed-strategy optimization.

The stress-test code now matches this theorem: `br_invariance_rate` is the all-mixed rate, while `pure_br_invariance_rate` is preserved only as a weaker diagnostic.

### Theorem 1: selection target shift

The theorem should be stated over a finite active set `L_0 subset L`, not all of `L`, because the replicator equation is written over a finite share vector. Also separate three claims:

1. Initial preference heterogeneity is erased within a common basin of a common closure law.
2. Selection over initial preference states is therefore degenerate in the `T_theta -> 0` limit.
3. Selection remains meaningful over closure laws, resistance parameters, institutions, or any variable that changes `theta_ell^*(E)` or `G_ell(E)`.

This avoids the accidental impression that Darwinian selection has become weak or irrelevant. It has not. Its target changed.

### Proposition 2: proxy alignment

This is logically sound but almost tautological. It should be renamed "Alignment Lemma" unless the article adds a sharper comparative-static result. The useful content is not the inclusion condition itself; it is the finite-game audit showing that aligned, independent, and misaligned proxies have sharply different material-loss rates.

## 2. Variables And Mixed-Strategy Notation

The core variables are mostly intuitive:

- `E`: slow material environment.
- `ell`: closure law.
- `theta`: preference state.
- `Gamma_ell^*(E)`: reduced subjective game.
- `sigma_ell(E)`: equilibrium-selection map.
- `G_ell(E)`: post-equilibrium material evaluator.

Two notational issues remain:

- Platform rule `I` conflicts visually with empirical internet exposure `I_{c,t}`. I recommend renaming the platform rule to `r in R` or `q in Q`, and reserving `D_{c,t}` or `Net_{c,t}` for internet exposure.
- The article should avoid saying "rank preservation" as if pure-action ranking is enough. The formal condition is preservation of mixed best-response correspondences over all `x_-i`. In two-action games this means the sign of each player's expected action-difference affine function agrees for every opponent mixing probability.

For the two-action audit, player `i`'s best response depends on an affine difference:

```text
D_i(q) = expected payoff from action 0 - expected payoff from action 1,
```

where `q` is the opponent's probability of action 0. Full mixed best-response invariance requires:

```text
sign D_i^*(q) = sign D_i^pi(q) for all q in [0,1] and all players i.
```

Checking only `q=0` and `q=1` is insufficient because the crossing point can move inside the interval.

## 3. Evidence To Add Or Reframe

### Updated model evidence

I added an exact all-mixed best-response diagnostic to the finite-game audit. New summary:

```text
neutral_control: mixed BR invariance = 1.0000, equilibrium shift = 0.0000
strategic_random_distortion: mixed BR invariance = 0.0762, pure endpoint invariance = 0.3126, equilibrium shift = 0.5044
proxy_aligned: material loss = 0.0432
proxy_independent: material loss = 0.5758
proxy_misaligned: material loss = 0.9706
```

This is a stronger result than the article currently reports. The article's finite-game table should replace `0.3126` with `0.0762` for full best-response invariance, while optionally mentioning `0.3126` as the weaker pure-endpoint check.

### Empirical evidence

The WDI section is best framed as "empirical discipline" or "calibration target," not as empirical fit to the platform model. It does not observe preference states, recommender exposure, AI mediation, individual behavior, or platform objectives. Its useful role is narrower:

```text
Digital exposure proxies move on measurable timescales.
Material and demographic variables move on measurable timescales.
Exposure-outcome associations can be estimated instead of assumed.
```

For a publication version, WDI should be demoted to a macro diagnostic unless augmented with more direct data: individual panels, deactivation experiments, feed-ranking experiments, time-use panels, adolescent mental-health panels, fertility/relationship data, or repeated preference elicitation.

## 4. Three Concrete Revisions For The Writer

1. Update the finite-game section and table to distinguish all-mixed best-response invariance from pure-endpoint invariance. Use `0.0762` as the theorem-aligned rate; do not call `0.3126` full best-response invariance.

2. Rewrite the formal notation just before Proposition 1 with explicit expected payoff functions `bar U_i` and `bar pi_i`. Then state the proposition in terms of equality of correspondences on `X_-i`, not "rank preservation" in informal language.

3. Rename the platform choice variable away from `I`, because the empirical section also uses `I_{c,t}` for internet adoption. My preferred convention: `r in R` for platform rule and `D_{c,t}` for digital exposure. This small change will remove a real source of reader confusion.

## Files Changed By Modeller

- `src/utility_endogenous/model_selection_audit.py`
- `scripts/run_model_selection_audit.py`
- `results/model_selection_audit_report.md`
- `results/tables/model_selection_summary.csv`
- `docs/agent_rounds/round_4_modeller.md`
