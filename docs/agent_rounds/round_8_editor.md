# Round 8 Editor Audit

## Verdict

Pass with next-cycle requirements. Round 8 did the right thing: it repaired public-facing draft language, aligned theorem labels across the working-paper and GEB versions, and removed unnecessary "proof sketch" modesty where the text already gives complete finite-game arguments. The paper now reads less like a project log and more like a manuscript.

## What Improved

- The working-paper status table no longer tells readers that the proof appendix is unfinished.
- Proposition 1 now has the same title in both versions: "Mixed Best-Response Invariance."
- Proof labels in the working paper no longer weaken the formal results.
- The archive PDF is documented in `paper/README.md` as an artifact generated from the working-paper HTML.

## Remaining Issues

The main remaining editorial weakness is orientation. A GEB referee should be able to identify the theorem package from the introduction without piecing it together from later sections. The current introduction is clear, but it could be more decisive: after the operator-order display, add a compact contribution paragraph that names Lemma 1, Proposition 1, Proposition 2, Theorem 1, and Proposition 3 in logical order.

The working paper has the opposite issue. It has good narrative, but the status note still creates a report-like opening. It is acceptable for working-paper circulation, but the arXiv PDF should probably move toward a "Version Note" rather than "Status Note," with less table-like self-classification.

## Required Round 9 Writer Edits

- In `paper/geb_submission_v1.html`, add a concise theorem-package paragraph to the introduction after the operator-order display.
- In `paper/working_paper_v1.html`, rename "Status Note" to "Version Note" and make its prose sound like authorial guidance rather than project management.
- Keep WDI absent from the GEB draft.
- Do not add new empirical claims.
- Do not change theorem statements unless the Round 9 modeller identifies a mathematical issue.

## PDF Guidance

Do not regenerate the final archive PDF yet. The final PDF should be produced after Round 10 so it reflects all three cycles.
