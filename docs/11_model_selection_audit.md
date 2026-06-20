# Model Selection Audit

Date: 2026-06-20

## Question

Are the current models the best route for the `T_P -> 0` limit, or did we pick
models that make the conclusion too easy?

Short answer: the current models are useful, but not all should carry the paper.
The best core route is now a generic finite-game singular-limit model. The
platform-control model should become the main application, not the theorem
spine. The one-dimensional taste model is an exposition device.

## Current Model Selection

| Model | Strength | Weakness | Decision |
| --- | --- | --- | --- |
| One-dimensional taste drift | Transparent, easy to visualize, clean survival frontier. | The monotone link "higher platform taste lowers growth" is doing too much work. | Keep as exposition and phase diagram, not central proof. |
| Indirect evolutionary Prisoner's Dilemma | Strong bridge to indirect evolutionary preferences. | Too special; cooperation reversal is already familiar in preference-evolution work. | Keep as literature benchmark and sanity check. |
| Platform preference control | Novel application: institution chooses the preference-transition intensity. | Can collapse into "engagement is not welfare" unless the transition kernel is essential. | Keep as first application after the general theorem. |
| Cultural transmission / OLG | Natural long-run extension. | Generation-length dynamics are not the cleanest `T_P -> 0` laboratory. | Postpone until after the singular-limit theorem. |
| Revealed preference with drift | Empirically important and publishable later. | Tests identification more than the limiting theorem. | Keep as empirical appendix/future paper. |
| Generic finite-game fast closure | Closest to mathematical economics and indirect-evolution literature; avoids one-dimensional assumptions. | Less vivid; needs careful equilibrium-selection conventions. | Promote to core theorem route. |

## Literature Check

The closest economics route is not the recommender-systems literature by itself.
It is the indirect evolutionary preference literature, with the timescale
reversed.

- [Sandholm's two-speed model](https://ideas.repec.org/a/red/issued/v4y2001i3p637-679.html)
  studies strategic environments where behavior adjusts quickly while natural
  selection slowly changes preference distributions. That is the right
  mathematical neighborhood, but our fast variable is the preference state
  itself.
- [Ely and Yilankaya](https://ideas.repec.org/a/eee/jetheo/v97y2001i2p255-272.html),
  and [Dekel, Ely, and Yilankaya](https://cet.econ.northwestern.edu/dekel/pdf/evolution%20of-preferences.pdf)
  model subjective preferences separately from material fitness in finite
  normal-form games. That is the strongest reason to move the core theorem into
  finite games.
- [Heifetz, Shannon, and Spiegel](https://eml.berkeley.edu/~cshannon/wp/what.pdf)
  are an important warning: in generic games, payoff maximization is not
  automatically justified by evolutionary arguments. This supports our
  insistence on separating subjective utility, material payoff, and selection.
- [Kleinberg, Mullainathan, and Raghavan](https://arxiv.org/abs/2202.11776)
  are the closest platform-welfare threat: engagement optimization can move in
  directions that lower welfare. Our paper must therefore use the endogenous
  transition of future utility functions essentially, not merely restate
  "engagement is not welfare."
- [Jiang et al.](https://arxiv.org/abs/1902.10730) and
  [Chaney, Stewart, and Engelhardt](https://arxiv.org/abs/1710.11214) show that
  recommender systems can create feedback loops, degeneracy, homogenization, and
  lower utility. This motivates the platform application, but it does not
  replace a mathematical economics equilibrium theorem.
- [Bernheim et al.](https://www.aeaweb.org/articles?id=10.1257%2Faer.20190390)
  and [Robson-Whitehead-Robalino](https://www.sfu.ca/~robson/ROWHRO.pdf) are
  useful for microfounding chosen/adaptive preferences, but they do not by
  themselves answer the Nash-selection question in the singular limit.
- [Fenichel-style singular perturbation](https://www.scirp.org/reference/referencespapers?referenceid=2446734)
  is the correct mathematical template once we formulate a smooth version; in
  finite games the first theorem can be stated directly as fast closure of a
  correspondence.

## Non-Trivial Check

I added a route-agnostic stress test:

```bash
python3 scripts/run_model_selection_audit.py
```

It writes:

- `results/model_selection_audit_report.md`
- `results/tables/model_selection_summary.csv`
- `results/tables/model_selection_proxy_routes.csv`

The test generates 5,000 random two-player, two-action games per route. It then
treats fast preference closure as a payoff transformation and asks whether Nash
best responses, selected equilibria, and material outcomes change.

Summary:

| Route | Best-response invariance | Equilibrium shift | Material loss under proxy selection |
| --- | ---: | ---: | ---: |
| Neutral control | 1.0000 | 0.0000 | n/a |
| Random strategic distortion | 0.3126 | 0.5044 | n/a |
| Proxy aligned with material welfare | n/a | 0.3766 | 0.0432 |
| Proxy independent of material welfare | n/a | 0.7244 | 0.5758 |
| Proxy misaligned with material welfare | n/a | 0.9730 | 0.9706 |

This is a better check than our previous simulations because the bad result is
not automatic. If the preference-generating proxy is aligned with material
welfare, material loss becomes rare. If the proxy is independent or misaligned,
loss becomes common. The current one-dimensional platform model is therefore a
misalignment application, not a universal theorem.

## Revised Core Claim

The paper should not claim:

```text
Fast endogenous utility implies collapse.
```

The stronger and more defensible claim is:

```text
Fast preference closure generically changes the reduced game.
Whether this produces material harm depends on the alignment between the
preference-generating operator and material welfare.
Selection acts on adaptation laws, institutions, or induced systems after
closure, not on initial preference states.
```

## Revised Model Spine

### Core Theorem Model

Finite game with material payoffs `Pi_i(a)` and fast preference state `P`.

Fast closure:

```text
P = P^star(E, I).
```

Subjective payoff:

```text
U_i(a; P^star(E, I), I).
```

Reduced equilibrium:

```text
a in NE(U(P^star(E, I), I)).
```

Material Nash invariance condition:

```text
BR_U(P^star(E, I), E, I) = BR_Pi(E, I).
```

Selection over adaptation laws:

```text
j -> P_j^star(E, I) -> NE(U(P_j^star)) -> G_j.
```

### Application Model

Platform-controlled preference transition. The platform or institution chooses
an adaptation law or proxy. The empirical and policy question becomes whether
the proxy is aligned, independent, or misaligned with material welfare.

### Exposition Models

Use the one-dimensional taste model and the Prisoner's Dilemma only after the
general theorem, as examples of the mechanism.

## Proof Targets

1. Fast finite-game closure: define the reduced game induced by `P^star`.
2. Nash invariance: material and fast-adapted subjective Nash sets coincide if
   and only if best-response correspondences coincide.
3. Generic object shift: payoff transformations that are not strategically
   irrelevant generically alter best-response correspondences in finite games.
4. Selection target shift: with common unique fast closure, initial preference
   heterogeneity is not selected; adaptation laws or institutions are selected.
5. Proxy alignment theorem: platform-selected adaptation laws need not reduce
   material welfare when the proxy is aligned; losses arise under independent or
   misaligned proxies, with the one-dimensional platform model as a tractable
   misalignment case.

## Decision

Do not lock the paper into the one-dimensional platform model. The next paper
draft should be reorganized around the finite-game singular-limit theorem, then
use platform preference control as the main application and policy section.
