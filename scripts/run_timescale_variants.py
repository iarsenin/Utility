#!/usr/bin/env python3
"""Run timescale variants under instantaneous preference adaptation."""

from __future__ import annotations

import csv
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from utility_endogenous.timescale_variants import (
    TimescaleVariantParams,
    estimate_ar1_half_life,
    fixed_rule_survival_table,
    simulate_timescale_variant,
    summarize_variant,
)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows for {path}")
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


def scenario_params() -> list[TimescaleVariantParams]:
    return [
        TimescaleVariantParams(
            name="fixed_survival_rule",
            target_mode="fixed",
            fixed_target_exposure=0.05,
            institution_speed=0.00,
            population_speed=0.25,
        ),
        TimescaleVariantParams(
            name="fixed_capture_rule",
            target_mode="fixed",
            fixed_target_exposure=0.80,
            initial_exposure=0.80,
            institution_speed=0.00,
            population_speed=0.25,
        ),
        TimescaleVariantParams(
            name="slow_institution_slow_population_myopic",
            institution_speed=0.02,
            population_speed=0.05,
            survival_weight=0.00,
        ),
        TimescaleVariantParams(
            name="fast_institution_slow_population_myopic",
            institution_speed=1.00,
            population_speed=0.05,
            survival_weight=0.00,
        ),
        TimescaleVariantParams(
            name="slow_institution_fast_population_myopic",
            institution_speed=0.02,
            population_speed=1.00,
            survival_weight=0.00,
        ),
        TimescaleVariantParams(
            name="all_fast_myopic",
            institution_speed=1.00,
            population_speed=1.00,
            survival_weight=0.00,
        ),
        TimescaleVariantParams(
            name="all_fast_survival_aware",
            institution_speed=1.00,
            population_speed=1.00,
            survival_weight=0.75,
        ),
        TimescaleVariantParams(
            name="slow_institution_survival_aware",
            institution_speed=0.02,
            population_speed=1.00,
            survival_weight=0.75,
        ),
    ]


def write_report(
    path: Path,
    summary_rows: list[dict[str, object]],
    fixed_rows: list[dict[str, object]],
    estimate_rows: list[dict[str, object]],
) -> None:
    viable_fixed = [row for row in fixed_rows if row["survives_long_run"] is True]
    max_viable_exposure = max(float(row["fixed_exposure"]) for row in viable_fixed)
    all_fast = next(row for row in summary_rows if row["scenario"] == "all_fast_myopic")
    survival_aware = next(
        row for row in summary_rows if row["scenario"] == "all_fast_survival_aware"
    )

    lines = [
        "# Timescale Variant Report",
        "",
        "## Correction To Language",
        "",
        "Nash equilibrium and Darwinian selection are methods/operators. They",
        "do not disappear or break. What changes in the infinite",
        "preference-velocity limit is the state space to which those operators",
        "are applied.",
        "",
        "Corrected statement:",
        "",
        "```text",
        "Nash fixed points are computed after fast preference closure.",
        "Darwinian selection then acts on whatever variables remain heterogeneous:",
        "population shares, adaptation laws, institutions, or biological resistance.",
        "```",
        "",
        "## Timescale Identification",
        "",
        "Do not assume population or institutions are slower. Treat the speeds as",
        "estimable quantities. For a measured latent state `y_t`, a first-pass",
        "timescale estimate is the AR(1) half-life from:",
        "",
        "```text",
        "y_{t+1} = alpha + rho y_t + error_t",
        "speed = -log(rho) / Delta t",
        "half_life = log(2) / speed",
        "```",
        "",
        "Better empirical versions should use latent-state, dynamic discrete-choice,",
        "or random-intercept panel models when observed choices are noisy proxies for",
        "preferences.",
        "",
        "Illustrative half-life estimates from synthetic paths:",
        "",
        markdown_table(
            estimate_rows,
            ["process", "rho", "continuous_speed", "half_life"],
        ),
        "",
        "## Fixed-Rule Survival Frontier",
        "",
        "In the instantaneous preference limit, a fixed institutional exposure `m`",
        "induces `theta = m / (m + anchor)`. Long-run survival depends on the",
        "material growth rate at that induced preference state.",
        "",
        f"The largest grid-tested exposure with nonnegative growth is `{max_viable_exposure:.3f}`.",
        "",
        markdown_table(
            [row for index, row in enumerate(fixed_rows) if index % 5 == 0],
            [
                "fixed_exposure",
                "theta",
                "material_growth",
                "survives_long_run",
                "platform_flow_value",
            ],
        ),
        "",
        "## Variant Outcomes",
        "",
        markdown_table(
            summary_rows,
            [
                "scenario",
                "institution_speed",
                "population_speed",
                "survival_weight",
                "final_exposure",
                "final_theta",
                "mean_tail_growth",
                "extinct_period",
                "survives_long_run",
            ],
        ),
        "",
        "Key comparison:",
        "",
        f"- all-fast myopic institutions end at theta `{fmt(all_fast['final_theta'])}`",
        f"  and extinction period `{fmt(all_fast['extinct_period'])}`.",
        "- all-fast survival-aware institutions choose a lower exposure, end at",
        f"  theta `{fmt(survival_aware['final_theta'])}`, and survive.",
        "",
        "## Interpretation",
        "",
        "In the `T_pref -> 0` limit, short-run preferences are pinned by the fast",
        "closure map. Medium-run outcomes depend on the measured speeds of",
        "institutions and population dynamics. Long-run survival is determined by",
        "the growth rate of the whole induced system, not by subjective utility",
        "alone and not by material Nash predictions alone.",
        "",
        "Thus the Darwinian question should be phrased as:",
        "",
        "```text",
        "Which adaptation laws or institutional regimes induce nonnegative long-run",
        "growth after fast preference closure?",
        "```",
        "",
        "The answer can be none. If every admissible institution drives the fast",
        "preference attractor into negative material growth, the model predicts",
        "system extinction rather than a surviving preference type.",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    path_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []
    for params in scenario_params():
        records = simulate_timescale_variant(params)
        path_rows.extend(records)
        summary_rows.append(summarize_variant(records, params))

    base_params = TimescaleVariantParams(name="fixed_rule_grid")
    fixed_rows = fixed_rule_survival_table(base_params)

    estimate_rows = [
        {
            "process": "fast_preference_proxy",
            **estimate_ar1_half_life([0.20, 0.65, 0.83, 0.90, 0.93, 0.94]),
        },
        {
            "process": "slow_institution_proxy",
            **estimate_ar1_half_life([0.05, 0.09, 0.12, 0.144, 0.163, 0.178]),
        },
        {
            "process": "population_proxy",
            **estimate_ar1_half_life([1.00, 0.80, 0.64, 0.512, 0.410, 0.328]),
        },
    ]

    write_csv(ROOT / "results/tables/timescale_variant_paths.csv", path_rows)
    write_csv(ROOT / "results/tables/timescale_variant_summary.csv", summary_rows)
    write_csv(ROOT / "results/tables/timescale_fixed_rule_survival.csv", fixed_rows)
    write_csv(ROOT / "results/tables/timescale_estimates.csv", estimate_rows)
    write_report(
        ROOT / "results/timescale_variant_report.md",
        summary_rows,
        fixed_rows,
        estimate_rows,
    )


if __name__ == "__main__":
    main()
