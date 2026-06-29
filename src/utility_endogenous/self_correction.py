"""Self-correction diagnostics for fast endogenous preference feedback.

This module asks whether a material-reality signal automatically repairs a bad
preference-capacity loop. The intentionally sharp distinction is between:

1. an instantaneous drift signal, which reports whether capacity is currently
   rising or falling; and
2. an enduring stock signal, where the current material capacity itself changes
   the subjective payoff map.

The first channel can damp motion but cannot move steady states in the scalar
normal form. The second channel can remove low-capacity traps when it is strong
enough.
"""

from __future__ import annotations

import csv
from dataclasses import asdict, dataclass, replace
import math
from pathlib import Path

from .chart_style import (
    CHART_AMBER,
    CHART_BLUE,
    CHART_GRID,
    CHART_INK,
    CHART_MUTED,
    CHART_PANEL,
    CHART_RED,
    CHART_TEAL,
    CHART_VIOLET,
    chart_footer,
    chart_header,
    svg_open,
    svg_text,
)
from .material_feedback import (
    EPSILON,
    CapacityFeedbackParams,
    baseline_scenarios,
    capacity_drift,
    capacity_equilibria,
    logistic,
    substitute_share,
)


@dataclass(frozen=True)
class MaterialSignalEquilibrium:
    signal_strength: float
    capacity: float
    substitute_share: float
    drift_slope: float
    stable: bool
    root_error_vs_no_signal: float


@dataclass(frozen=True)
class StockFeedbackEquilibrium:
    capacity_protection: float
    capacity: float
    substitute_share: float
    drift_slope: float
    stable: bool
    interpretation: str


@dataclass(frozen=True)
class StockFeedbackSummary:
    capacity_protection: float
    stable_count: int
    low_trap_present: bool
    threshold_present: bool
    high_state_present: bool


@dataclass(frozen=True)
class CompetitionPathPoint:
    selection_metric: str
    competition_intensity: float
    time: float
    bridge_share: float
    bridge_capacity: float
    sink_capacity: float
    bridge_selection_score: float
    sink_selection_score: float
    bridge_material_growth: float
    sink_material_growth: float
    mean_material_growth: float
    population_mass: float


@dataclass(frozen=True)
class CompetitionSummary:
    selection_metric: str
    competition_intensity: float
    final_bridge_share: float
    final_bridge_capacity: float
    final_sink_capacity: float
    final_population_mass: float
    final_mean_material_growth: float
    verdict: str


def repair_flow(capacity: float, params: CapacityFeedbackParams) -> float:
    """Capacity drift before damage from substitute behavior."""

    return (
        params.baseline_repair
        + params.repair_strength * capacity * capacity * (1.0 - capacity)
        - params.decay_rate * capacity
    )


def repair_flow_derivative(capacity: float, params: CapacityFeedbackParams) -> float:
    return params.repair_strength * (2.0 * capacity - 3.0 * capacity * capacity) - params.decay_rate


def material_signal_share(
    capacity: float,
    params: CapacityFeedbackParams,
    signal_strength: float,
) -> float:
    """Fast share when subjective appeal includes current material drift.

    The fixed point is

        p = sigma(beta * [q + z - rho K + chi * (R(K) - L p)]).

    For chi >= 0, the left side minus the right side is strictly increasing in
    p, so bisection is globally well behaved on [0, 1].
    """

    left = 0.0
    right = 1.0
    for _ in range(90):
        mid = (left + right) / 2.0
        field = (
            params.subjective_pull
            + params.exposure
            - params.capacity_protection * capacity
            + signal_strength * (repair_flow(capacity, params) - params.substitute_damage * mid)
        )
        value = mid - logistic(params.sensitivity * field)
        if value < 0.0:
            left = mid
        else:
            right = mid
    return (left + right) / 2.0


def material_signal_drift(
    capacity: float,
    params: CapacityFeedbackParams,
    signal_strength: float,
) -> float:
    share = material_signal_share(capacity, params, signal_strength)
    return repair_flow(capacity, params) - params.substitute_damage * share


def material_signal_drift_derivative(
    capacity: float,
    params: CapacityFeedbackParams,
    signal_strength: float,
) -> float:
    share = material_signal_share(capacity, params, signal_strength)
    logit_slope = params.sensitivity * share * (1.0 - share)
    numerator = repair_flow_derivative(capacity, params) + (
        params.substitute_damage * logit_slope * params.capacity_protection
    )
    denominator = 1.0 + signal_strength * params.substitute_damage * logit_slope
    return numerator / denominator


def _signal_root(
    left: float,
    right: float,
    params: CapacityFeedbackParams,
    signal_strength: float,
    iterations: int = 90,
) -> float:
    f_left = material_signal_drift(left, params, signal_strength)
    if abs(f_left) <= EPSILON:
        return left
    for _ in range(iterations):
        mid = (left + right) / 2.0
        f_mid = material_signal_drift(mid, params, signal_strength)
        if abs(f_mid) <= EPSILON:
            return mid
        if f_left * f_mid <= 0.0:
            right = mid
        else:
            left = mid
            f_left = f_mid
    return (left + right) / 2.0


def material_signal_equilibria(
    params: CapacityFeedbackParams,
    signal_strength: float,
    grid_size: int = 4000,
) -> list[MaterialSignalEquilibrium]:
    roots: list[float] = []
    previous_capacity = 0.0
    previous_value = material_signal_drift(previous_capacity, params, signal_strength)
    for index in range(1, grid_size + 1):
        capacity = index / grid_size
        value = material_signal_drift(capacity, params, signal_strength)
        if previous_value * value < 0.0:
            roots.append(_signal_root(previous_capacity, capacity, params, signal_strength))
        previous_capacity = capacity
        previous_value = value

    no_signal_roots = [point.capacity for point in capacity_equilibria(params) if point.state_scope == "interior"]
    rows: list[MaterialSignalEquilibrium] = []
    for root in roots:
        nearest = min((abs(root - base_root) for base_root in no_signal_roots), default=float("nan"))
        slope = material_signal_drift_derivative(root, params, signal_strength)
        rows.append(
            MaterialSignalEquilibrium(
                signal_strength=signal_strength,
                capacity=root,
                substitute_share=material_signal_share(root, params, signal_strength),
                drift_slope=slope,
                stable=slope < 0.0,
                root_error_vs_no_signal=nearest,
            )
        )
    return rows


def stock_feedback_sweep(
    params: CapacityFeedbackParams,
    grid_points: int = 81,
    maximum_protection: float = 4.0,
) -> tuple[list[StockFeedbackEquilibrium], list[StockFeedbackSummary]]:
    equilibrium_rows: list[StockFeedbackEquilibrium] = []
    summary_rows: list[StockFeedbackSummary] = []
    for index in range(grid_points):
        rho = maximum_protection * index / (grid_points - 1)
        scenario = replace(params, capacity_protection=rho)
        equilibria = capacity_equilibria(scenario)
        stable = [point for point in equilibria if point.stable]
        low_trap = any(point.stable and point.capacity < 0.25 for point in equilibria)
        threshold = any((not point.stable) and 0.02 < point.capacity < 0.60 for point in equilibria)
        high_state = any(point.stable and point.capacity > 0.60 for point in equilibria)
        summary_rows.append(
            StockFeedbackSummary(
                capacity_protection=rho,
                stable_count=len(stable),
                low_trap_present=low_trap,
                threshold_present=threshold,
                high_state_present=high_state,
            )
        )
        for point in equilibria:
            if point.stable and point.capacity < 0.25:
                interpretation = "low trap"
            elif point.stable and point.capacity > 0.60:
                interpretation = "high state"
            elif not point.stable:
                interpretation = "threshold"
            else:
                interpretation = "other"
            equilibrium_rows.append(
                StockFeedbackEquilibrium(
                    capacity_protection=rho,
                    capacity=point.capacity,
                    substitute_share=point.substitute_share,
                    drift_slope=point.drift_slope,
                    stable=point.stable,
                    interpretation=interpretation,
                )
            )
    return equilibrium_rows, summary_rows


def material_growth_score(capacity: float, share: float) -> float:
    """Small material growth score for absolute survival diagnostics.

    A score above zero means the rule is compatible with long-run material
    persistence in this stylized audit. The coefficients are deliberately small
    because the score is integrated over many periods.
    """

    return 0.06 * capacity - 0.04 * share - 0.015


def selection_score(metric: str, capacity: float, share: float) -> float:
    if metric == "material viability":
        return material_growth_score(capacity, share)
    if metric == "engagement proxy":
        return share
    raise ValueError(f"Unknown selection metric: {metric}")


def simulate_rule_competition(
    bridge_params: CapacityFeedbackParams,
    sink_params: CapacityFeedbackParams,
    selection_metric: str,
    competition_intensity: float,
    horizon: float = 80.0,
    dt: float = 0.05,
    sample_every: float = 1.0,
) -> list[CompetitionPathPoint]:
    """Simulate two preference-forming rules competing for population share."""

    bridge_capacity = 0.15
    sink_capacity = 0.15
    bridge_share = 0.50
    population_mass = 1.0
    steps = int(horizon / dt)
    sample_steps = max(1, int(sample_every / dt))
    points: list[CompetitionPathPoint] = []
    for step in range(steps + 1):
        bridge_substitute = substitute_share(bridge_capacity, bridge_params)
        sink_substitute = substitute_share(sink_capacity, sink_params)
        bridge_growth = material_growth_score(bridge_capacity, bridge_substitute)
        sink_growth = material_growth_score(sink_capacity, sink_substitute)
        bridge_score = selection_score(selection_metric, bridge_capacity, bridge_substitute)
        sink_score = selection_score(selection_metric, sink_capacity, sink_substitute)
        mean_growth = bridge_share * bridge_growth + (1.0 - bridge_share) * sink_growth
        if step % sample_steps == 0:
            points.append(
                CompetitionPathPoint(
                    selection_metric=selection_metric,
                    competition_intensity=competition_intensity,
                    time=step * dt,
                    bridge_share=bridge_share,
                    bridge_capacity=bridge_capacity,
                    sink_capacity=sink_capacity,
                    bridge_selection_score=bridge_score,
                    sink_selection_score=sink_score,
                    bridge_material_growth=bridge_growth,
                    sink_material_growth=sink_growth,
                    mean_material_growth=mean_growth,
                    population_mass=population_mass,
                )
            )
        bridge_capacity = min(1.0, max(0.0, bridge_capacity + dt * capacity_drift(bridge_capacity, bridge_params)))
        sink_capacity = min(1.0, max(0.0, sink_capacity + dt * capacity_drift(sink_capacity, sink_params)))
        bridge_share += dt * competition_intensity * bridge_share * (1.0 - bridge_share) * (bridge_score - sink_score)
        bridge_share = min(1.0, max(0.0, bridge_share))
        population_mass *= math.exp(dt * mean_growth)
    return points


def run_rule_competition_audit() -> tuple[list[CompetitionPathPoint], list[CompetitionSummary]]:
    scenarios = baseline_scenarios()
    bridge = scenarios["resilient"]
    sink = scenarios["trap"]
    all_points: list[CompetitionPathPoint] = []
    summaries: list[CompetitionSummary] = []
    for metric in ["material viability", "engagement proxy"]:
        for intensity in [0.0, 0.4, 1.2]:
            path = simulate_rule_competition(bridge, sink, metric, intensity)
            all_points.extend(path)
            final = path[-1]
            if intensity == 0.0:
                verdict = "no competition: shares remain fixed"
            elif metric == "material viability":
                verdict = "competition selects the capacity-preserving rule"
            elif final.bridge_share < 0.10:
                verdict = "competition selects the high-engagement sink"
            else:
                verdict = "proxy competition weakly favors the sink"
            summaries.append(
                CompetitionSummary(
                    selection_metric=metric,
                    competition_intensity=intensity,
                    final_bridge_share=final.bridge_share,
                    final_bridge_capacity=final.bridge_capacity,
                    final_sink_capacity=final.sink_capacity,
                    final_population_mass=final.population_mass,
                    final_mean_material_growth=final.mean_material_growth,
                    verdict=verdict,
                )
            )
    return all_points, summaries


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows for {path}")
    fieldnames: list[str] = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _polyline(points: list[tuple[float, float]], color: str, width: float = 3.0) -> str:
    point_text = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return f'<polyline points="{point_text}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"/>'


def write_self_correction_svg(
    path: Path,
    signal_rows: list[MaterialSignalEquilibrium],
    stock_rows: list[StockFeedbackEquilibrium],
) -> None:
    width = 940
    height = 640
    left = 78
    right = 46
    top = 114
    panel_gap = 64
    panel_width = (width - left - right - panel_gap) / 2.0
    panel_height = 390
    bottom = top + panel_height

    def y_scale(capacity: float) -> float:
        return top + panel_height * (1.0 - capacity)

    def x_signal(value: float) -> float:
        return left + panel_width * math.log1p(value) / math.log1p(50.0)

    stock_left = left + panel_width + panel_gap

    def x_stock(value: float) -> float:
        return stock_left + panel_width * value / 4.0

    elements = [
        *svg_open(width, height),
        *chart_header(
            "Two Kinds Of Reality Feedback",
            "Instant deterioration signals damp motion; stock-level feedback can remove a low-capacity trap",
            width,
        ),
    ]

    for panel_left, panel_title in [
        (left, "A. Current deterioration signal"),
        (stock_left, "B. Capacity stock signal"),
    ]:
        elements.append(svg_text(panel_left, top - 20, panel_title, font_size=14, font_weight=800, fill=CHART_INK))
        elements.append(
            f'<rect x="{panel_left}" y="{top}" width="{panel_width}" height="{panel_height}" fill="#ffffff" stroke="{CHART_GRID}"/>'
        )
        for tick in [0.0, 0.25, 0.5, 0.75, 1.0]:
            y = y_scale(tick)
            elements.append(
                f'<line x1="{panel_left}" y1="{y:.1f}" x2="{panel_left + panel_width}" y2="{y:.1f}" stroke="{CHART_GRID}" stroke-width="1"/>'
            )
            if panel_left == left:
                elements.append(svg_text(panel_left - 11, y + 4, f"{tick:.2f}".rstrip("0").rstrip("."), font_size=11, fill=CHART_MUTED, text_anchor="end"))

    signal_groups: dict[str, list[tuple[float, float]]] = {"low": [], "threshold": [], "high": []}
    for row in signal_rows:
        if row.capacity < 0.18:
            signal_groups["low"].append((row.signal_strength, row.capacity))
        elif row.capacity < 0.55:
            signal_groups["threshold"].append((row.signal_strength, row.capacity))
        else:
            signal_groups["high"].append((row.signal_strength, row.capacity))
    for label, color in [("low", CHART_RED), ("threshold", CHART_VIOLET), ("high", CHART_TEAL)]:
        points = [(x_signal(x), y_scale(y)) for x, y in sorted(signal_groups[label])]
        if len(points) >= 2:
            elements.append(_polyline(points, color, 3.0))

    for tick in [0, 1, 5, 10, 50]:
        x = x_signal(float(tick))
        elements.append(svg_text(x, bottom + 24, str(tick), font_size=11, fill=CHART_MUTED, text_anchor="middle"))
        elements.append(f'<line x1="{x:.1f}" y1="{bottom}" x2="{x:.1f}" y2="{bottom + 6}" stroke="{CHART_MUTED}"/>')
    elements.append(svg_text(left + panel_width / 2, bottom + 48, "material-drift salience chi", font_size=12, fill=CHART_MUTED, text_anchor="middle"))

    stock_colors = {"low trap": CHART_RED, "threshold": CHART_VIOLET, "high state": CHART_TEAL, "other": CHART_AMBER}
    for row in stock_rows:
        x = x_stock(row.capacity_protection)
        y = y_scale(row.capacity)
        radius = 3.8 if row.stable else 3.1
        fill = stock_colors[row.interpretation] if row.stable else CHART_PANEL
        stroke = stock_colors[row.interpretation]
        elements.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="1.7"/>')
    for tick in [0, 1, 2, 3, 4]:
        x = x_stock(float(tick))
        elements.append(svg_text(x, bottom + 24, str(tick), font_size=11, fill=CHART_MUTED, text_anchor="middle"))
        elements.append(f'<line x1="{x:.1f}" y1="{bottom}" x2="{x:.1f}" y2="{bottom + 6}" stroke="{CHART_MUTED}"/>')
    elements.append(svg_text(stock_left + panel_width / 2, bottom + 48, "capacity protection rho", font_size=12, fill=CHART_MUTED, text_anchor="middle"))

    legend_y = bottom + 92
    legend_items = [
        ("low trap", CHART_RED),
        ("threshold", CHART_VIOLET),
        ("high state", CHART_TEAL),
    ]
    for index, (label, color) in enumerate(legend_items):
        x = left + 230 * index
        elements.append(f'<circle cx="{x}" cy="{legend_y}" r="6" fill="{color}" stroke="{color}" stroke-width="1.5"/>')
        elements.append(svg_text(x + 13, legend_y + 4, label, font_size=12, font_weight=700, fill=CHART_INK))

    elements.append(svg_text(27, top + panel_height / 2, "equilibrium capacity K", font_size=12, fill=CHART_MUTED, transform=f"rotate(-90 27 {top + panel_height / 2})", text_anchor="middle"))
    elements.append(chart_footer("Same baseline trap calibration. Panel A varies chi; Panel B varies rho.", width, height))
    elements.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(elements) + "\n", encoding="utf-8")


def write_competition_svg(path: Path, points: list[CompetitionPathPoint]) -> None:
    width = 940
    height = 700
    left = 78
    right = 52
    top = 118
    column_gap = 64
    row_gap = 58
    panel_width = (width - left - right - column_gap) / 2.0
    panel_height = 190
    share_top = top
    mass_top = top + panel_height + row_gap
    bottom = mass_top + panel_height
    horizon = max(point.time for point in points)
    selected_intensity = 1.2

    def x_scale(panel_left: float, time: float) -> float:
        return panel_left + panel_width * time / horizon

    def y_unit(panel_top: float, value: float) -> float:
        return panel_top + panel_height * (1.0 - value)

    max_mass = max(
        point.population_mass
        for point in points
        if abs(point.competition_intensity - selected_intensity) < 1e-9
    )
    mass_axis_max = max(6.0, math.ceil(max_mass))

    def y_mass(value: float) -> float:
        return mass_top + panel_height * (1.0 - min(value, mass_axis_max) / mass_axis_max)

    elements = [
        *svg_open(width, height),
        *chart_header(
            "Competition Selects Whatever It Scores",
            "The same bridge and sink have opposite outcomes when the contest rewards viability versus engagement",
            width,
        ),
    ]

    panels = [
        ("material viability", left, "A. Competition on material viability"),
        ("engagement proxy", left + panel_width + column_gap, "B. Competition on engagement"),
    ]
    for metric, panel_left, panel_title in panels:
        panel_points = [
            point
            for point in points
            if point.selection_metric == metric and abs(point.competition_intensity - selected_intensity) < 1e-9
        ]
        elements.append(svg_text(panel_left, share_top - 22, panel_title, font_size=14, font_weight=800, fill=CHART_INK))
        for panel_top, row_label in [(share_top, "Bridge share"), (mass_top, "Carrier mass")]:
            elements.append(
                f'<rect x="{panel_left}" y="{panel_top}" width="{panel_width}" height="{panel_height}" fill="#ffffff" stroke="{CHART_GRID}"/>'
            )
            elements.append(svg_text(panel_left + 12, panel_top + 22, row_label, font_size=12, font_weight=800, fill=CHART_INK))
            for tick in [0.0, 0.5, 1.0]:
                y = y_unit(panel_top, tick) if panel_top == share_top else y_mass(tick * mass_axis_max)
                elements.append(
                    f'<line x1="{panel_left}" y1="{y:.1f}" x2="{panel_left + panel_width}" y2="{y:.1f}" stroke="{CHART_GRID}" stroke-width="1"/>'
                )
                if panel_left == left:
                    label = f"{tick:.1f}".rstrip("0").rstrip(".") if panel_top == share_top else f"{tick * mass_axis_max:.0f}"
                    elements.append(svg_text(panel_left - 11, y + 4, label, font_size=11, fill=CHART_MUTED, text_anchor="end"))
            for tick in [0, 20, 40, 60, 80]:
                x = x_scale(panel_left, tick)
                elements.append(f'<line x1="{x:.1f}" y1="{panel_top + panel_height}" x2="{x:.1f}" y2="{panel_top + panel_height + 5}" stroke="{CHART_MUTED}"/>')
                if panel_top == mass_top:
                    elements.append(svg_text(x, bottom + 24, str(tick), font_size=11, fill=CHART_MUTED, text_anchor="middle"))

        share_line = [(x_scale(panel_left, point.time), y_unit(share_top, point.bridge_share)) for point in panel_points]
        mass_line = [(x_scale(panel_left, point.time), y_mass(point.population_mass)) for point in panel_points]
        elements.append(_polyline(share_line, CHART_TEAL, 3.2))
        elements.append(_polyline(mass_line, CHART_RED, 3.2))
        final = panel_points[-1]
        share_note = f"ends at {final.bridge_share:.2f}"
        mass_note = f"ends at {final.population_mass:.2f}"
        elements.append(svg_text(panel_left + panel_width - 16, share_top + 24, share_note, font_size=12, font_weight=800, fill=CHART_TEAL, text_anchor="end"))
        elements.append(svg_text(panel_left + panel_width - 16, mass_top + 24, mass_note, font_size=12, font_weight=800, fill=CHART_RED, text_anchor="end"))
        elements.append(svg_text(panel_left + panel_width / 2, bottom + 50, "slow time", font_size=12, fill=CHART_MUTED, text_anchor="middle"))

    legend_y = bottom + 86
    elements.append(f'<line x1="{left}" y1="{legend_y}" x2="{left + 32}" y2="{legend_y}" stroke="{CHART_TEAL}" stroke-width="4" stroke-linecap="round"/>')
    elements.append(svg_text(left + 42, legend_y + 4, "share governed by bridge rule", font_size=12, font_weight=700, fill=CHART_INK))
    elements.append(f'<line x1="{left + 320}" y1="{legend_y}" x2="{left + 352}" y2="{legend_y}" stroke="{CHART_RED}" stroke-width="4" stroke-linecap="round"/>')
    elements.append(svg_text(left + 362, legend_y + 4, "absolute carrier mass", font_size=12, font_weight=700, fill=CHART_INK))
    elements.append(svg_text(27, share_top + panel_height / 2, "share", font_size=12, fill=CHART_MUTED, transform=f"rotate(-90 27 {share_top + panel_height / 2})", text_anchor="middle"))
    elements.append(svg_text(27, mass_top + panel_height / 2, "mass", font_size=12, fill=CHART_MUTED, transform=f"rotate(-90 27 {mass_top + panel_height / 2})", text_anchor="middle"))
    elements.append(chart_footer("Bridge and sink start at the same capacity and equal shares. Competition intensity omega = 1.2.", width, height))
    elements.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(elements) + "\n", encoding="utf-8")


def run_self_correction_analysis(root: Path) -> dict[str, object]:
    params = baseline_scenarios()["trap"]
    signal_values = [0.0, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0]
    signal_rows = [
        row
        for signal in signal_values
        for row in material_signal_equilibria(params, signal)
    ]
    stock_rows, stock_summary = stock_feedback_sweep(params)
    competition_points, competition_summary = run_rule_competition_audit()

    tables = root / "results" / "tables"
    figures = root / "results" / "figures"
    signal_path = tables / "self_correction_material_signal_roots.csv"
    stock_path = tables / "self_correction_stock_feedback_roots.csv"
    stock_summary_path = tables / "self_correction_stock_feedback_summary.csv"
    competition_path = tables / "self_correction_competition_paths.csv"
    competition_summary_path = tables / "self_correction_competition_summary.csv"
    figure_path = figures / "self_correction_channels.svg"
    competition_figure_path = figures / "competition_selection_channels.svg"
    write_csv(signal_path, [asdict(row) for row in signal_rows])
    write_csv(stock_path, [asdict(row) for row in stock_rows])
    write_csv(stock_summary_path, [asdict(row) for row in stock_summary])
    write_csv(competition_path, [asdict(row) for row in competition_points])
    write_csv(competition_summary_path, [asdict(row) for row in competition_summary])
    write_self_correction_svg(figure_path, signal_rows, stock_rows)
    write_competition_svg(competition_figure_path, competition_points)

    first_self_correcting = next(
        (
            row.capacity_protection
            for row in stock_summary
            if row.high_state_present and not row.low_trap_present
        ),
        float("nan"),
    )
    max_signal_root_error = max(row.root_error_vs_no_signal for row in signal_rows)
    return {
        "signal_rows": signal_rows,
        "stock_rows": stock_rows,
        "stock_summary": stock_summary,
        "competition_points": competition_points,
        "competition_summary": competition_summary,
        "first_self_correcting_rho": first_self_correcting,
        "max_signal_root_error": max_signal_root_error,
        "tables": [signal_path, stock_path, stock_summary_path, competition_path, competition_summary_path],
        "figures": [figure_path, competition_figure_path],
    }
