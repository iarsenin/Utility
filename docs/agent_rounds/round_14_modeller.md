# Round 14 Modeller Memo

## Verdict

Conditional pass. The friendlier prose has mostly preserved the mathematics. The fixed-\(E\), fixed-\(\ell\), unique-attractor boundary-layer scope is visible in both drafts; Nash equilibrium and material/Darwinian selection are generally treated as methods rather than conclusions; and the platform claims are mostly conditional on proxy/material alignment.

There is one important correction before production: several reader-facing sentences now make the mixed best-response invariance condition sound necessary for Nash-set agreement. Proposition 1 states a sufficient condition, not a necessary-and-sufficient characterization for one fixed game. The final writer should fix this language wherever it appears.

## Required Final Writer Edits

1. **Correct the necessity language around Nash invariance.**
   - In the GEB abstract, replace "Nash predictions agree with the material-payoff benchmark only under a mixed best-response invariance condition" with language such as: "A strong sufficient condition for agreement is mixed best-response invariance."
   - In GEB Section 5, replace "It does so only when fast closure leaves every player's mixed best responses unchanged" with: "A selection-robust sufficient condition is that fast closure leaves every player's mixed best responses unchanged."
   - In the GEB conclusion, replace "Nash predictions are robust to fast closure only when closure preserves..." with a sufficient-condition formulation.
   - Make the same correction in the working-paper abstract, Section 5 takeaway, and the invariant table row that says Nash sets "survive only under best-response preservation."

2. **Avoid calling the invariance test "sharp" unless the sentence means sharp as a sufficient diagnostic.**
   - The random audit shows the condition is restrictive and theorem-aligned; it does not show it is necessary for every fixed Nash-set comparison. Prefer "restrictive," "strong," or "theorem-aligned" over "sharp" in the abstract and simulation interpretation.

3. **Keep the first sentence positive rather than defensive.**
   - The GEB abstract still opens with "Nash equilibrium does not disappear." This is mathematically fine, but it reads like an answer to an earlier objection. A cleaner production sentence is: "In the fast-preference limit, Nash equilibrium is computed in the post-closure subjective game, not necessarily in the material-payoff game."

4. **Tighten platform/welfare wording.**
   - In the GEB abstract, "where the welfare concern enters" should be "where the material-evaluation concern enters" unless the sentence explicitly invokes a welfare criterion.
   - In the working-paper conclusion, do not say material harm requires both proxy/material misalignment and best-response movement. Proposition 3 requires misalignment on the feasible rule set; best-response movement is one mechanism, not a theorem-level necessity.
   - When reporting proxy losses, add "in this audit" where needed so the simulation is not read as an empirical platform claim.

5. **Preserve the fixed-state scope in the broad working-paper prose.**
   - The working-paper abstract says utility is "produced by the environment." More exact: it is produced by the slow environment together with the closure law.
   - The introduction phrase "before the rest of the economy moves" is acceptable as intuition, but one nearby sentence should remind the reader that the formal comparative statics hold \(E\) and \(\ell\) fixed through the fast boundary layer.

6. **Use "material selection" consistently where the model is formal.**
   - The GEB introduction phrase "Darwinian or material selection" is understandable, but the formal object is material selection. Prefer "material selection" in theorem-adjacent prose; reserve "Darwinian" for motivation or related-work language.

## No Required Mathematical Changes

The theorem statements themselves do not need revision. Lemma 1, Proposition 1, Proposition 2, Theorem 1, and Proposition 3 still match the intended finite-game model. The scope conditions that matter for rigor remain present: fixed slow state, fixed closure law, unique attracting closure branch, explicit equilibrium selection for scalar material comparisons, and post-closure admissibility for the selection theorem.

The empirical appendix in the working paper is also appropriately bounded. It is described as a timescale diagnostic rather than causal evidence, and the WDI limitations are explicit. Do not expand the empirical claims in this production pass.
