# Round 3 Modeller Review

Date: 2026-06-20

Scope: reviewed the latest `paper/article_v1.html` after the Round 2 editor
fixes and `docs/agent_rounds/round_2_editor.md`. I did not edit the article,
code, data, tables, or figures.

## Verdict

Round 3 largely passes the formal-consolidation test. The article now has one
coherent model spine:

```text
closure law ell
-> fast H dynamics
-> theta_ell^star(E)
-> reduced subjective game Gamma_ell^star(E)
-> equilibrium selection sigma_ell(E)
-> material evaluator G_ell(E)
-> selection over closure laws
-> platform proxy alignment as application
```

The previous notation conflict between `I` and `ell` is mostly resolved. The
paper now explicitly treats platform rules `I in mathcal I` as closure laws in
the general set `mathcal L`. The `H(theta;E,ell)` fast dynamic is vector-valued,
which is the correct repair for social/platform coupling, and the text now
properly says action-dependent closure is an extension.

There remains one real formal blocker before publication: the equilibrium set
is defined as a subset of pure action profiles even though finite games need not
have pure Nash equilibria and the stress test uses distributions/mixed
equilibria. A smaller formal assumption is also needed for the selection
equation over closure laws.

## Must-Fix Blockers

1. **Fix the Nash/equilibrium-selection domain.**

   Section 3 currently says:

   ```text
   For any finite game Gamma, let NE(Gamma) subseteq A denote its Nash
   equilibrium set.
   sigma_ell(E) in NE(Gamma_ell^star(E)).
   M: A x E x L -> R.
   ```

   This is not correct for general finite games. `A` is the set of pure action
   profiles, and pure Nash equilibria need not exist. The stress test already
   uses selected equilibrium distributions, mixed equilibria, and a uniform
   fallback. The formal model should therefore use mixed strategy profiles or
   distributions.

   Recommended repair:

   ```text
   Delta(A_i) = mixed strategies for player i
   X = product_i Delta(A_i)
   NE(Gamma) subseteq X
   sigma_ell(E) in NE(Gamma_ell^star(E))
   M: X x E x L -> R
   G_ell(E) = M(sigma_ell(E),E,ell)
   ```

   If the paper wants pure strategies only, it must explicitly assume existence
   of a selected pure equilibrium for every relevant `(E,ell)`. That route is
   less natural because the computational audit is already distribution-based.

2. **Specify the selection domain for the replicator equation.**

   The selection equation uses:

   ```text
   bar G(E) = sum_{k in L} n_k G_k(E).
   ```

   This requires `L` to be finite, countable with summable shares, or a finite
   active support. The simplest fix is: "For the selection equation, restrict to
   a finite set of closure laws with shares `n_ell >= 0` and
   `sum_ell n_ell = 1`." If `mathcal L` is meant to be continuous, replace the
   sum by an integral over a measure on laws.

## Component Assessment

### Closure Law And H Dynamics

Sound. The article now defines `E in mathcal E`, `ell in mathcal L`, and
`T_theta dot theta = H(theta;E,ell)`. The vector form is appropriate. The text
also correctly limits the lemma to action-independent closure and identifies
joint action-preference closure as an extension.

Residual risk: the platform motivation still evokes action feedback. The
current caveat is adequate, but the introduction should avoid implying that the
main theorem already solves a simultaneous action-preference fixed point.

### `theta_ell^star(E)` And Reduced Game

Sound, conditional on the stated unique globally attracting fixed point. The
notation `theta_ell^star(E)` and component `theta_{i,ell}^star(E)` are
internally consistent. Lemma 1 is correctly demoted to a fixed-slow-state
closure lemma, not a full singular perturbation theorem.

Residual risk: global attraction is strong. The limitations section flags
multi-basin closure appropriately.

### NE Set, `sigma_ell(E)`, And `G_ell(E)`

Structurally right but blocked by the pure-action-domain issue above. The idea
of adding an explicit equilibrium-selection map is the correct formal move.
Once `sigma_ell(E)` is defined over mixed strategy profiles and `M` evaluates
mixed profiles by expected material payoff or another specified criterion, this
part is internally consistent.

### Selection Target Shift Theorem

Sound after the domain fixes. The theorem now fixes `E`, `ell`, `sigma_ell(E)`,
and `M`, and states that initial preference-state heterogeneity is erased when
all initial states share the same unique closure. That is the correct theorem.

Residual risk: the theorem's final sentence about classes differing in `ell`
would be cleaner if the selection equation first specified a finite active set
of laws and a selection map for each law.

### Proxy Proposition

Sound. The condition

```text
argmax_I V(I) subseteq argmax_I G(I)
```

solves the tie problem. Strict ordinal equivalence is correctly presented as a
sufficient condition. The proposition now separates the formal claim from the
stress-test interpretation, which is the right separation.

Residual risk: if rankings differ on a fixed feasible set, loss is possible but
not necessary unless a proxy maximizer is materially inferior. The current
"there exist feasible sets" wording is acceptable.

### Finite-Game Stress Test

Substantially consistent with the code and generated tables. The article now
states the payoff distribution, equilibrium-selection convention,
distributional shift metric, `L1 > 0.25` threshold, proxy grid, and material-loss
definition. Figure 1 now explicitly says it mixes selected-equilibrium shift
rates and proxy material-loss rates.

Residual risk: the uniform fallback is a diagnostic convention, not generally a
Nash equilibrium. That is acceptable for a stress test, but the text should keep
calling it a selected distribution convention rather than a theoretical
equilibrium claim.

### WDI Measurement Section

Now internally consistent. The section defines:

```text
dI10_ct = (I_ct - I_c,t-1)/10
Delta_h y_ct = (Y_c,t+h - Y_c,t-1)/(h+1)
```

It also correctly states that `h=0` is a one-year change, that the regression
has no country fixed effects, and that the WDI exercise does not measure
platform-induced preference closure. The Figure 3 caption correctly warns that
panels have separate vertical scales.

Residual risks:

- The section title still includes "Alignment"; the body properly reframes the
  regression as exposure-outcome association.
- The lagged internet control appears as `I_c,t-1` in the equation, while the
  implementation uses it as a 0-1 share. This does not affect the reported
  coefficient on `dI10`, but the scale should be stated if the equation is
  made fully replicable.
- The 10-90 traversal metric remains an observed-range diagnostic, not a
  structural timescale.

## Publication Readiness Judgment

The formal model is now mostly internally consistent. The paper should not be
blocked on the closure-law notation, `H` dynamics, selection theorem, proxy
proposition, stress-test description, or WDI measurement language. Those pieces
now say approximately what the model can support.

Publication-quality consistency requires fixing the equilibrium domain and the
selection-law support assumption. After that, remaining issues are mainly
refinement risks: mixed-strategy notation, reference depth, and keeping the WDI
section visibly diagnostic rather than structural.
