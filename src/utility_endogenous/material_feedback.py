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
    CHART_GREEN,
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


@dataclass(frozen=True)
class RegimeGridPoint:
    repair_baseline: float
    substitute_damage: float
    regime: str
    stable_count: int
    low_trap_present: bool
    high_state_present: bool
    lower_boundary_present: bool


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


def regime_label(params: CapacityFeedbackParams) -> tuple[str, dict[str, bool | int]]:
    """Classify the baseline scalar dynamic for main-text regime mapping."""

    equilibria = capacity_equilibria(params)
    stable = [point for point in equilibria if point.stable]
    low_trap = any(point.stable and point.capacity < 0.25 for point in equilibria)
    high_state = any(point.stable and point.capacity > 0.60 for point in equilibria)
    lower_boundary = any(point.stable and point.state_scope == "lower boundary" for point in equilibria)
    two_basin_trap = bool(classify_equilibria(params)["low_high_trap"])

    if lower_boundary or not high_state:
        label = "collapse-prone"
    elif two_basin_trap or low_trap:
        label = "threshold trap"
    elif high_state:
        label = "capacity-building"
    else:
        label = "transition"
    return (
        label,
        {
            "stable_count": len(stable),
            "low_trap_present": low_trap,
            "high_state_present": high_state,
            "lower_boundary_present": lower_boundary,
        },
    )


def regime_grid(
    params: CapacityFeedbackParams,
    repair_min: float = 0.14,
    repair_max: float = 0.38,
    damage_min: float = 0.05,
    damage_max: float = 0.42,
    repair_steps: int = 49,
    damage_steps: int = 61,
) -> list[RegimeGridPoint]:
    """Grid over repair and substitute damage for the main-text regime map."""

    rows: list[RegimeGridPoint] = []
    for repair_index in range(repair_steps):
        repair = repair_min + (repair_max - repair_min) * repair_index / (repair_steps - 1)
        for damage_index in range(damage_steps):
            damage = damage_min + (damage_max - damage_min) * damage_index / (damage_steps - 1)
            scenario = replace(params, baseline_repair=repair, substitute_damage=damage)
            label, flags = regime_label(scenario)
            rows.append(
                RegimeGridPoint(
                    repair_baseline=repair,
                    substitute_damage=damage,
                    regime=label,
                    stable_count=int(flags["stable_count"]),
                    low_trap_present=bool(flags["low_trap_present"]),
                    high_state_present=bool(flags["high_state_present"]),
                    lower_boundary_present=bool(flags["lower_boundary_present"]),
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


def write_loop_svg(path: Path, params: CapacityFeedbackParams) -> None:
    """Main-text figure: the fast choice rule and the slow capacity law."""

    width = 940
    height = 670
    left = 78
    right = 44
    top = 118
    bottom = 132
    gap = 68
    panel_width = (width - left - right - gap) / 2.0
    panel_height = height - top - bottom
    drift_values = [capacity_drift(index / 500, params) for index in range(501)]
    drift_min = min(-0.18, min(drift_values) - 0.025)
    drift_max = max(0.18, max(drift_values) + 0.025)
    right_left = left + panel_width + gap

    def x_scale(panel_left: float, capacity: float) -> float:
        return panel_left + panel_width * capacity

    def y_share(value: float) -> float:
        return top + panel_height * (1.0 - value)

    def y_drift(value: float) -> float:
        return top + panel_height * (drift_max - value) / (drift_max - drift_min)

    equilibria = capacity_equilibria(params)
    low_state = next((point for point in equilibria if point.stable and point.capacity < 0.25), None)
    threshold = next((point for point in equilibria if not point.stable and 0.15 < point.capacity < 0.70), None)
    high_state = next((point for point in equilibria if point.stable and point.capacity > 0.60), None)
    markers = [
        ("low trap", low_state, CHART_RED),
        ("threshold", threshold, CHART_VIOLET),
        ("high state", high_state, CHART_TEAL),
    ]

    elements = [
        *svg_open(width, height),
        *chart_header(
            "Why A Rational Choice Can Become A Trap",
            "Fast payoff formation controls substitute use; substitute use controls the slow capacity stock",
            width,
        ),
    ]
    for panel_left, panel_title in [
        (left, "A. What the induced payoff makes attractive"),
        (right_left, "B. What that choice does to capacity"),
    ]:
        elements.append(svg_text(panel_left, top - 20, panel_title, font_size=14, font_weight=800, fill=CHART_INK))
        elements.append(
            f'<rect x="{panel_left}" y="{top}" width="{panel_width:.1f}" height="{panel_height}" fill="#ffffff" stroke="{CHART_GRID}"/>'
        )
        for tick in [0.0, 0.25, 0.5, 0.75, 1.0]:
            x = x_scale(panel_left, tick)
            elements.append(
                f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{top + panel_height}" stroke="{CHART_GRID}" stroke-width="1"/>'
            )
            elements.append(svg_text(x, top + panel_height + 25, f"{tick:.2f}".rstrip("0").rstrip("."), font_size=11, fill=CHART_MUTED, text_anchor="middle"))
        elements.append(svg_text(panel_left + panel_width / 2, top + panel_height + 51, "material capacity K", font_size=12, fill=CHART_MUTED, text_anchor="middle"))

    for tick in [0.0, 0.25, 0.5, 0.75, 1.0]:
        y = y_share(tick)
        elements.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + panel_width}" y2="{y:.1f}" stroke="{CHART_GRID}" stroke-width="1"/>')
        elements.append(svg_text(left - 12, y + 4, f"{tick:.2f}".rstrip("0").rstrip("."), font_size=11, fill=CHART_MUTED, text_anchor="end"))
    elements.append(svg_text(27, top + panel_height / 2, "substitute share", font_size=12, fill=CHART_MUTED, transform=f"rotate(-90 27 {top + panel_height / 2})", text_anchor="middle"))

    for tick in [-0.15, 0.0, 0.15]:
        y = y_drift(tick)
        elements.append(f'<line x1="{right_left}" y1="{y:.1f}" x2="{right_left + panel_width}" y2="{y:.1f}" stroke="{CHART_GRID}" stroke-width="1"/>')
        elements.append(svg_text(right_left - 12, y + 4, f"{tick:.2f}".rstrip("0"), font_size=11, fill=CHART_MUTED, text_anchor="end"))
    zero_y = y_drift(0.0)
    elements.append(f'<line x1="{right_left}" y1="{zero_y:.1f}" x2="{right_left + panel_width}" y2="{zero_y:.1f}" stroke="{CHART_INK}" stroke-width="1.3"/>')
    elements.append(svg_text(right_left - 50, top + panel_height / 2, "capacity drift", font_size=12, fill=CHART_MUTED, transform=f"rotate(-90 {right_left - 50} {top + panel_height / 2})", text_anchor="middle"))

    choice_line = [
        (x_scale(left, index / 500), y_share(substitute_share(index / 500, params)))
        for index in range(501)
    ]
    drift_line = [
        (x_scale(right_left, index / 500), y_drift(capacity_drift(index / 500, params)))
        for index in range(501)
    ]
    elements.append(_polyline(choice_line, CHART_RED, 3.4))
    elements.append(_polyline(drift_line, CHART_TEAL, 3.4))

    for label, point, color in markers:
        if point is None:
            continue
        for panel_left in [left, right_left]:
            x = x_scale(panel_left, point.capacity)
            elements.append(
                f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{top + panel_height}" stroke="{color}" stroke-width="1.4" stroke-dasharray="5 6" opacity="0.75"/>'
            )
        marker_fill = color if point.stable else CHART_PANEL
        elements.append(
            f'<circle cx="{x_scale(right_left, point.capacity):.1f}" cy="{zero_y:.1f}" r="6.5" fill="{marker_fill}" stroke="{color}" stroke-width="2"/>'
        )

    elements.append(svg_text(left + 16, top + 28, "low capacity: substitute is attractive", font_size=12, font_weight=800, fill=CHART_RED))
    elements.append(svg_text(left + panel_width - 16, top + panel_height - 18, "high capacity: outside option works", font_size=12, font_weight=800, fill=CHART_TEAL, text_anchor="end"))
    elements.append(svg_text(right_left + 18, zero_y + 34, "below zero: capacity falls", font_size=12, font_weight=800, fill=CHART_RED))
    elements.append(svg_text(right_left + panel_width - 18, zero_y - 22, "above zero: capacity rises", font_size=12, font_weight=800, fill=CHART_TEAL, text_anchor="end"))
    legend_y = top + panel_height + 86
    for index, (label, point, color) in enumerate(markers):
        x = left + 150 * index
        fill = color if point is not None and point.stable else CHART_PANEL
        elements.append(f'<circle cx="{x}" cy="{legend_y}" r="6" fill="{fill}" stroke="{color}" stroke-width="2"/>')
        elements.append(svg_text(x + 14, legend_y + 4, label, font_size=12, font_weight=800, fill=CHART_INK))
    elements.append(chart_footer("Same baseline trap calibration. Filled dots are stable states; the open dot is the threshold.", width, height))
    elements.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(elements) + "\n", encoding="utf-8")


def write_regime_map_svg(path: Path, rows: list[RegimeGridPoint], baseline: CapacityFeedbackParams) -> None:
    """Main-text figure: which parameter movements change the qualitative regime."""

    width = 940
    height = 700
    left = 94
    right = 54
    top = 112
    bottom = 152
    chart_width = width - left - right
    chart_height = height - top - bottom
    damage_values = [row.substitute_damage for row in rows]
    repair_values = [row.repair_baseline for row in rows]
    damage_min = min(damage_values)
    damage_max = max(damage_values)
    repair_min = min(repair_values)
    repair_max = max(repair_values)
    damage_steps = len(set(damage_values))
    repair_steps = len(set(repair_values))
    cell_width = chart_width / damage_steps
    cell_height = chart_height / repair_steps
    colors = {
        "capacity-building": "#dcebd8",
        "threshold trap": "#f4d7a1",
        "collapse-prone": "#f3b8ae",
        "transition": "#e6e1d8",
    }

    def x_scale(damage: float) -> float:
        return left + chart_width * (damage - damage_min) / (damage_max - damage_min)

    def y_scale(repair: float) -> float:
        return top + chart_height * (repair_max - repair) / (repair_max - repair_min)

    def arrow(x1: float, y1: float, x2: float, y2: float, color: str) -> str:
        return (
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="3.2" stroke-linecap="round" marker-end="url(#arrowhead)"/>'
        )

    elements = [
        *svg_open(width, height),
        '<defs><marker id="arrowhead" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">'
        f'<path d="M 0 0 L 10 4 L 0 8 z" fill="{CHART_INK}"/></marker></defs>',
        *chart_header(
            "What Actually Moves The System",
            "Repair capacity and damage per substitute use change the regime; a report-only signal stays put",
            width,
        ),
    ]
    for row in rows:
        damage_index = round((row.substitute_damage - damage_min) / (damage_max - damage_min) * (damage_steps - 1))
        repair_index = round((row.repair_baseline - repair_min) / (repair_max - repair_min) * (repair_steps - 1))
        x = left + damage_index * cell_width
        y = top + (repair_steps - 1 - repair_index) * cell_height
        elements.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{cell_width + 0.7:.1f}" height="{cell_height + 0.7:.1f}" fill="{colors[row.regime]}" stroke="none"/>'
        )
    elements.append(f'<rect x="{left}" y="{top}" width="{chart_width}" height="{chart_height}" fill="none" stroke="{CHART_GRID}" stroke-width="1.2"/>')
    for tick in [0.05, 0.15, 0.25, 0.35, 0.42]:
        x = x_scale(tick)
        elements.append(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{top + chart_height}" stroke="#ffffff" stroke-width="1" opacity="0.8"/>')
        elements.append(svg_text(x, top + chart_height + 26, f"{tick:.2f}", font_size=11, fill=CHART_MUTED, text_anchor="middle"))
    for tick in [0.14, 0.20, 0.26, 0.32, 0.38]:
        y = y_scale(tick)
        elements.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + chart_width}" y2="{y:.1f}" stroke="#ffffff" stroke-width="1" opacity="0.8"/>')
        elements.append(svg_text(left - 12, y + 4, f"{tick:.2f}", font_size=11, fill=CHART_MUTED, text_anchor="end"))
    elements.append(svg_text(left + chart_width / 2, top + chart_height + 54, "damage per substitute use", font_size=12, fill=CHART_MUTED, text_anchor="middle"))
    elements.append(svg_text(33, top + chart_height / 2, "baseline repair", font_size=12, fill=CHART_MUTED, transform=f"rotate(-90 33 {top + chart_height / 2})", text_anchor="middle"))

    base_x = x_scale(baseline.substitute_damage)
    base_y = y_scale(baseline.baseline_repair)
    elements.append(f'<circle cx="{base_x:.1f}" cy="{base_y:.1f}" r="8" fill="{CHART_INK}" stroke="#ffffff" stroke-width="2"/>')
    elements.append(svg_text(base_x + 14, base_y - 12, "baseline trap", font_size=12, font_weight=800, fill=CHART_INK))
    elements.append(arrow(base_x, base_y - 12, base_x, y_scale(0.305), CHART_INK))
    elements.append(svg_text(base_x + 12, y_scale(0.305) - 10, "raise repair", font_size=12, font_weight=800, fill=CHART_GREEN))
    elements.append(arrow(base_x - 8, base_y + 6, x_scale(0.105), base_y + 6, CHART_INK))
    elements.append(svg_text(x_scale(0.105), base_y + 25, "reduce damage", font_size=12, font_weight=800, fill=CHART_TEAL, text_anchor="middle"))
    elements.append(f'<circle cx="{base_x + 49:.1f}" cy="{base_y + 38:.1f}" r="19" fill="none" stroke="{CHART_VIOLET}" stroke-width="2.4" stroke-dasharray="4 5"/>')
    elements.append(svg_text(base_x + 78, base_y + 43, "report only: same coordinates", font_size=12, font_weight=800, fill=CHART_VIOLET))

    legend_y = top + chart_height + 84
    legend_items = [
        ("capacity-building", colors["capacity-building"], CHART_GREEN),
        ("threshold trap", colors["threshold trap"], CHART_AMBER),
        ("collapse-prone", colors["collapse-prone"], CHART_RED),
    ]
    for index, (label, fill, stroke) in enumerate(legend_items):
        x = left + 245 * index
        elements.append(f'<rect x="{x}" y="{legend_y - 13}" width="22" height="16" rx="2" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
        elements.append(svg_text(x + 31, legend_y, label, font_size=12, font_weight=800, fill=CHART_INK))
    elements.append(chart_footer("Grid holds the other baseline parameters fixed. Colors classify computed stable states of the scalar dynamic.", width, height))
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
    regime_rows = regime_grid(scenarios["trap"])

    equilibrium_path = tables_dir / "material_feedback_equilibria.csv"
    path_table = tables_dir / "material_feedback_paths.csv"
    audit_table = tables_dir / "material_feedback_parameter_audit.csv"
    regime_table = tables_dir / "material_feedback_regime_grid.csv"
    write_csv(equilibrium_path, equilibria)
    write_csv(path_table, path_rows)
    write_csv(audit_table, [asdict(row) for row in audit_rows])
    write_csv(regime_table, [asdict(row) for row in regime_rows])

    phase_svg = figures_dir / "material_feedback_phase.svg"
    paths_svg = figures_dir / "material_feedback_paths.svg"
    audit_svg = figures_dir / "material_feedback_audit.svg"
    loop_svg = figures_dir / "material_feedback_loop.svg"
    regime_svg = figures_dir / "material_feedback_regime_map.svg"
    write_phase_svg(phase_svg, [scenarios["resilient"], scenarios["trap"], scenarios["damaged"]])
    write_paths_svg(paths_svg, paths)
    write_audit_svg(audit_svg, audit_rows)
    write_loop_svg(loop_svg, scenarios["trap"])
    write_regime_map_svg(regime_svg, regime_rows, scenarios["trap"])

    return {
        "scenarios": scenarios,
        "equilibria": equilibria,
        "paths": path_rows,
        "audit": audit_rows,
        "regime_grid": regime_rows,
        "audit_classes": AUDIT_CLASSES,
        "tables": [equilibrium_path, path_table, audit_table, regime_table],
        "figures": [loop_svg, regime_svg, phase_svg, paths_svg, audit_svg],
    }
