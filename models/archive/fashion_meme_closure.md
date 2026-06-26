# Fashion, Influencer, And Meme Preference Closure

This model is a standalone extension candidate. It should not be folded into
the main GEB article until the interpretation is accepted.

## Plain Setup

People can come to want a style, product, identity, norm, or behavior partly
because it is visible, fashionable, memetically salient, or endorsed by
influencers. The key question is not merely whether choices imitate choices.
The key question is whether the utility representation itself closes around the
fashion environment.

The model treats fashion exposure as a fast preference-formation channel. A
slow economic environment supplies the baseline material or intrinsic field.
Influencers, memes, and bubbles supply a fast salience field. Social
reinforcement supplies a feedback loop: the more a taste is perceived as common,
the more valuable or natural it becomes to hold that taste.

## Core Closure Equation

Let \(m_i\in[-1,1]\) denote agent \(i\)'s settled taste intensity for a binary
fashion-coded action. Positive values favor adoption; negative values favor
rejection. The fast closure law is:

\[
  m_i
  =
  \tanh\!\left(
    \beta\left[
      h_i+\eta\sum_j W_{ij}m_j+\phi_i z
    \right]
  \right).
\]

Definitions:

- \(h_i\): baseline material, intrinsic, or pre-fashion field.
- \(W_{ij}\): attention weight agent \(i\) gives to agent \(j\).
- \(\eta\): social reinforcement strength.
- \(z\): meme, fashion, platform, or influencer shock.
- \(\phi_i\): exposure of agent \(i\) to the shock.
- \(\beta\): responsiveness of the taste state.

This equation can be interpreted as logit social interaction, an Ising
mean-field law, or a smooth threshold contagion law. The project interpretation
is preference closure: the fixed point is the post-adjustment preference state.

## Result 1: Subcritical Uniqueness

For a nonnegative attention matrix \(W\), if

\[
  \beta\eta\rho(W)<1,
\]

where \(\rho(W)\) is the spectral radius, the fashion closure map is a
contraction in a Perron-weighted norm. The settled taste vector is unique.
Influencer and meme shocks move preferences continuously and reversibly.

## Result 2: Influence Multiplier

At a stable fixed point \(m^\star\), with

\[
  D=\operatorname{diag}(1-(m_i^\star)^2),
\]

the local response to a small meme field is:

\[
  \frac{\partial m^\star}{\partial z}
  =
  \beta\left(I-\beta\eta D W\right)^{-1}D\phi.
\]

As \(\beta\eta\rho(DW)\) approaches one from below, the multiplier can become
very large. The direction of amplification follows the central influence
directions of the attention network.

## Result 3: Mean-Field Hysteresis

In the symmetric mean-field case,

\[
  m=\tanh\!\left(\beta(Jm+b)\right),
\]

the closure is unique if \(\beta J\le 1\). If \(\beta J>1\), define:

\[
  m_s=\sqrt{1-\frac{1}{\beta J}},
  \qquad
  B_c=Jm_s-\frac{\operatorname{arctanh}(m_s)}{\beta}.
\]

For \(|b|<B_c\), there are three closures: two stable taste states and one
unstable separator. A temporary positive shock that pushes \(b\) above \(B_c\)
can eliminate the low-fashion branch. If the shock is later removed but the
baseline \(b\) remains in \((-B_c,B_c)\), the high-fashion taste state persists.

## Result 4: Material-Loss Window

Let the material evaluator be \(G(m)=hm\), with \(h<0\) meaning the material
criterion favors the low-fashion state. If:

\[
  |h|<B_c
  \quad\text{and}\quad
  B_c-h< z_{\max},
\]

then, starting from the low stable branch, a temporary positive fashion shock
of size less than \(z_{\max}\) can move the system to the high stable taste
state, and that movement lowers \(G\) after the shock disappears. The strict
inequality avoids the knife-edge saddle-node case \(h+z=B_c\).

## Generated Artifacts

Executable implementation:

- `src/utility_endogenous/fashion_meme_dynamics.py`
- `scripts/run_fashion_meme_analysis.py`

Results:

- `results/fashion_meme_report.md`
- `results/tables/fashion_threshold_summary.csv`
- `results/tables/fashion_hysteresis_path.csv`
- `results/tables/fashion_mean_field_branches.csv`
- `results/tables/fashion_network_multipliers.csv`
- `results/tables/fashion_phase_audit_summary.csv`
- `results/figures/fashion_mean_field_hysteresis.svg`
- `results/figures/fashion_network_multiplier.svg`
- `results/figures/fashion_phase_audit.svg`
