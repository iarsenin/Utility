# Fashion/Meme Closure: Modeller Memo

Role: Modeller agent. Personality: exact, skeptical, mathematical.

Scope read:

- `paper/fashion_meme_closure_presentation.html`
- `models/fashion_meme_closure.md`
- `results/fashion_meme_report.md`
- `src/utility_endogenous/fashion_meme_dynamics.py`

I did not edit the presentation or any model artifact.

## Bottom Line

The module is mathematically coherent as a mechanism result. The central claim is sound if stated conditionally: a social-interaction preference-closure law can be single-valued below a critical feedback threshold and history-dependent above it. The mean-field hysteresis result and the calibrated flip example reproduce numerically.

The main risks are not algebraic. They are scope risks:

- the network multiplier is a local linear-response result, not a finite-shock adoption prediction;
- the random parameter audit is a mechanism audit, not an empirical frequency estimate;
- the material-loss claim depends on the toy evaluator \(G(m)=hm\) and on starting from the low branch;
- the threshold inequality should be presented with a small strict-crossing caveat if the text wants robust flipping rather than knife-edge branch contact.

## Theorem Scope

Result 1 is correctly scoped if \(W\ge 0\) and \(\beta\eta\rho(W)<1\). The contraction claim is defensible in a Perron-weighted norm: for any \(\alpha>\rho(W)\), one can choose a positive weight vector giving a weighted sup-norm Lipschitz constant below \(\beta\eta\alpha<1\). Because \(\tanh\) has derivative bounded by one, uniqueness follows.

The phrase "no hysteresis in the closure law itself" is acceptable under that same global subcritical condition. It should not be read as "influencers have no long-run effect"; the presentation already clarifies this.

Result 2 is correctly scoped for the scalar mean-field equation

\[
m=\tanh(\beta(Jm+b)),
\]

with \(\beta>0\), \(J>0\). If \(\beta J>1\), then \(|b|<B_c\) gives three fixed points: two locally stable and one unstable. At \(|b|=B_c\) there is a saddle-node contact, not three distinct closures.

Result 3 is correct as a toy material-evaluator claim, but it requires the starting branch and selection path. The result is path-dependent: starting on the high branch would not demonstrate the same "temporary shock creates persistent loss" mechanism.

## Critical-Field Formula

The critical-field formula is correct for the positive field needed to destroy the low-fashion branch:

\[
m_s=\sqrt{1-\frac{1}{\beta J}},
\qquad
B_c=Jm_s-\frac{\operatorname{arctanh}(m_s)}{\beta}.
\]

Derivation check:

\[
b(m)=\frac{\operatorname{arctanh}(m)}{\beta}-Jm,
\qquad
b'(m)=\frac{1}{\beta(1-m^2)}-J.
\]

The spinodals solve \(m=\pm m_s\). The positive critical field is attained at the negative spinodal \(m=-m_s\):

\[
b(-m_s)=Jm_s-\frac{\operatorname{arctanh}(m_s)}{\beta}=B_c.
\]

For the reported calibration, \(\beta=2\), \(J=0.8\), this gives \(B_c=0.1335437128\). With baseline \(h=-0.08\), the positive shock needed is \(B_c-h=0.2135437128\), matching the report.

One precision issue: the text sometimes says a shock that "pushes \(b\) above \(B_c\)" and the condition uses \(B_c-h\le z_{\max}\). For a robust flip, use \(h+z>B_c\). Equality is the saddle-node boundary and can be knife-edge unless a perturbation or selection rule is specified.

## Network Multiplier

The local derivative formula is correct at a stable fixed point:

\[
\frac{\partial m^\star}{\partial z}
=
\beta(I-\beta\eta DW)^{-1}D\phi,
\qquad
D=\operatorname{diag}(1-(m_i^\star)^2).
\]

The presentation correctly calls the figure "linear response" and states that the plotted values are local derivatives, not bounded adoption shares. That caveat is essential and should remain.

Additional caveat: the code's network table computes linear response around the zero-flexibility benchmark \(D=I\). Thus the reported threshold column is \(\beta\eta\rho(W)\), not \(\beta\eta\rho(DW)\). This is acceptable as a clean illustrative benchmark, but the presentation should not imply the table covers arbitrary nonzero fixed points.

Also, the `contraction_bound` in the code is a norm bound while the plotted/reported central and peripheral responses are aggregate sums over agents. Therefore the central response can exceed the displayed bound without contradiction. If the bound is shown later, label it as a local norm bound or omit it from reader-facing tables.

## Notation

Notation is mostly consistent:

- \(m_i\): settled taste intensity;
- \(h_i\): baseline/pre-fashion field;
- \(W_{ij}\): attention weight from \(i\) to \(j\);
- \(\eta\): network social reinforcement;
- \(J\): scalar mean-field social reinforcement;
- \(z\): external meme/fashion/platform shock;
- \(\phi_i\): direct exposure loading;
- \(\beta\): responsiveness;
- \(b=h+z\): total scalar mean-field field;
- \(G(m)=hm\): toy material evaluator.

Potential ambiguity: \(h\) plays two roles in the scalar section: baseline taste field and coefficient in the material evaluator. This is mathematically convenient but interpretively loaded. It is acceptable for the toy result, provided the text keeps saying that this is a deliberately simple material evaluator.

## Empirical Relevance

The current text is appropriately cautious in several places: it says the audit is not an empirical estimate and that TikTok/Instagram/AI-specific claims are not established here.

The phrase "computational audit supports the mechanism" is acceptable if "supports" means "the simulated parameter draw contains the mechanism." It should not be interpreted as empirical support. A stricter phrase would be "illustrates the mechanism over a broad parameter draw."

No result here estimates real social-feedback reproduction numbers, real \(z\), or real exposure loadings \(\phi\). The empirical contribution remains prospective: the model identifies what would need to be measured.

## Recommendation

Keep the module as a standalone candidate. It is mathematically promising and likely useful for the main paper because it gives a concrete closure law \(\ell\) with a sharp qualitative prediction: below criticality, fashion exposure is reversible comparative statics; above criticality, temporary exposure can select a persistent preference state.

Before incorporation into the article, I recommend one model-side edit: state all flip results with either strict crossing \(h+z>B_c\) or an explicit tie/perturbation rule at \(h+z=B_c\). This prevents a minor but real knife-edge objection.
