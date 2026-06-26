# Round 9 Modeller Audit

## Verdict

The formal model is adequate for the next public draft if the reader is oriented faster. The core mathematical object is a finite normal-form game with two payoff layers and a fast closure map. That is a clean enough object for GEB because the results are not empirical claims about platforms; they are comparative-static statements about the reduced game induced by an attracting preference branch.

The paper should not add a new theorem in this round. It should make the existing theorem chain unmistakable.

## Mathematical Strength

Lemma 1 is a boundary-layer reduction, and the paper correctly avoids claiming a full moving-slow-state singular perturbation theorem. This is important. The limit is not "preferences move infinitely fast in all possible dynamic systems." It is: for fixed \(E\) and \(\ell\), the preference subsystem closes before equilibrium analysis is conducted.

Proposition 1 is the correct Nash bridge. It says equality of mixed best-response correspondences implies equality of Nash sets. It is sufficient, not necessary. This is exactly the right level of generality.

Proposition 2 and Example 1 are complementary. Proposition 2 shows failure of the invariance discipline. Example 1 shows actual Nash-set change. Keep both, because neither alone gives the right message.

Theorem 1 is the most novel selection result. Its strength comes from post-closure admissibility: selection over initial taste states is degenerate only when selection observes the initial state through post-closure play. That restriction should be visible in the introduction.

Proposition 3 is a small but useful alignment proposition. It prevents the paper from overclaiming that endogenous preferences imply harm.

## What Must Be Clear To A GEB Referee

The GEB version needs a theorem map before Section 2. The current introduction states three implications, but a referee should see the formal architecture explicitly:

1. Fast closure defines the reduced subjective game.
2. Mixed best-response equality preserves Nash sets.
3. Ranking reversal breaks robust best-response invariance, and a two-action construction can change the Nash set.
4. Post-closure admissible material selection cannot distinguish initial preference states inside closure-equivalence classes.
5. Material loss under platform choice is an alignment result, not an automatic consequence of fast preferences.

This paragraph should appear immediately after the operator-order display.

## Archive PDF Issues

The working-paper PDF should be broad, but it should not feel like a lab notebook. "Status Note" is too process-heavy for an arXiv-facing first page. Rename it "Version Note" and make the prose about how to read the paper, not about internal development status.

The WDI appendix can remain because it disciplines timescale claims, but the note should say explicitly that the GEB version excludes it to keep the journal submission theorem-led.

## Recommended Writer Edits

- Add the theorem map to the GEB introduction.
- Rename the working-paper "Status Note" to "Version Note."
- In the working-paper version note, replace "status" language with "role" or "interpretation" language where possible.
- Do not alter theorem statements.
- Keep the computational section auxiliary and visibly non-evidentiary for the theorems.
