#!/usr/bin/env python3
"""Run the infinitely fast preference-adaptation limit across current models."""

from __future__ import annotations

import csv
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from utility_endogenous.endogenous_taste import TasteDriftParams, simulate_taste_drift
from utility_endogenous.fast_limit import (
    platform_fast_limit,
    social_fast_limit,
    taste_fast_limit,
)
from utility_endogenous.indirect_evolution import (
    SocialPreferenceParams,
    simulate_social_preferences,
    social_preference_scenarios,
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
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |"
    body = [
        "| " + " | ".join(fmt(row.get(column)) for column in columns) + " |"
        for row in rows
    ]
    return "\n".join([header, separator, *body])


def first_row(rows: list[dict[str, object]]) -> dict[str, object]:
    return rows[0]


def final_row(rows: list[dict[str, object]]) -> dict[str, object]:
    return rows[-1]


def taste_limit_rows() -> list[dict[str, object]]:
    scenarios = [
        TasteDriftParams(
            name="no_fast_preference_law",
            periods=80,
            persuasion_rate=0.0,
            ai_power=0.0,
            platform_bias=0.0,
            offline_anchor=0.0,
            selection_strength=0.85,
        ),
        TasteDriftParams(
            name="weak_algorithmic_adaptation",
            periods=80,
            persuasion_rate=0.04,
            ai_power=0.25,
            personalization=0.30,
            platform_bias=0.03,
            offline_anchor=0.09,
            selection_strength=0.85,
        ),
        TasteDriftParams(
            name="strong_algorithmic_adaptation",
            periods=80,
            persuasion_rate=0.18,
            ai_power=0.95,
            personalization=0.85,
            platform_bias=0.12,
            offline_anchor=0.04,
            selection_strength=0.85,
        ),
    ]

    rows: list[dict[str, object]] = []
    for scenario in scenarios:
        finite = simulate_taste_drift(scenario)
        limit = taste_fast_limit(scenario)
        rows.append(
            {
                "scenario": scenario.name,
                "finite_rate": scenario.persuasion_rate,
                "initial_theta": float(first_row(finite)["mean_theta"]),
                "finite_final_theta": float(final_row(finite)["mean_theta"]),
                "fast_limit_theta": limit.fast_attractor_theta,
                "finite_final_fitness": float(final_row(finite)["mean_fitness"]),
                "fast_limit_fitness": limit.mean_fitness,
                "selection_can_move_preferences": limit.selection_can_move_preferences,
                "note": limit.note,
            }
        )

    for selection in [0.20, 0.60, 1.00, 1.80, 3.20, 5.00]:
        scenario = TasteDriftParams(
            name=f"selection_invariance_s{selection:.2f}",
            periods=80,
            persuasion_rate=0.18,
            ai_power=0.95,
            personalization=0.85,
            platform_bias=0.12,
            offline_anchor=0.04,
            selection_strength=selection,
        )
        limit = taste_fast_limit(scenario)
        rows.append(
            {
                "scenario": scenario.name,
                "finite_rate": scenario.persuasion_rate,
                "initial_theta": scenario.initial_center,
                "finite_final_theta": None,
                "fast_limit_theta": limit.fast_attractor_theta,
                "finite_final_fitness": None,
                "fast_limit_fitness": limit.mean_fitness,
                "selection_can_move_preferences": limit.selection_can_move_preferences,
                "note": (
                    "Same fast attractor across selection strengths; only realized "
                    "fitness changes."
                ),
            }
        )

    return rows


def social_limit_rows() -> list[dict[str, object]]:
    scenarios = social_preference_scenarios() + [
        SocialPreferenceParams(
            name="knife_edge_mixed_fast_preference",
            periods=80,
            influence_rate=0.10,
            lambda_target=0.38,
            norm_bonus=0.00,
            selection_strength=0.45,
        )
    ]

    rows: list[dict[str, object]] = []
    for scenario in scenarios:
        finite = simulate_social_preferences(scenario)
        limit = social_fast_limit(scenario)
        rows.append(
            {
                "scenario": scenario.name,
                "finite_rate": scenario.influence_rate,
                "initial_lambda": float(first_row(finite)["mean_lambda"]),
                "finite_final_lambda": float(final_row(finite)["mean_lambda"]),
                "fast_limit_lambda": limit.fast_attractor_lambda,
                "finite_final_cooperation": float(final_row(finite)["cooperation_rate"]),
                "fast_limit_cooperation": limit.cooperation_rate,
                "fast_limit_material_payoff": limit.material_payoff,
                "material_nash": limit.material_nash,
                "note": limit.note,
            }
        )
    return rows


def platform_limit_rows() -> list[dict[str, object]]:
    scenarios = platform_scenarios() + [
        PlatformControlParams(
            name="platform_fast_limit_high_autonomy",
            policy="platform",
            exposure_cost=0.04,
            plasticity=0.50,
            selection_strength=1.00,
            predictability_weight=0.25,
            autonomy_weight=150.00,
        )
    ]

    rows: list[dict[str, object]] = []
    for scenario in scenarios:
        finite = simulate_platform_control(scenario)
        for penalty_case in ["steady", "boundary_layer"]:
            limit = platform_fast_limit(scenario, penalty_case)
            rows.append(
                {
                    "scenario": scenario.name,
                    "penalty_case": penalty_case,
                    "finite_policy": scenario.policy,
                    "finite_final_exposure": float(final_row(finite)["exposure"]),
                    "fast_limit_exposure": limit.exposure,
                    "finite_final_theta": float(final_row(finite)["mean_theta"]),
                    "fast_limit_theta": limit.fast_attractor_theta,
                    "finite_final_fitness": float(final_row(finite)["mean_fitness"]),
                    "fast_limit_fitness": limit.fitness,
                    "fast_limit_initial_preference_value": limit.initial_preference_value,
                    "fast_limit_platform_value": limit.platform_value,
                    "autonomy_penalty": limit.autonomy_penalty,
                }
            )
    return rows


def write_report(
    path: Path,
    taste_rows: list[dict[str, object]],
    social_rows: list[dict[str, object]],
    platform_rows: list[dict[str, object]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    strong_taste = next(
        row for row in taste_rows if row["scenario"] == "strong_algorithmic_adaptation"
    )
    prosocial = next(row for row in social_rows if row["scenario"] == "prosocial_institution")
    conflict = next(row for row in social_rows if row["scenario"] == "conflict_algorithm")
    platform_low_cost = [
        row for row in platform_rows
        if row["scenario"] == "myopic_platform_low_cost" and row["penalty_case"] == "steady"
    ][0]
    platform_guardrail = [
        row for row in platform_rows
        if row["scenario"] == "platform_with_calibrated_guardrail"
        and row["penalty_case"] == "boundary_layer"
    ][0]

    lines = [
        "# Fast Preference Limit Report",
        "",
        "## Mathematical Limit",
        "",
        "Let slow economic state be `z` and preference state be `theta`. The extreme case is:",
        "",
        "```text",
        "T d theta / dt = G(theta, z, a, m)",
        "d z / dt = H(z, theta, a, m)",
        "a in BR(theta, z, m)",
        "```",
        "",
        "Taking `T -> 0` forces the system onto the critical set:",
        "",
        "```text",
        "G(theta, z, a, m) = 0",
        "```",
        "",
        "If the fast subsystem has a unique attracting branch `theta = Phi(z, m)`,",
        "the slow economy becomes:",
        "",
        "```text",
        "d z / dt = H(z, Phi(z, m), BR(Phi(z, m), z, m), m)",
        "```",
        "",
        "Preferences no longer behave like a slowly selected trait. They behave like an",
        "instantaneous state constraint.",
        "",
        "## Cross-Model Numerical Readout",
        "",
        "### Taste Drift",
        "",
        markdown_table(
            [
                row for row in taste_rows
                if row["scenario"] in [
                    "no_fast_preference_law",
                    "weak_algorithmic_adaptation",
                    "strong_algorithmic_adaptation",
                ]
            ],
            [
                "scenario",
                "finite_final_theta",
                "fast_limit_theta",
                "finite_final_fitness",
                "fast_limit_fitness",
                "selection_can_move_preferences",
            ],
        ),
        "",
        "In the strong-adaptation case the finite model already approaches the singular",
        f"attractor: finite theta `{fmt(strong_taste['finite_final_theta'])}`,",
        f"fast-limit theta `{fmt(strong_taste['fast_limit_theta'])}`.",
        "",
        "### Selection Invariance",
        "",
        markdown_table(
            [row for row in taste_rows if row["scenario"].startswith("selection_invariance")],
            ["scenario", "fast_limit_theta", "fast_limit_fitness", "note"],
        ),
        "",
        "The fast attractor is invariant to selection strength in this model because",
        "selection acts on the slow population distribution after the fast taste state",
        "has already collapsed. Selection changes realized fitness, not the preference",
        "state.",
        "",
        "### Indirect Evolutionary Prisoner's Dilemma",
        "",
        markdown_table(
            social_rows,
            [
                "scenario",
                "finite_final_lambda",
                "fast_limit_lambda",
                "finite_final_cooperation",
                "fast_limit_cooperation",
                "material_nash",
            ],
        ),
        "",
        "Fast prosocial adaptation gives cooperation "
        f"`{fmt(prosocial['fast_limit_cooperation'])}`.",
        f"Fast conflict adaptation gives cooperation `{fmt(conflict['fast_limit_cooperation'])}`.",
        "Thus the material Nash prediction survives only when the fast preference",
        "attractor itself points to material self-interest.",
        "",
        "### Platform Control",
        "",
        markdown_table(
            [
                row for row in platform_rows
                if row["scenario"] in [
                    "no_platform_selection_benchmark",
                    "myopic_platform_low_cost",
                    "platform_with_calibrated_guardrail",
                ]
            ],
            [
                "scenario",
                "penalty_case",
                "fast_limit_exposure",
                "fast_limit_theta",
                "fast_limit_fitness",
                "fast_limit_platform_value",
                "autonomy_penalty",
            ],
        ),
        "",
        "In the steady fast limit, transition penalties vanish after the boundary layer.",
        f"The low-cost platform chooses exposure `{fmt(platform_low_cost['fast_limit_exposure'])}`",
        f"and pushes theta to `{fmt(platform_low_cost['fast_limit_theta'])}`.",
        "If autonomy is charged on the boundary-layer jump itself, the calibrated",
        f"guardrail chooses exposure `{fmt(platform_guardrail['fast_limit_exposure'])}`.",
        "",
        "## Candidate Invariant Results",
        "",
        "1. **Attractor Replacement**: with a unique fast preference attractor, utility",
        "   is no longer a primitive or a selected type; it is the graph of a fast",
        "   response map `Phi(z, m)`.",
        "2. **Darwinian Selection Loses Its Preference Target**: selection can change",
        "   population size or select adaptation rules, but it cannot select among",
        "   preference types that are instantly reset by the fast law.",
        "3. **Material Nash Need Not Survive**: actions are Nash only with respect to",
        "   instantaneous adapted preferences. They need not be Nash in the material",
        "   payoff game.",
        "4. **Ex Post Welfare Becomes Fragile**: if final preferences adapt to the",
        "   reached state, final-preference Pareto comparisons can validate the path",
        "   that produced those preferences.",
        "5. **Only Meta-Objects Survive**: invariant welfare/equilibrium claims must be",
        "   stated over adaptation laws, admissible transition kernels, initial or",
        "   meta-preferences, material fitness, or constitutional constraints.",
        "",
        "## Research Verdict",
        "",
        "This limit is more fundamental than the platform-specific model. The platform",
        "case becomes one application of a broader singular-limit theorem: when utility",
        "adapts infinitely fast, economics on fixed utility functions is replaced by",
        "economics on the critical manifold of preference adaptation.",
    ]

    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    taste_rows = taste_limit_rows()
    social_rows = social_limit_rows()
    platform_rows = platform_limit_rows()

    write_csv(ROOT / "results/tables/fast_limit_taste.csv", taste_rows)
    write_csv(ROOT / "results/tables/fast_limit_social.csv", social_rows)
    write_csv(ROOT / "results/tables/fast_limit_platform.csv", platform_rows)
    write_report(
        ROOT / "results/fast_preference_limit_report.md",
        taste_rows,
        social_rows,
        platform_rows,
    )


if __name__ == "__main__":
    main()
