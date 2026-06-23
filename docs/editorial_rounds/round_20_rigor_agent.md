# Round 20 Rigor Agent Memo

Scope: read `docs/agent_objective_function.md` and `paper/geb_submission_v1.html`; write only this memo. I did not edit the manuscript.

## Bottom Line

The new plain-language edits mostly preserve the mathematics. I do not see a scope-breaking overclaim in the named theorem/proposition chain. The draft now repeatedly marks the fast subsystem as fixed in \(E\) and \(\ell\), uses unique attracting closure, treats Proposition 1 as sufficient not necessary, treats Proposition 2 as a non-invariance test rather than Nash-set separation, limits Theorem 1 to post-closure admissible selection, and limits Proposition 3 to proxy/material alignment on a feasible rule set.

## Required Edits

1. Introduce \(H\) in prose before the first fast-dynamics display.
   - Current source introduces \(T_\theta\) and \(\theta\), then displays \(T_\theta\dot\theta=H(\theta;E,\ell)\).
   - To satisfy the objective function's symbol-before-display rule, add a short phrase before the display, e.g. "Let \(H\) denote the fast preference-adjustment vector field."

2. Keep the current limiting language in any future polishing.
   - The abstract and model correctly say that \(E\) and \(\ell\) are held constant during fast adjustment.
   - The model and Lemma 1 correctly require a unique globally attracting fixed point for each active \((E,\ell)\).
   - Do not shorten these passages back to bare "fixed-\(E\), fixed-\(\ell\)" shorthand.

No required mathematical edit is needed for Propositions 1-3 or Theorem 1.

## Scope Checks

- Fixed slow state and closure law: pass. The draft says \(E\) and \(\ell\) are held fixed during fast adjustment and confines the moving-slow-state discussion to a non-used extension.
- Unique attracting state: pass. The model and Lemma 1 require a unique globally attracting fixed point \(\theta_\ell^\star(E)\).
- Proposition 1: pass. It is stated as a strong sufficient condition, and the theorem text says it is not necessary for one fixed game.
- Proposition 2: pass. It now identifies failure of mixed best-response invariance only. The text explicitly says Nash sets may still coincide in special games.
- Theorem 1: pass. The post-closure admissibility restriction is defined before the theorem, and direct observability or reward of pre-closure \(q\) is excluded.
- Proposition 3: pass. The result is stated for a fixed feasible set \(\mathcal R\), with loss tied to proxy/material misalignment on that feasible set.

## Formula Numbering And Rendering Risks

- Source-level numbering is internally consistent: there are 15 `<div class="equation">` blocks, 15 equation labels, and the displayed `\[...\]` math blocks appear inside those equation containers.
- The numbering is CSS-counter based: `main` resets `equation`, `.equation` increments it, and `.equation::after` prints the number. Current MathJax use should not double-number the existing displays because the source uses `\[...\]` with `aligned`, not top-level `equation` or `align` environments.
- Residual risk: MathJax is configured with `tags: 'ams'`. If a later edit introduces top-level AMS numbered environments inside `.equation` blocks, the page could show both MathJax tags and CSS counter numbers. Future edits should either keep displays in the present `\[...\]` pattern or disable MathJax tags when CSS counters are the numbering system.
- Residual risk: equation numbers are absolutely positioned pseudo-elements. Long displays should still be visually checked after MathJax loads, especially the expected-payoff, best-response, and nested theorem equations, because the number can crowd horizontally scrollable math on narrow screens.
- Repository note: there is no `source/` directory in this checkout, so the source/CSS check used the inline CSS in `paper/geb_submission_v1.html`.
