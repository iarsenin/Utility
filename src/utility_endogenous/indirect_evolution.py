"""Indirect evolutionary Prisoner's Dilemma with mutable social preferences."""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class SocialPreferenceParams:
    name: str
    periods: int = 80
    grid_size: int = 81
    lambda_min: float = -0.50
    lambda_max: float = 1.50
    initial_center: float = 0.25
    initial_spread: float = 0.22
    influence_rate: float = 0.00
    lambda_target: float = 0.25
    norm_bonus: float = 0.00
    selection_strength: float = 0.45
    mutation: float = 0.004


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def lambda_grid(params: SocialPreferenceParams) -> list[float]:
    if params.grid_size < 2:
        raise ValueError("grid_size must be at least 2")
    step = (params.lambda_max - params.lambda_min) / (params.grid_size - 1)
    return [params.lambda_min + i * step for i in range(params.grid_size)]


def initial_distribution(points: list[float], center: float, spread: float) -> list[float]:
    weights = [math.exp(-((x - center) ** 2) / (2 * spread**2)) for x in points]
    total = sum(weights)
    return [w / total for w in weights]


def cooperate(lambda_value: float, q: float, norm_bonus: float) -> bool:
    """Best response under U_i = pi_i + lambda_i pi_j + norm_bonus * 1{C}."""

    utility_c_minus_d = -1.0 - q + lambda_value * (4.0 - q) + norm_bonus
    return utility_c_minus_d >= 0.0


def equilibrium_cooperation_rate(
    lambdas: list[float], distribution: list[float], norm_bonus: float
) -> float:
    q = 0.5
    for _ in range(200):
        q_next = sum(
            mass
            for lambda_value, mass in zip(lambdas, distribution, strict=True)
            if cooperate(lambda_value, q, norm_bonus)
        )
        if abs(q_next - q) < 1e-10:
            return q_next
        q = 0.70 * q + 0.30 * q_next
    return q


def material_payoff(action_cooperate: bool, q: float) -> float:
    if action_cooperate:
        return 3.0 * q
    return 5.0 * q + 1.0 * (1.0 - q)


def move_mass(
    target: list[float],
    value: float,
    mass: float,
    params: SocialPreferenceParams,
) -> None:
    value = clamp(value, params.lambda_min, params.lambda_max)
    scaled = (value - params.lambda_min) / (params.lambda_max - params.lambda_min)
    scaled *= params.grid_size - 1
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
    return [x / total for x in out]


def summarize(
    period: int,
    lambdas: list[float],
    distribution: list[float],
    params: SocialPreferenceParams,
) -> dict[str, float | int | str]:
    q = equilibrium_cooperation_rate(lambdas, distribution, params.norm_bonus)
    mean_lambda = sum(value * mass for value, mass in zip(lambdas, distribution, strict=True))
    payoffs = []
    subjective_values = []
    for lambda_value, mass in zip(lambdas, distribution, strict=True):
        action_c = cooperate(lambda_value, q, params.norm_bonus)
        own = material_payoff(action_c, q)
        other = 3.0 * q if action_c else 1.0 - q
        subjective = own + lambda_value * other + (params.norm_bonus if action_c else 0.0)
        payoffs.append(mass * own)
        subjective_values.append(mass * subjective)

    return {
        "scenario": params.name,
        "period": period,
        "mean_lambda": mean_lambda,
        "cooperation_rate": q,
        "mean_material_payoff": sum(payoffs),
        "mean_subjective_value": sum(subjective_values),
    }


def simulate_social_preferences(
    params: SocialPreferenceParams,
) -> list[dict[str, float | int | str]]:
    lambdas = lambda_grid(params)
    distribution = initial_distribution(lambdas, params.initial_center, params.initial_spread)
    records = [summarize(0, lambdas, distribution, params)]

    for period in range(1, params.periods + 1):
        q = equilibrium_cooperation_rate(lambdas, distribution, params.norm_bonus)
        selected_weights = []
        for lambda_value, mass in zip(lambdas, distribution, strict=True):
            action_c = cooperate(lambda_value, q, params.norm_bonus)
            payoff = material_payoff(action_c, q)
            selected_weights.append(mass * math.exp(params.selection_strength * payoff))

        total = sum(selected_weights)
        selected = [w / total for w in selected_weights]

        shifted = [0.0] * len(lambdas)
        for lambda_value, mass in zip(lambdas, selected, strict=True):
            lambda_next = lambda_value + params.influence_rate * (
                params.lambda_target - lambda_value
            )
            move_mass(shifted, lambda_next, mass, params)

        distribution = diffuse(shifted, params.mutation)
        records.append(summarize(period, lambdas, distribution, params))

    return records


def social_preference_scenarios() -> list[SocialPreferenceParams]:
    return [
        SocialPreferenceParams(
            name="fixed_preferences_selection_only",
            influence_rate=0.00,
            lambda_target=0.25,
            norm_bonus=0.00,
            selection_strength=0.45,
        ),
        SocialPreferenceParams(
            name="prosocial_institution",
            influence_rate=0.055,
            lambda_target=1.10,
            norm_bonus=0.18,
            selection_strength=0.45,
        ),
        SocialPreferenceParams(
            name="conflict_algorithm",
            influence_rate=0.085,
            lambda_target=-0.25,
            norm_bonus=-0.20,
            selection_strength=0.45,
        ),
    ]
