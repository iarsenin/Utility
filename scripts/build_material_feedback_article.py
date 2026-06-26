#!/usr/bin/env python3
"""Build the current HTML article from generated model outputs."""

from __future__ import annotations

import csv
from html import escape
from pathlib import Path
from string import Template
import sys


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper" / "when_preferences_move_faster_than_equilibrium_v1.html"


def fmt(value: str) -> str:
    if value in {"True", "False"}:
        return "yes" if value == "True" else "no"
    if value.isdigit():
        return f"{int(value):,}"
    try:
        number = float(value)
    except ValueError:
        return value
    if number != number:
        return ""
    return f"{number:.3f}"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def enrich_equilibria(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    counters: dict[str, int] = {}
    enriched = []
    for row in rows:
        scenario = row["scenario"]
        counters[scenario] = counters.get(scenario, 0) + 1
        stable = row["stable"] == "True"
        slope = float(row["drift_slope"])
        capacity = float(row["capacity"])
        if stable and capacity < 0.2:
            interpretation = "low-capacity trap"
        elif stable and capacity > 0.7:
            interpretation = "high-capacity state"
        elif not stable and slope > 0:
            interpretation = "threshold"
        elif stable:
            interpretation = "stable state"
        else:
            interpretation = "unstable state"
        enriched.append({**row, "interpretation": interpretation})
    return enriched


def enrich_audit(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    enriched = []
    for row in rows:
        updated = dict(row)
        updated["draws"] = f"{int(float(updated['draws'])):,}"
        for key in [
            "one_stable_state_rate",
            "multiple_stable_states_rate",
            "no_interior_stable_state_rate",
            "lower_boundary_state_rate",
            "low_high_trap_rate",
            "median_trap_threshold_when_present",
        ]:
            updated[key] = f"{100 * float(updated[key]):.1f}%"
        enriched.append(updated)
    return enriched


def html_table(
    rows: list[dict[str, str]],
    columns: list[tuple[str, str]],
    numeric: set[str] | None = None,
) -> str:
    numeric = numeric or set()
    header = "".join(f"<th>{escape(label)}</th>" for key, label in columns)
    body_rows = []
    for row in rows:
        cells = []
        for key, _ in columns:
            klass = ' class="num"' if key in numeric else ""
            cells.append(f"<td{klass}>{escape(fmt(row.get(key, '')))}</td>")
        body_rows.append("<tr>" + "".join(cells) + "</tr>")
    return "<table><thead><tr>" + header + "</tr></thead><tbody>" + "\n".join(body_rows) + "</tbody></table>"


def build_article() -> str:
    equilibria = enrich_equilibria(
        read_csv(ROOT / "results" / "tables" / "material_feedback_equilibria.csv")
    )
    audit = enrich_audit(read_csv(ROOT / "results" / "tables" / "material_feedback_parameter_audit.csv"))
    equilibria_table = html_table(
        equilibria,
        [
            ("scenario", "Scenario"),
            ("capacity", "Capacity K"),
            ("substitute_share", "Substitute share p"),
            ("drift_slope", "Local slope"),
            ("stable", "Stable"),
            ("interpretation", "Interpretation"),
        ],
        {"capacity", "substitute_share", "drift_slope"},
    )
    audit_table = html_table(
        audit,
        [
            ("feedback_class", "Feedback class"),
            ("draws", "Draws"),
            ("one_stable_state_rate", "One stable"),
            ("multiple_stable_states_rate", "Multiple stable"),
            ("no_interior_stable_state_rate", "No interior stable"),
            ("lower_boundary_state_rate", "Lower boundary"),
            ("low_high_trap_rate", "Low-high trap"),
            ("median_trap_threshold_when_present", "Median trap threshold"),
        ],
        {"capacity", "substitute_share", "drift_slope"},
    )

    template = Template(
        r"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>When Preferences Move Faster Than Equilibrium</title>
  <script>
    window.MathJax = {
      tex: {
        inlineMath: [['\\(', '\\)']],
        displayMath: [['\\[', '\\]']],
        processEscapes: true,
        tags: 'none'
      },
      chtml: {
        scale: 1.03,
        linebreaks: { automatic: true }
      }
    };
  </script>
  <script defer src="../vendor/mathjax/es5/tex-chtml.js"></script>
  <style>
    :root {
      --ink: #151719;
      --muted: #5f6368;
      --rule: #ded8cf;
      --soft: #f6f8fb;
      --box: #fbfcfe;
      --accent: #c74332;
      --accent-2: #007f83;
      --accent-soft: #fff1ee;
      --theorem: #f8fbf5;
      --theorem-rule: #78a55a;
      --warning: #fff8ed;
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      background: #ffffff;
      color: var(--ink);
      font-family: Charter, "Iowan Old Style", Georgia, serif;
      font-size: 19px;
      line-height: 1.62;
    }

    main {
      counter-reset: equation figure table lemma proposition corollary theorem example;
      max-width: 980px;
      margin: 0 auto;
      padding: 48px 30px 86px;
    }

    header {
      border-bottom: 1px solid var(--rule);
      margin-bottom: 34px;
      padding-bottom: 26px;
    }

    h1, h2, h3, h4, .meta, .subtitle, .label, table, figcaption, .table-title, .takeaway, .note, .theorem-title {
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    h1, h2, h3, h4 {
      color: #101418;
      line-height: 1.22;
    }

    h1 {
      font-size: clamp(2.2rem, 5.7vw, 4.25rem);
      letter-spacing: 0;
      margin: 0 0 12px;
    }

    h2 {
      border-top: 1px solid var(--rule);
      font-size: 1.58rem;
      margin: 46px 0 15px;
      padding-top: 26px;
    }

    h3 {
      font-size: 1.14rem;
      margin: 30px 0 9px;
    }

    p { margin: 0 0 16px; }

    a {
      color: #1e6078;
      text-decoration: underline;
      text-decoration-thickness: 1px;
      text-underline-offset: 2px;
    }

    ul, ol {
      margin: 0 0 18px 1.25rem;
      padding: 0;
    }

    li { margin: 5px 0; }

    .subtitle {
      color: var(--accent);
      font-size: 1.25rem;
      font-weight: 650;
      margin: 0 0 16px;
    }

    .meta {
      color: var(--muted);
      font-size: 0.95rem;
      margin: 0 0 6px;
    }

    .abstract {
      background: var(--soft);
      border-left: 5px solid var(--accent);
      margin: 24px 0 34px;
      padding: 19px 23px 17px;
    }

    .abstract h2 {
      border-top: 0;
      font-size: 1.24rem;
      margin: 0 0 10px;
      padding: 0;
    }

    .lede {
      color: #26313c;
      font-size: 1.12rem;
      line-height: 1.58;
    }

    .result-strip {
      border-top: 3px solid var(--accent);
      border-bottom: 1px solid var(--rule);
      display: grid;
      gap: 14px;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      margin: 26px 0 30px;
      padding: 17px 0 19px;
    }

    .result-strip strong {
      color: var(--accent-2);
      display: block;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 0.82rem;
      letter-spacing: 0.03em;
      margin-bottom: 4px;
      text-transform: uppercase;
    }

    .result-strip span {
      color: #26313c;
      display: block;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 0.9rem;
      line-height: 1.36;
    }

    .note, .takeaway, .reader-result {
      background: var(--accent-soft);
      border: 1px solid #f0c8bf;
      color: #4d2119;
      font-size: 0.98rem;
      line-height: 1.5;
      margin: 22px 0;
      padding: 14px 16px;
    }

    .reader-result {
      background: #f8fbf5;
      border-color: #d9e8ce;
      border-left: 4px solid var(--theorem-rule);
      color: #243420;
    }

    .reader-result strong {
      color: #385928;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    .warning {
      background: var(--warning);
      border-color: #ecd3aa;
      color: #593b12;
    }

    .equation {
      background: var(--box);
      border: 1px solid var(--rule);
      border-left: 5px solid var(--accent);
      counter-increment: equation;
      margin: 22px auto;
      max-width: 900px;
      overflow-x: auto;
      overflow-y: hidden;
      padding: 14px 62px 12px 18px;
      position: relative;
      -webkit-overflow-scrolling: touch;
    }

    .equation::after {
      color: var(--accent);
      content: "(" counter(equation) ")";
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 0.9rem;
      font-weight: 650;
      position: absolute;
      right: 18px;
      top: 50%;
      transform: translateY(-50%);
    }

    .equation .label {
      color: #756f66;
      display: block;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 0.72rem;
      font-weight: 750;
      letter-spacing: 0.06em;
      margin-bottom: 4px;
      text-transform: uppercase;
    }

    .equation mjx-container[jax="CHTML"][display="true"] {
      margin: 0.2em 0;
      max-width: 100%;
      overflow-x: auto;
      overflow-y: hidden;
      text-align: center !important;
    }

    .theorem {
      background: var(--theorem);
      border: 1px solid #d9e8ce;
      border-left: 4px solid var(--theorem-rule);
      margin: 24px 0;
      padding: 15px 18px 13px;
    }

    .theorem[data-kind="Lemma"] { counter-increment: lemma; }
    .theorem[data-kind="Proposition"] { counter-increment: proposition; }
    .theorem[data-kind="Corollary"] { counter-increment: corollary; }
    .theorem[data-kind="Theorem"] { counter-increment: theorem; }
    .theorem[data-kind="Example"] { counter-increment: example; }
    .theorem[data-kind="Lemma"] .theorem-title::before { content: "Lemma " counter(lemma) ". "; }
    .theorem[data-kind="Proposition"] .theorem-title::before { content: "Proposition " counter(proposition) ". "; }
    .theorem[data-kind="Corollary"] .theorem-title::before { content: "Corollary " counter(corollary) ". "; }
    .theorem[data-kind="Theorem"] .theorem-title::before { content: "Theorem " counter(theorem) ". "; }
    .theorem[data-kind="Example"] .theorem-title::before { content: "Example " counter(example) ". "; }

    .theorem-title {
      color: #385928;
      display: block;
      font-size: 0.91rem;
      font-weight: 750;
      letter-spacing: 0.01em;
      margin-bottom: 8px;
    }

    .proof {
      color: #2d343b;
      font-size: 0.96em;
    }

    figure {
      counter-increment: figure;
      margin: 30px 0;
    }

    figure img {
      background: #fffaf2;
      border: 1px solid #eadfce;
      display: block;
      height: auto;
      max-width: 100%;
      width: 100%;
    }

    figcaption {
      color: var(--muted);
      font-size: 0.9rem;
      line-height: 1.45;
      margin-top: 8px;
      max-width: 860px;
    }

    figcaption::before {
      color: var(--ink);
      content: "Figure " counter(figure) ". ";
      font-weight: 700;
    }

    .table-title { counter-increment: table; }
    .table-title::before { content: "Table " counter(table) ". "; font-weight: 700; }

    table {
      border-collapse: collapse;
      font-size: 0.92rem;
      line-height: 1.4;
      margin: 18px 0 24px;
      width: 100%;
    }

    th, td {
      border-bottom: 1px solid var(--rule);
      padding: 9px 10px;
      text-align: left;
      vertical-align: top;
    }

    th {
      background: #fbfaf7;
      color: #26313c;
      font-weight: 720;
    }

    tbody tr:nth-child(even) td { background: #fcfcfd; }
    .num { font-variant-numeric: tabular-nums; text-align: right; white-space: nowrap; }
    .small { color: var(--muted); font-size: 0.92rem; line-height: 1.48; }
    .refs p { font-size: 0.94rem; line-height: 1.42; margin-bottom: 10px; }

    @media (max-width: 720px) {
      body { font-size: 17px; }
      main { padding: 30px 18px 60px; }
      .equation { padding-right: 48px; }
      .equation::after { right: 12px; }
      .result-strip { grid-template-columns: 1fr; }
      .table-title::after {
        color: var(--muted);
        content: "Wide tables scroll horizontally on small screens.";
        display: block;
        font-size: 0.72rem;
        font-weight: 520;
        letter-spacing: 0;
        margin-top: 2px;
      }
      table {
        display: block;
        max-width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        box-shadow: inset -18px 0 18px -18px rgba(21, 23, 25, 0.55);
      }
    }
  </style>
</head>
<body>
<main>
  <header>
    <h1>When Preferences Move Faster Than Equilibrium</h1>
    <p class="subtitle">Endogenous utility, material-capacity feedback, and Nash equilibrium</p>
    <p class="meta"><strong>Working paper draft.</strong> Prepared for comment.</p>
    <p class="meta"><strong>JEL codes:</strong> C72, D01, D11, D83, D91, I12, J13. <strong>Keywords:</strong> endogenous preferences, utility, Nash equilibrium, material capacity, social media, AI, addiction, fertility, loneliness, selection.</p>
  </header>

  <section class="abstract">
    <h2>Abstract</h2>
    <p>Economic models often treat preferences as fixed. This article studies cases where environments quickly change what feels rewarding, while the real capacities needed for other choices change slowly. A feed, peer group, market, institution, or AI system can make a substitute behavior attractive today. The resulting choice can then change the capacity that would make tomorrow's alternatives attractive: social skill, solvency, metabolic health, family agency, learning, trust, or institutional competence.</p>
    <p>The central result is a feedback classification. When capacity remains protective, the system self-corrects. When the substitute erodes the same capacity that would make it less attractive, the model can have two stable states: a low-capacity state with heavy substitute use and a high-capacity state with little substitute use. A threshold separates them. When damage overwhelms repair, the high-capacity state can disappear rather than merely become harder to reach. These outcomes can arise even when each choice is rational under the payoff criterion formed at the moment of choice.</p>
    <p>The framework gives a disciplined test for candidate applications such as low fertility, loneliness, dating retreat, AI companions, online betting and debt, ultra-processed food, appearance arms races, political outrage, migration backlash, and international trust. It does not claim that these phenomena have one cause. It asks: what forms the subjective payoff, what substitute behavior is chosen, what material capacity is changed, and does the loop build capacity, deplete it, or trap the system below a threshold?</p>
  </section>

  <section>
    <h2>1. The Puzzle In Plain Words</h2>
    <p class="lede">People can make coherent choices inside a payoff criterion that the environment helped produce. The choice may be rational, sincere, and stable in the short run, while still weakening the slower capacity that would make a different life possible.</p>

    <p>A teenager who retreats from courtship into screens may not be confused at the moment of choice. An isolated adult may rationally prefer an AI companion tonight. A bettor may value the next in-game wager as participation in the match. A young couple may sincerely delay children because the visible threshold for adequate parenthood has moved. A citizen may prefer outrage media because institutional verification feels remote while a familiar personality feels fluent and alive.</p>

    <p>The hard question is not whether the subjective payoff is "real." In economic terms it is real if it guides choice. The hard question is whether the system that forms that payoff builds or depletes the material capacity being evaluated. Capacity means the stock that matters for the application: social skill, friendship, solvency, metabolic health, fertility agency, learning, trust, institutional competence, or demographic continuity.</p>

    <p>Three terms do the work. A <em>subjective payoff</em> is what the agent maximizes at the moment of choice. A <em>substitute behavior</em> is the action that gives immediate relief or reward while possibly replacing practice of another capacity. A <em>material evaluator</em> is the criterion used to judge the longer-run consequence after the capacity has been named. For example, an AI companion may reduce loneliness tonight; the material evaluator asks whether it also builds friendship capacity outside the companion system.</p>

    <div class="result-strip">
      <div><strong>Subjective payoff</strong><span>The criterion used at choice time, after exposure and current capacity have shaped what feels rewarding.</span></div>
      <div><strong>Nash step</strong><span>The consistency condition applied to the induced game. It is not a welfare certificate.</span></div>
      <div><strong>Material capacity</strong><span>The slower stock used to evaluate consequences and to shape future payoffs.</span></div>
      <div><strong>Selection</strong><span>The long-run question: which rules reproduce capacity, spread, or disappear?</span></div>
    </div>

    <p>The old fixed-preference account is enough when exposure changes information, prices, or constraints while leaving the relevant payoff criterion stable. It is not enough when the environment changes the criterion and the resulting action changes the future environment of choice. That second case is the object here.</p>
  </section>

  <section>
    <h2>2. The Feedback Loop</h2>
    <p>The model has two clocks. On the fast clock, a preference-forming rule maps current capacity and exposure into the subjective payoff used for choice. On the slow clock, choices update the material capacity. No claim is made that every institution, population process, or cultural process is slow. If an institutional rule changes as quickly as the preference state, it belongs in the fast environment; if it changes with capacity, it belongs in the slow state. The empirical task is to estimate the clocks, not assume them.</p>

    <p>The simplest version uses one normalized material capacity, \(K\), between 0 and 1. High \(K\) means the person or system has more of the relevant stock: social competence, liquidity, metabolic resilience, trust, institutional capability, or realized agency. The symbol \(p\) is the fast-settled probability for an individual or share for a population choosing a substitute behavior. A substitute is not automatically bad. It is the behavior whose short-run subjective appeal may either bridge back to capacity or crowd it out. Formally, the fast comparison is between preference formation and material-capacity motion; Nash equilibrium remains a static consistency condition applied after subjective payoffs are formed.</p>

    <p>Read the equations this way before reading the symbols. More exposure makes the substitute more attractive. More capacity makes the substitute less attractive. Substitute use can damage or crowd out capacity. Repair can rebuild capacity, but repair is hardest when capacity is already very low.</p>

    <div class="equation">
      <span class="label">Fast subjective payoff formation</span>
      \[
        p(K,z)=\frac{1}{1+\exp[-\beta(q+z-\rho K)]}
      \]
    </div>

    <p>Here \(z\) is exposure or inducement, \(q\) is the baseline pull of the substitute, \(\beta\) is sensitivity, and \(\rho\) measures how strongly material capacity protects against the substitute becoming dominant. The sign convention is intentional: when \(K\) is high, the substitute is less likely to take over because the underlying capacity makes the non-substitute life more feasible or rewarding.</p>

    <div class="equation">
      <span class="label">Slow material-capacity dynamic</span>
      \[
        \dot K=\alpha+rK^2(1-K)-dK-Lp(K,z)
      \]
    </div>

    <p>The term \(\alpha\) is baseline repair. The term \(rK^2(1-K)\) says that practice-based repair is weak when capacity is very low, stronger at intermediate capacity, and limited near the top. The term \(dK\) is maintenance decay. The term \(Lp(K,z)\) is damage or crowding out from the substitute. Because \(K\) is normalized, the model is interpreted as a projected dynamic on \([0,1]\): if the unprojected drift points below zero or above one, the boundary is a feasible boundary state. The scalar form is deliberately austere: it is a normal form for a feedback loop, not a claim that all domains share one psychology.</p>

    <div class="reader-result">
      <strong>Why this form?</strong> It is the smallest model that allows three empirically distinct cases: self-correction, a threshold trap, and collapse-prone capacity loss. A linear repair term would make the low-capacity region too easy to escape. A purely exogenous taste shock would miss the feedback from material capacity back into the next subjective payoff.
    </div>
  </section>

  <section>
    <h2>3. What The Model Says</h2>
    <p>The model's first result is reassuring: fast preference formation does not automatically imply bad outcomes. If capacity remains high enough, or if the substitute does not damage capacity much, the system can converge to a high-capacity state.</p>

    <p>The second result is the trap. A low-capacity state can be stable because low capacity makes the substitute attractive, and the substitute prevents the capacity from rebuilding. A high-capacity state can also be stable because capacity makes the substitute less attractive, and lower substitute use allows capacity to rebuild. The unstable middle point is the threshold. Moving just above it changes the long-run destination; moving just below it does not.</p>

    <p>The third result matters for policy and design: more severe feedback need not simply make hysteresis larger. It can remove the interior high-capacity equilibrium. In plain words, there is a difference between a system that is trapped below a threshold and a system whose repair process has been overwhelmed.</p>

    <div class="reader-result">
      <strong>Relation to prior work.</strong> <a href="#ref-stigler-becker">Stigler and Becker</a> move apparent taste changes into shadow prices and consumption capital. <a href="#ref-grossman">Grossman</a> models health as a durable capital stock. <a href="#ref-becker-murphy">Becker and Murphy</a> model addiction through intertemporal complementarity. <a href="#ref-bowles">Bowles</a>, <a href="#ref-bisin">Bisin and Verdier</a>, and <a href="#ref-bernheim-chosen">Bernheim et al.</a> put preference formation inside institutions, transmission, or chosen worldviews. <a href="#ref-koszegi-rabin">Koszegi and Rabin</a> and <a href="#ref-genicot-ray">Genicot and Ray</a> make reference points and aspirations endogenous. <a href="#ref-brock-durlauf">Brock and Durlauf</a> and <a href="#ref-arthur">Arthur</a> show how social interactions and increasing returns create multiple states. Recommender-system work such as <a href="#ref-jiang">Jiang et al.</a> and <a href="#ref-kleinberg">Kleinberg, Mullainathan, and Raghavan</a> supplies the modern preference-forming environment. The contribution here is the timing discipline: fast subjective payoff formation, ordinary equilibrium choice, and slow capacity feedback in one loop.
    </div>

    <figure>
      <img src="../results/figures/material_feedback_phase.svg" alt="Phase-line chart for material-capacity feedback">
      <figcaption>Phase-line diagnostic. The self-correcting calibration has one stable high-capacity state. The capacity-trap calibration has two stable states separated by an unstable threshold. Higher exposure lowers the high-capacity state and raises the substitute share at that state.</figcaption>
    </figure>

    <figure>
      <img src="../results/figures/material_feedback_paths.svg" alt="Capacity paths from different starting values">
      <figcaption>Path diagnostic. Under the same preference-forming rule, an initial condition below the unstable threshold converges to the low-capacity state, while an initial condition above the threshold converges to the high-capacity state. A repair intervention can move the same low initial condition to the high-capacity basin.</figcaption>
    </figure>

    <p class="table-title">Equilibria in the scalar model.</p>
    <p class="small">A negative local slope means the state is stable; a positive local slope marks a threshold. In the table, shares are rounded, so values shown as 1.000 are very close to one, not assumed exactly equal to one.</p>
    $equilibria_table

    <p class="table-title">Random parameter audit.</p>
    <p class="small">Entries are shares of parameter draws. The audit is designed to check mechanism robustness, not to estimate real-world frequencies.</p>
    $audit_table

    <p class="table-title">Audit design.</p>
    <p class="small">The audit uses seed 20260626 and 3,000 draws per class. Classes differ only in substitute damage \(L\), sensitivity \(\beta\), and capacity protection \(\rho\). Shared ranges are \(\alpha\in[0.10,0.28]\), \(r\in[1,4]\), \(d\in[0.22,0.78]\), \(q\in[0.35,0.65]\), and \(z\in[-0.05,0.10]\).</p>
    <table>
      <thead><tr><th>Feedback class</th><th>\(L\)</th><th>\(\beta\)</th><th>\(\rho\)</th><th>Interpretation</th></tr></thead>
      <tbody>
        <tr><td>Weak feedback</td><td>[0.04, 0.12]</td><td>[8, 18]</td><td>[0.55, 1.00]</td><td>Low substitute damage and moderate sensitivity.</td></tr>
        <tr><td>Trap-prone feedback</td><td>[0.12, 0.24]</td><td>[10, 24]</td><td>[0.70, 1.20]</td><td>Intermediate damage and sharper capacity protection.</td></tr>
        <tr><td>Collapse-prone feedback</td><td>[0.20, 0.36]</td><td>[14, 30]</td><td>[0.75, 1.35]</td><td>High damage and high sensitivity, often pushing the projected state to the lower boundary.</td></tr>
      </tbody>
    </table>

    <figure>
      <img src="../results/figures/material_feedback_audit.svg" alt="Parameter audit for capacity traps">
      <figcaption>Random parameter audit. Weak feedback mostly produces one stable state. Trap-prone feedback produces the highest share of low-high traps. Collapse-prone feedback more often reaches the lower boundary of the projected capacity interval. The audit is a mechanism check, not an empirical estimate.</figcaption>
    </figure>
  </section>

  <section>
    <h2>4. Why This Helps With Real Puzzles</h2>
    <p>The model is useful only when it explains something that a stable-preference story leaves obscure. The candidate applications below are not proofs that one mechanism explains everything. The test is concrete: identify the substitute, the capacity, the feedback sign, and the evidence that would distinguish capacity feedback from ordinary constraints.</p>

    <p class="table-title">Ten places to test the mechanism.</p>
    <table>
      <thead>
        <tr><th>Domain</th><th>Substitute</th><th>Capacity</th><th>Preference-forming rule</th><th>Non-obvious prediction</th></tr>
      </thead>
      <tbody>
        <tr><td>Low fertility</td><td>Delay, smaller family size, child-free status competition</td><td>Family agency, partner-market capacity, household formation</td><td>Status comparison raises the subjective threshold for acceptable parenthood.</td><td>Policy works better when it lowers material barriers and the perceived standard of "responsible" parenthood.</td></tr>
        <tr><td>Loneliness</td><td>Mediated contact, scrolling, parasocial connection</td><td>Friendship skill, ordinary social practice, trust</td><td>Mediated substitutes reduce the immediate cost of solitude.</td><td>Short-run relief can coexist with long-run social-capacity loss.</td></tr>
        <tr><td>Dating retreat</td><td>Avoidance, pornography, games, low-risk digital interaction</td><td>Courtship confidence, mixed social networks, intimacy practice</td><td>Rejection avoidance and online substitutes raise the subjective payoff of non-courtship.</td><td>Small nudges fail below the threshold; assisted practice can work if it moves people across it.</td></tr>
        <tr><td>AI companions</td><td>Always-available synthetic relationship</td><td>Social capacity outside the AI system</td><td>Always-available response makes synthetic companionship highly rewarding.</td><td>Companions help when they bridge to human practice and harm when they replace it.</td></tr>
        <tr><td>Sports betting and debt</td><td>Micro-wagers, frictionless checkout, identity purchases</td><td>Liquidity, savings, credit resilience</td><td>Frictionless risk turns fandom or shopping into repeated immediate reward.</td><td>Financial harm is largest where losses reduce future self-control and raise the appeal of further risk.</td></tr>
        <tr><td>Food and GLP-1s</td><td>Hyper-palatable food; repair via appetite-changing medicine</td><td>Metabolic health, appetite regulation, agency</td><td>Food environments or medicines alter the subjective reward of consumption.</td><td>Preference change can be repair, not manipulation, if it builds durable capacity.</td></tr>
        <tr><td>Appearance arms races</td><td>Filters, cosmetic escalation, lookmaxxing advice</td><td>Body satisfaction, identity flexibility, financial resilience</td><td>Ranked visual comparison makes yesterday's enhancement today's baseline.</td><td>Temporary fashion becomes a trap when the old baseline remains unacceptable after exposure fades.</td></tr>
        <tr><td>Political outrage</td><td>Outrage feeds, parasocial news trust</td><td>Verification capacity, institutional trust, civic patience</td><td>Feeds and personalities make anger and familiarity more rewarding than correction.</td><td>Distrust can become self-confirming even when some grievances are real.</td></tr>
        <tr><td>Migration</td><td>Threat framing, withdrawal, status defense</td><td>Integration capacity, state competence, local trust</td><td>Border images and identity cues change the subjective payoff of openness.</td><td>Public willingness to cooperate can move faster than labor-market or demographic fundamentals.</td></tr>
        <tr><td>Alliances</td><td>Unilateralism, burden-sharing resentment, contempt for partners</td><td>Credible commitment, alliance trust, defense coordination</td><td>Domestic media can change the subjective payoff of reliability.</td><td>Alliance capacity erodes when defection becomes a locally rational political equilibrium.</td></tr>
      </tbody>
    </table>

    <h3>Fertility And The Moving Standard Of Readiness</h3>
    <p><a href="#ref-oecd">OECD</a>, <a href="#ref-unfpa-2025">UNFPA</a>, <a href="#ref-eurostat-fertility">Eurostat</a>, and <a href="#ref-cdc-births">CDC/NCHS</a> document low fertility, delayed births, and gaps between desired and realized family life across many high-income settings. A standard budget story is essential: housing, care costs, income risk, and gendered burdens matter. The feedback model adds a second channel. <a href="#ref-mahler">Mahler, Tertilt, and Yum</a> study social comparisons in low-fertility policy concerns, and <a href="#ref-aassve">Aassve et al.</a> emphasize family ideals in low-fertility societies. If social comparison raises the subjective threshold for being ready, delay can be rational under the induced payoff. Delay then changes partner markets, age constraints, housing expectations, and confidence, which can further raise the subjective cost of parenthood.</p>

    <p>The model does not say people owe society children. It says that "revealed preference" is ambiguous when the preference-forming environment also changes the feasible capacity for later choice. A policy that only transfers money may disappoint if the standard of acceptable parenthood keeps moving. A policy that only moralizes family formation may fail because the material constraint is real. A falsifiable prediction is that family policy should move behavior partly through measured readiness standards, not only disposable income or formal eligibility.</p>

    <h3>Loneliness, Dating, And Synthetic Ease</h3>
    <p>The <a href="#ref-who-loneliness">WHO Commission on Social Connection</a> and the <a href="#ref-surgeon-general">US Surgeon General</a> treat loneliness and disconnection as health and community problems. Yet modern economies provide abundant mediated contact. The capacity loop offers one testable explanation for the paradox. If mediated substitutes reduce the immediate pain of loneliness but reduce practice at initiating and repairing relationships, then future human interaction becomes harder. The person is not irrational. The local payoff changed, and the capacity needed to escape the substitute weakened.</p>

    <p>Dating retreat is the same loop with higher stakes. <a href="#ref-ueda">Ueda et al.</a> document increases in sexual inactivity among US adults aged 18 to 44 from 2000 to 2018, and <a href="#ref-cdc-yrbs">CDC youth surveys</a> show long-run changes in adolescent sexual behavior. Apps, pornography, gaming, safety concerns, reputational risk, economic insecurity, and rejection avoidance can all raise the payoff of non-courtship. The capacity test is whether avoidance reduces later confidence, mixed social networks, and opportunity, or whether it simply reflects safer and more autonomous choice.</p>

    <p>AI companions sharpen the distinction. <a href="#ref-hbs-ai">De Freitas et al.</a> find that AI companions can reduce loneliness; <a href="#ref-common-sense-ai">Common Sense Media</a> reports teen use of AI companions; <a href="#ref-ai-companions">Malfacini</a> emphasizes both risks and benefits. The model says not to classify AI companionship as good or bad in the abstract. It asks whether the design is a bridge or a sink. A bridge lowers anxiety, rehearses social skill, and returns the person to human connection with more capacity. A sink gives enough reward that the outside capacity decays. The measurable outcomes are offline contact, friendship repair attempts, social anxiety, and later human interaction, not only loneliness tonight.</p>

    <h3>Reward Loops: Betting, Debt, Food, And Appearance</h3>
    <p>Online sports betting is a clean test case because it is measurable and repeated. <a href="#ref-nber-sports-betting">Baker et al.</a> link sports-betting access to financial stress for vulnerable households, while the <a href="#ref-aga-revenue">American Gaming Association</a> tracks the growth of the legal market. In the model, the relevant capacity is liquidity and financial resilience. A small wager can be locally rational as entertainment, identity, or attention. Losses can then weaken the capacity that would make restraint easier tomorrow.</p>

    <p>Food and medicine show the positive side of the same logic. <a href="#ref-cdc-upf">CDC/NCHS</a> documents high ultra-processed-food intake. <a href="#ref-wilding-semaglutide">Wilding et al.</a> show large weight effects for semaglutide in clinical trials. The model interprets appetite or craving change as a candidate preference-formation channel to be measured, not as something proven by weight loss alone. <a href="#ref-wilding-withdrawal">Wilding et al.'s extension study</a> also documents weight regain after treatment withdrawal, which is exactly the model's durability question. Does the intervention build a stable metabolic and behavioral state, or does capacity depend entirely on continued external control?</p>

    <p>Appearance markets and lookmaxxing, the online subculture of optimizing appearance through routines, ratings, and procedures, are positional versions of the same loop. The <a href="#ref-asps-2024">American Society of Plastic Surgeons</a> documents a large cosmetic-procedure market. The model does not condemn cosmetic choice. It identifies an arms-race condition: if each visible enhancement raises the future standard, the old baseline loses subjective acceptability. The material capacity may be body satisfaction, financial resilience, or identity flexibility. A fashion is reversible; a trap is not.</p>

    <h3>Politics, Migration, And International Trust</h3>
    <p><a href="#ref-pew-news-influencers">Pew</a> documents the role of news influencers, while platform-ranking studies such as <a href="#ref-pnas-divisive">PNAS Nexus</a> and recommender-system research show how engagement criteria can amplify divisive material. <a href="#ref-gallup-institutions">Gallup</a> and <a href="#ref-pew-trust">Pew</a> document low institutional trust. The model's contribution is not "people are manipulated." It is more precise: if anger and familiar personalities become the rewarding way to process public life, then verification and institutional patience can become subjectively unrewarding. That erodes the capacity needed to correct distrust. A strategic version is an outrage game: each actor may escalate because restraint loses attention under the induced payoff, while the collective equilibrium lowers trust.</p>

    <p>Migration is an international version of the capacity loop. <a href="#ref-oecd-migration">OECD</a> reports high migration flows, and <a href="#ref-unhcr-global-trends">UNHCR</a> reports historically high forced displacement. Aging economies may need labor and care capacity, but publics may experience migration through housing pressure, border images, identity threat, or state-capacity failure. <a href="#ref-pew-border">Pew</a> and <a href="#ref-gallup-immigration">Gallup</a> show that salience and opinion can move. If the mechanism is active, the largest political swings should occur where exposure changes the subjective payoff of openness faster than labor-market or demographic fundamentals change.</p>

    <p>Alliances are separate from migration. <a href="#ref-pew-nato">Pew's NATO surveys</a> show generally favorable views of NATO across many member countries, but alliance politics repeatedly turns on domestic narratives about reliability, burden sharing, and respect. The capacity is credible commitment: partners invest and coordinate only when they believe promises will hold. A domestic media environment can make unilateralism feel rewarding even when the material evaluator is alliance capacity. The Nash version is a coordination problem: if each country defects because it expects others to defect, the equilibrium can validate the distrust that produced it.</p>
  </section>

  <section>
    <h2>5. Empirical Strategy</h2>
    <p>The model becomes empirical when the capacity stock is named and measured. For fertility, capacity may include partner-market opportunity, housing security, age constraints, and perceived readiness. For loneliness, it may include friendship frequency, social anxiety, and offline practice. For betting, it may include savings, credit scores, missed payments, and debt service. For politics, it may include institutional trust, correction acceptance, and cross-cutting exposure.</p>

    <p>The plain test has three steps. First, do exposure shocks change what feels rewarding? Second, does the changed payoff alter behavior? Third, does the behavior change later capacity in a way that predicts the next payoff state? Without all three links, the case is weaker than the model.</p>

    <p>The minimal panel test separates within-person or within-place feedback from stable heterogeneity. Let \(\theta_{it}\) be a measured or latent subjective payoff state, \(K_{it}\) a material capacity, \(z_{it}\) exposure, and \(x_{it}\) behavior.</p>

    <div class="equation">
      <span class="label">Empirical preference-formation equation</span>
      \[
        \theta_{i,t+1}=\alpha_i+\lambda_t+\varphi\theta_{it}+\gamma z_{it}-\rho K_{it}+u_{i,t+1}
      \]
    </div>

    <div class="equation">
      <span class="label">Empirical capacity-feedback equation</span>
      \[
        K_{i,t+1}=\eta_i+\tau_t+\psi K_{it}+b x_{it}+c\theta_{it}+v_{i,t+1}
      \]
    </div>

    <div class="equation">
      <span class="label">Empirical behavior equation</span>
      \[
        x_{it}=m(\theta_{it},K_{it},z_{it},W_{it})+\varepsilon_{it}
      \]
    </div>

    <p>Here \(x_{it}\) is the observed substitute behavior and \(W_{it}\) collects prices, income, constraints, and other controls. A fixed-preference account is adequate when \(\gamma\), \(\rho\), \(b\), and \(c\) are small or when the apparent relationship disappears after those controls and stable heterogeneity are included. A feedback account becomes plausible when exposure changes the payoff state, the payoff state changes behavior, and behavior changes the future capacity that predicts the later payoff state.</p>

    <p>Identification requires care. <a href="#ref-lachaab">State-space choice models</a> are useful when preference parameters are latent. <a href="#ref-hamaker">Random-intercept cross-lagged panel models</a> help separate within-person movement from stable between-person differences. Randomized deactivation and feed experiments, such as <a href="#ref-allcott-social">Allcott et al.</a>, <a href="#ref-braghieri-social">Braghieri, Levy, and Makarin</a>, and <a href="#ref-guess-feed">Guess et al.</a>, are especially valuable because they shift exposure before all material stocks have had time to adjust.</p>
  </section>

  <section>
    <h2>6. Nash Equilibrium And Selection</h2>
    <p>Nash equilibrium is used as a mathematical consistency condition. The model changes the game to which Nash equilibrium is applied. First the preference-forming rule creates subjective payoffs. Then agents choose, possibly strategically, inside the induced game. The equilibrium can be fully coherent while the material capacity being evaluated moves in a bad direction.</p>

    <p>Selection also remains a method. The question is what selection acts on. If fast preference formation repeatedly produces the same payoff criterion from many initial states, then initial preference states are not the durable object. The durable objects are the rules, platforms, institutions, communities, and AI designs that keep producing payoff criteria and capacity paths.</p>

    <div class="reader-result">
      <strong>Selection claim.</strong> A preference-forming rule survives in the long run only if the capacity path it induces is compatible with the material evaluator that reproduces the system. If every available rule depletes the relevant capacity, the long-run conclusion can be disappearance rather than convergence to a fitter taste.
    </div>

    <p>This is where the Darwinian language becomes disciplined. "Fitness" is not a loose metaphor. It must be named: reproduction, solvency, health, learning, institutional continuity, military capacity, alliance reliability, or some other material evaluator. Different evaluators can disagree, and the disagreement is part of the economics.</p>
  </section>

  <section>
    <h2>7. Design And Policy</h2>
    <p>The policy levers are human before they are algebraic. Reduce exposure or inducement. Lower sensitivity to cues. Reduce harm per use. Strengthen repair. Make real capacity more rewarding and protective. In the scalar notation, these correspond to lowering \(z\), \(\beta\), or \(L\), raising \(\alpha\) or \(r\), and increasing the protective channel \(\rho\).</p>

    <p>The protective channel \(\rho\) has a dual role. Higher capacity protection can help people in the high-capacity region resist substitutes. But it can also sharpen the gap between low and high states, making thresholds more pronounced. This is why repair and threshold-crossing matter as much as exposure reduction.</p>

    <p>That list is intentionally neutral about technology. A platform can worsen the loop by optimizing engagement, intensity, or retention while ignoring capacity. The same AI layer can improve the loop by helping people cross thresholds: practicing social skills, reducing anxiety, budgeting before betting, translating health goals into appetite changes, or making institutional verification easier and less humiliating.</p>

    <p>The strongest interventions are likely to be bridge designs. They make the desired outside capacity easier to practice and then hand the person back to the world stronger. The weakest interventions are likely to be pure warnings below a threshold. If the low-capacity state is stable, information alone may be absorbed into the same payoff criterion that created the trap.</p>
  </section>

  <section>
    <h2>8. Conclusion</h2>
    <p>Utility can be endogenous without being unreal. People optimize the payoff criterion they have, and modern preference-forming systems can change that criterion quickly. The economic problem is that material capacity often moves more slowly and feeds back into what will feel rewarding next.</p>

    <p>The model turns that observation into a tractable object. Fast subjective payoff formation plus slow capacity feedback yields self-correction, threshold traps, or collapse-prone dynamics. Nash equilibrium disciplines the strategic step after subjective payoffs are formed. Selection disciplines the long-run step after the capacity evaluator is named. The same mathematics can describe harmful loops and repair loops. That is why the framework is useful for current problems without becoming a theory that every current problem has the same cause.</p>
  </section>

  <section>
    <h2>Appendix A. General Formal Model</h2>
    <h3>A.1 Primitives</h3>
    <p>There is a finite set of players \(N=\{1,\ldots,n\}\). Player \(i\) has action set \(A_i\), and \(A=\prod_i A_i\). The slow state is \(K\in\mathcal K\). In applications \(K\) may be scalar or vector-valued. The slow environment is \(E\). The preference-forming rule is \(\ell\). Exposure or input is \(z\). Player \(i\)'s preference state is \(\theta_i\), and subjective utility is \(U_i(a;\theta_i,K,E,\ell)\). The material evaluator is \(G(K,a,E,\ell)\), or player-specific material payoff \(\pi_i(a,K,E,\ell)\) when needed. The material law of motion is \(F(K,x,E,\ell,z)\); it describes how equilibrium behavior changes the slow capacity state. The evaluator \(G\) ranks consequences, while \(F\) moves the capacity stock.</p>

    <div class="equation">
      <span class="label">Fast preference state</span>
      \[
        \varepsilon\dot\theta_i=H_i(\theta_i;K,E,\ell,z),\qquad 0<\varepsilon\ll 1
      \]
    </div>

    <p>If the fast dynamic has a selected attracting state, write it as \(C_i(K,E,\ell,z)\). This is the settled preference state used for choice while \(K\), \(E\), and \(\ell\) are held fixed on the fast clock.</p>

    <div class="equation">
      <span class="label">Settled subjective payoff</span>
      \[
        U_i^\star(a;K,E,\ell,z)=U_i(a;C_i(K,E,\ell,z),K,E,\ell)
      \]
    </div>

    <p>The induced game \(\Gamma^\star(K,E,\ell,z)\) has the original action sets and the settled subjective payoffs \(U_i^\star\). A mixed-strategy profile \(x\) is a Nash equilibrium of that induced game when every player's mixed strategy maximizes expected settled subjective payoff against the others.</p>

    <div class="equation">
      <span class="label">Nash step after payoff formation</span>
      \[
        x^\star\in NE\bigl(\Gamma^\star(K,E,\ell,z)\bigr)
      \]
    </div>

    <p>The slow state then changes according to a material law. If the induced game has several equilibria, the right-hand side is a differential inclusion; an equilibrium-selection rule can be added as an explicit primitive.</p>

    <div class="equation">
      <span class="label">Reduced slow dynamic</span>
      \[
        \dot K\in\left\{F(K,x,E,\ell,z):x\in NE\bigl(\Gamma^\star(K,E,\ell,z)\bigr)\right\}
      \]
    </div>

    <div class="theorem" data-kind="Proposition">
      <span class="theorem-title">Fast-limit reduction</span>
      <p>Assume that for each fixed \((K,E,\ell,z)\) in the region studied, the fast preference dynamic has a selected normally hyperbolic attracting branch \(C(K,E,\ell,z)\), with attraction uniform on the compact region considered. Assume also that the slow vector field is regular and that either the induced Nash equilibrium is locally single-valued and continuous or an explicit equilibrium-selection rule is included. Then along any interval on which the selected branch is maintained, the \(\varepsilon\to0\) limit is governed by the displayed reduced slow dynamic. If the induced Nash set is genuinely multivalued and no selection rule is imposed, the limit is a differential inclusion rather than a single ordinary differential equation.</p>
    </div>
    <p class="proof"><strong>Proof.</strong> Under the stated normal-hyperbolicity and uniform-attraction assumptions, the fast state approaches the selected branch while \(K\), \(E\), \(\ell\), and \(z\) are fixed on the fast clock; this is the standard singular-perturbation logic associated with <a href="#ref-fenichel">Fenichel</a>. Substituting that branch into subjective utility gives the induced game. Slow motion is then evaluated at the selected Nash equilibrium, or as a differential inclusion when selection is not imposed.</p>

    <h3>A.2 Local Feedback Multiplier</h3>
    <p>When \(K\) is scalar and the equilibrium branch is locally single-valued and differentiable, write the reduced law as \(\dot K=\Phi(K)\). The derivative of \(\Phi\) is the local feedback multiplier. For vector-valued \(K\), the same expression is a Jacobian and local stability depends on eigenvalues.</p>

    <div class="equation">
      <span class="label">Local feedback multiplier</span>
      \[
        D\Phi(K)=F_K+F_x\bigl(x_\theta C_K+x_K\bigr)
      \]
    </div>

    <p>The term \(C_K\) is the effect of capacity on the settled preference state. The term \(x_\theta\) is the effect of that preference state on behavior. The term \(F_x\) is the effect of behavior on the material capacity. Their product is the preference-capacity feedback loop. Negative feedback is locally self-correcting; sufficiently positive feedback can produce thresholds or instability.</p>

    <h3>A.3 Nash Invariance</h3>
    <p>Let \(BR_i^\star(x_{-i};K,E,\ell,z)\) be player \(i\)'s best-response correspondence in the induced subjective game, and let \(BR_i^\pi(x_{-i};K,E,\ell)\) be the best-response correspondence under the material payoff benchmark.</p>

    <div class="theorem" data-kind="Proposition">
      <span class="theorem-title">Best-response preservation</span>
      <p>If \(BR_i^\star(x_{-i};K,E,\ell,z)=BR_i^\pi(x_{-i};K,E,\ell)\) for every player and every opponent mixed profile, then the induced subjective game and the material benchmark game have the same mixed Nash equilibrium set at that state. The condition is sufficient; special games may have the same equilibrium set even when the full best-response correspondences differ.</p>
    </div>
    <p class="proof"><strong>Proof.</strong> A mixed Nash equilibrium is a fixed point of the product of best-response correspondences. Equality of the correspondences at every opponent profile gives equality of the fixed-point sets.</p>

    <h3>A.4 Selection Over Rules</h3>
    <p>Let \(s_\ell\) be the share or prevalence of preference-forming rule \(\ell\). Let \(\mathcal G_\ell\) be the long-run material growth, reproduction, persistence, or institutional payoff induced by the reduced capacity path under \(\ell\).</p>

    <div class="equation">
      <span class="label">Selection over preference-forming rules</span>
      \[
        \dot s_\ell=s_\ell\left(\mathcal G_\ell-\sum_r s_r\mathcal G_r\right)
      \]
    </div>

    <p>This equation is not an additional welfare assumption. It is a way to state the Darwinian question after the material evaluator has been named. If all available rules imply negative \(\mathcal G_\ell\), the limiting result may be disappearance of the population, institution, or practice rather than survival of a better preference type.</p>
  </section>

  <section>
    <h2>Appendix B. Scalar Capacity Model</h2>
    <p>The scalar model used for Figures 1-3 is the special case in which the fast subsystem directly yields a substitute share \(p(K,z)\) and the slow law is one-dimensional.</p>

    <div class="equation">
      <span class="label">Scalar substitute share</span>
      \[
        p(K,z)=\sigma\{\beta(q+z-\rho K)\},\qquad \sigma(y)=\frac{1}{1+\exp(-y)}
      \]
    </div>

    <div class="equation">
      <span class="label">Scalar capacity law</span>
      \[
        \Phi(K)=\alpha+rK^2(1-K)-dK-Lp(K,z)
      \]
    </div>

    <p>The feasible dynamic is the projected dynamic on \([0,1]\): in the interior, \(\dot K=\Phi(K)\); at \(K=0\), outward negative drift is held at the lower boundary; at \(K=1\), outward positive drift is held at the upper boundary.</p>

    <div class="equation">
      <span class="label">Projected scalar dynamic</span>
      \[
        \dot K=
        \begin{cases}
          \max\{0,\Phi(0)\}, & K=0,\\
          \Phi(K), & 0<K<1,\\
          \min\{0,\Phi(1)\}, & K=1.
        \end{cases}
      \]
    </div>

    <p>The derivative is:</p>

    <div class="equation">
      <span class="label">Scalar local multiplier</span>
      \[
        \Phi'(K)=r(2K-3K^2)-d+L\beta\rho p(K,z)\bigl[1-p(K,z)\bigr]
      \]
    </div>

    <p>The final term is the induced-preference feedback. It is largest when the substitute share is near one half and small when the substitute is almost never or almost always chosen. This explains why the middle region can be unstable even when the low and high states are stable.</p>

    <div class="theorem" data-kind="Proposition">
      <span class="theorem-title">Two-basin capacity trap</span>
      <p>Suppose the projected scalar dynamic has exactly three interior equilibria \(K_L&lt;K_U&lt;K_H\) in the relevant interval, no attracting boundary state in that interval, and \(\Phi'(K_L)&lt;0\), \(\Phi'(K_U)&gt;0\), and \(\Phi'(K_H)&lt;0\). Then \(K_L\) and \(K_H\) are locally stable, \(K_U\) is locally unstable, and the interval is split into two local basins separated by \(K_U\).</p>
    </div>
    <p class="proof"><strong>Proof.</strong> In one dimension, a fixed point with negative derivative of the vector field is locally attracting and a fixed point with positive derivative is locally repelling. With exactly the three stated interior equilibria and no attracting boundary state in the relevant interval, continuity implies the sign of \(\Phi\) alternates across the simple roots. Initial conditions on one side of the unstable root move toward the low stable root; initial conditions on the other side move toward the high stable root.</p>

    <div class="theorem" data-kind="Proposition">
      <span class="theorem-title">Conditional derivatives and existence of traps</span>
      <p>For interior \(K\), the direct derivatives are \(\partial\Phi/\partial L=-p\), \(\partial\Phi/\partial z=-L\beta p(1-p)\), \(\partial\Phi/\partial \rho=L\beta Kp(1-p)\), and \(\partial\Phi/\partial\beta=-L(q+z-\rho K)p(1-p)\). Thus damage and exposure lower the drift pointwise, capacity protection raises the drift at fixed \(K&gt;0\), and sensitivity has a sign that depends on whether the substitute field \(q+z-\rho K\) is positive or negative. Parameter changes can create or remove low-high traps by changing the root pattern of \(\Phi\); the capacity-trap calibration gives one such constructive case.</p>
    </div>
    <p class="proof"><strong>Proof.</strong> The derivative expressions follow by differentiating the logit formula and the scalar drift. The existence claim follows constructively from the reported calibration, where the computed roots satisfy the two-basin conditions in the preceding proposition. More general monotone comparative statics are not asserted because \(\beta\) and \(\rho\) affect both levels and slopes of the vector field.</p>

    <p>The baseline capacity-trap calibration used for Table 1 and Figures 1-2 sets \(\alpha=0.235\), \(r=2.90\), \(d=0.66\), \(L=0.198\), \(\beta=21.0\), \(q=0.51\), and \(\rho=0.855\). The self-correcting scenario lowers \(L\) and \(\beta\). The repair scenario raises \(\alpha\). Reproducibility details appear in `results/material_feedback_report.md`.</p>
  </section>

  <section class="refs">
    <h2>References</h2>
    <p id="ref-adomavicius">Adomavicius, Gediminas, Jesse C. Bockstedt, Shawn P. Curley, and Jingjing Zhang. "Do Recommender Systems Manipulate Consumer Preferences? A Study of Anchoring Effects." <em>Information Systems Research</em> 24(4), 2013, 956-975. <a href="https://ideas.repec.org/a/inm/orisre/v24y2013i4p956-975.html">Record</a>.</p>
    <p id="ref-aassve">Aassve, Arnstein, Alicia Adsera, Paul Y. Chang, Letizia Mencarini, Hyunjoon Park, Chen Peng, Samuel Plach, James M. Raymo, Senhu Wang, and Wei-Jun Jean Yeung. "Family Ideals in an Era of Low Fertility." <em>Proceedings of the National Academy of Sciences</em>, 2024. <a href="https://www.pnas.org/doi/10.1073/pnas.2311847121">Record</a>.</p>
    <p id="ref-aga-revenue">American Gaming Association. "Commercial Gaming Revenue Tracker." 2026. <a href="https://www.americangaming.org/resources/commercial-gaming-revenue-tracker/">Tracker</a>.</p>
    <p id="ref-ai-companions">Malfacini, Kim. "The Impacts of Companion AI on Human Relationships: Risks, Benefits, and Design Considerations." <em>AI &amp; Society</em> 40, 2025, 5527-5540. <a href="https://link.springer.com/article/10.1007/s00146-025-02318-6">Record</a>.</p>
    <p id="ref-allcott-social">Allcott, Hunt, Luca Braghieri, Sarah Eichmeyer, and Matthew Gentzkow. "The Welfare Effects of Social Media." <em>American Economic Review</em> 110(3), 2020, 629-676. <a href="https://www.aeaweb.org/articles?id=10.1257/aer.20190658">Record</a>.</p>
    <p id="ref-arthur">Arthur, W. Brian. "Competing Technologies, Increasing Returns, and Lock-In by Historical Events." <em>Economic Journal</em> 99(394), 1989, 116-131. <a href="https://www.jstor.org/stable/2234208">Record</a>.</p>
    <p id="ref-asps-2024">American Society of Plastic Surgeons. "Plastic Surgery Statistics Report." 2024. <a href="https://www.plasticsurgery.org/plastic-surgery-statistics">Report</a>.</p>
    <p id="ref-becker-murphy">Becker, Gary S., and Kevin M. Murphy. "A Theory of Rational Addiction." <em>Journal of Political Economy</em> 96(4), 1988, 675-700. <a href="https://www.journals.uchicago.edu/doi/10.1086/261558">Record</a>.</p>
    <p id="ref-bernheim-chosen">Bernheim, B. Douglas, Luca Braghieri, Alejandro Martinez-Marquina, and David Zuckerman. "A Theory of Chosen Preferences." <em>American Economic Review</em> 111(2), 2021, 720-754. <a href="https://www.aeaweb.org/articles?id=10.1257/aer.20190390">Record</a>.</p>
    <p id="ref-bisin">Bisin, Alberto, and Thierry Verdier. "The Economics of Cultural Transmission and the Dynamics of Preferences." <em>Journal of Economic Theory</em> 97(2), 2001, 298-319. <a href="https://doi.org/10.1006/jeth.2000.2678">Record</a>.</p>
    <p id="ref-bowles">Bowles, Samuel. "Endogenous Preferences: The Cultural Consequences of Markets and Other Economic Institutions." <em>Journal of Economic Literature</em> 36(1), 1998, 75-111. <a href="https://ideas.repec.org/a/aea/jeclit/v36y1998i1p75-111.html">Record</a>.</p>
    <p id="ref-braghieri-social">Braghieri, Luca, Ro'ee Levy, and Alexey Makarin. "Social Media and Mental Health." <em>American Economic Review</em> 112(11), 2022, 3660-3693. <a href="https://www.aeaweb.org/articles?id=10.1257/aer.20211218">Record</a>.</p>
    <p id="ref-brock-durlauf">Brock, William A., and Steven N. Durlauf. "Discrete Choice with Social Interactions." <em>Review of Economic Studies</em> 68(2), 2001, 235-260. <a href="https://academic.oup.com/restud/article-abstract/68/2/235/1588432">Record</a>.</p>
    <p id="ref-cdc-births">Centers for Disease Control and Prevention, National Center for Health Statistics. "Births: Provisional Data for 2025." Vital Statistics Rapid Release, 2026. <a href="https://www.cdc.gov/nchs/data/vsrr/vsrr043.pdf">PDF</a>.</p>
    <p id="ref-cdc-upf">Centers for Disease Control and Prevention, National Center for Health Statistics. "Ultra-Processed Food Intake in the United States." Data Brief No. 536, 2025. <a href="https://www.cdc.gov/nchs/products/databriefs/db536.htm">Report</a>.</p>
    <p id="ref-cdc-yrbs">Centers for Disease Control and Prevention. "Youth Risk Behavior Survey Data Summary &amp; Trends Report: 2013-2023." 2024. <a href="https://www.cdc.gov/yrbs/dstr/pdf/YRBS-2023-Data-Summary-Trend-Report.pdf">PDF</a>.</p>
    <p id="ref-chaney">Chaney, Allison J. B., Brandon M. Stewart, and Barbara E. Engelhardt. "How Algorithmic Confounding in Recommendation Systems Increases Homogeneity and Decreases Utility." RecSys, 2018. <a href="https://arxiv.org/abs/1710.11214">arXiv</a>.</p>
    <p id="ref-common-sense-ai">Common Sense Media. "Talk, Trust, and Trade-Offs: How and Why Teens Use AI Companions." 2025. <a href="https://www.commonsensemedia.org/research/talk-trust-and-trade-offs-how-and-why-teens-use-ai-companions">Report</a>.</p>
    <p id="ref-dekel">Dekel, Eddie, Jeffrey C. Ely, and Okan Yilankaya. "Evolution of Preferences." <em>Review of Economic Studies</em> 74(3), 2007, 685-704. <a href="https://academic.oup.com/restud/article/74/3/685/1599139">Record</a>.</p>
    <p id="ref-eurostat-fertility">Eurostat. "Fertility Statistics." 2026 update. <a href="https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Fertility_statistics">Report</a>.</p>
    <p id="ref-fenichel">Fenichel, Neil. "Geometric Singular Perturbation Theory for Ordinary Differential Equations." <em>Journal of Differential Equations</em> 31, 1979, 53-98. <a href="https://doi.org/10.1016/0022-0396(79)90152-9">Record</a>.</p>
    <p id="ref-gallup-immigration">Gallup. "Surge in Concern About Immigration Has Abated." 2025. <a href="https://news.gallup.com/poll/692522/surge-concern-immigration-abated.aspx">Report</a>.</p>
    <p id="ref-gallup-institutions">Gallup. "Confidence in Institutions Mostly Flat, Police Highest." 2025. <a href="https://news.gallup.com/poll/647303/confidence-institutions-mostly-flat-police.aspx">Report</a>.</p>
    <p id="ref-genicot-ray">Genicot, Garance, and Debraj Ray. "Aspirations and Inequality." <em>Econometrica</em> 85(2), 2017, 489-519. <a href="https://doi.org/10.3982/ECTA13865">Record</a>.</p>
    <p id="ref-grossman">Grossman, Michael. "On the Concept of Health Capital and the Demand for Health." <em>Journal of Political Economy</em> 80(2), 1972, 223-255. <a href="https://www.journals.uchicago.edu/doi/10.1086/259880">Record</a>.</p>
    <p id="ref-guess-feed">Guess, Andrew M., Neil Malhotra, Jennifer Pan, Pablo Barbera, Hunt Allcott, and others. "How Do Social Media Feed Algorithms Affect Attitudes and Behavior in an Election Campaign?" <em>Science</em> 381(6656), 2023, 398-404. <a href="https://www.science.org/doi/10.1126/science.abp9364">Record</a>.</p>
    <p id="ref-hamaker">Hamaker, Ellen L., Rebecca M. Kuiper, and Raoul P. P. P. Grasman. "A Critique of the Cross-Lagged Panel Model." <em>Psychological Methods</em> 20(1), 2015, 102-116. <a href="https://doi.org/10.1037/a0038889">Record</a>.</p>
    <p id="ref-hbs-ai">De Freitas, Julian, Ahmet K. Uguralp, Zeliha O. Uguralp, and Stefano Puntoni. "AI Companions Reduce Loneliness." Harvard Business School Working Paper 24-078, 2024. <a href="https://www.hbs.edu/ris/download.aspx?name=24-078.pdf">PDF</a>.</p>
    <p id="ref-jiang">Jiang, Ray, Silvia Chiappa, Tor Lattimore, Andras Gyorgy, and Pushmeet Kohli. "Degenerate Feedback Loops in Recommender Systems." AIES, 2019. <a href="https://arxiv.org/abs/1902.10730">arXiv</a>.</p>
    <p id="ref-kleinberg">Kleinberg, Jon, Sendhil Mullainathan, and Manish Raghavan. "The Challenge of Understanding What Users Want: Inconsistent Preferences and Engagement Optimization." <em>Management Science</em> 70(9), 2024, 6336-6355. <a href="https://pubsonline.informs.org/doi/10.1287/mnsc.2022.03683">Record</a>.</p>
    <p id="ref-koszegi-rabin">Koszegi, Botond, and Matthew Rabin. "A Model of Reference-Dependent Preferences." <em>Quarterly Journal of Economics</em> 121(4), 2006, 1133-1165. <a href="https://academic.oup.com/qje/article/121/4/1133/1935100">Record</a>.</p>
    <p id="ref-lachaab">Lachaab, Mohamed, Asim Ansari, Kamel Jedidi, and Abdelwahed Trabelsi. "Modeling Preference Evolution in Discrete Choice Models: A Bayesian State-Space Approach." <em>Quantitative Marketing and Economics</em> 4, 2006, 57-81. <a href="https://doi.org/10.1007/s11129-006-6559-x">Record</a>.</p>
    <p id="ref-mahler">Mahler, Lukas, Michele Tertilt, and Minchul Yum. "Policy Concerns in an Era of Low Fertility: The Role of Social Comparisons." 2025. <a href="https://lukasmahler.github.io/assets/pdf/5_Mahler_Tertilt_Yum_unembargoed.pdf">PDF</a>.</p>
    <p id="ref-nber-sports-betting">Baker, Scott R., Justin Balthrop, Mark J. Johnson, Jason D. Kotter, and Kevin Pisciotta. "Gambling Away Stability: Sports Betting's Impact on Vulnerable Households." NBER Working Paper 33108, 2024. <a href="https://www.nber.org/papers/w33108">Record</a>.</p>
    <p id="ref-oecd">OECD. "Fertility Trends Across the OECD: Underlying Drivers and the Role for Policy." <em>Society at a Glance 2024</em>. <a href="https://www.oecd.org/en/publications/society-at-a-glance-2024_918d8db3-en/full-report/fertility-trends-across-the-oecd-underlying-drivers-and-the-role-for-policy_770679b8.html">Report</a>.</p>
    <p id="ref-oecd-migration">OECD. <em>International Migration Outlook 2025</em>. 2025. <a href="https://www.oecd.org/en/publications/international-migration-outlook-2025_ae26c893-en.html">Report</a>.</p>
    <p id="ref-pew-border">Pew Research Center. "How Americans View the Situation at the U.S.-Mexico Border, Its Causes and Consequences." 2024. <a href="https://www.pewresearch.org/politics/2024/02/15/how-americans-view-the-situation-at-the-u-s-mexico-border-its-causes-and-consequences/">Report</a>.</p>
    <p id="ref-pew-news-influencers">Pew Research Center. "America's News Influencers." 2024. <a href="https://www.pewresearch.org/journalism/2024/11/18/americas-news-influencers/">Report</a>.</p>
    <p id="ref-pew-nato">Pew Research Center. "NATO Viewed Favorably Across 13 Member Nations." 2025. <a href="https://www.pewresearch.org/global/2025/06/23/nato-viewed-favorably-across-13-member-nations/">Report</a>.</p>
    <p id="ref-pew-trust">Pew Charitable Trusts. "Americans' Deepening Mistrust of Institutions." 2024. <a href="https://www.pew.org/en/trend/archive/fall-2024/americans-deepening-mistrust-of-institutions">Report</a>.</p>
    <p id="ref-pnas-divisive">PNAS Nexus. "Ranking Social Media Feeds by Engagement Can Amplify Divisive Content." 2025. <a href="https://academic.oup.com/pnasnexus/article/4/3/pgaf062/8052060">Record</a>.</p>
    <p id="ref-stigler-becker">Stigler, George J., and Gary S. Becker. "De Gustibus Non Est Disputandum." <em>American Economic Review</em> 67(2), 1977, 76-90. <a href="https://econpapers.repec.org/RePEc:aea:aecrev:v:67:y:1977:i:2:p:76-90">Record</a>.</p>
    <p id="ref-surgeon-general">Office of the Surgeon General. "Our Epidemic of Loneliness and Isolation: The U.S. Surgeon General's Advisory on the Healing Effects of Social Connection and Community." US Department of Health and Human Services, 2023. <a href="https://www.ncbi.nlm.nih.gov/books/NBK595227/">NCBI Bookshelf</a>.</p>
    <p id="ref-unfpa-2025">UNFPA. <em>The State of World Population 2025: The Real Fertility Crisis</em>. 2025. <a href="https://www.unfpa.org/swp2025">Report</a>.</p>
    <p id="ref-ueda">Ueda, Peter, Catherine H. Mercer, Cyrus Ghaznavi, and Debby Herbenick. "Trends in Frequency of Sexual Activity and Number of Sexual Partners Among Adults Aged 18 to 44 Years in the US, 2000-2018." <em>JAMA Network Open</em> 3(6), 2020, e203833. <a href="https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2767066">Record</a>.</p>
    <p id="ref-unhcr-global-trends">UNHCR. <em>Global Trends</em>. 2026. <a href="https://www.unhcr.org/global-trends">Report</a>.</p>
    <p id="ref-who-loneliness">World Health Organization. "Social Connection Linked to Improved Health and Reduced Risk of Early Death." WHO Commission on Social Connection, 2025. <a href="https://www.who.int/news/item/30-06-2025-social-connection-linked-to-improved-heath-and-reduced-risk-of-early-death">Report</a>.</p>
    <p id="ref-wilding-semaglutide">Wilding, John P. H., Rachel L. Batterham, Salvatore Calanna, Melanie Davies, Luc F. Van Gaal, Ildiko Lingvay, Barbara M. McGowan, Julio Rosenstock, Marie T. D. Tran, Thomas A. Wadden, Sean Wharton, Kazuma Yokote, Niels Zeuthen, and Robert F. Kushner. "Once-Weekly Semaglutide in Adults with Overweight or Obesity." <em>New England Journal of Medicine</em> 384, 2021, 989-1002. <a href="https://www.nejm.org/doi/full/10.1056/NEJMoa2032183">Record</a>.</p>
    <p id="ref-wilding-withdrawal">Wilding, John P. H., Rachel L. Batterham, Melanie Davies, Luc F. Van Gaal, Ildiko Lingvay, Thomas A. Wadden, and others. "Weight Regain and Cardiometabolic Effects After Withdrawal of Semaglutide: The STEP 1 Trial Extension." <em>Diabetes, Obesity and Metabolism</em> 24(8), 2022, 1553-1564. <a href="https://dom-pubs.onlinelibrary.wiley.com/doi/10.1111/dom.14725">Record</a>.</p>
  </section>
</main>
</body>
</html>
"""
    )
    return template.substitute(
        equilibria_table=equilibria_table,
        audit_table=audit_table,
    )


def main() -> None:
    if not (ROOT / "results" / "tables" / "material_feedback_equilibria.csv").exists():
        print("Run scripts/run_material_feedback_analysis.py first.", file=sys.stderr)
        raise SystemExit(1)
    PAPER.write_text(build_article(), encoding="utf-8")
    print(PAPER)


if __name__ == "__main__":
    main()
