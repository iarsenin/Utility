# Paper Drafts

This folder contains readable manuscript drafts assembled from the research
notes, model results, and literature checks.

- `article_draft_v0.md`: first integrated draft for comments. It focuses on
  the fast preference limit, Nash object shift, selection target shift,
  long-run survival, and welfare non-invariance.
- `article_draft_v0_math.md`: same draft with display equations converted to
  Markdown/LaTeX math for easier reading.
- `article_draft_v0.html`: preferred reader copy. It uses HTML and MathJax so
  formulas render as actual equations instead of fragile Markdown/Unicode
  approximations.
- `article_draft_v0_codex.md`: plain-text backup retained for continuity. Use
  the HTML file for reading and comments because the Markdown viewer has been
  unreliable for formulas.
- `article_v1.html`: integrated article draft from the first five agent review
  rounds. It remains useful as a record of the full project before the venue
  split.
- `working_paper_v1.html`: broad working-paper version for circulation,
  comments, seminar discussion, and project development. It keeps the finite
  game theory, platform/proxy application, welfare interpretation, and WDI
  empirical appendix, with status notes that separate theorem, simulation, and
  diagnostic evidence.
- `arxiv_submission.pdf`: archive-style PDF generated from
  `working_paper_v1.html` and regenerated after the Round 14 reader-facing
  edits. It is a 30-page self-contained reader copy for arXiv/working-paper
  circulation; the HTML remains the editable source until a later LaTeX
  conversion.
- `geb_submission_v1.html`: narrower Games and Economic Behavior-facing
  version. It removes the WDI appendix from the main manuscript and centers the
  finite-game theorem spine: fast closure, mixed best-response invariance,
  best-response non-invariance, selection-target shift, proxy alignment, and a
  compact computational stress test.
- `fashion_meme_closure_presentation.html`: standalone extension-candidate
  presentation on fashion, influencers, memes, bubbles, and fast preference
  closure. It is intentionally separate from the GEB article until the results
  and interpretation are accepted.
- `combined_fast_preference_closure_v1.html`: current integrated manuscript.
  It combines the GEB-style fast-preference/Nash/selection paper with the
  fashion/meme social-feedback closure mechanism. The standalone GEB and
  fashion files remain preserved as source drafts, but this combined file is
  now the main reader copy for the merged direction.
- `venue_strategy.md`: venue plan and boundary between the working-paper and
  GEB-facing versions.

For any reader-facing article update, render the HTML and inspect screenshots
before reporting the draft as ready.

Latest visual QA artifacts for the Round 14 reading pass are in
`results/figures/`:

- `geb_submission_v1_round14_qa_top.png`
- `geb_submission_v1_round14_qa_intro_order.png`
- `geb_submission_v1_round14_qa_nash.png`
- `geb_submission_v1_round14_qa_stress.png`
- `working_paper_v1_round14_qa_top.png`
- `working_paper_v1_round14_qa_invariant_table.png`
- `arxiv_submission.pdf.png`

Latest GEB readability QA artifacts after the Round 15-17 editorial pass are
also in `results/figures/`:

- `geb_submission_v1_round17_qa_top.png`
- `geb_submission_v1_round17_qa_intro_terms.png`
- `geb_submission_v1_round17_qa_model.png`
- `geb_submission_v1_round17_qa_nash.png`

Latest formula-numbering and non-specialist readability QA artifacts after the
Round 18-21 pass are also in `results/figures/`:

- `geb_submission_v1_round21_qa_top.png`
- `geb_submission_v1_round21_qa_intro_formula_number.png`
- `geb_submission_v1_round21_qa_model_formula_numbers.png`
- `geb_submission_v1_round21_qa_material_scalar.png`
- `geb_submission_v1_round21_qa_nash.png`

Latest fashion/meme closure presentation QA artifacts are in
`results/figures/` after rendering:

- `fashion_meme_presentation_round5_top.png`
- `fashion_meme_presentation_round5_first_formula.png`
- `fashion_meme_presentation_round5_multiplier.png`
- `fashion_meme_presentation_round5_hysteresis.png`
- `fashion_meme_presentation_round5_material_loss.png`

Latest combined-manuscript QA artifacts are in `results/figures/`:

- `combined_v1_qa_top.png`
- `combined_v1_qa_closure_map.png`
- `combined_v1_qa_model_closure.png`
- `combined_v1_qa_social_feedback.png`
- `combined_v1_qa_hysteresis.png`
- `combined_v1_qa_appendix.png`
- `combined_v1_formula_explanations_model.png`
- `combined_v1_formula_explanations_eq17.png`

The five merge review notes are:

- `docs/agent_rounds/combined_round_1_modeller.md`
- `docs/agent_rounds/combined_round_2_literature.md`
- `docs/agent_rounds/combined_round_3_writer.md`
- `docs/agent_rounds/combined_round_4_editor.md`
- `docs/agent_rounds/combined_round_5_production.md`

Latest combined-manuscript numbering, numerical-integration, and chart-style
QA artifacts are in `results/figures/`:

- `combined_v1_round8_numbering.png`
- `combined_v1_round8_section9_bridge.png`
- `combined_v1_round8_social_figures.png`
- `combined_v1_round8_finite_figures.png`
- `combined_v1_round8_sensitivity_figure.png`

The additional three review notes are:

- `docs/agent_rounds/combined_round_6_modeller_numbering_palette.md`
- `docs/agent_rounds/combined_round_7_writer_numerical_integration.md`
- `docs/agent_rounds/combined_round_8_editor_production.md`

Latest narrative-pivot review notes are:

- `docs/agent_rounds/combined_round_9_narrative_pivot.md`
- `docs/agent_rounds/combined_round_10_narrative_rigor.md`
- `docs/agent_rounds/combined_round_11_final_reader_pass.md`

The combined manuscript now loads MathJax locally from
`vendor/mathjax/es5/tex-chtml.js`, so opening
`paper/combined_fast_preference_closure_v1.html` as a local file should not
produce a MathJax CDN connection error. If the in-app browser still shows stale
content, reload the tab.
