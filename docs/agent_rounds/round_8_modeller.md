# Round 8 Modeller Audit

## Verdict

The project is now strong enough to deserve a GEB-facing draft and an arXiv/working-paper PDF, but it is not yet submission-clean. The core formal spine is coherent: finite normal-form games, subjective utility distinct from material payoff, fast fixed-state closure, Nash equilibrium in the reduced subjective game, material evaluation after equilibrium, and selection over closure laws rather than vanished initial preference states. That is a publishable mathematical-economics object if the notation and proof discipline are tightened.

The weakest current feature is not the idea. It is draft residue: duplicated markup, a duplicated closure equation in the working paper, proof sketches mixed with formal statements, and a few places where broad claims are stated before the exact restrictions are clear. These defects matter because the paper's selling point is logical order. If the document itself reads stitched together, readers will distrust the timing argument.

## Must Fix This Cycle

1. Fix visible artifact errors before any substantive polishing: the GEB HTML has a duplicated `<section>` opener and a duplicated `<tr>` tag; the working paper repeats \(H(\theta_\ell^\star(E);E,\ell)=0\) inside the closure display.

2. Make the archive PDF read as a paper rather than a project report. The working paper can keep a status note, but the arXiv version should not lead with too much internal development language. Keep caveats, remove workshop-process phrasing where possible.

3. State the maintained timing assumptions earlier and more compactly. Readers need to know before the first theorem that the formal results are fixed-\(E\), fixed-\(\ell\), after-boundary-layer comparative statics.

4. Convert the main proof labels in the working paper from "proof sketch" to either "Proof" when complete or "Proof." followed by a concise formal argument. Current sketches are mathematically sufficient for Lemma 1, Proposition 1, Proposition 2, Theorem 1, and Proposition 3; calling them sketches weakens the draft unnecessarily.

## Theorem/Proof Issues

Lemma 1 is acceptable as a boundary-layer reduction for fixed \(E,\ell\), not as a full Tikhonov/Fenichel theorem. The text says this, but the working-paper display should remove the repeated fixed-point equation. The proof should say explicitly that finite action sets make pointwise payoff convergence enough to define the limiting finite game. It already does.

Proposition 1 is correct and properly only sufficient. It should be called "mixed best-response invariance" consistently in both drafts. The working paper currently uses the weaker title "A Sufficient Nash-Invariance Condition"; that is accurate but less memorable and less aligned with the GEB draft.

Proposition 2 is now safely stated as a best-response non-invariance test. It should not be sold as a theorem that Nash sets always change. The two-action example is the right device for showing possible Nash-set change.

Theorem 1 is promising but should be carefully bounded. It is a theorem about post-closure admissible selection rules, not about all conceivable selection. The text should emphasize that direct selection on pre-closure labels or observables is outside the theorem. This is already present in GEB and should be mirrored more crisply in the working paper.

Proposition 3 is correct after the fixed-feasible-set split. The simulation must keep distinguishing exact maximizer-set alignment from noisy approximate alignment.

## Archive PDF Issues

arXiv can accept PDF submissions, but the PDF must be one file with all text and figures, embedded outline fonts, machine-readable text, and no embedded JavaScript. A Chrome-generated PDF from the HTML is plausible for a draft archive version, but it should be validated visually and by string checks for JavaScript. The generated file should be treated as an archive artifact derived from `working_paper_v1.html`, not as a substitute for eventually preparing TeX source.

The archive version should keep the WDI empirical appendix because it helps readers understand the measurement agenda. But it should reduce internal status language. A public working paper may say "diagnostic only"; it should not say "proof appendix still needs conversion" in a front table if we want it to look like a paper.

## GEB Issues

The GEB version is appropriately narrower: no WDI appendix, finite-game framing, theorem-led contribution. The main remaining GEB risks are:

- It still contains small HTML artifacts that would look careless in PDF.
- The computational section should be explicitly auxiliary; the theorems cannot rely on Monte Carlo evidence.
- The "moving slow states" paragraph belongs as a remark only, not a claimed extension.
- The abstract is strong, but the introduction should state the theorem package in a clean list so readers see the result structure early.

## Recommended Writer Edits

For this cycle, do not invent new theory. Fix integrity and coherence:

- Repair HTML artifacts in both drafts.
- Rename the working-paper Proposition 1 title to match the GEB title.
- Change completed working-paper proof sketches to proofs.
- Replace the status-note table language that says proofs still need conversion with cleaner public-facing status language.
- Add a short arXiv/PDF note in project docs recording the PDF source, the reason WDI remains in the working paper, and the PDF limitations.
- Regenerate the PDF only after the three editing cycles, so the archive artifact matches the final HTML.
