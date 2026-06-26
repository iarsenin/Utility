# Round 7 GEB Modeller Memo

Role: Modeller. Personality: exact, rigorous, skeptical mathematical economist.

Task: final GEB-focused model audit of `paper/geb_submission_v1.html` and `paper/working_paper_v1.html` after Round 6. I did not edit HTML files or code. I read the GEB target as a general-interest game-theory venue where the paper must clearly advance game theory or its applications, not merely motivate a broad social-science concern.

## Verdict

The GEB version now has a plausible theorem spine. It is no longer an essay about social media or AI; it is a finite-game paper about a fast operator that maps environments into subjective payoff representations before Nash equilibrium is computed. That is the right target.

My verdict is **submission-track, not submission-ready**. The main claims are logically defensible after the Round 6 fixes, but the manuscript still needs a final tightening around assumptions, proof convention, and the exact relation between propositions and simulations. The working-paper version should remain broader and should carry WDI, welfare interpretation, and empirical measurement discipline. The GEB version should remain narrow.

## Must Fix

1. **State the boundary-layer status of Lemma 1 without ambiguity.** The fixed-slow-state closure lemma is enough for the finite-game theorem package. Do not let Appendix A.1 read like an unproved moving-state theorem. The current remark is mostly safe, but the main text should say plainly: all formal results are fixed-\(E\), fixed-\(\ell\) comparative statics after the fast boundary layer.

2. **Make Theorem 1 depend on an explicit class of material selection rules.** The theorem is true for selection rules that depend on an initial preference state only through post-closure play. It is false if selection can observe and reward the initial state \(q\) directly. Define the admissible selection functional, e.g. \(S(q)=\Phi(\Gamma_\ell^\star(E;q))\) or \(S(q)=M(\sigma(\Gamma_\ell^\star(E;q)),E,\ell)\). Then closure-equivalent states are genuinely indistinguishable.

3. **Clarify law-level selection.** The theorem cleanly proves degeneracy within a closure-equivalence class. The statement “selection can operate on closure laws” requires a separate object: a finite set \(\mathcal L_0\), an evaluator \(G_\ell(E)\), and a population dynamic over laws. The current replicator equation does this, but the theorem should not sound as if it proves the population dynamic itself.

4. **Separate exact proxy alignment from noisy simulated alignment.** Proposition 3 is exact: if \(\arg\max V\subseteq\arg\max G\), material loss is zero on the feasible set. Table 1B’s “proxy aligned” route still has positive loss. That is not a contradiction if the route is noisy or approximate alignment, but the text should say so explicitly. Otherwise a referee will think the simulation violates the proposition.

5. **Proof architecture should be made journal-standard.** Body statements plus short interpretations; proofs in Appendix A. Keep the short proof of Corollary 1 if desired. Remove remaining proof-sketch tone in the working paper before public circulation.

## Nice To Have

Add one explicit two-player, two-action example in the GEB draft where fast closure changes the Nash set, not merely the best-response correspondence at some off-equilibrium profile. Proposition 2 is now correctly stated as a best-response non-invariance test; an example would give readers the stronger intuition without overstating the proposition.

Add Monte Carlo standard errors or a short “simulation design” paragraph for the computational stress test. The tables are not evidence for the theorem, but GEB readers will still ask whether the rates are stable, seeded, and reproducible.

Consider renaming Proposition 2 to “Best-Response Non-Invariance Test.” The current title is acceptable, but the sharper title prevents readers from mentally upgrading it to a Nash-set theorem.

## Model Spine

The spine is logically sufficient if presented as follows:

1. **Fast closure lemma:** for fixed \(E,\ell\), \(T_\theta\to0\) replaces the initial preference state by \(\theta_\ell^\star(E)\).
2. **Reduced game:** the object of Nash analysis is \(\Gamma_\ell^\star(E)\), not the material benchmark game.
3. **Best-response invariance:** material Nash predictions are guaranteed to survive only when mixed best-response correspondences coincide.
4. **Non-invariance test:** a strict subjective/material ranking reversal at a mixed opponent profile breaks the invariance condition.
5. **Selection-target shift:** common closure eliminates selection over initial preference states within closure-equivalence classes; remaining selection is over closure laws, institutions, or rules that induce different post-closure games.
6. **Proxy alignment:** material loss from institutional rule choice is conditional on proxy/material misalignment, not on preference endogeneity by itself.
7. **Stress test:** random finite games illustrate that the invariance condition is restrictive and that proxy alignment controls material loss.

This is a real GEB argument because it modifies the payoff-representation side of finite games while preserving the fixed-point method. The contribution is operator order: closure precedes equilibrium and material selection evaluates the induced law.

## Working Paper Boundary

Keep in the working paper only: WDI diagnostics, broad social-media and AI motivation, macro timescale comparisons, extended welfare discussion, identification warnings, and speculative measurement agenda. These are useful for the research program but distracting for GEB.

Keep in the GEB version: finite-game primitives, fast closure, Nash invariance, selection-target shift, proxy alignment, compact computational stress test, and a brief statement that empirical work must measure relative clocks and proxy/material alignment.

The working paper can ask, “Is this how modern preference formation behaves?” The GEB paper should ask, “What happens to Nash equilibrium and material selection in finite games when the utility representation closes first?”
