"""Algorithmic taste drift with Darwinian selection.

The model is deliberately small: a one-dimensional taste parameter moves under
algorithmic exposure, while population mass is selected by a separate fitness
criterion. This lets us test whether subjective utility and fitness can diverge.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


EPSILON = 1e-12


@dataclass(frozen=True)
class TasteDriftParams:
    name: str
    periods: int = 80
    grid_size: int = 81
    initial_center: float = 0.35
    initial_spread: float = 0.10
    persuasion_rate: float = 0.08
    ai_power: float = 0.10
    personalization: float = 0.50
    platform_bias: float = 0.05
    offline_anchor: float = 0.08
    selection_strength: float = 0.70
    mutation: float = 0.002


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def grid(size: int) -> list[float]:
    if size < 2:
        raise ValueError("grid_size must be at least 2")
    return [i / (size - 1) for i in range(size)]


def initial_distribution(points: list[float], center: float, spread: float) -> list[float]:
    weights = [math.exp(-((x - center) ** 2) / (2 * spread**2)) for x in points]
    total = sum(weights)
    return [w / total for w in weights]


def algorithmic_field(theta: float, params: TasteDriftParams) -> float:
    """Exposure pressure toward online/artificial taste."""

    return clamp(params.platform_bias + params.ai_power * (0.25 + params.personalization * theta))


def biological_fitness(theta: float, params: TasteDriftParams) -> float:
    """Fitness is intentionally distinct from subjective utility.

    High online orientation is penalized as a proxy for lower reproduction,
    offline social capital, or embodied resilience.
    """

    offline_social_capital = 1.0 - theta
    online_penalty = theta * theta
    return math.exp(params.selection_strength * (1.20 * offline_social_capital - 0.35 * online_penalty))


def cobb_douglas_satisfaction(theta: float) -> float:
    """Maximized Cobb-Douglas index theta^theta (1-theta)^(1-theta)."""

    left = 1.0 if theta <= EPSILON else theta**theta
    right = 1.0 if 1.0 - theta <= EPSILON else (1.0 - theta) ** (1.0 - theta)
    return left * right


def move_mass(target: list[float], points: list[float], theta_next: float, mass: float) -> None:
    scaled = clamp(theta_next) * (len(points) - 1)
    lower = int(math.floor(scaled))
    upper = int(math.ceil(scaled))
    if lower == upper:
        target[lower] += mass
        return
    upper_weight = scaled - lower
    target[lower] += mass * (1.0 - upper_weight)
    target[upper] += mass * upper_weight


def diffuse(distribution: list[float], mutation: float) -> list[float]:
    if mutation <= 0:
        return distribution

    n = len(distribution)
    out = [0.0] * n
    for i, mass in enumerate(distribution):
        stay = mass * (1.0 - mutation)
        out[i] += stay
        leak = mass * mutation
        if i == 0:
            out[i] += leak / 2.0
            out[i + 1] += leak / 2.0
        elif i == n - 1:
            out[i] += leak / 2.0
            out[i - 1] += leak / 2.0
        else:
            out[i - 1] += leak / 2.0
            out[i + 1] += leak / 2.0
    total = sum(out)
    return [x / total for x in out]


def summarize(period: int, points: list[float], distribution: list[float], params: TasteDriftParams) -> dict[str, float | int | str]:
    mean_theta = sum(theta * mass for theta, mass in zip(points, distribution, strict=True))
    mean_fitness = sum(
        biological_fitness(theta, params) * mass for theta, mass in zip(points, distribution, strict=True)
    )
    subjective_index = sum(
        cobb_douglas_satisfaction(theta) * mass for theta, mass in zip(points, distribution, strict=True)
    )
    entropy = -sum(mass * math.log(mass + EPSILON) for mass in distribution) / math.log(len(points))
    return {
        "scenario": params.name,
        "period": period,
        "mean_theta": mean_theta,
        "attention_share": mean_theta,
        "offline_social_capital": 1.0 - mean_theta,
        "mean_fitness": mean_fitness,
        "subjective_satisfaction": subjective_index,
        "entropy": entropy,
    }


def simulate_taste_drift(params: TasteDriftParams) -> list[dict[str, float | int | str]]:
    points = grid(params.grid_size)
    distribution = initial_distribution(points, params.initial_center, params.initial_spread)
    records = [summarize(0, points, distribution, params)]

    for period in range(1, params.periods + 1):
        fitnesses = [biological_fitness(theta, params) for theta in points]
        avg_fitness = sum(mass * fit for mass, fit in zip(distribution, fitnesses, strict=True))
        selected = [
            mass * fit / avg_fitness for mass, fit in zip(distribution, fitnesses, strict=True)
        ]

        shifted = [0.0] * len(points)
        for theta, mass in zip(points, selected, strict=True):
            exposure = algorithmic_field(theta, params)
            drift = params.persuasion_rate * (
                exposure * (1.0 - theta) - params.offline_anchor * theta
            )
            theta_next = clamp(theta + drift)
            move_mass(shifted, points, theta_next, mass)

        distribution = diffuse(shifted, params.mutation)
        records.append(summarize(period, points, distribution, params))

    return records


def taste_scenarios() -> list[TasteDriftParams]:
    return [
        TasteDriftParams(
            name="slow_culture_benchmark",
            persuasion_rate=0.025,
            ai_power=0.05,
            personalization=0.20,
            platform_bias=0.02,
            offline_anchor=0.10,
            selection_strength=0.70,
        ),
        TasteDriftParams(
            name="ai_speed_preference_capture",
            persuasion_rate=0.18,
            ai_power=0.95,
            personalization=0.85,
            platform_bias=0.12,
            offline_anchor=0.04,
            selection_strength=0.70,
        ),
        TasteDriftParams(
            name="strong_selection_overwhelmed",
            persuasion_rate=0.18,
            ai_power=0.95,
            personalization=0.85,
            platform_bias=0.12,
            offline_anchor=0.04,
            selection_strength=2.30,
        ),
    ]
