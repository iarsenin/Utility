# Round 7 GEB Writer Memo

Role: Writer. Personality: narrative-driven but mathematically careful.

## Changed Files

- `paper/geb_submission_v1.html`
- `docs/agent_rounds/round_7_geb_writer.md`

I did not edit code, results, or replication files. I left `paper/working_paper_v1.html` unchanged because the WDI material is already contained in the working-paper empirical appendix and absent from the GEB version.

## Main Revisions

- Stated in the abstract and model section that all formal results are fixed-\(E\), fixed-\(\ell\) comparative statics after the fast boundary layer. Moving slow states are framed only as a possible extension.
- Tightened Theorem 1 by defining post-closure admissible material selection rules. The theorem now explicitly excludes selection rules that directly observe or reward the initial preference state \(q\).
- Separated theorem-level degeneracy within closure-equivalence classes from law-level selection. Selection over laws now requires a finite active set \(\mathcal L_0\), an equilibrium-selection rule, a material evaluator \(G_\ell(E)\), and a population dynamic or institutional choice rule.
- Renamed Proposition 2 to "Best-Response Non-Invariance Test" and added a short two-player, two-action example in which fast closure changes the Nash set from \((A,A)\) to \((B,B)\).
- Clarified that Proposition 3 is an exact fixed-feasible-set alignment result, while the simulation's "aligned" proxy is noisy and approximate. Positive proxy loss in the simulation is therefore not a contradiction.

## Remaining Risks

- The GEB version still needs a final editor pass for journal polish, especially around proof economy and whether the two-action example should remain in the main text or move to an appendix.
- The computational stress test would be stronger with Monte Carlo standard errors or a short reproducibility note in the GEB draft.
- The working paper remains broader and more exploratory by design; it should not be submitted to GEB without stripping the empirical appendix and broader motivation.
