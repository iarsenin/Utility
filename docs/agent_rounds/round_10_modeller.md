# Round 10 Modeller Audit

## Verdict

Conditional pass, with one mathematical fix required before the final archive PDF. The core paper is now coherent: fixed-\(E\), fixed-\(\ell\) fast closure induces a reduced subjective finite game; Nash equilibrium is computed in that game; material payoff and material selection are evaluated afterward. The GEB boundary is mostly clean, and the working-paper boundary is defensible. The remaining risks are not conceptual sprawl but theorem hygiene: Proposition 2 is currently too broad for arbitrary finite action sets, and the selection theorem terminology is cleaner in the GEB version than in the working paper.

## Must Fix Before Final PDF

1. Fix Proposition 2 in both versions. As written, a subjective/material ranking reversal between two actions \(a_i,b_i\) does not imply \(BR_{i,\ell}^\star(x_{-i};E)\ne BR_{i,\ell}^\pi(x_{-i};E)\) when player \(i\) has a third action that is the unique maximizer under both payoff systems. The claim is valid if \(A_i=\{a_i,b_i\}\), or if the statement assumes \(a_i\) is a strict material maximizer and \(b_i\) is a strict subjective maximizer at the same \(x_{-i}\). Prefer the latter if the paper wants a general finite-action statement; prefer the former if the proposition is meant to match the two-action audit.

2. Define the equivalence relation as \(q\sim_{E,\ell}q'\), not \(q\sim_E q'\), or explicitly say \(\ell\) is fixed throughout the relation. The current notation is formally acceptable after “fix \(E\) and \(\ell\),” but it invites confusion because the closure map depends on \(\ell\).

3. Mirror the GEB definition of “post-closure admissible” in the working paper before Theorem 1. The working-paper theorem states the restriction in words, but the GEB version is sharper and should be the canonical language.

4. Regenerate `paper/arxiv_submission.pdf` only after the Round 10 writer/editor edits. The existing PDF is a pre-Round-10 artifact and should not be treated as final.

## Mathematical Risks

Lemma 1 is acceptable as a fixed-slow-state boundary-layer reduction. It should not be upgraded into a moving-slow-state singular perturbation theorem without stronger uniform attraction and regularity assumptions. The current wording respects that boundary.

Proposition 1 is correct and well-positioned: equality of mixed best-response correspondences is sufficient, not necessary, for Nash-set equality.

Proposition 2 is the active defect. After repair, it should say either “in a two-action choice set” or “when the reversed actions are strict maximizers under the respective payoff systems.”

Proposition 3 is correct, but “strict ordinal equivalence” should be understood as bidirectional order equivalence on the fixed feasible set, including ties when maximizer sets matter. A safer phrase is “the two functions have the same maximizer set; strict ordinal equivalence is one sufficient condition when it preserves ties appropriately.”

## GEB Boundary

The GEB draft is now appropriately theorem-led: no WDI appendix, no broad empirical claims, and the platform discussion is presented as an application of closure-law selection. Keep it that way. The computational section should remain explicitly auxiliary: it audits sharpness and simulations; it does not support the theorems.

The most important GEB repair is Proposition 2. A referee will catch the third-action counterexample quickly. Once fixed, the theorem spine is suitable for a GEB-style theory submission.

## Working-Paper Boundary

The working paper can retain the scalar taste model, welfare discussion, and WDI empirical appendix. The Version Note now correctly tells readers that WDI is diagnostic, not causal evidence. Keep the archive version broad, but avoid implying that the empirical appendix tests preference closure. It measures clocks and exposure-outcome associations only.

The working paper should track the corrected Proposition 2 and the refined equivalence-relation notation so that the arXiv PDF and GEB draft do not diverge mathematically.

## Writer Instructions

Fix Proposition 2 first in both HTML files. Then standardize \(q\sim_{E,\ell}q'\), add the post-closure admissibility definition to the working paper, and lightly tighten Proposition 3 language about strict ordinal equivalence and maximizer sets. Do not add new results. Do not add new empirical claims. After those edits and the final editor check, regenerate the archive PDF from the working-paper HTML and run visual QA on the Proposition 2 display, Theorem 1, and tables.
