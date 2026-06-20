# Round 3 Editor Addendum

Date: 2026-06-20

Scope: narrow verification of the Round 3 structural blocker identified in
`docs/agent_rounds/round_3_editor.md`. I checked only the revised Proposition 1
block and the renamed WDI equation label in `paper/article_v1.html`. I did not
edit the article, code, data, tables, or figures.

## Blocker Verdict

Pass. The Round 3 structural blocker is resolved.

The article now defines mixed best-response correspondences over:

```text
x_-i in X_-i = product_{j != i} Delta(A_j)
```

with expected subjective and material payoffs. Proposition 1 now states that if
these mixed best-response correspondences coincide for every player and every
mixed opponent profile, then the mixed Nash equilibrium sets of the reduced
subjective game and the material benchmark game coincide. The proof sketch now
correctly refers to mixed Nash equilibria as fixed points of mixed
best-response correspondences.

This matches the article's earlier definition:

```text
NE(Gamma) subseteq X = product_i Delta(A_i)
```

The previous pure-profile/mixed-Nash mismatch is gone.

## WDI Label

Pass. The WDI equation label has been renamed from "Alignment Regression" to:

```text
Exposure-Outcome Regression
```

That resolves the non-blocking terminology note from the Round 3 review.

## Residual Note

No structural blocker remains before visual QA and commit. Remaining issues are
ordinary residual risks: verify HTML rendering, keep the finite-game stress test
framed as diagnostic rather than generic proof, and keep the WDI exercise framed
as exposure-outcome measurement rather than structural platform evidence.
