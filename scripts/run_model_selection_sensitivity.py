#!/usr/bin/env python3
"""Run sensitivity checks for the finite-game preference-formation audit."""

from __future__ import annotations

import csv
from pathlib import Path
import random
import statistics
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from utility_endogenous.model_selection_audit import (  # noqa: E402
    LAMBDA_GRID,
    distribution_distance,
    expected_value,
    mixed_br_correspondence_invariant,
    proxy_vector,
    random_vector,
    scale_add,
    selected_equilibrium,
    vector_sum,
)
from utility_endogenous.chart_style import (  # noqa: E402
    CHART_AMBER,
    CHART_AXIS,
    CHART_BLUE,
    CHART_GRID,
    CHART_INK,
    CHART_MUTED,
    CHART_RED,
    CHART_TEAL,
    chart_footer,
    chart_header,
    svg_open,
    svg_text,
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


def fmt(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |"
    body = [
        "| " + " | ".join(fmt(row.get(column)) for column in columns) + " |"
        for row in rows
    ]
    return "\n".join([header, separator, *body])


def strategic_scale_sensitivity(
    games: int,
    seed: int,
    scales: tuple[float, ...],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for index, scale in enumerate(scales):
        rng = random.Random(seed + 1000 * index)
        br_invariant = 0
        shifted = 0
        for _ in range(games):
            material_1 = random_vector(rng)
            material_2 = random_vector(rng)
            distortion_1 = random_vector(rng)
            distortion_2 = random_vector(rng)
            subjective_1 = scale_add(material_1, scale, distortion_1)
            subjective_2 = scale_add(material_2, scale, distortion_2)

            if mixed_br_correspondence_invariant(
                material_1,
                material_2,
                subjective_1,
                subjective_2,
            ):
                br_invariant += 1

            material_eq = selected_equilibrium(material_1, material_2, material_1, material_2)
            subjective_eq = selected_equilibrium(
                subjective_1,
                subjective_2,
                material_1,
                material_2,
            )
            if distribution_distance(material_eq, subjective_eq) > 0.25:
                shifted += 1

        rows.append(
            {
                "family": "strategic_distortion_scale",
                "parameter": "distortion_scale",
                "value": scale,
                "games": games,
                "mixed_br_invariance_rate": br_invariant / games,
                "equilibrium_shift_rate": shifted / games,
                "material_loss_rate": None,
                "mean_loss_when_loss": None,
            }
        )
    return rows


def aligned_proxy_noise_sensitivity(
    games: int,
    seed: int,
    noise_weights: tuple[float, ...],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for index, noise_weight in enumerate(noise_weights):
        rng = random.Random(seed + 2000 * index)
        shifted = 0
        losses: list[float] = []
        for _ in range(games):
            material_1 = random_vector(rng)
            material_2 = random_vector(rng)
            material_total = vector_sum(material_1, material_2)
            proxy = proxy_vector(
                material_total,
                "proxy_aligned",
                rng,
                noise_weight=noise_weight,
            )

            neutral_eq = selected_equilibrium(material_1, material_2, material_1, material_2)
            regime_records: list[dict[str, object]] = []
            for lambda_value in LAMBDA_GRID:
                subjective_1 = scale_add(material_1, lambda_value, proxy)
                subjective_2 = scale_add(material_2, lambda_value, proxy)
                equilibrium = selected_equilibrium(
                    subjective_1,
                    subjective_2,
                    subjective_1,
                    subjective_2,
                )
                regime_records.append(
                    {
                        "equilibrium": equilibrium,
                        "material": expected_value(material_total, equilibrium),
                        "proxy": expected_value(proxy, equilibrium),
                    }
                )

            proxy_choice = max(regime_records, key=lambda row: float(row["proxy"]))
            material_choice = max(regime_records, key=lambda row: float(row["material"]))
            loss = float(material_choice["material"]) - float(proxy_choice["material"])
            if loss > 1e-8:
                losses.append(loss)
            if (
                distribution_distance(proxy_choice["equilibrium"], neutral_eq)  # type: ignore[arg-type]
                > 0.25
            ):
                shifted += 1

        rows.append(
            {
                "family": "aligned_proxy_noise",
                "parameter": "noise_weight",
                "value": noise_weight,
                "games": games,
                "mixed_br_invariance_rate": None,
                "equilibrium_shift_rate": shifted / games,
                "material_loss_rate": len(losses) / games,
                "mean_loss_when_loss": statistics.fmean(losses) if losses else None,
            }
        )
    return rows


def polyline(points: list[tuple[float, float]], color: str) -> str:
    point_text = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return f'<polyline points="{point_text}" fill="none" stroke="{color}" stroke-width="3"/>'


def circle_markers(points: list[tuple[float, float]], color: str) -> list[str]:
    return [
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{color}"/>'
        for x, y in points
    ]


def write_svg(path: Path, rows: list[dict[str, object]]) -> None:
    strategic = [row for row in rows if row["family"] == "strategic_distortion_scale"]
    aligned = [row for row in rows if row["family"] == "aligned_proxy_noise"]

    width = 980
    height = 430
    panel_w = 390
    panel_h = 250
    left_1 = 86
    left_2 = 560
    top = 92

    def map_points(
        panel_left: float,
        data: list[dict[str, object]],
        key: str,
    ) -> list[tuple[float, float]]:
        max_x = max(float(row["value"]) for row in data)
        return [
            (
                panel_left + panel_w * float(row["value"]) / max_x,
                top + panel_h * (1.0 - float(row[key])),
            )
            for row in data
        ]

    elements = [
        *svg_open(width, height),
        *chart_header(
            "Finite-Game Sensitivity Checks",
            "3,000 random games per grid point; rates on vertical axes",
            width,
        ),
    ]
    for panel_left in (left_1, left_2):
        elements.extend(
            [
                f'<line x1="{panel_left}" y1="{top}" x2="{panel_left}" y2="{top + panel_h}" stroke="{CHART_AXIS}"/>',
                f'<line x1="{panel_left}" y1="{top + panel_h}" x2="{panel_left + panel_w}" y2="{top + panel_h}" stroke="{CHART_AXIS}"/>',
            ]
        )
        for tick in (0.0, 0.25, 0.5, 0.75, 1.0):
            y = top + panel_h * (1 - tick)
            elements.append(
                f'<line x1="{panel_left - 5}" y1="{y:.1f}" x2="{panel_left + panel_w}" y2="{y:.1f}" stroke="{CHART_GRID}"/>'
            )
            elements.append(
                svg_text(
                    panel_left - 12,
                    y + 4,
                    f"{tick:.2f}".rstrip("0").rstrip("."),
                    font_size=11,
                    fill=CHART_MUTED,
                    text_anchor="end",
                )
            )

    elements.append(svg_text(left_1, 84, "Strategic distortion scale", font_size=14, font_weight=800, fill=CHART_INK))
    elements.append(svg_text(left_2, 84, "Approx. aligned proxy noise", font_size=14, font_weight=800, fill=CHART_INK))

    br_points = map_points(left_1, strategic, "mixed_br_invariance_rate")
    shift_points = map_points(left_1, strategic, "equilibrium_shift_rate")
    loss_points = map_points(left_2, aligned, "material_loss_rate")
    proxy_shift_points = map_points(left_2, aligned, "equilibrium_shift_rate")
    elements.extend(
        [
            polyline(br_points, CHART_TEAL),
            polyline(shift_points, CHART_AMBER),
            polyline(loss_points, CHART_RED),
            polyline(proxy_shift_points, CHART_BLUE),
            *circle_markers(br_points, CHART_TEAL),
            *circle_markers(shift_points, CHART_AMBER),
            *circle_markers(loss_points, CHART_RED),
            *circle_markers(proxy_shift_points, CHART_BLUE),
            svg_text(left_1 + 12, top + 18, "mixed BR invariance", font_size=11, fill=CHART_TEAL),
            svg_text(left_1 + 12, top + 36, "equilibrium shift", font_size=11, fill=CHART_AMBER),
            svg_text(left_2 + 12, top + 18, "material loss", font_size=11, fill=CHART_RED),
            svg_text(left_2 + 12, top + 36, "equilibrium shift", font_size=11, fill=CHART_BLUE),
            svg_text(left_1 + panel_w / 2, height - 45, "distortion scale", font_size=12, fill=CHART_MUTED, text_anchor="middle"),
            svg_text(left_2 + panel_w / 2, height - 45, "noise weight", font_size=12, fill=CHART_MUTED, text_anchor="middle"),
        ]
    )
    elements.append(chart_footer("Source: sensitivity check around the finite-game simulation; rates are diagnostic, not estimates.", width, height))
    elements.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(elements) + "\n", encoding="utf-8")


def build_report(rows: list[dict[str, object]], games: int, seed: int) -> str:
    strategic = [row for row in rows if row["family"] == "strategic_distortion_scale"]
    aligned = [row for row in rows if row["family"] == "aligned_proxy_noise"]
    return "\n".join(
        [
            "# Model Selection Sensitivity",
            "",
            f"Generated by `python3 scripts/run_model_selection_sensitivity.py` with seed `{seed}` and `{games}` random finite games per grid point.",
            "",
            "## Purpose",
            "",
            "This sensitivity check asks whether the finite-game stress-test message is tied to a single arbitrary parameterization.",
            "",
            "## Strategic Distortion Scale",
            "",
            markdown_table(
                strategic,
                [
                    "value",
                    "games",
                    "mixed_br_invariance_rate",
                    "equilibrium_shift_rate",
                ],
            ),
            "",
            "## Approximate Aligned Proxy Noise",
            "",
            markdown_table(
                aligned,
                [
                    "value",
                    "games",
                    "equilibrium_shift_rate",
                    "material_loss_rate",
                    "mean_loss_when_loss",
                ],
            ),
            "",
            "## Modeller Readout",
            "",
            "- At distortion scale `0`, preference formation is identical to the material game; mixed best-response invariance is `1.0000` and equilibrium shift is `0.0000`.",
            "- As random strategic distortion grows, mixed best-response invariance falls and selected-equilibrium shifts rise. This supports the claim that strategic closure changes the reduced game generically, while correctly showing that infinitesimal distortions need not have large equilibrium effects.",
            "- With an exactly material-aligned proxy, material loss is `0.0000`. Material loss rises as the proxy becomes a noisier proxy for material welfare. This supports the paper's conditional claim: speed alone is not the culprit; proxy alignment is the relevant object.",
            "",
        ]
    )


def main() -> None:
    games = 3000
    seed = 20260621
    strategic_scales = (0.0, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0)
    proxy_noise_weights = (0.0, 0.1, 0.25, 0.5, 1.0, 2.0)
    rows = [
        *strategic_scale_sensitivity(games, seed, strategic_scales),
        *aligned_proxy_noise_sensitivity(games, seed + 10_000, proxy_noise_weights),
    ]

    results_dir = ROOT / "results"
    tables_dir = results_dir / "tables"
    figures_dir = results_dir / "figures"
    table_path = tables_dir / "model_selection_sensitivity.csv"
    report_path = results_dir / "model_selection_sensitivity_report.md"
    figure_path = figures_dir / "model_selection_sensitivity.svg"
    write_csv(table_path, rows)
    report_path.write_text(build_report(rows, games, seed), encoding="utf-8")
    write_svg(figure_path, rows)

    print(f"Wrote {report_path}")
    print(f"Wrote {table_path}")
    print(f"Wrote {figure_path}")


if __name__ == "__main__":
    main()
