# Round 10 Editor Memo

## Verdict

Conditional pass. The Round 10 Writer repaired the substantive mathematical issue identified by the modeller. Proposition 2 is no longer a loose pairwise-ranking-reversal claim; it now requires distinct unique best responses at the same opponent mixed profile, which is the right finite-action statement. Theorem 1 now uses \(q\sim_{E,\ell}q'\) consistently, and the working paper has adopted the post-closure admissibility language that was already clearer in the GEB version. Proposition 3 is also in acceptable fixed-feasible-set form.

The paper is close enough for a final writer pass and archive-PDF regeneration. It is not yet ready to call the user's three-cycle request complete, because the current archive PDF predates the Round 10 HTML edits.

## Blocking Issues

No theorem-level blocking issue remains in the current HTML drafts.

Proposition 2 is now correctly bounded. The statement assumes \(a_i\) is the unique material best response and \(b_i\ne a_i\) is the unique subjective best response. That avoids the third-action counterexample. The final sentence, saying that in a two-action choice set this is equivalent to strict subjective/material ranking reversal, is accurate.

Theorem 1's equivalence notation is acceptable. The relation \(q\sim_{E,\ell}q'\) is defined through \(C_\ell(E,q)=C_\ell(E,q')\), so the dependence on both the slow environment and closure law is explicit. The theorem's restriction to post-closure admissible selection rules is also visible enough for a referee.

Proposition 3's maximizer-set language is acceptable. The inclusion \(\arg\max_\mathcal R V\subseteq\arg\max_\mathcal R G\) correctly covers every proxy maximizer, including ties. The reversal construction is properly stated on the two-rule feasible set \(\{r_1,r_2\}\).

The remaining blocker is derivative-artifact integrity: `paper/arxiv_submission.pdf` is older than both `paper/working_paper_v1.html` and `paper/geb_submission_v1.html`.

## Final Writer Edits

Do not add new theory. Do not strengthen empirical claims. Do not change the GEB/working-paper boundary.

The final writer should make only last-mile consistency edits if needed: ensure Proposition 2 has identical mathematical content in both drafts; keep Theorem 1's post-closure admissibility wording aligned across drafts; and avoid describing strict ordinal equivalence as sufficient unless maximizers and ties on the fixed feasible set are preserved.

After that, regenerate the archive PDF from the working-paper HTML and update any project note that records the PDF source or timestamp. The PDF regeneration should happen after all content edits, not before.

## PDF Regeneration Targets

Regenerate:

- `paper/arxiv_submission.pdf`
- `results/figures/arxiv_submission.pdf.png`

The source should be `paper/working_paper_v1.html`, not the GEB submission HTML. The archive/working-paper version should retain the broader motivation, scalar model, welfare discussion, and WDI empirical appendix. The GEB version should remain the narrower journal-facing manuscript without WDI.

Visual QA targets after regeneration:

- title page and Version Note;
- Proposition 2 display and surrounding theorem box;
- Theorem 1 equivalence notation;
- Proposition 3 maximizer-set display;
- computational tables;
- WDI empirical appendix pages.

## Submission Readiness

Rounds 8, 9, and 10 now constitute three substantive editing cycles at the modeller-writer-editor level. They improved artifact integrity, reader orientation, and theorem hygiene in sequence. That satisfies the spirit of the requested three-cycle process, but the production sequence is not finished until a final writer incorporates this memo and regenerates the archive PDF.

For GEB, the HTML draft is now defensible as a theory-first submission draft, though a real submission should eventually be converted to LaTeX with journal-standard theorem environments and bibliography management. For archive circulation, the working-paper HTML is the correct source, but the current PDF should be treated as stale until regenerated and visually checked.
