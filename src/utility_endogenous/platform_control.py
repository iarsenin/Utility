"""Platform-controlled preference transition model.

The platform chooses exposure intensity to maximize engagement and predictability.
Users choose according to local preferences, while preference states evolve under the
chosen exposure and are selected by a separate fitness proxy.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


EPSILON = 1e-9


@dataclass(frozen=True)
class PlatformControlParams:
    name: str
    periods: int = 100
    grid_size: int = 101
    initial_center: float = 0.35
    initial_spread: float = 0.10
    plasticity: float = 0.12
    offline_anchor: float = 0.05
    selection_strength: float = 1.00
    mutation: float = 0.002
    max_exposure: float = 1.00
    exposure_grid_size: int = 21
    exposure_cost: float = 0.10
    engagement_weight: float = 1.00
    predictability_weight: float = 0.20
    autonomy_weight: float = 0.00
    policy: str = "platform"
    fixed_exposure: float = 0.00


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def theta_grid(size: int) -> list[float]:
    if size < 2:
        raise ValueError("grid_size must be at least 2")
    return [i / (size - 1) for i in range(size)]


def exposure_grid(params: PlatformControlParams) -> list[float]:
    if params.exposure_grid_size < 2:
        return [clamp(params.max_exposure)]
    return [
        params.max_exposure * i / (params.exposure_grid_size - 1)
        for i in range(params.exposure_grid_size)
    ]


def initial_distribution(points: list[float], center: float, spread: float) -> list[float]:
    weights = [math.exp(-((theta - center) ** 2) / (2 * spread**2)) for theta in points]
    total = sum(weights)
    return [weight / total for weight in weights]


def entropy(distribution: list[float]) -> float:
    return -sum(mass * math.log(mass + EPSILON) for mass in distribution) / math.log(
        len(distribution)
    )


def local_indirect_utility(theta: float) -> float:
    """Common-cardinalized indirect utility from a local Cobb-Douglas problem."""

    theta = clamp(theta, EPSILON, 1.0 - EPSILON)
    return theta * math.log(theta) + (1.0 - theta) * math.log(1.0 - theta)


def initial_preference_value(theta: float, initial_theta: float) -> float:
    """Final allocation evaluated by the initial preference parameter.

    A user with final state theta chooses platform attention theta. We ask how the
    initial self would evaluate that final attention allocation.
    """

    theta = clamp(theta, EPSILON, 1.0 - EPSILON)
    return initial_theta * math.log(theta) + (1.0 - initial_theta) * math.log(1.0 - theta)


def fitness(theta: float, params: PlatformControlParams) -> float:
    offline_capital = 1.0 - theta
    high_theta_penalty = theta * theta
    return math.exp(params.selection_strength * (1.10 * offline_capital - 0.50 * high_theta_penalty))


def move_mass(target: list[float], theta_next: float, mass: float) -> None:
    scaled = clamp(theta_next) * (len(target) - 1)
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
        out[i] += mass * (1.0 - mutation)
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
    return [mass / total for mass in out]


def selected_distribution(
    points: list[float], distribution: list[float], params: PlatformControlParams
) -> list[float]:
    fitnesses = [fitness(theta, params) for theta in points]
    average_fitness = sum(
        mass * fit for mass, fit in zip(distribution, fitnesses, strict=True)
    )
    return [
        mass * fit / average_fitness
        for mass, fit in zip(distribution, fitnesses, strict=True)
    ]


def transition_with_exposure(
    points: list[float],
    distribution: list[float],
    exposure: float,
    params: PlatformControlParams,
) -> tuple[list[float], float]:
    selected = selected_distribution(points, distribution, params)
    shifted = [0.0] * len(points)
    autonomy_loss = 0.0

    for theta, mass in zip(points, selected, strict=True):
        drift = params.plasticity * (
            exposure * (1.0 - theta) - params.offline_anchor * theta
        )
        theta_next = clamp(theta + drift)
        autonomy_loss += mass * (theta_next - theta) ** 2
        move_mass(shifted, theta_next, mass)

    return diffuse(shifted, params.mutation), autonomy_loss


def summarize_distribution(
    period: int,
    points: list[float],
    distribution: list[float],
    exposure: float,
    platform_value: float,
    autonomy_loss: float,
    params: PlatformControlParams,
) -> dict[str, float | int | str]:
    mean_theta = sum(theta * mass for theta, mass in zip(points, distribution, strict=True))
    mean_fitness = sum(
        fitness(theta, params) * mass for theta, mass in zip(points, distribution, strict=True)
    )
    local_value = sum(
        local_indirect_utility(theta) * mass
        for theta, mass in zip(points, distribution, strict=True)
    )
    initial_value = sum(
        initial_preference_value(theta, params.initial_center) * mass
        for theta, mass in zip(points, distribution, strict=True)
    )
    normalized_entropy = entropy(distribution)

    return {
        "scenario": params.name,
        "period": period,
        "policy": params.policy,
        "exposure": exposure,
        "mean_theta": mean_theta,
        "offline_social_capital": 1.0 - mean_theta,
        "mean_fitness": mean_fitness,
        "local_subjective_value": local_value,
        "initial_preference_value": initial_value,
        "entropy": normalized_entropy,
        "predictability": 1.0 - normalized_entropy,
        "platform_value": platform_value,
        "autonomy_loss": autonomy_loss,
    }


def platform_objective(
    exposure: float,
    next_distribution: list[float],
    autonomy_loss: float,
    params: PlatformControlParams,
) -> float:
    points = theta_grid(params.grid_size)
    mean_theta = sum(theta * mass for theta, mass in zip(points, next_distribution, strict=True))
    predictability = 1.0 - entropy(next_distribution)
    return (
        params.engagement_weight * mean_theta
        + params.predictability_weight * predictability
        - params.exposure_cost * exposure * exposure
        - params.autonomy_weight * autonomy_loss
    )


def choose_exposure(
    points: list[float], distribution: list[float], params: PlatformControlParams
) -> tuple[float, list[float], float, float]:
    if params.policy == "fixed":
        exposure = clamp(params.fixed_exposure, 0.0, params.max_exposure)
        next_distribution, autonomy_loss = transition_with_exposure(
            points, distribution, exposure, params
        )
        value = platform_objective(exposure, next_distribution, autonomy_loss, params)
        return exposure, next_distribution, value, autonomy_loss

    best: tuple[float, list[float], float, float] | None = None
    for exposure in exposure_grid(params):
        next_distribution, autonomy_loss = transition_with_exposure(
            points, distribution, exposure, params
        )
        value = platform_objective(exposure, next_distribution, autonomy_loss, params)
        if best is None or value > best[2]:
            best = (exposure, next_distribution, value, autonomy_loss)

    if best is None:
        raise RuntimeError("No exposure candidates available")
    return best


def simulate_platform_control(
    params: PlatformControlParams,
) -> list[dict[str, float | int | str]]:
    points = theta_grid(params.grid_size)
    distribution = initial_distribution(points, params.initial_center, params.initial_spread)
    initial_value = platform_objective(0.0, distribution, 0.0, params)
    records = [
        summarize_distribution(0, points, distribution, 0.0, initial_value, 0.0, params)
    ]

    for period in range(1, params.periods + 1):
        exposure, distribution, platform_value, autonomy_loss = choose_exposure(
            points, distribution, params
        )
        records.append(
            summarize_distribution(
                period,
                points,
                distribution,
                exposure,
                platform_value,
                autonomy_loss,
                params,
            )
        )

    return records


def platform_scenarios() -> list[PlatformControlParams]:
    return [
        PlatformControlParams(
            name="no_platform_selection_benchmark",
            policy="fixed",
            fixed_exposure=0.00,
            exposure_cost=0.20,
            plasticity=0.10,
            selection_strength=1.00,
        ),
        PlatformControlParams(
            name="fixed_high_exposure",
            policy="fixed",
            fixed_exposure=0.80,
            exposure_cost=0.20,
            plasticity=0.10,
            selection_strength=1.00,
        ),
        PlatformControlParams(
            name="myopic_platform_low_cost",
            policy="platform",
            exposure_cost=0.04,
            plasticity=0.12,
            selection_strength=1.00,
            predictability_weight=0.25,
        ),
        PlatformControlParams(
            name="myopic_platform_high_cost",
            policy="platform",
            exposure_cost=0.35,
            plasticity=0.12,
            selection_strength=1.00,
            predictability_weight=0.25,
        ),
        PlatformControlParams(
            name="platform_with_weak_autonomy_penalty",
            policy="platform",
            exposure_cost=0.04,
            plasticity=0.12,
            selection_strength=1.00,
            predictability_weight=0.25,
            autonomy_weight=25.00,
        ),
        PlatformControlParams(
            name="platform_with_calibrated_guardrail",
            policy="platform",
            exposure_cost=0.04,
            plasticity=0.12,
            selection_strength=1.00,
            predictability_weight=0.25,
            autonomy_weight=150.00,
        ),
    ]
