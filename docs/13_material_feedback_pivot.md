# Material Feedback Pivot

Date: 2026-06-26.

## Reason For Pivot

The previous manuscript correctly separated subjective payoff, Nash
equilibrium, and material evaluation, but it left preference formation too
one-way. A fast environment produced subjective payoffs; agents optimized; a
material evaluator judged the result. The missing piece was feedback from
material consequences into future preference formation.

The current direction makes that feedback explicit.

## Current Core Claim

Fast preference formation is economically important when it is coupled to a
slow material capacity:

```text
preference-forming rule -> subjective payoff -> action/equilibrium -> material capacity -> future subjective payoff
```

This loop can produce three qualitatively different regimes:

- self-correction when capacity remains protective;
- threshold traps when substitute behavior erodes the capacity that would make
  the substitute less attractive;
- collapse-prone projected dynamics when damage overwhelms interior repair and
  the lower capacity boundary becomes relevant.

## Why This Is Better

The model now answers real puzzles more directly. Low fertility, loneliness,
dating retreat, AI companions, betting, ultra-processed food, appearance arms
races, political outrage, migration backlash, and alliance distrust are not
presented as examples of "fake preferences." They are examples where a payoff
criterion can be rational at the moment of choice while the choice changes a
capacity stock that shapes future payoff criteria.

This avoids two weak positions:

- saying only that preferences move fast;
- implying that Nash equilibrium or Darwinian selection disappears.

Nash equilibrium remains the consistency condition after subjective payoffs are
formed. Selection remains the long-run persistence operator after the material
capacity and evaluator are named.

## Literature Backbone

The revised backbone uses:

- Stigler-Becker consumption capital as the stable-preference foil;
- Grossman health capital for slow material stocks;
- Becker-Murphy rational addiction for dynamic complementarity;
- Bowles, Bisin-Verdier, and Bernheim et al. for endogenous and chosen
  preferences;
- Koszegi-Rabin and Genicot-Ray for reference points and aspirations;
- Brock-Durlauf and Arthur for social interactions, multiple states, and
  lock-in;
- recommender-feedback literature for modern preference-forming environments;
- Allcott et al., Braghieri-Levy-Makarin, and Guess et al. for exposure
  experiments useful in identification.

## Current Files

- Model note: `models/material_capacity_feedback.md`
- Code: `src/utility_endogenous/material_feedback.py`
- Runner: `scripts/run_material_feedback_analysis.py`
- Article builder: `scripts/build_material_feedback_article.py`
- Generated article: `paper/when_preferences_move_faster_than_equilibrium_v1.html`
- Generated report: `results/material_feedback_report.md`

## Instructions For Future Sessions

Start from the material-capacity loop. Do not restore the old
fast-closure-only language as the main frame. It can remain as a special case
in the appendix, but the live manuscript should lead with:

1. plain-language puzzle;
2. material-capacity feedback loop;
3. analytical classification;
4. empirical strategy;
5. Nash and selection interpretation.

Avoid prominent use of "closure." Use "preference formation," "settling," or
"subjective payoff formation" unless discussing old notes.
