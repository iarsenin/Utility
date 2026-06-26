# Round 5 Writer Memo

Role: narrative-focused writer. Objective: absorb the Pass 5 Modeller memo without making the article heavier than necessary.

## Revisions Made

1. **Named the maintained assumptions before Lemma 1.**

   I added a compact assumptions note before the fast-closure lemma. It now explicitly names:

   - unique stable closure;
   - boundary-layer timing;
   - state-only closure;
   - equilibrium selection for scalar material evaluation;
   - exogenous material evaluator;
   - finite active selection set;
   - random-game audit scope.

   The point is to make the theorem honest without making the article feel like a contract.

2. **Promoted strategic irrelevance into Corollary 1.**

   The former prose condition is now a formal corollary after Proposition 1. The proof is short: for fixed opponent mixing, the expected \(\alpha_i\) term is constant in \(x_i\), and \(\beta_i>0\) preserves the expected-material-payoff argmax. This analytically anchors the neutral-control simulation.

3. **Added sensitivity results as conditional robustness.**

   I added a compact robustness paragraph and included `results/figures/model_selection_sensitivity.svg` after the finite-game tables. The text uses the requested key grid points:

   - strategic distortion scale \(0,1,4\);
   - aligned-proxy noise \(0,0.5,2\).

   The paragraph emphasizes the core distinction: strategic distortion changes games; material loss rises as alignment erodes; equilibrium movement is not itself material loss.

4. **Clarified the platform interpretation.**

   The platform section now says directly that equilibrium shifts are not necessarily material losses. Material loss requires misalignment with the chosen evaluator, not merely a changed induced game or changed selected equilibrium.

5. **Kept WDI in its proper evidentiary role.**

   I did not strengthen the WDI claims. The empirical section still says WDI does not test whether platforms produce preferences and functions as empirical discipline/calibration scaffolding.

## Files Changed

- `paper/article_v1.html`
- `docs/agent_rounds/round_5_writer.md`

## Suggested Editor Checks

- Make sure the maintained-assumptions note is clear enough without feeling defensive.
- Check whether the sensitivity figure is visually acceptable in the Codex article view.
- Confirm that Corollary 1's theorem/proof formatting does not make the equations look cramped.
