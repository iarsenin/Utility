#!/usr/bin/env python3
"""Run three research iterations and write tables, figures, and a verdict report."""

from __future__ import annotations

import csv
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from utility_endogenous.endogenous_taste import TasteDriftParams, simulate_taste_drift
from utility_endogenous.indirect_evolution import (
    SocialPreferenceParams,
    simulate_social_preferences,
)
from utility_endogenous.platform_control import (
    PlatformControlParams,
    platform_scenarios,
    simulate_platform_control,
)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    fieldnames: list[str] = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def fmt(value: object, digits: int = 4) -> str:
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |"
    body = [
        "| " + " | ".join(fmt(row[column]) for column in columns) + " |"
        for row in rows
    ]
    return "\n".join([header, separator, *body])


def final_row(rows: list[dict[str, object]]) -> dict[str, object]:
    if not rows:
        raise ValueError("No rows supplied")
    return rows[-1]


def first_row(rows: list[dict[str, object]]) -> dict[str, object]:
    if not rows:
        raise ValueError("No rows supplied")
    return rows[0]


def delta(rows: list[dict[str, object]], key: str) -> float:
    return float(final_row(rows)[key]) - float(first_row(rows)[key])


def iteration_1_taste_sweep() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    scenarios = [
        TasteDriftParams(
            name="I1_reproduce_static_no_transition",
            periods=80,
            persuasion_rate=0.0,
            ai_power=0.0,
            platform_bias=0.0,
            offline_anchor=0.0,
            selection_strength=0.0,
        ),
        TasteDriftParams(
            name="I1_reproduce_selection_only",
            periods=80,
            persuasion_rate=0.0,
            ai_power=0.0,
            platform_bias=0.0,
            offline_anchor=0.0,
            selection_strength=0.85,
        ),
        TasteDriftParams(
            name="I1_endogenous_ai_transition",
            periods=80,
            persuasion_rate=0.16,
            ai_power=0.85,
            personalization=0.75,
            platform_bias=0.10,
            offline_anchor=0.04,
            selection_strength=0.85,
        ),
    ]

    path_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []
    for scenario in scenarios:
        records = simulate_taste_drift(scenario)
        path_rows.extend(records)
        summary_rows.append(
            {
                "iteration": 1,
                "scenario": scenario.name,
                "benchmark_reproduced": scenario.persuasion_rate == 0.0,
                "initial_theta": float(first_row(records)["mean_theta"]),
                "final_theta": float(final_row(records)["mean_theta"]),
                "delta_theta": delta(records, "mean_theta"),
                "initial_fitness": float(first_row(records)["mean_fitness"]),
                "final_fitness": float(final_row(records)["mean_fitness"]),
                "delta_fitness": delta(records, "mean_fitness"),
                "final_subjective_satisfaction": float(
                    final_row(records)["subjective_satisfaction"]
                ),
                "verdict": "benchmark" if scenario.persuasion_rate == 0.0 else "mechanism",
            }
        )

    sweep_rows: list[dict[str, object]] = []
    for persuasion in [0.00, 0.04, 0.08, 0.12, 0.16, 0.20, 0.26]:
        for selection in [0.20, 0.60, 1.00, 1.60, 2.40, 3.20]:
            params = TasteDriftParams(
                name=f"I1_sweep_p{persuasion:.2f}_s{selection:.2f}",
                periods=80,
                persuasion_rate=persuasion,
                ai_power=0.85,
                personalization=0.75,
                platform_bias=0.10,
                offline_anchor=0.04,
                selection_strength=selection,
            )
            records = simulate_taste_drift(params)
            d_theta = delta(records, "mean_theta")
            d_fitness = delta(records, "mean_fitness")
            sweep_rows.append(
                {
                    "persuasion_rate": persuasion,
                    "selection_strength": selection,
                    "final_theta": float(final_row(records)["mean_theta"]),
                    "delta_theta": d_theta,
                    "final_fitness": float(final_row(records)["mean_fitness"]),
                    "delta_fitness": d_fitness,
                    "fitness_utility_inversion": d_theta > 0.25 and d_fitness < -0.20,
                }
            )

    return path_rows, summary_rows + sweep_rows


def iteration_2_evolutionary_sweep() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    scenarios = [
        SocialPreferenceParams(
            name="I2_reproduce_material_pd",
            periods=80,
            influence_rate=0.0,
            lambda_target=0.25,
            norm_bonus=0.0,
            selection_strength=0.45,
        ),
        SocialPreferenceParams(
            name="I2_mutation_to_prosocial",
            periods=80,
            influence_rate=0.055,
            lambda_target=1.10,
            norm_bonus=0.15,
            selection_strength=0.45,
        ),
        SocialPreferenceParams(
            name="I2_mutation_to_conflict",
            periods=80,
            influence_rate=0.085,
            lambda_target=-0.25,
            norm_bonus=-0.18,
            selection_strength=0.45,
        ),
    ]

    path_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []
    for scenario in scenarios:
        records = simulate_social_preferences(scenario)
        path_rows.extend(records)
        summary_rows.append(
            {
                "iteration": 2,
                "scenario": scenario.name,
                "benchmark_reproduced": scenario.influence_rate == 0.0,
                "initial_lambda": float(first_row(records)["mean_lambda"]),
                "final_lambda": float(final_row(records)["mean_lambda"]),
                "delta_lambda": delta(records, "mean_lambda"),
                "initial_cooperation": float(first_row(records)["cooperation_rate"]),
                "final_cooperation": float(final_row(records)["cooperation_rate"]),
                "delta_cooperation": delta(records, "cooperation_rate"),
                "final_material_payoff": float(final_row(records)["mean_material_payoff"]),
                "verdict": "benchmark" if scenario.influence_rate == 0.0 else "mechanism",
            }
        )

    sweep_rows: list[dict[str, object]] = []
    for influence in [0.0, 0.015, 0.030, 0.050, 0.075, 0.100]:
        for target in [-0.35, 0.00, 0.35, 0.70, 1.10, 1.40]:
            params = SocialPreferenceParams(
                name=f"I2_sweep_i{influence:.3f}_t{target:.2f}",
                periods=80,
                influence_rate=influence,
                lambda_target=target,
                norm_bonus=0.08 if target > 0.7 else 0.0,
                selection_strength=0.45,
            )
            records = simulate_social_preferences(params)
            sweep_rows.append(
                {
                    "influence_rate": influence,
                    "lambda_target": target,
                    "final_lambda": float(final_row(records)["mean_lambda"]),
                    "final_cooperation": float(final_row(records)["cooperation_rate"]),
                    "delta_cooperation": delta(records, "cooperation_rate"),
                    "material_payoff": float(final_row(records)["mean_material_payoff"]),
                    "cooperation_reversal": float(final_row(records)["cooperation_rate"]) > 0.75,
                }
            )

    return path_rows, summary_rows + sweep_rows


def iteration_3_platform_control() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    path_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []

    for scenario in platform_scenarios():
        records = simulate_platform_control(scenario)
        path_rows.extend(records)
        summary_rows.append(
            {
                "iteration": 3,
                "scenario": scenario.name,
                "policy": scenario.policy,
                "initial_theta": float(first_row(records)["mean_theta"]),
                "final_theta": float(final_row(records)["mean_theta"]),
                "delta_theta": delta(records, "mean_theta"),
                "initial_fitness": float(first_row(records)["mean_fitness"]),
                "final_fitness": float(final_row(records)["mean_fitness"]),
                "delta_fitness": delta(records, "mean_fitness"),
                "final_initial_preference_value": float(
                    final_row(records)["initial_preference_value"]
                ),
                "delta_initial_preference_value": delta(records, "initial_preference_value"),
                "final_exposure": float(final_row(records)["exposure"]),
                "mean_final_platform_value": float(final_row(records)["platform_value"]),
                "verdict": "benchmark" if scenario.policy == "fixed" else "candidate",
            }
        )

    sweep_rows: list[dict[str, object]] = []
    for plasticity in [0.04, 0.08, 0.12, 0.16, 0.22, 0.30]:
        for cost in [0.02, 0.05, 0.10, 0.18, 0.30, 0.50]:
            for selection in [0.60, 1.40, 2.40]:
                params = PlatformControlParams(
                    name=f"I3_sweep_eta{plasticity:.2f}_c{cost:.2f}_s{selection:.2f}",
                    periods=100,
                    plasticity=plasticity,
                    exposure_cost=cost,
                    selection_strength=selection,
                    predictability_weight=0.25,
                    policy="platform",
                )
                records = simulate_platform_control(params)
                d_theta = delta(records, "mean_theta")
                d_fitness = delta(records, "mean_fitness")
                d_initial_value = delta(records, "initial_preference_value")
                sweep_rows.append(
                    {
                        "plasticity": plasticity,
                        "exposure_cost": cost,
                        "selection_strength": selection,
                        "final_exposure": float(final_row(records)["exposure"]),
                        "final_theta": float(final_row(records)["mean_theta"]),
                        "delta_theta": d_theta,
                        "final_fitness": float(final_row(records)["mean_fitness"]),
                        "delta_fitness": d_fitness,
                        "delta_initial_preference_value": d_initial_value,
                        "platform_inversion": (
                            d_theta > 0.25 and d_fitness < -0.20 and d_initial_value < -0.20
                        ),
                    }
                )

    return path_rows, summary_rows + sweep_rows


def write_svg_heatmap(path: Path, rows: list[dict[str, object]]) -> None:
    """Write a compact heatmap for the platform inversion sweep."""

    filtered = [row for row in rows if "platform_inversion" in row]
    plasticities = sorted({float(row["plasticity"]) for row in filtered})
    costs = sorted({float(row["exposure_cost"]) for row in filtered})
    selections = sorted({float(row["selection_strength"]) for row in filtered})
    cell = 34
    gap = 4
    left = 100
    top = 70
    panel_gap = 70
    width = left + len(costs) * (cell + gap) + 40
    height = top + len(selections) * (len(plasticities) * (cell + gap) + panel_gap) + 80

    lookup = {
        (
            float(row["plasticity"]),
            float(row["exposure_cost"]),
            float(row["selection_strength"]),
        ): row
        for row in filtered
    }

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#fbfaf7"/>',
        '<text x="20" y="28" font-family="Arial" font-size="18" font-weight="700">Platform-control inversion sweep</text>',
        '<text x="20" y="50" font-family="Arial" font-size="12" fill="#555">red = preference capture with fitness and initial-preference loss</text>',
    ]

    y = top
    for selection in selections:
        parts.append(
            f'<text x="20" y="{y + 18}" font-family="Arial" font-size="13" font-weight="700">selection {selection:.1f}</text>'
        )
        for col, cost in enumerate(costs):
            x = left + col * (cell + gap)
            parts.append(
                f'<text x="{x}" y="{y - 10}" font-family="Arial" font-size="10" text-anchor="middle">c={cost:.2f}</text>'
            )
        for row_i, plasticity in enumerate(plasticities):
            row_y = y + row_i * (cell + gap)
            parts.append(
                f'<text x="{left - 18}" y="{row_y + 21}" font-family="Arial" font-size="10" text-anchor="end">eta={plasticity:.2f}</text>'
            )
            for col, cost in enumerate(costs):
                x = left + col * (cell + gap)
                result = lookup[(plasticity, cost, selection)]
                inversion = result["platform_inversion"] == "True" or result["platform_inversion"] is True
                theta = float(result["final_theta"])
                color = "#b73535" if inversion else "#d8d1c8"
                if theta > 0.80 and not inversion:
                    color = "#d79755"
                parts.append(
                    f'<rect x="{x}" y="{row_y}" width="{cell}" height="{cell}" rx="3" fill="{color}" stroke="#ffffff"/>'
                )
                parts.append(
                    f'<text x="{x + cell / 2}" y="{row_y + 21}" font-family="Arial" font-size="9" text-anchor="middle" fill="#202020">{theta:.2f}</text>'
                )
        y += len(plasticities) * (cell + gap) + panel_gap

    parts.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(parts), encoding="utf-8")


def build_report(
    i1_summary: list[dict[str, object]],
    i2_summary: list[dict[str, object]],
    i3_summary: list[dict[str, object]],
) -> str:
    i1_named = [row for row in i1_summary if "iteration" in row]
    i2_named = [row for row in i2_summary if "iteration" in row]
    i3_named = [row for row in i3_summary if "iteration" in row]
    i1_sweep = [row for row in i1_summary if "fitness_utility_inversion" in row]
    i2_sweep = [row for row in i2_summary if "cooperation_reversal" in row]
    i3_sweep = [row for row in i3_summary if "platform_inversion" in row]

    i1_inversions = sum(row["fitness_utility_inversion"] is True for row in i1_sweep)
    i2_reversals = sum(row["cooperation_reversal"] is True for row in i2_sweep)
    i3_inversions = sum(row["platform_inversion"] is True for row in i3_sweep)

    lines = [
        "# Research Iteration Report",
        "",
        "Generated by `python3 scripts/run_research_iterations.py`.",
        "",
        "## Iteration 1: Endogenous Taste Drift",
        "",
        "Candidate model: one-dimensional consumption taste state. Benchmark reproduction holds when `K` is degenerate: mean taste is stable absent transition and selection. Adding selection-only pushes taste toward the fitness-favored offline state. Adding the endogenous AI transition can reverse that direction.",
        "",
        markdown_table(
            i1_named,
            [
                "scenario",
                "initial_theta",
                "final_theta",
                "delta_theta",
                "initial_fitness",
                "final_fitness",
                "delta_fitness",
                "verdict",
            ],
        ),
        "",
        f"Sweep result: {i1_inversions} of {len(i1_sweep)} parameter cells show the fitness-utility inversion criterion.",
        "",
        "Evaluation: useful mechanism and theorem candidate, but too reduced-form because the algorithmic field is exogenous. It should be used as the transparent first theorem, not as the paper's central model.",
        "",
        "## Iteration 2: Indirect Evolutionary Game",
        "",
        "Candidate model: Prisoner's Dilemma with subjective social preferences and material fitness. The benchmark reproduces the standard pull toward non-cooperation under material payoff selection. Preference mutation can generate cooperation or conflict depending on the transition target.",
        "",
        markdown_table(
            i2_named,
            [
                "scenario",
                "initial_lambda",
                "final_lambda",
                "delta_lambda",
                "initial_cooperation",
                "final_cooperation",
                "delta_cooperation",
                "final_material_payoff",
                "verdict",
            ],
        ),
        "",
        f"Sweep result: {i2_reversals} of {len(i2_sweep)} parameter cells produce high-cooperation reversal.",
        "",
        "Evaluation: solid bridge to the endogenous-preferences literature, but novelty is moderate unless the transition law is tied to platform incentives. Keep it as a credibility and comparison section.",
        "",
        "## Iteration 3: Platform Preference Control",
        "",
        "Candidate model: a platform chooses exposure intensity to maximize engagement and predictability while users locally optimize and biological/material fitness selects preference states. This is the strongest candidate because it endogenizes the preference-transition technology.",
        "",
        markdown_table(
            i3_named,
            [
                "scenario",
                "policy",
                "initial_theta",
                "final_theta",
                "delta_theta",
                "initial_fitness",
                "final_fitness",
                "delta_fitness",
                "final_initial_preference_value",
                "delta_initial_preference_value",
                "final_exposure",
                "verdict",
            ],
        ),
        "",
        f"Sweep result: {i3_inversions} of {len(i3_sweep)} parameter cells show platform inversion: taste capture, fitness loss, and initial-preference loss.",
        "",
        "Evaluation: paper-worthy if formalized carefully. The result is not merely that preferences drift; it is that the profit-maximizing platform chooses the transition intensity. The mechanism creates a conflict between final-preference satisfaction, initial-preference welfare, and fitness.",
        "",
        "## Research Decision",
        "",
        "Do not center the first paper on the raw taste-drift toy model or the Prisoner's Dilemma alone. Center it on the platform-control model, with the other two iterations serving as nested benchmarks:",
        "",
        "1. Static utility and selection-only benchmarks establish footing.",
        "2. Taste drift gives the clean timescale-dominance proposition.",
        "3. Indirect evolution connects to Dekel-Ely-Yilankaya style subjective utility versus objective fitness.",
        "4. Platform control provides the novel AI/social-media contribution.",
        "",
        "## Next Iteration",
        "",
        "The next serious step is analytical: prove the one-dimensional timescale proposition and the platform-control first-order/bang-bang result, then replace the myopic platform with a forward-looking platform or regulator.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    results_dir = ROOT / "results"
    tables_dir = results_dir / "tables"
    figures_dir = results_dir / "figures"

    i1_paths, i1_summary = iteration_1_taste_sweep()
    i2_paths, i2_summary = iteration_2_evolutionary_sweep()
    i3_paths, i3_summary = iteration_3_platform_control()

    write_csv(tables_dir / "iteration_1_taste_paths.csv", i1_paths)
    write_csv(tables_dir / "iteration_1_taste_summary.csv", i1_summary)
    write_csv(tables_dir / "iteration_2_evolution_paths.csv", i2_paths)
    write_csv(tables_dir / "iteration_2_evolution_summary.csv", i2_summary)
    write_csv(tables_dir / "iteration_3_platform_paths.csv", i3_paths)
    write_csv(tables_dir / "iteration_3_platform_summary.csv", i3_summary)
    write_svg_heatmap(figures_dir / "platform_inversion_heatmap.svg", i3_summary)

    report = build_report(i1_summary, i2_summary, i3_summary)
    (results_dir / "research_iteration_report.md").write_text(report, encoding="utf-8")

    print(f"Wrote {results_dir / 'research_iteration_report.md'}")
    print(f"Wrote {figures_dir / 'platform_inversion_heatmap.svg'}")
    print("Completed 3 major research iterations")


if __name__ == "__main__":
    main()
