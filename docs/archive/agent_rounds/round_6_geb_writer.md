# Round 6 GEB Writer Memo

Role: Writer. Personality: narrative-focused, disciplined, mathematically literate; aim is to preserve the broad working-paper arc while producing a narrower Games and Economic Behavior-facing manuscript.

## Files Changed

- `paper/working_paper_v1.html`
- `paper/geb_submission_v1.html`
- `docs/agent_rounds/round_6_geb_writer.md`

## Working-Paper Version

I kept `working_paper_v1.html` broad. The body still carries the platform application, welfare discussion, computational stress tests, and WDI empirical diagnostic.

The main additions are front matter and reader discipline:

- changed the title metadata to mark it as a working paper;
- added JEL codes and keywords;
- added a status note explaining that the working paper has three layers: formal theory, platform/proxy application, and empirical timescale discipline;
- added a status-of-evidence table distinguishing theorem, computational stress test, empirical diagnostic, application, and welfare interpretation;
- added a roadmap paragraph in the introduction.

The WDI material is explicitly framed as diagnostic and calibration discipline, not causal evidence and not validation of platform preference closure.

## GEB Submission Version

I created `paper/geb_submission_v1.html` as a separate, narrower manuscript. It is not a shortened copy of the working paper; it is reorganized around the finite-game theorem spine.

Structure:

1. Introduction
2. Related Work
3. Model
4. Fast Closure And Reduced Games
5. Nash Invariance And Non-Invariance
6. Selection After Closure
7. Platform Proxy Choice
8. Computational Stress Test
9. Welfare And Interpretation
10. Conclusion
11. Appendix A. Proof Details
12. References

Main changes relative to the broad draft:

- removed WDI from the main body;
- shortened social-media and AI motivation;
- made the finite normal-form game object primary;
- stated the operator order early;
- added a generic analytic non-invariance proposition;
- rewrote the selection theorem using closure-equivalence classes before introducing scalar selection;
- kept platform control as an application rather than the paper identity;
- retained computational audits as stress tests, not empirical evidence;
- added an appendix with proof details and a compact moving-slow-state note.

## Remaining Gaps Before True GEB Submission

The GEB version is a serious first submission-facing HTML draft, but not yet final submission material. The next pass should:

- check theorem numbering and labels against final LaTeX conventions;
- decide whether Appendix A.1 needs a formal citation-backed singular perturbation proposition or should be weakened further;
- convert the HTML manuscript to LaTeX/PDF once the prose and theorem sequence stabilize;
- have the Editor verify that no working-paper residue remains in the GEB version.
