# Progress Ledger

## 2026-06-20

### Completed

- Created Drive-backed repository at `/Users/igor/My Drive/git/Utility`.
- Connected local working copy to `https://github.com/iarsenin/Utility.git`.
- Created initial project structure.
- Drafted first research plan, literature map, axioms, and model inventory.
- Implemented dependency-free simulations for:
  - endogenous taste drift under algorithmic exposure and Darwinian selection,
  - indirect evolutionary Prisoner's Dilemma with mutable social preferences.
- Ran the bootstrap simulations and generated first outputs in `results/`.

### First Simulation Readout

- Slow cultural drift moves mean online/artificial taste from about `0.35` to `0.06`; fitness rises.
- AI-speed preference capture moves mean online/artificial taste from about `0.35` to `0.96`; fitness falls.
- Even when selection against high online orientation is made much stronger, the chosen high-persuasion parameters still move the population near `0.96`; this is a useful stress case, not a proof.
- In the Prisoner's Dilemma model, prosocial preference drift restores near-full cooperation; conflict-oriented drift collapses cooperation.

### Research Planning Pass

- Added `docs/05_research_synthesis_v1.md`.
- Added `docs/06_formal_research_plan.md`.
- Added `docs/07_paper_outline_v1.md`.
- Added `references/literature_matrix.md` and `references/bibliography.bib`.
- Added model specs for:
  - platform preference control,
  - revealed preference with drifting tastes.

### Source-Grounded Finding

The literature already has endogenous preferences through consumption capital, habit, addiction, time preference, cultural transmission, indirect evolution, chosen preferences, and meta-preferences. The novel wedge is not "preferences can change." It is:

```text
algorithmic and AI systems can optimize the preference-transition kernel K_m
at a much faster timescale than culture or biological selection.
```

### Three-Iteration Research Sprint

Completed three major iterations in `scripts/run_research_iterations.py`.

Iteration 1: one-dimensional taste drift.

- Benchmark reproduced: with degenerate `K`, mean taste is stable; with selection only, taste moves toward the fitness-favored offline state.
- Endogenous modification: AI-speed transition pushes mean online/artificial taste from about `0.35` to `0.96` while fitness falls.
- Verdict: useful theorem candidate, too reduced-form to carry the paper.

Iteration 2: indirect evolutionary Prisoner's Dilemma.

- Benchmark reproduced: material payoff selection pushes cooperation nearly to zero.
- Endogenous modification: preference mutation toward prosocial types restores cooperation; mutation toward conflict collapses it.
- Verdict: strong bridge to the literature, not novel enough unless platform incentives choose the mutation law.

Iteration 3: platform preference control.

- Benchmark reproduced: no-platform selection increases fitness but can move taste away from the initial optimum.
- Endogenous modification: a myopic platform chooses exposure, raising mean online/artificial taste from about `0.35` to `0.79` while fitness falls by about `1.02`.
- Parameter sweep: `49/108` platform cells show taste capture, fitness loss, and initial-preference loss.
- Guardrail result: a calibrated autonomy penalty prevents capture and improves fitness; a weak penalty barely changes platform behavior.
- Verdict: this is the first paper's core candidate.

### Novelty Check

Added `docs/08_novelty_check_v1.md`.

Preliminary conclusion:

- Not novel: endogenous preferences, recommender feedback loops, engagement-welfare divergence, AI preference manipulation, or welfare trouble under endogenous preferences.
- Potentially novel: a mathematical economics model in which a platform chooses the preference-transition kernel `K_m`, producing a four-way split between platform value, final subjective utility, initial-preference welfare, and material/fitness welfare.
- Closest current threats: Kleinberg-Mullainathan-Raghavan on engagement optimization, Jiang et al. on recommender feedback loops, and Khosrowi-Beck on recommender welfare foundations.

### Fast Preference Limit Pass

Added `docs/09_fast_preference_limit.md`, `src/utility_endogenous/fast_limit.py`, and `scripts/run_fast_limit.py`.

Preliminary conclusion:

- This direction is more fundamental than the platform-only framing.
- Let preference adaptation occur on timescale `T` and take `T -> 0`. If the fast preference subsystem has a unique attracting branch `theta = Phi(z, m)`, utility is replaced by the critical manifold of preference adaptation.
- In the unique-attractor limit, selection over initial preference states becomes degenerate; material selection acts on objects that remain heterogeneous after closure, such as adaptation rules, institutions, biological resistance, or population size.
- The Nash operator is applied to the fast-adapted subjective game. The material-payoff Nash prediction is invariant only when fast preference closure preserves material best responses.
- Final-preference welfare is too weak in this limit because a path can create the preferences that endorse it.

Numerical readout:

- Strong taste adaptation has fast attractor `theta ~= 0.9615`; the finite AI-speed simulation converges to the same value.
- Selection strength from `0.20` to `5.00` leaves that fast attractor unchanged, while realized fitness falls.
- In the Prisoner's Dilemma model, fast prosocial adaptation yields full cooperation even though cooperation is not material Nash.
- In the platform model, the limit depends on transition-cost scaling: steady penalties vanish after the boundary layer, while boundary-layer penalties can block capture.

### Timescale And Survival Correction

Added `docs/10_timescales_and_survival.md`, `src/utility_endogenous/timescale_variants.py`, and `scripts/run_timescale_variants.py`.

Correction:

- Nash equilibrium is a fixed-point method. The material-payoff Nash prediction is invariant only when fast preference closure preserves the material best-response correspondence.
- Darwinian selection is an update operator, not a conclusion. In the `T_pref -> 0` limit, it acts on whatever remains heterogeneous after fast closure: populations, adaptation laws, institutions, or resistance to adaptation.
- We should not assume institutions or population are slower than preferences. Their speeds should be estimated or varied.

New numerical readout:

- Fixed exposure `m = 0.05` induces `theta = 0.50` and survives.
- Fixed exposure `m = 0.80` induces `theta ~= 0.94` and goes extinct.
- Myopic institutions select exposure around `m = 0.645`, induce `theta ~= 0.928`, and go extinct under all tested speed orderings.
- Survival-aware institutions select `m = 0.030`, induce `theta = 0.375`, and survive.
- The answer to "what survives?" can be "none" if all admissible institutions induce negative long-run growth after fast preference closure.

### Article Draft v0

Added `paper/article_draft_v0.md`.
Added `paper/article_draft_v0_math.md` as the preferred reading copy with
Markdown/LaTeX display equations.
Added `paper/article_draft_v0_codex.md` as the Codex-app reading copy with
flowing paragraphs and Unicode equation blocks.

Updated `paper/article_draft_v0_codex.md` to reader-facing draft v0.2.
This version expands the article prose, introduces the model intuition before
the equations, replaces slash-style derivatives with dot notation, and displays
key equations in boxed Unicode blocks for easier reading in Codex.

Updated the Codex draft again to v0.3 after visual review. Removed the
box-drawing equation frames because Codex displayed the right border as a
distracting pipe-like character. Formula displays now use plain quote blocks
with no side borders.

Updated the Codex draft to v0.4. Replaced abstract variable names with
reader-facing mnemonics: `P` for preferences, `E` for economic/material state,
`I` for institutions/environment, `A` for actions, and `N` for population or
survival mass. Replaced underscore time markers with Unicode subscripts such as
`Pₜ`, and rewrote formula labels to avoid code-like parameter names.

Added `paper/article_draft_v0.html` as the preferred reader copy. This version
uses HTML plus MathJax for formulas, avoiding fragile Markdown and Unicode
equation rendering. Going forward, any article draft intended for reading must
be rendered visually and checked with a screenshot before being reported as
ready. Visual QA screenshots for this pass are in:
`results/figures/article_draft_v0_html_preview_equation.jpg` and
`results/figures/article_draft_v0_html_preview_complex.jpg`.

Clarified the abstract definition of `P^star`: it is the stable preference
state induced by economic state `E` and institution `I` after fast adjustment,
not an optimum. Visual QA screenshot:
`results/figures/article_draft_v0_html_preview_abstract_pstar.jpg`.

Updated the HTML reader draft to v0.7 with a residue-removal and argument-order
pass. The draft now states the model primitives first: subjective best response
and material selection are fixed operators, while the preference state is
endogenous. The Nash and Darwinian-selection sections now distinguish the
operator from the payoff or state object without arguing against earlier
conversation notes. Visual QA screenshots:
`results/figures/article_draft_v0_html_preview_logic_pass.jpg` and
`results/figures/article_draft_v0_html_preview_logic_pass_equations.jpg`.

Purpose:

- Give a single readable manuscript for comments.
- Reframe the project around the fast-preference singular limit rather than the platform-only model.
- Keep theorem candidates clearly separated from simulation results.
- Preserve the correction that Nash equilibrium and Darwinian selection are methods/operators; what changes is the state space on which they operate.

### Current Conjectures

1. If preference-transition technology is fast relative to biological or material selection, current subjective welfare can rise while fitness falls.
2. Pareto comparisons over allocations alone are ill-defined when allocations alter the preferences used to evaluate them.
3. A Nash equilibrium of actions is not enough. In an endogenous-preference economy, equilibrium must include the preference-transition policy or institution.
4. Platform objectives can become an alternative selection criterion, creating a conflict between survival fitness and engagement fitness.

### Model Selection Audit

Added `docs/11_model_selection_audit.md`,
`src/utility_endogenous/model_selection_audit.py`, and
`scripts/run_model_selection_audit.py`.

The audit deliberately moved away from the one-dimensional taste/platform
models. It generated 5,000 random finite games per route and treated fast
preference closure as a payoff transformation.

Key readout:

- Neutral strategically irrelevant preference movement preserved best-response
  correspondences in `1.0000` of games and shifted equilibria in `0.0000`.
- Random strategic preference closure preserved best-response correspondences
  in only `0.3126` of games and shifted selected equilibria in `0.5044`.
- If a platform proxy is aligned with material welfare, proxy-selected material
  loss is rare: `0.0432`.
- If the proxy is independent, proxy-selected material loss is common: `0.5758`.
- If the proxy is misaligned, proxy-selected material loss is nearly generic:
  `0.9706`.

Research decision: promote a generic finite-game fast-closure theorem to the
core paper route. Keep platform preference control as the main application. Use
the one-dimensional taste model as exposition, not as the central proof.

### Article v1 And Agent Review Loop

Added `paper/article_v1.html` as the current main article draft.

The article is organized around the finite-game fast-preference closure model:

```text
closure law ell
-> theta_ell^star(E)
-> reduced subjective game Gamma_ell^star(E)
-> selected mixed equilibrium sigma_ell(E)
-> material evaluator G_ell(E)
-> selection or platform choice
```

The article incorporates three Modeller -> Writer -> Editor review rounds,
logged in `docs/agent_rounds/`. The final Round 3 structural blocker concerned
mixed-strategy Nash: Proposition 1 originally stated best-response invariance
only against pure opponent profiles. It has been repaired to use mixed
opponent profiles and expected payoffs over `Delta(A_i)`.

Current article claims:

- Fast closure is a fixed-slow-state closure lemma, not a full moving-slow
  singular perturbation theorem.
- Nash equilibrium remains the method; material Nash predictions are preserved
  only when mixed best-response correspondences are preserved.
- Material selection acts on closure laws or induced systems when initial
  preference states are erased by common unique fast closure.
- Platform control is an application in which platform rules are closure laws.
  Material loss is conditional on proxy/material alignment.
- Welfare comparisons based only on final induced preferences are not invariant
  when the transition law produces those preferences.

Added a World Bank WDI diagnostic pipeline:

- `src/utility_endogenous/empirical_wdi.py`
- `scripts/run_empirical_wdi.py`
- raw cached WDI JSON in `data/raw/`
- processed panels in `data/processed/`
- WDI tables and SVG figures in `results/`

The WDI section is explicitly a measurement prototype. It measures digital
exposure timescales and exposure-outcome associations. It does not identify
platform-induced preference closure.

Visual QA for `paper/article_v1.html` was performed in the Codex in-app browser
through a local server. Screenshots are saved in `results/figures/`:

- `article_v1_visual_qa_top.png`
- `article_v1_visual_qa_formal_equations.png`
- `article_v1_visual_qa_stress_test.png`
- `article_v1_visual_qa_wdi_equations.png`
- `article_v1_visual_qa_wdi_equations_fixed.png`
- `article_v1_visual_qa_formal_equations_fixed.png`

### Article v1 Passes 4 And 5

Completed two additional agent passes using the requested sequence:

```text
Modeller -> Writer -> Editor -> Writer
```

The round logs are:

- `docs/agent_rounds/round_4_modeller.md`
- `docs/agent_rounds/round_4_writer.md`
- `docs/agent_rounds/round_4_editor.md`
- `docs/agent_rounds/round_4_writer_final.md`
- `docs/agent_rounds/round_5_modeller.md`
- `docs/agent_rounds/round_5_writer.md`
- `docs/agent_rounds/round_5_editor.md`
- `docs/agent_rounds/round_5_writer_final.md`

Pass 4 corrected the finite-game audit so that the reported best-response
invariance statistic matches Proposition 1. The old `0.3126` number is now
classified as a weaker pure-endpoint diagnostic. The theorem-aligned mixed
best-response invariance rate for random strategic closure is `0.0762`, while
the selected-equilibrium shift rate remains `0.5044`.

Pass 5 added `scripts/run_model_selection_sensitivity.py`, which writes
`results/model_selection_sensitivity_report.md`,
`results/tables/model_selection_sensitivity.csv`, and
`results/figures/model_selection_sensitivity.svg`. The sensitivity audit shows
that strategic distortion scale and proxy-alignment noise move the results in
the expected directions, while exact proxy alignment can shift equilibria with
zero material loss.

Article updates from these passes:

- Added explicit expected payoff notation before Proposition 1.
- Added Corollary 1 proving that strategically irrelevant closure preserves
  mixed best responses and mixed Nash equilibrium sets.
- Renamed platform rules from `I` to `r` and internet exposure from `I_{c,t}`
  to `D_{c,t}` to avoid notation collision.
- Fixed the WDI regression units by writing the lagged internet control as
  `D_{c,t-1}/100`.
- Added a maintained-assumptions note before the closure lemma.
- Split the finite-game diagnostics into narrower tables and added a
  sensitivity figure.
- Localized robustness and material-harm claims to the stress-test design,
  proxy alignment, and the specified material evaluator.

Pass 5 visual QA was performed in the Codex in-app browser through a local
server. Screenshots are saved in `results/figures/`:

- `article_v1_pass5_visual_qa_top.png`
- `article_v1_pass5_visual_qa_assumptions_corollary.png`
- `article_v1_pass5_visual_qa_corollary.png`
- `article_v1_pass5_visual_qa_stress_tables.png`
- `article_v1_pass5_visual_qa_sensitivity.png`
- `article_v1_pass5_visual_qa_wdi_equation.png`

### Working Paper And GEB Submission Split

Created two venue-specific manuscripts:

- `paper/working_paper_v1.html`: broad working-paper version for circulation,
  comments, seminar discussion, and project development.
- `paper/geb_submission_v1.html`: narrower Games and Economic Behavior-facing
  version centered on the finite-game theorem package.

Added `paper/venue_strategy.md` to record the publication path, GEB positioning,
and the boundary between the broad working paper and journal-submission draft.

Completed two more venue-focused review rounds:

```text
Round 6: Modeller -> Writer -> Editor -> Writer
Round 7: Modeller -> Writer -> Editor -> Writer
```

The round logs are:

- `docs/agent_rounds/round_6_geb_modeller.md`
- `docs/agent_rounds/round_6_geb_writer.md`
- `docs/agent_rounds/round_6_geb_editor.md`
- `docs/agent_rounds/round_6_geb_writer_final.md`
- `docs/agent_rounds/round_7_geb_modeller.md`
- `docs/agent_rounds/round_7_geb_writer.md`
- `docs/agent_rounds/round_7_geb_editor.md`
- `docs/agent_rounds/round_7_geb_writer_final.md`

GEB-facing changes:

- Removed WDI and broad macro diagnostics from the GEB manuscript.
- Made the formal scope fixed-\(E\), fixed-\(\ell\) comparative statics after
  the fast boundary layer.
- Added an analytic best-response non-invariance proposition and a two-action
  example where fast closure changes the Nash set.
- Restricted the selection-target-shift theorem to post-closure admissible
  material selection rules, so direct reward of the pre-closure state is
  outside the theorem.
- Split exact proxy alignment from noisy approximate alignment in the simulation
  route.
- Added simulation replication details: entry point, seed, payoff distribution,
  selection convention, shift threshold, and Monte Carlo standard-error formula.

Working-paper changes:

- Retained WDI as an empirical appendix and measurement agenda, not causal
  evidence.
- Imported the Round 7 theorem refinements so the working paper and GEB draft
  share the same formal spine.
- Kept the broader AI/social-media motivation and welfare interpretation in the
  working-paper version only.

Visual QA for the split drafts was performed through a local server and
headless browser capture. Screenshots are saved in `results/figures/`:

- `geb_submission_v1_visual_qa_top.png`
- `geb_submission_v1_visual_qa_prop2_example.png`
- `geb_submission_v1_visual_qa_tables.png`
- `geb_submission_v1_visual_qa_mobile_prop2.png`
- `working_paper_v1_visual_qa_empirical_appendix.png`

The mobile Proposition 2 equation initially overflowed; it was fixed by using
compact payoff-difference notation and by adding horizontal-overflow protection
to equation boxes.

### Archive PDF And Rounds 8-10

Generated `paper/arxiv_submission.pdf` from `paper/working_paper_v1.html` as
the archive-style working-paper artifact. The PDF is a reader copy for
arXiv/working-paper circulation; the HTML remains the editable source until a
later LaTeX conversion.

Completed three additional editing cycles after generating the first PDF:

```text
Round 8: Modeller -> Writer -> Editor -> Writer
Round 9: Modeller -> Writer -> Editor -> Writer
Round 10: Modeller -> Writer -> Editor -> Writer
```

The round logs are:

- `docs/agent_rounds/round_8_modeller.md`
- `docs/agent_rounds/round_8_writer.md`
- `docs/agent_rounds/round_8_editor.md`
- `docs/agent_rounds/round_8_writer_final.md`
- `docs/agent_rounds/round_9_modeller.md`
- `docs/agent_rounds/round_9_writer.md`
- `docs/agent_rounds/round_9_editor.md`
- `docs/agent_rounds/round_9_writer_final.md`
- `docs/agent_rounds/round_10_modeller.md`
- `docs/agent_rounds/round_10_writer.md`
- `docs/agent_rounds/round_10_editor.md`
- `docs/agent_rounds/round_10_writer_final.md`

Round 8 cleaned archive-facing language and proof labels. Round 9 added a
theorem-map paragraph to the GEB introduction and renamed the working-paper
front note to "Version Note." Round 10 fixed a real theorem hygiene issue:
Proposition 2 is now a strict-maximizer non-invariance result rather than an
overbroad pairwise ranking-reversal claim for arbitrary finite action sets.
Theorem 1 now uses \(q\sim_{E,\ell}q'\), and Proposition 3 uses maximizer-set
alignment as the core sufficient condition.

The final PDF was regenerated after the Round 10 edits, and the first-page
thumbnail is saved as `results/figures/arxiv_submission.pdf.png`.

Round 10 visual QA screenshots are saved in `results/figures/`:

- `working_paper_v1_round10_qa_prop2.png`
- `working_paper_v1_round10_qa_theorem1.png`
- `working_paper_v1_round10_qa_prop3.png`
- `working_paper_v1_round10_qa_tables.png`
- `working_paper_v1_round10_qa_wdi_appendix.png`
- `geb_submission_v1_round10_qa_prop2.png`
- `geb_submission_v1_round10_qa_prop3.png`

### Reader-Facing Revision Rounds 11-14

Completed four additional editing cycles in response to the request that the
abstract and article read less like a high-formal math note and more like a
rigorous paper with conclusions stated upfront:

```text
Round 11: Modeller -> Writer -> Editor -> Writer
Round 12: Modeller -> Writer -> Editor -> Writer
Round 13: Modeller -> Writer -> Editor -> Writer
Round 14: Modeller -> Writer -> Editor -> Writer
```

The new round logs are:

- `docs/agent_rounds/round_11_modeller.md`
- `docs/agent_rounds/round_11_writer.md`
- `docs/agent_rounds/round_11_editor.md`
- `docs/agent_rounds/round_11_writer_final.md`
- `docs/agent_rounds/round_12_modeller.md`
- `docs/agent_rounds/round_12_writer.md`
- `docs/agent_rounds/round_12_editor.md`
- `docs/agent_rounds/round_12_writer_final.md`
- `docs/agent_rounds/round_13_modeller.md`
- `docs/agent_rounds/round_13_writer.md`
- `docs/agent_rounds/round_13_editor.md`
- `docs/agent_rounds/round_13_writer_final.md`
- `docs/agent_rounds/round_14_modeller.md`
- `docs/agent_rounds/round_14_writer.md`
- `docs/agent_rounds/round_14_editor.md`

Main changes:

- Rewrote the GEB abstract to state the result first: in the fast-preference
  limit, Nash equilibrium is computed in the post-closure subjective game, not
  necessarily in the material-payoff game.
- Added section-level bridges and interpretation blocks across the GEB body so
  the model, Nash invariance, selection-target shift, platform application,
  stress test, welfare discussion, and conclusion all tell the reader what is
  being proved before the notation does the work.
- Added a compact survival/change table in the GEB introduction distinguishing
  what survives from what changes for Nash equilibrium, material payoff,
  material selection, and welfare.
- Corrected reader-facing prose that could have made mixed best-response
  invariance sound necessary. The final language says it is a strong sufficient
  condition for Nash-set agreement with the material benchmark; Proposition 1
  remains sufficient but not necessary for one fixed game.
- Replaced "sharp" and other over-strong wording around the finite-game audit
  with "restrictive" and "in this audit" language, keeping the simulation as a
  stress test rather than empirical platform evidence.
- Tightened platform and welfare language so material loss is tied to
  proxy/material misalignment on the feasible rule set, while welfare claims
  remain explicitly criterion-dependent.
- Updated the working paper in parallel where the same interpretation or
  sufficiency language mattered, while preserving its broader Version Note and
  WDI diagnostic appendix.

The archive PDF was regenerated from `paper/working_paper_v1.html` after the
Round 14 edits. The regenerated PDF has 30 pages, and its refreshed first-page
thumbnail is saved as `results/figures/arxiv_submission.pdf.png`.

Round 14 visual QA was performed through the local server and headless Chrome
after MathJax rendering. Screenshots are saved in `results/figures/`:

- `geb_submission_v1_round14_qa_top.png`
- `geb_submission_v1_round14_qa_intro_order.png`
- `geb_submission_v1_round14_qa_nash.png`
- `geb_submission_v1_round14_qa_stress.png`
- `working_paper_v1_round14_qa_top.png`
- `working_paper_v1_round14_qa_invariant_table.png`

Validation:

- `paper/geb_submission_v1.html` and `paper/working_paper_v1.html` parse with
  Python's `HTMLParser`.
- Manuscript phrase audit found no remaining targeted overclaim triggers such
  as "only under," "only when," "sharp," "welfare concern," or
  "Darwinian or material" in the paper HTML files.
- Round 14 editor passed the manuscripts with no required final writer edits.

### GEB Readability Revision Rounds 15-17

Completed three additional editorial rounds on `paper/geb_submission_v1.html`
after the abstract still failed to make the model and results clear to a
highly educated general reader.

The round logs are:

- `docs/editorial_rounds/round_15_plain_setup.md`
- `docs/editorial_rounds/round_16_concept_flow.md`
- `docs/editorial_rounds/round_17_rigor_sweep.md`

Main changes:

- Rewrote the GEB abstract so it starts with the model in plain words:
  finite games, utility used for choice, fast preference formation, subjective
  Nash play, and separate material evaluation.
- Stated the core results in the abstract in reader order: fast reduction to a
  post-closure subjective game, a strong sufficient mixed-best-response
  invariance condition, possible Nash-set change, selection target shift, and
  proxy/material misalignment in the platform application.
- Rewrote the start of the introduction to define finite games, payoff tables,
  and Nash equilibrium before introducing endogenous utility.
- Added a term table for preference state, closure law, subjective utility,
  material payoff, and the reduced subjective game.
- Expanded the model section so finite games, mixed strategies, the fast
  preference timescale, closure laws, reduced subjective games, material
  benchmark games, and scalar material evaluation are introduced before the
  formulas.
- Reframed the Nash section by explaining that Nash equilibrium is a
  consistency condition rather than a welfare claim.
- Reframed selection, platform proxies, and welfare in plainer language while
  preserving the theorem restrictions.
- Ran a rigor sweep to avoid making the mixed-best-response condition sound
  necessary and to keep Proposition 3 framed as a material-evaluation result,
  not a complete welfare theorem.

Round 17 visual QA was performed through the local server and headless Chrome
after MathJax rendering. Screenshots are saved in `results/figures/`:

- `geb_submission_v1_round17_qa_top.png`
- `geb_submission_v1_round17_qa_intro_terms.png`
- `geb_submission_v1_round17_qa_model.png`
- `geb_submission_v1_round17_qa_nash.png`

Validation:

- `paper/geb_submission_v1.html` parses with Python's `HTMLParser`.
- Manuscript phrase audit found no new overclaim in the targeted terms; the
  remaining hits are the deliberate "deliberately sharp" motivating phrase and
  Proposition 2's "not a necessary-and-sufficient" caveat.
- Visual inspection confirmed that the abstract, term table, and formula boxes
  render cleanly in HTML.

### Formula Numbering And Non-Specialist Readability Rounds 18-21

Completed four further editing cycles on `paper/geb_submission_v1.html` after
the article still expected too much notation guessing from the reader.

The round logs are:

- `docs/editorial_rounds/round_18_objective_and_numbering.md`
- `docs/editorial_rounds/round_19_reader_agent.md`
- `docs/editorial_rounds/round_20_rigor_agent.md`
- `docs/editorial_rounds/round_21_production_check.md`

Main changes:

- Updated `docs/agent_objective_function.md` with role-specific objectives for
  the modeller/rigor agent, writer/reader agent, and editor/production agent.
- Added visible equation numbering to every display formula in the GEB HTML.
- Switched MathJax display tagging to `tags: 'none'` so CSS counters are the
  single numbering system.
- Rewrote the abstract to define \(E\), \(\ell\), \(\theta_\ell^\star(E)\),
  \(\Gamma_\ell^\star(E)\), Nash set, and mixed best-response invariance before
  relying on those terms.
- Expanded the introduction glossary with the slow environment, action profile,
  settled preference state, Nash set, and scalar material value.
- Reintroduced the first formal display as Equation (1), explicitly holding the
  slow environment \(E\) fixed while the closure law \(\ell\) maps to the
  settled preference state, reduced game, Nash set, and material value.
- Expanded the model section so \(a\), \(H\), \(\dot\theta\), \(T_\theta\),
  \(\theta_{i,\ell}^\star(E)\), and \(NE(\Gamma)\) are defined before their
  key displays.
- Replaced unexplained boundary-layer wording in the main text with plain
  "fast adjustment" language; the singular-perturbation term now appears only
  in the appendix with an immediate explanation.

Round 21 visual QA was performed through the local server and headless Chrome
after MathJax rendering. Screenshots are saved in `results/figures/`:

- `geb_submission_v1_round21_qa_top.png`
- `geb_submission_v1_round21_qa_intro_formula_number.png`
- `geb_submission_v1_round21_qa_model_formula_numbers.png`
- `geb_submission_v1_round21_qa_material_scalar.png`
- `geb_submission_v1_round21_qa_nash.png`

Validation:

- `paper/geb_submission_v1.html` parses with Python's `HTMLParser`.
- The manuscript has 15 `.equation` blocks, 15 labels, and balanced source
  display-math delimiters.
- Rendered text has no `fixed-E` or `fixed-l` residue.
- Visual inspection confirmed that formula numbers, equation boxes, and the
  abstract/model/Nash formula sections render cleanly.

### Fashion, Influencer, Meme, And Bubble Closure Module

Built a standalone extension candidate that is not yet incorporated into the
GEB article. The module asks whether fashion, influencers, memes, and online
bubbles can be modeled as a fast preference-formation process.

Core files:

- `references/fashion_meme_literature.md`
- `models/fashion_meme_closure.md`
- `src/utility_endogenous/fashion_meme_dynamics.py`
- `scripts/run_fashion_meme_analysis.py`
- `results/fashion_meme_report.md`
- `paper/fashion_meme_closure_presentation.html`

Generated outputs:

- `results/tables/fashion_threshold_summary.csv`
- `results/tables/fashion_hysteresis_path.csv`
- `results/tables/fashion_mean_field_branches.csv`
- `results/tables/fashion_network_multipliers.csv`
- `results/tables/fashion_phase_audit_summary.csv`
- `results/figures/fashion_mean_field_hysteresis.svg`
- `results/figures/fashion_network_multiplier.svg`
- `results/figures/fashion_phase_audit.svg`

Main result:

- A familiar social-interactions closure law can be used as a fast
  utility-closure law.
- Below the critical feedback threshold, the closure is unique and reversible.
- Near the threshold, local influencer multipliers can become large and
  centrality-dependent.
- Above the threshold, the mean-field closure has hysteresis: a temporary shock
  can move the system from the low branch to the high branch and the new
  preference state can persist after the shock disappears.
- With the toy material evaluator \(G(m)=hm\), a persistent flip can be a
  material loss when the initial state is on the low branch, \(h<0\), and the
  temporary shock strictly crosses the critical field.

Numerical results:

- Calibrated case: \(\beta=2.0\), \(J=0.8\), \(h=-0.08\); critical field
  \(B_c=0.1335\); positive shock needed \(0.2135\); tested shock \(0.35\), so
  the flip persists.
- Random audit: 6,000 mean-field economies; 48.65 percent subcritical unique
  closure, 26.98 percent hysteresis possible, 15.40 percent flippable by a
  temporary shock of size 0.35, and 4.10 percent flip in a direction that lowers
  the toy material evaluator.
- Network multiplier audit: central targeted response rises sharply as
  \(\beta\eta\rho(W)\) approaches one from below; this is a local derivative,
  not a bounded adoption share.

Five editorial/review rounds:

- `docs/agent_rounds/fashion_round_1_modeller.md`
- `docs/agent_rounds/fashion_round_2_literature.md`
- `docs/agent_rounds/fashion_round_3_writer.md`
- `docs/agent_rounds/fashion_round_4_editor.md`
- `docs/agent_rounds/fashion_round_5_production.md`

Key review edits:

- Narrowed novelty: the social-interaction and threshold math is not new; the
  candidate contribution is embedding those mechanisms as fast
  preference-closure laws.
- Added an old/new framing box.
- Defined criticality, hysteresis, and the material evaluator in plain language.
- Added a numbered Result 2 for the local network influence multiplier.
- Added table numbers and captions.
- Tightened the material-loss result to require starting on the low branch and
  strict threshold crossing.
- Fixed a browser rendering issue caused by raw less-than signs inside TeX
  source embedded in HTML.

Round 5 visual QA screenshots:

- `fashion_meme_presentation_round5_top.png`
- `fashion_meme_presentation_round5_first_formula.png`
- `fashion_meme_presentation_round5_multiplier.png`
- `fashion_meme_presentation_round5_hysteresis.png`
- `fashion_meme_presentation_round5_material_loss.png`

### Combined Fast-Preference And Social-Feedback Manuscript

Merged the GEB-facing fast-preference/Nash/selection article with the
fashion/meme closure module into:

- `paper/combined_fast_preference_closure_v1.html`

The combined structure is now:

1. General finite-game fast-preference framework.
2. Nash invariance and non-invariance results.
3. Selection after closure and platform proxy choice.
4. Social-feedback closure law as the main worked mechanism.
5. Computational audits for both social-feedback criticality and finite-game
   strategic invariance.
6. Welfare interpretation, conclusion, and proof appendices.

Key formal repair during the merge:

- Introduced the branch-selection closure map
  \(C_\ell(E,q,\zeta)\), where \(q\) is the initial preference state and
  \(\zeta\) is a fast exposure or transition input.
- Preserved \(\theta_\ell^\star(E)\) as the unique-closure abbreviation.
- Added the branch-selected reduced game
  \(\Gamma_{\ell,q,\zeta}^\star(E)\).
- Embedded the social-feedback state \(m_i\) into subjective utility via a
  simple fashion-coded action term.
- Added explicit social-feedback fast dynamics
  \(T_m\dot m_i=-m_i+\tanh(\cdot)\).

Five merge review cycles were logged:

- `docs/agent_rounds/combined_round_1_modeller.md`
- `docs/agent_rounds/combined_round_2_literature.md`
- `docs/agent_rounds/combined_round_3_writer.md`
- `docs/agent_rounds/combined_round_4_editor.md`
- `docs/agent_rounds/combined_round_5_production.md`

Notes on process:

- The first two merge passes used live subagents.
- The remaining three were documented local role passes because the subagent
  thread pool remained capped after earlier completed agents.

Validation:

- Re-ran `scripts/run_fashion_meme_analysis.py`.
- Re-ran `scripts/run_model_selection_audit.py`.
- `paper/combined_fast_preference_closure_v1.html` parses with Python's
  `HTMLParser`.
- `git diff --check` passes.
- Raw less-than TeX checks passed for the known problematic patterns
  `<B_c`, `< z`, `<0`, `<1`, `B_c-h<`, and `|h|<`.
- Browser QA found 392 rendered MathJax containers, 23 equation blocks, 5
  figures, and 8 tables, with no raw display delimiters.

Combined visual QA screenshots:

- `combined_v1_qa_top.png`
- `combined_v1_qa_closure_map.png`
- `combined_v1_qa_model_closure.png`
- `combined_v1_qa_social_feedback.png`
- `combined_v1_qa_hysteresis.png`
- `combined_v1_qa_appendix.png`

### Combined Manuscript Formula-Explanation Pass

Added a formula-by-formula explanation pass to
`paper/combined_fast_preference_closure_v1.html`.

Main edit:

- Every displayed equation now has a nearby "Why this form" explanation unless
  it is embedded in the text as a theorem statement.
- The pass is especially explicit for Equation (17), the network
  social-feedback closure law. It now explains the total-field structure,
  the role of \(h_i\), \(W_{ij}\), \(\eta\), \(\phi_i z\), and \(\beta\),
  why \(\tanh\) is used, and why the dynamic takes the leaky-adjustment form
  \(T_m\dot m_i=-m_i+\tanh(\cdot)\).
- The social taste embedding, subcritical spectral-radius condition, local
  influence multiplier, mean-field reduction, critical-field formula, and
  persistent-loss window now each include short motivation for the chosen
  formula.

Validation:

- HTML parse passed.
- The draft still has 23 displayed equation blocks.
- The draft now has 23 "Why this form" explanation blocks.
- Browser render check found 444 MathJax containers and no raw display
  delimiters.

Formula-explanation QA screenshots:

- `combined_v1_formula_explanations_model.png`
- `combined_v1_formula_explanations_eq17.png`

### Combined Manuscript Numbering And Numerical-Style Pass

Completed three additional review/editing rounds on
`paper/combined_fast_preference_closure_v1.html`.

Round logs:

- `docs/agent_rounds/combined_round_6_modeller_numbering_palette.md`
- `docs/agent_rounds/combined_round_7_writer_numerical_integration.md`
- `docs/agent_rounds/combined_round_8_editor_production.md`

Main edits:

- Automated theorem-like labels with CSS counters by result type. The rendered
  manuscript now has 7 propositions, 1 lemma, 1 corollary, 1 example, and 1
  theorem, with no hand-numbered theorem titles.
- Automated figure captions and table titles with CSS counters. The source no
  longer contains hand-numbered `<strong>Figure ...</strong>` or
  `<strong>Table ...</strong>` prefixes.
- Added a shared chart palette across the social-feedback and finite-game SVG
  generation scripts.
- Rewrote the Section 9 bridge so the computational audits are explicitly
  connected to the formal propositions.
- Clarified that the finite-game simulation uses a noisy approximately aligned
  proxy, not the exact alignment condition of Proposition 3.
- Added reader-facing interpretation around the local influence multiplier,
  calibrated hysteresis flip, random parameter audit, and Section 9 synthesis.

Validation:

- Re-ran `scripts/run_fashion_meme_analysis.py`.
- Re-ran `scripts/run_model_selection_audit.py`.
- Re-ran `scripts/run_model_selection_sensitivity.py`.
- `python3 -m py_compile` passed for the modified analysis/generation scripts.
- HTML parse passed.
- Render check found 446 MathJax containers, 23 equation blocks, 5 figures, 8
  table titles, and 11 theorem-like blocks.
- `git diff --check` passed.

Round 8 visual QA screenshots:

- `combined_v1_round8_numbering.png`
- `combined_v1_round8_section9_bridge.png`
- `combined_v1_round8_social_figures.png`
- `combined_v1_round8_finite_figures.png`
- `combined_v1_round8_sensitivity_figure.png`

### Next Actions

- Decide whether `paper/combined_fast_preference_closure_v1.html` becomes the
  working-paper source, the GEB-facing source, or a broad working paper from
  which a shorter GEB submission is later carved out.
- Convert the selected source manuscript to a LaTeX/PDF submission package with
  journal-standard theorem environments and bibliography management.
- Tighten proof sketches into final proof blocks during the LaTeX conversion.
- Prove a formal non-neutral closure result beyond the numerical stress test.
- Prove the timescale-dominance proposition in `docs/06_formal_research_plan.md`.
- Derive the platform-control first-order or threshold condition.
- Replace the myopic platform with a forward-looking platform or regulator.
- Tighten welfare language around initial preferences, final preferences, meta-preferences, and fitness.
- Begin a formal note for the preference-laundering theorem.
- Map the exact difference from Kleinberg, Mullainathan, and Raghavan's engagement-optimization model.
- Extend the fixed-slow-state closure lemma into a full moving-slow-state
  singular perturbation theorem, if the paper keeps leaning on that language.
- Extend the long-run survival model to allow competition among institutional regimes and empirically estimated timescale priors.

### Open Questions

- What is the right welfare criterion: initial preferences, long-run preferences, meta-preferences, biological fitness, or constitutional constraints?
- Should "preference autonomy" be modeled as a constraint on the transition kernel `K`?
- Can we derive a clean impossibility theorem without importing psychology?

### Narrative Pivot And Local Rendering Pass

Completed a narrative pivot of `paper/combined_fast_preference_closure_v1.html`
on June 24, 2026.

Main edits:

- Reframed the article around preference-fitness wedges rather than a
  formula-first exposition.
- Removed self-referential scaffolding such as "this paper will show" /
  "the paper's main object" style prose from the article body.
- Added a permanent agent rule rejecting "song about the song" meta-commentary.
- Kept theorem statements and proofs in appendices while making the main text
  explain low fertility, loneliness, dating retreat, fashion/status cascades,
  and AI risk/repair in plainer language.
- Moved detailed simulation tables and sensitivity material into Appendix C.
- Added simulation replication details: scripts, seeds, sample sizes, random
  draws, proxy conventions, selection rules, and Monte Carlo error scale.
- Vendored MathJax locally under `vendor/mathjax` and changed the combined
  article to load `../vendor/mathjax/es5/tex-chtml.js` instead of jsDelivr.
  This removes the immediate external network request that could produce
  connection errors when reading the local file.

### Title And Artifact Rename

On June 25, 2026, renamed the current reader-facing manuscript to:

- `paper/when_preferences_move_faster_than_equilibrium_v1.html`

The displayed article title is now "When Preferences Move Faster Than
Equilibrium," with the subtitle "Endogenous utility, induced Nash games, and
selection in mathematical economics." The former
`paper/combined_fast_preference_closure_v1.html` path remains as a compatibility
redirect only.

Validation:

- HTML parse passed.
- Internal anchors resolve.
- All immediate `src`/stylesheet assets are local and present.
- No immediate external scripts, stylesheets, or images remain.
- Equation/theorem/figure/table counts: 15 / 11 / 5 / 8.
- `git diff --check` passed.

Browser note:

- Programmatic inspection of the existing in-app `file://` tab was blocked by
  Browser Use URL policy. Source-level connection checks were completed
  instead, and the obvious external-load cause was removed by vendoring
  MathJax.

## 2026-06-26 Material Feedback Pivot

### Reason

The previous fast-preference manuscript separated subjective payoff, Nash
equilibrium, and material evaluation, but it did not close the feedback loop
from material consequences back into future preference formation. The new
direction makes that loop the core object.

### Implemented

- Added `models/material_capacity_feedback.md`.
- Added `docs/13_material_feedback_pivot.md`.
- Added `src/utility_endogenous/material_feedback.py`.
- Added `scripts/run_material_feedback_analysis.py`.
- Added `scripts/build_material_feedback_article.py`.
- Regenerated `paper/when_preferences_move_faster_than_equilibrium_v1.html`
  from model outputs.
- Updated `README.md`, `PROJECT_PLAN.md`, `paper/README.md`,
  `results/README.md`, `models/README.md`, and
  `docs/agent_objective_function.md`.

### Current Model

Fast subjective payoff formation:

```text
p(K,z) = logistic(beta * (q + z - rho K))
```

Slow projected capacity dynamic:

```text
Kdot = alpha + r K^2 (1 - K) - d K - L p(K,z)
```

Capacity is normalized to `[0,1]`. If the unprojected drift points outside the
interval, the boundary is treated as a feasible projected state.

### Current Readout

- The baseline trap calibration has two stable states and one unstable
  threshold.
- The self-correcting calibration has one high-capacity stable state.
- The repair calibration moves a low initial condition into the high-capacity
  basin.
- The random audit now distinguishes:
  - single-state feedback;
  - interior low-high traps;
  - lower-boundary projected states.

### Important Corrections

- Use `alpha` for baseline repair; reserve action notation for actions.
- Do not claim global monotone comparative statics for `beta` or `rho`.
  Appendix B now gives conditional derivatives and a constructive trap
  calibration.
- The fast-limit result now assumes a selected normally hyperbolic attracting
  branch and either a continuous equilibrium branch or an explicit selection
  rule.
- The article frames social examples as candidate applications with empirical
  tests, not as one master explanation.

### Next Actions

- Visual QA the regenerated HTML in the browser.
- Convert the working paper to a LaTeX/PDF version after the model direction is
  stable.
- Decide whether to develop a richer strategic application: appearance arms
  race, outrage game, dating market withdrawal, or alliance reliability game.
