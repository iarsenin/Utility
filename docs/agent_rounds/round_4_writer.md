# Round 4 Writer Memo

Role: narrative-focused writer. Objective: make the formal correction from the Modeller leg readable, keep the paper's novelty visible, and avoid overclaiming.

## Revisions Made

1. **Made Proposition 1 easier to parse.**

   The article now defines expected subjective and material payoffs before introducing mixed best-response correspondences:

   ```text
   bar U_{i,ell}(x_i,x_-i;E)
   bar pi_{i,ell}(x_i,x_-i;E)
   ```

   The best-response equations now maximize these named expected payoff functions rather than embedding expectations inline. This should make the proposition read as a statement about correspondences on mixed-strategy spaces, not as an informal rank comparison over pure actions.

2. **Updated the finite-game section to reflect the stricter audit.**

   The table now distinguishes:

   - mixed best-response invariance: `0.0762` for random strategic closure;
   - pure-endpoint best-response check: `0.3126` for the same route.

   The text explicitly explains why the distinction matters: Proposition 1 requires agreement over all mixed opponent profiles. Pure-action endpoints are a weaker diagnostic and should not be described as full best-response invariance.

3. **Reduced notation collision.**

   The platform rule is now `r in R` rather than `I in I`. The empirical internet exposure variable is now `D_{c,t}` rather than `I_{c,t}`. This reserves `I` for ordinary prose and avoids making the platform and WDI sections fight over the same symbol.

4. **Made the empirical section more cautious while keeping it useful.**

   The WDI section now states more directly that it does not observe preference closure and is not a causal test of social media or AI effects. Its value is framed as empirical discipline: measuring clocks, estimating exposure-outcome associations, and forcing proposed mechanisms to face data rather than intuition.

## Current Read

The paper is stronger after the Modeller correction. The surprising number is now cleaner: random strategic closure preserves full mixed best-response correspondences in only `7.62%` of random finite games, while the weaker pure-endpoint check would have overstated invariance at `31.26%`. That is a sharper mathematical reason to keep the finite-game route central.

The empirical section remains deliberately modest. That is a virtue at this stage. It gives the paper a measurement program without pretending that WDI country aggregates identify preference manipulation.

## Requests For Editor

- Check whether the new finite-game table is too wide in the Codex/HTML view.
- Check whether the notation `D_{c,t}` for internet exposure is mnemonic enough, or whether `Net_{c,t}` would read better for economists.
- Look for any remaining sentence that implies material harm follows from speed alone. The article should say speed changes the object of analysis; harm requires misalignment or an adverse closure law.

## Files Changed

- `paper/article_v1.html`
- `docs/agent_rounds/round_4_writer.md`
