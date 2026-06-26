# Venue Strategy

Date: 2026-06-20

## Primary Path

Start with a working paper, then prepare a Games and Economic Behavior
submission.

The working-paper version can be broad, exploratory, and public-facing. It
should retain the social-media and AI motivation, the platform application, the
welfare discussion, and the WDI timescale diagnostic.

The GEB-facing version should be narrower. It should read as a finite-game
theory paper about fast preference closure, Nash invariance, material
selection, and proxy choice. Social media, recommender systems, and AI should
be motivating applications, not the paper's identity.

## Target Versions

- `working_paper_v1.html`: broad version for circulation, comments, SSRN/arXiv
  style posting, seminar discussion, and project development.
- `geb_submission_v1.html`: narrow version for a Games and Economic Behavior
  submission package.

## GEB Positioning

Games and Economic Behavior is the right first aspirational target if the
paper's center is:

```text
finite games
+ subjective payoffs distinct from material payoffs
+ fast preference closure
+ Nash invariance / non-invariance
+ material selection over closure laws
+ platform proxy choice as an application
```

The paper should not be pitched to GEB as mainly about social media, AI,
mental health, or macro evidence. Those examples motivate the closure-law
technology, but the publishable game-theoretic contribution is the operator
order:

```text
closure law -> induced preference state -> subjective game
-> Nash equilibrium -> material evaluation -> selection over laws
```

This positioning follows the journal's stated scope: GEB is a general-interest
game-theory journal for theory and applications, including axiomatic and
behavioral models and applications across social, behavioral, mathematical, and
biological sciences. The submission-facing draft must therefore make the
game-theoretic contribution visible in the paper itself rather than rely on the
social-media or AI motivation.

Reference pages checked on 2026-06-20:

- https://www.sciencedirect.com/journal/games-and-economic-behavior
- https://gametheorysociety.org/games-and-economic-behavior/

## Before GEB Submission

- Convert the HTML manuscript to a LaTeX/PDF submission package with
  journal-standard theorem environments and bibliography management.
- Expand Appendix A from proof sketches into final proof prose if the current
  compact proof style feels too compressed after LaTeX conversion.
- Keep WDI out of the GEB main body; use at most the existing short paragraph on
  empirical implications and keep the full diagnostic in the working paper or
  appendix.
- Produce a PDF/LaTeX submission package once local tooling is available.

Already completed in `geb_submission_v1.html`:

- WDI is absent from the GEB body.
- The non-invariance result is an analytic best-response proposition, with a
  separate two-action example showing Nash-set change.
- Theorem 1 is restricted to post-closure admissible material selection rules.
- The proxy section distinguishes exact maximizer-set alignment from noisy
  approximate alignment in the simulation route.
- The computational stress test reports replication entry point, seed, payoff
  distribution, selection convention, threshold, and Monte Carlo standard-error
  formula.

## Working-Paper Posting

The working paper should include:

- a clear version/date line;
- abstract, keywords, and JEL codes;
- a "status of evidence" note distinguishing theorem, computational stress
  test, empirical diagnostic, and conjecture;
- links or appendix references for code and data;
- a statement that the paper is not yet a journal-submission manuscript.
