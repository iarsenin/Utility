# Round 4 Editor Memo

Role: senior economics editor. Objective: protect the argument from reader confusion, notation drift, visual clutter, and journal-referee overclaiming.

## Verdict

Conditional Pass.

The Writer successfully absorbed the Modeller's main correction. The article now distinguishes the theorem-aligned mixed best-response diagnostic from the weaker pure-endpoint check, and the empirical section is appropriately cautious. I do not see a blocker. The final Writer pass should make several targeted fixes before this pass is considered clean.

## 1. Mixed Best-Response Diagnostic

The stricter diagnostic is explained correctly. The article now says that Proposition 1 is about mixed best-response correspondences over all opponent mixed profiles, and that the pure-endpoint check is weaker. The numbers are also used correctly:

- full mixed best-response invariance: `0.0762`;
- pure-endpoint best-response check: `0.3126`.

The risk is exposition, not substance. The key explanation is embedded in a long methods paragraph before Figure 1. A reader may reach the table before fully absorbing why `0.0762` is the theorem-relevant number. The final Writer should add one short bridge sentence before the table:

```text
The first diagnostic is the one used by Proposition 1; the second reports the weaker test one would get by checking only pure opponent actions.
```

Also avoid any shorthand implying that pure-action rank preservation is the same thing as best-response preservation. The article is mostly clean on this, but the final pass should keep "pure-endpoint" visibly subordinate to "mixed BR invariance."

## 2. Notation Consistency

The platform notation change is successful. I found no remaining conflict between platform rules and the old empirical `I_{c,t}` notation in the article. The convention

```text
r in R
```

is readable and consistent in the platform section.

The empirical notation has one unit inconsistency that should be fixed. The article defines `D_{c,t}` as internet users measured in percent of population, but the regression paragraph says the lagged internet control enters as a 0-1 share, and the code confirms that the regression uses `internet_lag / 100.0`. The displayed equation currently writes:

```text
gamma_1 D_{c,t-1}
```

The final Writer should either:

1. keep `D_{c,t}` in percent and write `gamma_1 D_{c,t-1}/100` in the regression equation, or
2. define a separate share variable, for example `S_{c,t}=D_{c,t}/100`, and use `S_{c,t-1}` as the lagged control.

I recommend option 1 because it is the smallest change and preserves the intuitive "percentage point" interpretation of `dD^{10}_{c,t}`.

There is also an older formal notation issue in Section 7: the text says the selection equation is restricted to a finite active set of closure laws, but the displayed average uses `sum_{k in L}`. If the active set is finite, write it explicitly as something like `L_0 subset L` and sum over `k in L_0`. This is not from the `r/R` or `D` changes, but it is exactly the kind of detail a theory referee will notice.

## 3. Empirical And Material-Harm Claims

The empirical section is now appropriately modest. It says WDI does not observe preference closure, is not causal, and does not identify the platform-control mechanism. That is the right posture.

The article also avoids claiming that fast preferences mechanically imply harm. The abstract, finite-game discussion, limitations, and conclusion all state that material harm depends on alignment, feasible laws, and material evaluation. Good.

Two phrases should be softened in the final Writer pass:

- "it is evidence that the alignment condition is doing real work" should become "it illustrates that the alignment condition is doing real work" or "it is a computational check..."
- "losses are common under independent and misaligned proxies" is acceptable if tied to "in the finite-game stress test"; do not let it stand as an empirical claim about real platforms.

The suicide-mortality interpretation is also cautious enough, but I would replace "directionally favorable" with "opposite the simple harm narrative" to avoid sounding like the paper is making a welfare judgment from one noisy macro proxy.

## 4. Finite-Game Table Visual Risk

The finite-game table is intellectually useful but visually risky. It has five columns, long route names, long headers, and several `n/a` cells. The CSS makes tables horizontally scroll on narrow screens, so it will not technically break, but it may look like a spreadsheet inside the paper.

The final Writer should either split it into two smaller tables or reduce visual load. Best option:

- Table 1A: neutral/random strategic routes with `Mixed BR`, `Endpoint BR`, and `Equilibrium shift`.
- Table 1B: proxy routes with `Equilibrium shift` and `Proxy loss`.

If keeping one table, shorten headers:

```text
Mixed BR
Endpoint BR
Outcome shift
Proxy loss
```

and replace `n/a` with `--` to reduce clutter.

## 5. Concrete Final Writer Instructions

1. Add one plain-English sentence before the finite-game table stating that the mixed-BR column is the Proposition 1 diagnostic and the endpoint column is only a weaker comparison.

2. Fix the WDI regression unit mismatch by writing `D_{c,t-1}/100` in the displayed equation, or by defining a separate share variable. Prefer `D_{c,t-1}/100`.

3. Fix the Section 7 selection equation so the active finite set is named and the average payoff sums over that active set, not over all of `L`.

4. Reduce the finite-game table's visual width by splitting it into two tables, or at minimum shorten headers and replace `n/a` with `--`.

5. Replace "evidence that the alignment condition is doing real work" with "computational check" or "illustration" language, and keep all material-harm language conditional on the stress-test design or on proxy misalignment.

6. After edits, visually inspect the HTML again at the finite-game table and WDI regression equation. These are the two places most likely to produce either layout trouble or notation trouble.

## Files Changed

- `docs/agent_rounds/round_4_editor.md`
