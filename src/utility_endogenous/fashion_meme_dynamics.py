"""Fashion, meme, and influencer preference-closure models.

The module keeps the model deliberately small. It studies binary taste states
with social reinforcement, meme fields, and influencer exposure. The same
closure equation can be read as a logit social-interactions model, an Ising
mean-field equation, or a smoothed threshold contagion model.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
import csv
import html
import math
from pathlib import Path
import random


EPSILON = 1e-10


@dataclass(frozen=True)
class FixedPoint:
    field: float
    adoption: float
    stable: bool
    slope: float


@dataclass(frozen=True)
class ThresholdSummary:
    beta: float
    social_feedback: float
    material_field: float
    beta_j: float
    critical_field: float
    low_branch_at_zero: float
    high_branch_at_zero: float
    positive_shock_needed: float
    shock_size: float
    persistent_flip: bool
    material_loss_if_material_field_negative: bool


@dataclass(frozen=True)
class NetworkMultiplierRow:
    eta: float
    beta_eta_rho: float
    central_response: float
    peripheral_response: float
    central_to_peripheral_ratio: float
    contraction_bound: float


@dataclass(frozen=True)
class PhaseAuditSummary:
    draws: int
    shock_size: float
    subcritical_unique_rate: float
    hysteresis_possible_rate: float
    temporary_shock_flip_rate: float
    material_loss_flip_rate: float
    mean_positive_shock_needed_when_flippable: float
    median_positive_shock_needed_when_flippable: float


def atanh(value: float) -> float:
    value = max(-1.0 + EPSILON, min(1.0 - EPSILON, value))
    return 0.5 * math.log((1.0 + value) / (1.0 - value))


def fashion_map(adoption: float, beta: float, social_feedback: float, field: float) -> float:
    return math.tanh(beta * (social_feedback * adoption + field))


def fixed_point_residual(
    adoption: float, beta: float, social_feedback: float, field: float
) -> float:
    return fashion_map(adoption, beta, social_feedback, field) - adoption


def bisection_root(
    left: float,
    right: float,
    beta: float,
    social_feedback: float,
    field: float,
    iterations: int = 80,
) -> float:
    f_left = fixed_point_residual(left, beta, social_feedback, field)
    f_right = fixed_point_residual(right, beta, social_feedback, field)
    if abs(f_left) <= EPSILON:
        return left
    if abs(f_right) <= EPSILON:
        return right
    for _ in range(iterations):
        mid = (left + right) / 2.0
        f_mid = fixed_point_residual(mid, beta, social_feedback, field)
        if abs(f_mid) <= EPSILON:
            return mid
        if f_left * f_mid <= 0:
            right = mid
            f_right = f_mid
        else:
            left = mid
            f_left = f_mid
    return (left + right) / 2.0


def mean_field_fixed_points(
    beta: float,
    social_feedback: float,
    field: float,
    grid_size: int = 2400,
) -> list[FixedPoint]:
    """Return fixed points of m = tanh(beta * (J m + b))."""

    low = -1.0 + 1e-8
    high = 1.0 - 1e-8
    step = (high - low) / grid_size
    candidates: list[float] = []
    prev_x = low
    prev_y = fixed_point_residual(prev_x, beta, social_feedback, field)

    for index in range(1, grid_size + 1):
        x = low + index * step
        y = fixed_point_residual(x, beta, social_feedback, field)
        if abs(y) < 1e-7:
            candidates.append(x)
        if prev_y * y < 0:
            candidates.append(bisection_root(prev_x, x, beta, social_feedback, field))
        prev_x = x
        prev_y = y

    roots: list[float] = []
    for candidate in sorted(candidates):
        if not roots or abs(candidate - roots[-1]) > 1e-5:
            roots.append(candidate)

    points: list[FixedPoint] = []
    for root in roots:
        slope = beta * social_feedback * (1.0 - root * root)
        points.append(FixedPoint(field=field, adoption=root, stable=abs(slope) < 1.0, slope=slope))
    return points


def critical_field(beta: float, social_feedback: float) -> float:
    """Positive spinodal field for the mean-field fashion model.

    If beta * social_feedback <= 1, the closure map is single-valued and there
    is no hysteresis window.
    """

    interaction = beta * social_feedback
    if interaction <= 1.0:
        return 0.0
    spin = math.sqrt(1.0 - 1.0 / interaction)
    return social_feedback * spin - atanh(spin) / beta


def threshold_summary(
    beta: float = 2.0,
    social_feedback: float = 0.8,
    material_field: float = -0.08,
    shock_size: float = 0.35,
) -> ThresholdSummary:
    crit = critical_field(beta, social_feedback)
    roots = mean_field_fixed_points(beta, social_feedback, material_field)
    stable = [point.adoption for point in roots if point.stable]
    low_branch = min(stable) if stable else float("nan")
    high_branch = max(stable) if stable else float("nan")
    shock_needed = max(0.0, crit - material_field)
    persistent_flip = bool(crit > abs(material_field) and shock_needed <= shock_size)
    return ThresholdSummary(
        beta=beta,
        social_feedback=social_feedback,
        material_field=material_field,
        beta_j=beta * social_feedback,
        critical_field=crit,
        low_branch_at_zero=low_branch,
        high_branch_at_zero=high_branch,
        positive_shock_needed=shock_needed,
        shock_size=shock_size,
        persistent_flip=persistent_flip,
        material_loss_if_material_field_negative=bool(persistent_flip and material_field < 0.0),
    )


def hysteresis_path(
    beta: float,
    social_feedback: float,
    material_field: float,
    shock_size: float,
    steps: int = 80,
) -> list[tuple[float, float, float, str]]:
    up = [shock_size * index / steps for index in range(steps + 1)]
    down = [shock_size * (1.0 - index / steps) for index in range(1, steps + 1)]
    sequence = [*up, *down]
    previous = None
    path: list[tuple[float, float, float, str]] = []
    for index, shock in enumerate(sequence):
        field = material_field + shock
        stable = [point.adoption for point in mean_field_fixed_points(beta, social_feedback, field) if point.stable]
        if not stable:
            stable = [point.adoption for point in mean_field_fixed_points(beta, social_feedback, field)]
        if previous is None:
            chosen = min(stable)
        else:
            chosen = min(stable, key=lambda value: abs(value - previous))
        phase = "up" if index <= steps else "down"
        path.append((shock, field, chosen, phase))
        previous = chosen
    return path


def weighted_sample_without_replacement(
    rng: random.Random,
    weights: list[float],
    sample_size: int,
    excluded: int,
) -> list[int]:
    available = [index for index in range(len(weights)) if index != excluded]
    chosen: list[int] = []
    for _ in range(min(sample_size, len(available))):
        total = sum(weights[index] for index in available)
        draw = rng.random() * total
        cumulative = 0.0
        selected = available[-1]
        for index in available:
            cumulative += weights[index]
            if cumulative >= draw:
                selected = index
                break
        chosen.append(selected)
        available.remove(selected)
    return chosen


def generate_attention_network(
    node_count: int = 120,
    follows_per_agent: int = 8,
    seed: int = 20260623,
) -> list[list[float]]:
    rng = random.Random(seed)
    popularity = [rng.paretovariate(1.35) for _ in range(node_count)]
    network: list[list[float]] = []
    for row_index in range(node_count):
        followed = weighted_sample_without_replacement(rng, popularity, follows_per_agent, row_index)
        total = sum(popularity[index] for index in followed)
        row = [0.0] * node_count
        for column_index in followed:
            row[column_index] = popularity[column_index] / total
        network.append(row)
    return network


def mat_vec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(weight * vector[j] for j, weight in enumerate(row)) for row in matrix]


def stationary_attention_centrality(matrix: list[list[float]], iterations: int = 500) -> list[float]:
    node_count = len(matrix)
    vector = [1.0 / node_count] * node_count
    for _ in range(iterations):
        new_vector = [0.0] * node_count
        for i, row in enumerate(matrix):
            for j, weight in enumerate(row):
                new_vector[j] += vector[i] * weight
        total = sum(new_vector)
        if total <= EPSILON:
            return vector
        vector = [value / total for value in new_vector]
    return vector


def spectral_radius_power(matrix: list[list[float]], iterations: int = 250) -> float:
    node_count = len(matrix)
    vector = [1.0 / node_count] * node_count
    radius = 0.0
    for _ in range(iterations):
        new_vector = mat_vec(matrix, vector)
        radius = max(abs(value) for value in new_vector)
        if radius <= EPSILON:
            return 0.0
        vector = [value / radius for value in new_vector]
    numerator = sum(a * b for a, b in zip(mat_vec(matrix, vector), vector, strict=True))
    denominator = sum(value * value for value in vector)
    return abs(numerator / denominator)


def linear_response(
    matrix: list[list[float]],
    beta: float,
    eta: float,
    field_vector: list[float],
    iterations: int = 10000,
    tolerance: float = 1e-11,
) -> list[float]:
    """Solve x = beta * field + beta * eta * W x by fixed-point iteration."""

    response = [0.0] * len(matrix)
    source = [beta * value for value in field_vector]
    for _ in range(iterations):
        propagated = mat_vec(matrix, response)
        new_response = [
            source[i] + beta * eta * propagated[i] for i in range(len(response))
        ]
        gap = max(abs(a - b) for a, b in zip(new_response, response, strict=True))
        response = new_response
        if gap <= tolerance:
            break
    return response


def network_multiplier_rows(
    beta: float = 1.15,
    eta_grid: tuple[float, ...] = (0.0, 0.15, 0.30, 0.45, 0.60, 0.72, 0.80, 0.84),
    node_count: int = 120,
    follows_per_agent: int = 8,
    seed: int = 20260623,
) -> list[NetworkMultiplierRow]:
    matrix = generate_attention_network(node_count, follows_per_agent, seed)
    centrality = stationary_attention_centrality(matrix)
    positive_nodes = [index for index, value in enumerate(centrality) if value > 0.0]
    central = max(positive_nodes, key=lambda index: centrality[index])
    peripheral = min(positive_nodes, key=lambda index: centrality[index])
    rho = spectral_radius_power(matrix)
    rows: list[NetworkMultiplierRow] = []
    for eta in eta_grid:
        central_field = [0.0] * node_count
        peripheral_field = [0.0] * node_count
        central_field[central] = 1.0
        peripheral_field[peripheral] = 1.0
        central_response = sum(linear_response(matrix, beta, eta, central_field))
        peripheral_response = sum(linear_response(matrix, beta, eta, peripheral_field))
        contraction_gap = max(0.0, 1.0 - beta * eta * rho)
        bound = float("inf") if contraction_gap <= 0.0 else beta / contraction_gap
        rows.append(
            NetworkMultiplierRow(
                eta=eta,
                beta_eta_rho=beta * eta * rho,
                central_response=central_response,
                peripheral_response=peripheral_response,
                central_to_peripheral_ratio=central_response / max(peripheral_response, EPSILON),
                contraction_bound=bound,
            )
        )
    return rows


def phase_audit(
    draws: int = 6000,
    shock_size: float = 0.35,
    seed: int = 20260623,
) -> PhaseAuditSummary:
    rng = random.Random(seed)
    subcritical = 0
    hysteresis = 0
    flippable = 0
    material_loss = 0
    needed_values: list[float] = []

    for _ in range(draws):
        beta = rng.uniform(0.5, 3.0)
        social_feedback = rng.uniform(0.1, 1.3)
        material_field = rng.uniform(-0.35, 0.35)
        if beta * social_feedback <= 1.0:
            subcritical += 1
            continue
        crit = critical_field(beta, social_feedback)
        if abs(material_field) < crit:
            hysteresis += 1
            shock_needed = max(0.0, crit - material_field)
            if shock_needed <= shock_size:
                flippable += 1
                needed_values.append(shock_needed)
                if material_field < 0.0:
                    material_loss += 1

    needed_values.sort()
    if needed_values:
        mean_needed = sum(needed_values) / len(needed_values)
        median_needed = needed_values[len(needed_values) // 2]
    else:
        mean_needed = float("nan")
        median_needed = float("nan")

    return PhaseAuditSummary(
        draws=draws,
        shock_size=shock_size,
        subcritical_unique_rate=subcritical / draws,
        hysteresis_possible_rate=hysteresis / draws,
        temporary_shock_flip_rate=flippable / draws,
        material_loss_flip_rate=material_loss / draws,
        mean_positive_shock_needed_when_flippable=mean_needed,
        median_positive_shock_needed_when_flippable=median_needed,
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


def svg_text(x: float, y: float, text: str, **attrs: object) -> str:
    attributes = {"x": x, "y": y, "font-family": "Arial, sans-serif"}
    attributes.update(attrs)
    attr_text = " ".join(
        f'{key.replace("_", "-")}="{html.escape(str(value))}"'
        for key, value in attributes.items()
    )
    return f"<text {attr_text}>{html.escape(text)}</text>"


def write_mean_field_hysteresis_svg(
    path: Path,
    beta: float = 2.0,
    social_feedback: float = 0.8,
    material_field: float = -0.08,
    shock_size: float = 0.35,
) -> None:
    width = 920
    height = 560
    margin_left = 82
    margin_right = 38
    margin_top = 72
    margin_bottom = 72
    x_min = -0.32
    x_max = 0.36
    y_min = -1.0
    y_max = 1.0

    def sx(field: float) -> float:
        return margin_left + (field - x_min) / (x_max - x_min) * (width - margin_left - margin_right)

    def sy(adoption: float) -> float:
        return height - margin_bottom - (adoption - y_min) / (y_max - y_min) * (
            height - margin_top - margin_bottom
        )

    fields = [x_min + (x_max - x_min) * index / 260 for index in range(261)]
    stable_points: list[tuple[float, float]] = []
    unstable_points: list[tuple[float, float]] = []
    for field in fields:
        for point in mean_field_fixed_points(beta, social_feedback, field):
            target = stable_points if point.stable else unstable_points
            target.append((field, point.adoption))

    path_rows = hysteresis_path(beta, social_feedback, material_field, shock_size)
    up_path = [(field, adoption) for _, field, adoption, phase in path_rows if phase == "up"]
    down_path = [(field, adoption) for _, field, adoption, phase in path_rows if phase == "down"]

    def polyline(points: list[tuple[float, float]], color: str, width_value: float, dash: str = "") -> str:
        coords = " ".join(f"{sx(x):.1f},{sy(y):.1f}" for x, y in points)
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        return (
            f'<polyline points="{coords}" fill="none" stroke="{color}" '
            f'stroke-width="{width_value}" stroke-linecap="round"{dash_attr}/>'
        )

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        svg_text(34, 34, "Mean-Field Fashion Closure Has Hysteresis", font_size=22, font_weight=700, fill="#18212f"),
        svg_text(
            34,
            58,
            f"m = tanh(beta(Jm+b)); beta={beta:.1f}, J={social_feedback:.1f}, material field h={material_field:.2f}",
            font_size=13,
            fill="#526173",
        ),
    ]
    for tick in [-0.3, -0.15, 0.0, 0.15, 0.3]:
        x = sx(tick)
        elements.append(f'<line x1="{x:.1f}" y1="{margin_top}" x2="{x:.1f}" y2="{height-margin_bottom}" stroke="#e3e8ef"/>')
        elements.append(svg_text(x, height - 38, f"{tick:.2f}", font_size=12, fill="#526173", text_anchor="middle"))
    for tick in [-1.0, -0.5, 0.0, 0.5, 1.0]:
        y = sy(tick)
        elements.append(f'<line x1="{margin_left}" y1="{y:.1f}" x2="{width-margin_right}" y2="{y:.1f}" stroke="#e3e8ef"/>')
        elements.append(svg_text(62, y + 4, f"{tick:.1f}", font_size=12, fill="#526173", text_anchor="end"))
    elements.append(polyline(stable_points, "#236f76", 3.0))
    elements.append(polyline(unstable_points, "#c66b2e", 2.0, "6 5"))
    elements.append(polyline(up_path, "#1f4e9d", 3.0))
    elements.append(polyline(down_path, "#8b3fa8", 3.0, "4 4"))
    elements.append(
        f'<circle cx="{sx(material_field):.1f}" cy="{sy(up_path[0][1]):.1f}" r="5" fill="#1f4e9d"/>'
    )
    elements.append(
        f'<circle cx="{sx(material_field + shock_size):.1f}" cy="{sy(up_path[-1][1]):.1f}" r="5" fill="#1f4e9d"/>'
    )
    elements.append(
        f'<circle cx="{sx(material_field):.1f}" cy="{sy(down_path[-1][1]):.1f}" r="5" fill="#8b3fa8"/>'
    )
    elements.append(svg_text(width / 2, height - 12, "total fashion field b = h + z", font_size=13, fill="#26313c", text_anchor="middle"))
    elements.append(svg_text(18, height / 2, "adoption / taste m", font_size=13, fill="#26313c", transform=f"rotate(-90 18 {height/2})", text_anchor="middle"))
    elements.append(svg_text(625, 104, "stable closure branches", font_size=12, fill="#236f76", font_weight=700))
    elements.append(svg_text(625, 125, "unstable separator", font_size=12, fill="#c66b2e", font_weight=700))
    elements.append(svg_text(625, 146, "shock up", font_size=12, fill="#1f4e9d", font_weight=700))
    elements.append(svg_text(625, 167, "shock removed", font_size=12, fill="#8b3fa8", font_weight=700))
    elements.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(elements) + "\n", encoding="utf-8")


def write_network_multiplier_svg(path: Path, rows: list[NetworkMultiplierRow]) -> None:
    width = 920
    height = 540
    margin_left = 72
    margin_right = 38
    margin_top = 78
    margin_bottom = 68
    x_min = 0.0
    x_max = max(row.eta for row in rows) + 0.03
    y_max = max(row.central_response for row in rows) * 1.08

    def sx(eta: float) -> float:
        return margin_left + (eta - x_min) / (x_max - x_min) * (width - margin_left - margin_right)

    def sy(response: float) -> float:
        return height - margin_bottom - response / y_max * (height - margin_top - margin_bottom)

    def polyline(values: list[tuple[float, float]], color: str, width_value: float) -> str:
        coords = " ".join(f"{sx(x):.1f},{sy(y):.1f}" for x, y in values)
        return f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="{width_value}" stroke-linecap="round"/>'

    central = [(row.eta, row.central_response) for row in rows]
    peripheral = [(row.eta, row.peripheral_response) for row in rows]
    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        svg_text(34, 34, "Influence Multiplier Near The Fashion Critical Point", font_size=22, font_weight=700, fill="#18212f"),
        svg_text(34, 58, "Linear response to one targeted influencer field on a heterogeneous attention network", font_size=13, fill="#526173"),
    ]
    for tick in [0.0, 0.2, 0.4, 0.6, 0.8]:
        x = sx(tick)
        elements.append(f'<line x1="{x:.1f}" y1="{margin_top}" x2="{x:.1f}" y2="{height-margin_bottom}" stroke="#e3e8ef"/>')
        elements.append(svg_text(x, height - 38, f"{tick:.1f}", font_size=12, fill="#526173", text_anchor="middle"))
    for fraction in [0.0, 0.25, 0.5, 0.75, 1.0]:
        y_value = y_max * fraction
        y = sy(y_value)
        elements.append(f'<line x1="{margin_left}" y1="{y:.1f}" x2="{width-margin_right}" y2="{y:.1f}" stroke="#e3e8ef"/>')
        elements.append(svg_text(58, y + 4, f"{y_value:.0f}", font_size=12, fill="#526173", text_anchor="end"))
    elements.append(polyline(central, "#1f4e9d", 3.2))
    elements.append(polyline(peripheral, "#c66b2e", 3.2))
    for row in rows:
        elements.append(f'<circle cx="{sx(row.eta):.1f}" cy="{sy(row.central_response):.1f}" r="4" fill="#1f4e9d"/>')
        elements.append(f'<circle cx="{sx(row.eta):.1f}" cy="{sy(row.peripheral_response):.1f}" r="4" fill="#c66b2e"/>')
    elements.append(svg_text(650, 116, "central target", font_size=13, fill="#1f4e9d", font_weight=700))
    elements.append(svg_text(650, 140, "peripheral target", font_size=13, fill="#c66b2e", font_weight=700))
    elements.append(svg_text(width / 2, height - 12, "social reinforcement eta", font_size=13, fill="#26313c", text_anchor="middle"))
    elements.append(svg_text(18, height / 2, "aggregate response", font_size=13, fill="#26313c", transform=f"rotate(-90 18 {height/2})", text_anchor="middle"))
    elements.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(elements) + "\n", encoding="utf-8")


def write_phase_audit_svg(path: Path, summary: PhaseAuditSummary) -> None:
    rows = [
        ("Subcritical unique closure", summary.subcritical_unique_rate, "#287c6f"),
        ("Hysteresis possible", summary.hysteresis_possible_rate, "#c9822b"),
        ("Temporary shock flips state", summary.temporary_shock_flip_rate, "#1f4e9d"),
        ("Flip is material loss", summary.material_loss_flip_rate, "#b84545"),
    ]
    width = 920
    margin_left = 260
    margin_right = 70
    margin_top = 82
    row_height = 62
    height = margin_top + row_height * len(rows) + 70
    chart_width = width - margin_left - margin_right
    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        svg_text(34, 34, "Random Parameter Audit", font_size=22, font_weight=700, fill="#18212f"),
        svg_text(
            34,
            58,
            f"{summary.draws:,} mean-field economies; temporary positive meme shock z <= {summary.shock_size:.2f}",
            font_size=13,
            fill="#526173",
        ),
    ]
    for tick in [0.0, 0.25, 0.5, 0.75, 1.0]:
        x = margin_left + chart_width * tick
        elements.append(f'<line x1="{x:.1f}" y1="{margin_top-16}" x2="{x:.1f}" y2="{height-58}" stroke="#e3e8ef"/>')
        elements.append(svg_text(x, height - 30, f"{tick:.2f}".rstrip("0").rstrip("."), font_size=12, fill="#526173", text_anchor="middle"))
    for index, (label, value, color) in enumerate(rows):
        y = margin_top + index * row_height
        elements.append(svg_text(34, y + 24, label, font_size=13, fill="#18212f", font_weight=700))
        elements.append(f'<rect x="{margin_left}" y="{y+7}" width="{chart_width*value:.1f}" height="30" rx="3" fill="{color}"/>')
        elements.append(svg_text(margin_left + chart_width * value + 10, y + 27, f"{value:.3f}", font_size=12, fill="#18212f", font_weight=700))
    elements.append(svg_text(width / 2, height - 8, "rate", font_size=13, fill="#26313c", text_anchor="middle"))
    elements.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(elements) + "\n", encoding="utf-8")


def run_fashion_meme_analysis(root: Path) -> dict[str, object]:
    results = root / "results"
    tables = results / "tables"
    figures = results / "figures"

    threshold = threshold_summary()
    network_rows = network_multiplier_rows()
    audit = phase_audit()

    path_rows = [
        {
            "shock": shock,
            "total_field": field,
            "adoption": adoption,
            "phase": phase,
        }
        for shock, field, adoption, phase in hysteresis_path(
            threshold.beta,
            threshold.social_feedback,
            threshold.material_field,
            threshold.shock_size,
        )
    ]
    branch_rows = []
    for index in range(181):
        field = -0.32 + (0.36 + 0.32) * index / 180
        for point in mean_field_fixed_points(threshold.beta, threshold.social_feedback, field):
            branch_rows.append(asdict(point))

    write_csv(tables / "fashion_threshold_summary.csv", [asdict(threshold)])
    write_csv(tables / "fashion_hysteresis_path.csv", path_rows)
    write_csv(tables / "fashion_mean_field_branches.csv", branch_rows)
    write_csv(tables / "fashion_network_multipliers.csv", [asdict(row) for row in network_rows])
    write_csv(tables / "fashion_phase_audit_summary.csv", [asdict(audit)])

    write_mean_field_hysteresis_svg(figures / "fashion_mean_field_hysteresis.svg")
    write_network_multiplier_svg(figures / "fashion_network_multiplier.svg", network_rows)
    write_phase_audit_svg(figures / "fashion_phase_audit.svg", audit)

    return {
        "threshold": threshold,
        "network_rows": network_rows,
        "audit": audit,
        "tables": [
            tables / "fashion_threshold_summary.csv",
            tables / "fashion_hysteresis_path.csv",
            tables / "fashion_mean_field_branches.csv",
            tables / "fashion_network_multipliers.csv",
            tables / "fashion_phase_audit_summary.csv",
        ],
        "figures": [
            figures / "fashion_mean_field_hysteresis.svg",
            figures / "fashion_network_multiplier.svg",
            figures / "fashion_phase_audit.svg",
        ],
    }

