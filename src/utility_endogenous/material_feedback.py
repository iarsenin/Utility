"""Fast subjective payoff formation with slow material-capacity feedback.

The model is intentionally small. A fast preference-forming system maps a slow
capacity stock into the subjective payoff of a substitute action. The chosen
action then changes the capacity stock. This gives a closed reduced dynamic in
the fast-preference limit.
"""

from __future__ import annotations

import csv
from dataclasses import asdict, dataclass, replace
import math
from pathlib import Path
import random

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


EPSILON = 1e-10

AUDIT_CLASSES: tuple[tuple[str, float, float, float, float, float, float], ...] = (
    ("weak feedback", 0.04, 0.12, 8.0, 18.0, 0.55, 1.00),
    ("trap-prone feedback", 0.12, 0.24, 10.0, 24.0, 0.70, 1.20),
    ("collapse-prone feedback", 0.20, 0.36, 14.0, 30.0, 0.75, 1.35),
)


@dataclass(frozen=True)
class CapacityFeedbackParams:
    """Parameters for the reduced capacity dynamic.

    capacity K is normalized to [0, 1].
    substitute_share is the fast-settled probability/share of a substitute
    behavior such as solitary media use, betting, hyper-palatable food, or an
    outrage feed.
    """

    name: str
    baseline_repair: float
    repair_strength: float
    decay_rate: float
    substitute_damage: float
    sensitivity: float
    subjective_pull: float
    capacity_protection: float
    exposure: float = 0.0


@dataclass(frozen=True)
class CapacityEquilibrium:
    scenario: str
    capacity: float
    substitute_share: float
    drift_slope: float
    stable: bool
    state_scope: str


@dataclass(frozen=True)
class CapacityPathPoint:
    scenario: str
    initial_capacity: float
    time: float
    capacity: float
    substitute_share: float


@dataclass(frozen=True)
class FeedbackAuditRow:
    feedback_class: str
    draws: int
    one_stable_state_rate: float
    multiple_stable_states_rate: float
    no_interior_stable_state_rate: float
    lower_boundary_state_rate: float
    low_high_trap_rate: float
    mean_trap_threshold_when_present: float
    median_trap_threshold_when_present: float


def logistic(value: float) -> float:
    value = max(-60.0, min(60.0, value))
    return 1.0 / (1.0 + math.exp(-value))


def substitute_share(capacity: float, params: CapacityFeedbackParams) -> float:
    """Fast-settled subjective probability/share of the substitute action."""

    field = params.subjective_pull + params.exposure - params.capacity_protection * capacity
    return logistic(params.sensitivity * field)


def capacity_drift(capacity: float, params: CapacityFeedbackParams) -> float:
    """Reduced slow dynamic after fast subjective payoff adjustment."""

    repair = params.baseline_repair + params.repair_strength * capacity * capacity * (1.0 - capacity)
    decay = params.decay_rate * capacity
    damage = params.substitute_damage * substitute_share(capacity, params)
    return repair - decay - damage


def capacity_drift_derivative(capacity: float, params: CapacityFeedbackParams) -> float:
    p = substitute_share(capacity, params)
    repair_derivative = params.repair_strength * (2.0 * capacity - 3.0 * capacity * capacity)
    decay_derivative = -params.decay_rate
    damage_derivative = (
        params.substitute_damage
        * params.sensitivity
        * params.capacity_protection
        * p
        * (1.0 - p)
    )
    return repair_derivative + decay_derivative + damage_derivative


def _bisection_root(
    left: float,
    right: float,
    params: CapacityFeedbackParams,
    iterations: int = 80,
) -> float:
    f_left = capacity_drift(left, params)
    f_right = capacity_drift(right, params)
    if abs(f_left) <= EPSILON:
        return left
    if abs(f_right) <= EPSILON:
        return right
    for _ in range(iterations):
        mid = (left + right) / 2.0
        f_mid = capacity_drift(mid, params)
        if abs(f_mid) <= EPSILON:
            return mid
        if f_left * f_mid <= 0.0:
            right = mid
            f_right = f_mid
        else:
            left = mid
            f_left = f_mid
    return (left + right) / 2.0


def capacity_equilibria(
    params: CapacityFeedbackParams,
    grid_size: int = 4000,
) -> list[CapacityEquilibrium]:
    """Return equilibria of the projected dynamic on [0, 1].

    Interior roots solve the unprojected drift equation. A boundary is an
    equilibrium when the unprojected drift points out of the feasible interval.
    """

    roots: list[float] = []
    previous_k = 0.0
    previous_value = capacity_drift(previous_k, params)
    for index in range(1, grid_size + 1):
        capacity = index / grid_size
        value = capacity_drift(capacity, params)
        if abs(value) <= 1e-7:
            roots.append(capacity)
        if previous_value * value < 0.0:
            roots.append(_bisection_root(previous_k, capacity, params))
        previous_k = capacity
        previous_value = value

    unique_roots: list[float] = []
    for root in sorted(roots):
        if not unique_roots or abs(root - unique_roots[-1]) > 1e-5:
            unique_roots.append(root)

    equilibria: list[CapacityEquilibrium] = []
    if capacity_drift(0.0, params) <= 0.0:
        equilibria.append(
            CapacityEquilibrium(
                scenario=params.name,
                capacity=0.0,
                substitute_share=substitute_share(0.0, params),
                drift_slope=capacity_drift_derivative(0.0, params),
                stable=True,
                state_scope="lower boundary",
            )
        )
    for root in unique_roots:
        slope = capacity_drift_derivative(root, params)
        equilibria.append(
            CapacityEquilibrium(
                scenario=params.name,
                capacity=root,
                substitute_share=substitute_share(root, params),
                drift_slope=slope,
                stable=slope < 0.0,
                state_scope="interior",
            )
        )
    if capacity_drift(1.0, params) >= 0.0:
        equilibria.append(
            CapacityEquilibrium(
                scenario=params.name,
                capacity=1.0,
                substitute_share=substitute_share(1.0, params),
                drift_slope=capacity_drift_derivative(1.0, params),
                stable=True,
                state_scope="upper boundary",
            )
        )
    return equilibria


def simulate_capacity_path(
    params: CapacityFeedbackParams,
    initial_capacity: float,
    horizon: float = 80.0,
    dt: float = 0.05,
    sample_every: float = 1.0,
) -> list[CapacityPathPoint]:
    capacity = min(1.0, max(0.0, initial_capacity))
    points: list[CapacityPathPoint] = []
    steps = int(horizon / dt)
    sample_steps = max(1, int(sample_every / dt))
    for step in range(steps + 1):
        if step % sample_steps == 0:
            points.append(
                CapacityPathPoint(
                    scenario=params.name,
                    initial_capacity=initial_capacity,
                    time=step * dt,
                    capacity=capacity,
                    substitute_share=substitute_share(capacity, params),
                )
            )
        drift = capacity_drift(capacity, params)
        capacity = min(1.0, max(0.0, capacity + dt * drift))
    return points


def classify_equilibria(params: CapacityFeedbackParams) -> dict[str, object]:
    equilibria = capacity_equilibria(params)
    stable = [point for point in equilibria if point.stable]
    interior_stable = [point for point in stable if point.state_scope == "interior"]
    lower_boundary = any(point.state_scope == "lower boundary" for point in stable)
    trap_threshold = None
    for point in equilibria:
        if point.stable or point.state_scope != "interior":
            continue
        has_low_stable = any(
            stable_point.state_scope == "interior"
            and stable_point.capacity < point.capacity
            and stable_point.capacity < 0.25
            for stable_point in stable
        )
        has_high_stable = any(
            stable_point.capacity > point.capacity and stable_point.capacity > 0.60
            for stable_point in stable
        )
        if has_low_stable and has_high_stable:
            trap_threshold = point.capacity
            break
    return {
        "stable_count": len(stable),
        "interior_stable_count": len(interior_stable),
        "lower_boundary": lower_boundary,
        "low_high_trap": trap_threshold is not None,
        "trap_threshold": trap_threshold,
    }


def feedback_parameter_audit(draws: int = 3000, seed: int = 20260626) -> list[FeedbackAuditRow]:
    rng = random.Random(seed)
    rows: list[FeedbackAuditRow] = []
    for label, damage_low, damage_high, beta_low, beta_high, rho_low, rho_high in AUDIT_CLASSES:
        stable_counts: list[int] = []
        interior_stable_counts: list[int] = []
        lower_boundary_count = 0
        trap_count = 0
        thresholds: list[float] = []
        for _ in range(draws):
            params = CapacityFeedbackParams(
                name=label,
                baseline_repair=rng.uniform(0.10, 0.28),
                repair_strength=rng.uniform(1.0, 4.0),
                decay_rate=rng.uniform(0.22, 0.78),
                substitute_damage=rng.uniform(damage_low, damage_high),
                sensitivity=rng.uniform(beta_low, beta_high),
                subjective_pull=rng.uniform(0.35, 0.65),
                capacity_protection=rng.uniform(rho_low, rho_high),
                exposure=rng.uniform(-0.05, 0.10),
            )
            classified = classify_equilibria(params)
            stable_count = int(classified["stable_count"])
            stable_counts.append(stable_count)
            interior_stable_counts.append(int(classified["interior_stable_count"]))
            if bool(classified["lower_boundary"]):
                lower_boundary_count += 1
            if bool(classified["low_high_trap"]):
                trap_count += 1
                thresholds.append(float(classified["trap_threshold"]))

        one_stable = sum(1 for count in stable_counts if count == 1)
        multiple = sum(1 for count in stable_counts if count >= 2)
        none = sum(1 for count in interior_stable_counts if count == 0)
        thresholds_sorted = sorted(thresholds)
        if thresholds_sorted:
            mean_threshold = sum(thresholds_sorted) / len(thresholds_sorted)
            median_threshold = thresholds_sorted[len(thresholds_sorted) // 2]
        else:
            mean_threshold = float("nan")
            median_threshold = float("nan")
        rows.append(
            FeedbackAuditRow(
                feedback_class=label,
                draws=draws,
                one_stable_state_rate=one_stable / draws,
                multiple_stable_states_rate=multiple / draws,
                no_interior_stable_state_rate=none / draws,
                lower_boundary_state_rate=lower_boundary_count / draws,
                low_high_trap_rate=trap_count / draws,
                mean_trap_threshold_when_present=mean_threshold,
                median_trap_threshold_when_present=median_threshold,
            )
        )
    return rows


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
    value = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return f'<polyline points="{value}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"/>'


def write_phase_svg(path: Path, scenarios: list[CapacityFeedbackParams]) -> None:
    width = 940
    height = 560
    left = 86
    right = 50
    top = 104
    bottom = 82
    chart_width = width - left - right
    chart_height = height - top - bottom
    y_min = -0.50
    y_max = 0.32

    def x_scale(capacity: float) -> float:
        return left + chart_width * capacity

    def y_scale(value: float) -> float:
        return top + chart_height * (y_max - value) / (y_max - y_min)

    colors = [CHART_TEAL, CHART_RED, CHART_BLUE, CHART_AMBER]
    elements = [
        *svg_open(width, height),
        *chart_header(
            "Material-Capacity Feedback",
            "A fast subjective payoff can create one stable capacity level or a low-capacity trap",
            width,
        ),
    ]
    for tick in [0.0, 0.25, 0.5, 0.75, 1.0]:
        x = x_scale(tick)
        elements.append(
            f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{height - bottom}" stroke="{CHART_GRID}" stroke-width="1"/>'
        )
        elements.append(svg_text(x, height - 55, f"{tick:.2f}".rstrip("0").rstrip("."), font_size=11, fill=CHART_MUTED, text_anchor="middle"))
    for tick in [-0.4, -0.2, 0.0, 0.2]:
        y = y_scale(tick)
        elements.append(
            f'<line x1="{left}" y1="{y:.1f}" x2="{width - right}" y2="{y:.1f}" stroke="{CHART_GRID}" stroke-width="1"/>'
        )
        elements.append(svg_text(left - 13, y + 4, f"{tick:.1f}", font_size=11, fill=CHART_MUTED, text_anchor="end"))
    zero_y = y_scale(0.0)
    elements.append(f'<line x1="{left}" y1="{zero_y:.1f}" x2="{width - right}" y2="{zero_y:.1f}" stroke="{CHART_INK}" stroke-width="1.3"/>')
    elements.append(svg_text(left + chart_width / 2, height - 34, "material capacity K", font_size=12, fill=CHART_MUTED, text_anchor="middle"))
    elements.append(svg_text(28, top + chart_height / 2, "capacity drift", font_size=12, fill=CHART_MUTED, transform=f"rotate(-90 28 {top + chart_height / 2})", text_anchor="middle"))

    for index, params in enumerate(scenarios):
        color = colors[index % len(colors)]
        sampled = []
        for point in range(401):
            capacity = point / 400
            value = capacity_drift(capacity, params)
            value = max(y_min, min(y_max, value))
            sampled.append((x_scale(capacity), y_scale(value)))
        elements.append(_polyline(sampled, color, 3.2))
        for equilibrium in capacity_equilibria(params):
            x = x_scale(equilibrium.capacity)
            y = y_scale(0.0)
            fill = color if equilibrium.stable else CHART_PANEL
            elements.append(
                f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6.5" fill="{fill}" stroke="{color}" stroke-width="2"/>'
            )
        legend_x = 650
        legend_y = 118 + 26 * index
        elements.append(f'<line x1="{legend_x}" y1="{legend_y}" x2="{legend_x + 26}" y2="{legend_y}" stroke="{color}" stroke-width="4" stroke-linecap="round"/>')
        elements.append(svg_text(legend_x + 34, legend_y + 4, params.name, font_size=12, font_weight=700, fill=CHART_INK))

    elements.append(chart_footer("Filled dots are stable equilibria; open dots are thresholds. Source: scripts/run_material_feedback_analysis.py.", width, height))
    elements.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(elements) + "\n", encoding="utf-8")


def write_paths_svg(path: Path, paths: list[list[CapacityPathPoint]]) -> None:
    width = 940
    height = 560
    left = 78
    right = 48
    top = 104
    bottom = 78
    chart_width = width - left - right
    chart_height = height - top - bottom
    horizon = max(point.time for path_points in paths for point in path_points)

    def x_scale(time: float) -> float:
        return left + chart_width * time / horizon

    def y_scale(capacity: float) -> float:
        return top + chart_height * (1.0 - capacity)

    colors = [CHART_RED, CHART_TEAL, CHART_BLUE, CHART_AMBER]
    elements = [
        *svg_open(width, height),
        *chart_header(
            "Same Payoff Rule, Different Basins",
            "Small differences in initial material capacity can settle into different long-run states",
            width,
        ),
    ]
    for tick in [0, 20, 40, 60, 80]:
        x = x_scale(tick)
        elements.append(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{height - bottom}" stroke="{CHART_GRID}" stroke-width="1"/>')
        elements.append(svg_text(x, height - 52, str(tick), font_size=11, fill=CHART_MUTED, text_anchor="middle"))
    for tick in [0.0, 0.25, 0.5, 0.75, 1.0]:
        y = y_scale(tick)
        elements.append(f'<line x1="{left}" y1="{y:.1f}" x2="{width - right}" y2="{y:.1f}" stroke="{CHART_GRID}" stroke-width="1"/>')
        elements.append(svg_text(left - 12, y + 4, f"{tick:.2f}".rstrip("0").rstrip("."), font_size=11, fill=CHART_MUTED, text_anchor="end"))
    elements.append(svg_text(left + chart_width / 2, height - 31, "slow time", font_size=12, fill=CHART_MUTED, text_anchor="middle"))
    elements.append(svg_text(25, top + chart_height / 2, "capacity K", font_size=12, fill=CHART_MUTED, transform=f"rotate(-90 25 {top + chart_height / 2})", text_anchor="middle"))
    for index, path_points in enumerate(paths):
        color = colors[index % len(colors)]
        line = [(x_scale(point.time), y_scale(point.capacity)) for point in path_points]
        elements.append(_polyline(line, color, 3.2))
        label = f"{path_points[0].scenario}, K0={path_points[0].initial_capacity:.2f}"
        legend_x = 604
        legend_y = 120 + 26 * index
        elements.append(f'<line x1="{legend_x}" y1="{legend_y}" x2="{legend_x + 26}" y2="{legend_y}" stroke="{color}" stroke-width="4" stroke-linecap="round"/>')
        elements.append(svg_text(legend_x + 34, legend_y + 4, label, font_size=12, font_weight=700, fill=CHART_INK))
    elements.append(chart_footer("Capacity is normalized to [0,1]. Paths use explicit Euler with dt=0.05.", width, height))
    elements.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(elements) + "\n", encoding="utf-8")


def write_audit_svg(path: Path, rows: list[FeedbackAuditRow]) -> None:
    width = 940
    height = 500
    left = 238
    right = 66
    top = 108
    bottom = 66
    row_height = 82
    chart_width = width - left - right
    elements = [
        *svg_open(width, height),
        *chart_header(
            "When Do Capacity Traps Or Boundary States Appear?",
            "Random parameter audit across weak, trap-prone, and collapse-prone feedback classes",
            width,
        ),
    ]
    for tick in [0.0, 0.25, 0.5, 0.75, 1.0]:
        x = left + chart_width * tick
        elements.append(f'<line x1="{x:.1f}" y1="{top - 18}" x2="{x:.1f}" y2="{height - bottom + 7}" stroke="{CHART_GRID}" stroke-width="1"/>')
        elements.append(svg_text(x, height - 42, f"{tick:.2f}".rstrip("0").rstrip("."), font_size=11, fill=CHART_MUTED, text_anchor="middle"))
    colors = [CHART_TEAL, CHART_AMBER, CHART_RED]
    for index, row in enumerate(rows):
        y = top + row_height * index
        elements.append(svg_text(36, y + 22, row.feedback_class.title(), font_size=14, font_weight=800, fill=CHART_INK))
        elements.append(svg_text(36, y + 43, f"{row.draws:,} draws", font_size=11, fill=CHART_MUTED))
        multiple_width = chart_width * row.multiple_stable_states_rate
        boundary_width = chart_width * row.lower_boundary_state_rate
        trap_width = chart_width * row.low_high_trap_rate
        elements.append(f'<rect x="{left}" y="{y + 6}" width="{max(1, multiple_width):.1f}" height="22" rx="3" fill="{colors[index]}"/>')
        elements.append(f'<rect x="{left}" y="{y + 34}" width="{max(1, trap_width):.1f}" height="18" rx="3" fill="{CHART_VIOLET}"/>')
        elements.append(f'<rect x="{left}" y="{y + 58}" width="{max(1, boundary_width):.1f}" height="18" rx="3" fill="{CHART_RED}"/>')
        elements.append(svg_text(left + multiple_width + 9, y + 22, f"multi-state {row.multiple_stable_states_rate:.2f}", font_size=11.5, font_weight=700, fill=CHART_INK))
        elements.append(svg_text(left + trap_width + 9, y + 48, f"low-high trap {row.low_high_trap_rate:.2f}", font_size=11.5, font_weight=700, fill=CHART_INK))
        elements.append(svg_text(left + boundary_width + 9, y + 72, f"lower boundary {row.lower_boundary_state_rate:.2f}", font_size=11.5, font_weight=700, fill=CHART_INK))
    elements.append(svg_text(left + chart_width / 2, height - 24, "share of parameter draws", font_size=12, fill=CHART_MUTED, text_anchor="middle"))
    elements.append(chart_footer("Audit is a mechanism check, not an empirical estimate. Parameter ranges are reported in results/material_feedback_report.md.", width, height))
    elements.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(elements) + "\n", encoding="utf-8")


def baseline_scenarios() -> dict[str, CapacityFeedbackParams]:
    trap = CapacityFeedbackParams(
        name="capacity trap",
        baseline_repair=0.235,
        repair_strength=2.90,
        decay_rate=0.66,
        substitute_damage=0.198,
        sensitivity=21.0,
        subjective_pull=0.51,
        capacity_protection=0.855,
    )
    resilient = replace(trap, name="self-correcting", substitute_damage=0.12, sensitivity=12.0)
    damaged = replace(trap, name="higher exposure", exposure=0.18)
    repaired = replace(trap, name="repair intervention", baseline_repair=0.285)
    return {
        "trap": trap,
        "resilient": resilient,
        "damaged": damaged,
        "repaired": repaired,
    }


def run_material_feedback_analysis(root: Path) -> dict[str, object]:
    scenarios = baseline_scenarios()
    tables_dir = root / "results" / "tables"
    figures_dir = root / "results" / "figures"

    equilibria = []
    for params in scenarios.values():
        equilibria.extend(asdict(point) for point in capacity_equilibria(params))

    paths = [
        simulate_capacity_path(scenarios["trap"], 0.15),
        simulate_capacity_path(scenarios["trap"], 0.30),
        simulate_capacity_path(scenarios["repaired"], 0.15),
        simulate_capacity_path(scenarios["resilient"], 0.15),
    ]
    path_rows = [asdict(point) for path_points in paths for point in path_points]
    audit_rows = feedback_parameter_audit()

    equilibrium_path = tables_dir / "material_feedback_equilibria.csv"
    path_table = tables_dir / "material_feedback_paths.csv"
    audit_table = tables_dir / "material_feedback_parameter_audit.csv"
    write_csv(equilibrium_path, equilibria)
    write_csv(path_table, path_rows)
    write_csv(audit_table, [asdict(row) for row in audit_rows])

    phase_svg = figures_dir / "material_feedback_phase.svg"
    paths_svg = figures_dir / "material_feedback_paths.svg"
    audit_svg = figures_dir / "material_feedback_audit.svg"
    write_phase_svg(phase_svg, [scenarios["resilient"], scenarios["trap"], scenarios["damaged"]])
    write_paths_svg(paths_svg, paths)
    write_audit_svg(audit_svg, audit_rows)

    return {
        "scenarios": scenarios,
        "equilibria": equilibria,
        "paths": path_rows,
        "audit": audit_rows,
        "audit_classes": AUDIT_CLASSES,
        "tables": [equilibrium_path, path_table, audit_table],
        "figures": [phase_svg, paths_svg, audit_svg],
    }
