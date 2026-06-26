# Round 5 Editor Memo

Role: senior economics editor. Objective: protect exposition, formal credibility, article flow, and visual readability after the Pass 5 modelling and writing additions.

## Verdict

Conditional Pass.

The Pass 5 additions are directionally right. The maintained-assumptions note protects the formal claims, Corollary 1 gives the neutral-control benchmark a clean theorem-level anchor, and the sensitivity audit improves credibility by showing comparative movement rather than one cherry-picked stress-test result. The article is stronger. The remaining issue is editorial compression: Section 6 is now carrying several tables, two figures, and many numerical claims, while the assumptions note reads too much like a packed referee response. The final Writer pass should keep the new content but make it lighter on first read.

## 1. Maintained-Assumptions Note

The note is useful and should stay. It prevents misreadings of the fast-limit claim and names the assumptions that a theory referee would otherwise have to infer: unique closure, boundary-layer timing, state-only closure, equilibrium selection, exogenous material evaluator, finite active selection set, and random-game audit scope.

It is too dense in its current one-paragraph form. Seven assumptions in one sentence-like list create a "legal disclosure" feeling right before Lemma 1. The final Writer should convert it into either:

- a shorter prose note with only the four assumptions needed immediately for Lemma 1 and Proposition 1; or
- a compact bullet list inside the note.

My preferred fix is a two-sentence note:

```text
Maintained assumptions. The formal results use a unique stable closure, boundary-layer timing, and state-only preference dynamics; scalar material comparisons also require an explicit equilibrium-selection rule and an exogenous material evaluator. Later selection equations are restricted to a finite active set, and the random-game audits are stress tests of the logic rather than empirical distributions of platform environments.
```

This keeps the protection without making the reader feel stopped at the courthouse door.

## 2. Corollary 1

Corollary 1 is formally well placed. It belongs immediately after Proposition 1 because it turns the neutral-control simulation into an exact benchmark. The proof is also right: for fixed opponent mixing, the expected \(\alpha_i\) term is constant in \(x_i\), and \(\beta_i>0\) preserves the argmax.

Two stylistic issues remain:

1. The corollary should say "mixed Nash equilibrium sets" rather than only `NE(...) = NE(...)`, to maintain the same precision as Proposition 1.
2. The equation box nested inside the theorem box may be visually heavy. If the rendered view looks cramped, remove the inner equation label and let the displayed equation sit directly inside the corollary box.

The sentence before the corollary is good in spirit but could be less psychological: replace "psychologically real but strategically irrelevant" with "can change subjective representation without changing strategic incentives." That is cleaner economics prose.

## 3. Sensitivity Figure And Paragraph

The sensitivity audit helps. It adds a needed robustness check and, more importantly, clarifies that equilibrium movement and material loss are distinct. The exact-alignment result with zero material loss despite equilibrium shift is valuable and should remain in the article.

But Section 6 is now overloaded. It has:

- route definitions;
- a long simulation-method paragraph;
- Figure 1;
- Table 1A;
- Table 1B;
- a results interpretation paragraph;
- a sensitivity interpretation paragraph;
- Figure 2.

That is too much numerical density for one uninterrupted section. The final Writer should create a short subsection structure:

```text
Main Stress Test
Sensitivity Checks
```

or move most sensitivity numbers into the caption/report and keep only three anchor claims in text:

```text
At zero distortion the subjective and material games coincide. As distortion grows, mixed-BR invariance falls and outcome shifts rise. With exact proxy alignment, material loss is zero even when the selected equilibrium changes.
```

Then cite the figure for the grid. The current paragraph is correct but reads like a lab notebook excerpt.

## 4. Figure Numbering And Captions

Figure numbering is consistent after inserting the sensitivity figure:

- Figure 1: finite-game stress test;
- Figure 2: sensitivity checks;
- Figure 3: WDI timescales;
- Figure 4: WDI exposure-outcome associations.

Captions are mostly consistent. One caption-level adjustment: Figure 2 says "Larger strategic distortions lower..." and "Noisier material-aligned proxies raise..." That is fine visually, but for precision it should say "in this audit" or "in the sensitivity grid." Otherwise the caption sounds like a general theorem.

The tables are improved after being split into Table 1A and Table 1B. This solves the width problem from Pass 4.

## 5. Robustness And Genericity Language

The article is mostly disciplined. It does not claim that speed alone causes harm, and it repeatedly ties material loss to alignment and evaluator choice. Good.

The following phrases should be softened or localized:

- "strategic preference closure should often change equilibrium predictions" should become "can often change equilibrium predictions in the random-game audit" or "is expected to change predictions when it alters mixed best responses."
- "Larger strategic distortions lower..." in Figure 2's caption should become "In this grid, larger strategic distortions lower..."
- "The theory is testable" in the conclusion should become "The theory yields testable restrictions once a closure law and evaluator are specified." The current phrase is a little too broad because the abstract theory alone is a framework, not a single testable hypothesis.
- "material loss becomes common" is acceptable only when tied to "in this stress test." The current Section 6 wording does this once, but the final pass should keep that qualifier nearby.

No blocker here. These are credibility edits, not conceptual repairs.

## 6. Specific Final Writer Instructions

1. Compress the maintained-assumptions note into two sentences or a short bullet list. Keep all seven assumptions, but do not present them as one dense sentence.

2. In Corollary 1, say "mixed Nash equilibrium sets" and consider removing the nested equation box if the HTML view looks visually cramped.

3. Add subsection labels inside Section 6, preferably "Main Stress Test" and "Sensitivity Checks."

4. Shorten the sensitivity paragraph. Keep the zero-distortion, scale-4, and exact-alignment facts; let Figure 2 carry the rest of the grid.

5. Add "in this audit" or "in this sensitivity grid" to Figure 2's caption.

6. Replace the broad conclusion sentence "The theory is testable..." with the narrower claim that the framework yields testable restrictions once the closure law, exposure proxy, and material evaluator are specified.

7. After edits, visually inspect only three locations: the assumptions note, Corollary 1, and the Section 6 sensitivity block. Those are the live readability risks.

## Files Changed

- `docs/agent_rounds/round_5_editor.md`
