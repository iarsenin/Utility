"""Timescale variants for the infinite preference-velocity limit.

This module keeps preference adaptation instantaneous, but it does not assume
population or institutional dynamics are slow. Their speeds are explicit
parameters that can be calibrated or estimated from panel data.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


EPSILON = 1e-12


@dataclass(frozen=True)
class TimescaleVariantParams:
    name: str
    horizon: int = 400
    initial_exposure: float = 0.05
    fixed_target_exposure: float = 0.05
    institution_speed: float = 0.10
    population_speed: float = 0.10
    offline_anchor: float = 0.05
    exposure_cost: float = 0.08
    growth_baseline: float = 0.12
    offline_growth: float = 0.55
    high_theta_penalty: float = 1.05
    survival_weight: float = 0.00
    target_mode: str = "myopic_platform"
    extinction_log_threshold: float = -4.605170185988091


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def fast_theta(exposure: float, offline_anchor: float) -> float:
    denominator = exposure + offline_anchor
    if denominator <= EPSILON:
        return 0.0
    return clamp(exposure / denominator)


def material_growth(theta: float, params: TimescaleVariantParams) -> float:
    return (
        params.growth_baseline
        + params.offline_growth * (1.0 - theta)
        - params.high_theta_penalty * theta * theta
    )


def platform_flow_value(exposure: float, params: TimescaleVariantParams) -> float:
    theta = fast_theta(exposure, params.offline_anchor)
    growth = material_growth(theta, params)
    return theta - params.exposure_cost * exposure * exposure + params.survival_weight * growth


def exposure_grid(steps: int = 201) -> list[float]:
    return [i / (steps - 1) for i in range(steps)]


def target_exposure(params: TimescaleVariantParams) -> float:
    if params.target_mode == "fixed":
        return clamp(params.fixed_target_exposure)
    if params.target_mode != "myopic_platform":
        raise ValueError(f"Unknown target mode: {params.target_mode}")
    return max(exposure_grid(), key=lambda exposure: platform_flow_value(exposure, params))


def simulate_timescale_variant(
    params: TimescaleVariantParams,
) -> list[dict[str, float | int | str | bool]]:
    exposure = clamp(params.initial_exposure)
    log_population = 0.0
    target = target_exposure(params)
    records: list[dict[str, float | int | str | bool]] = []

    for period in range(params.horizon + 1):
        theta = fast_theta(exposure, params.offline_anchor)
        growth = material_growth(theta, params)
        material_best_response_gap = theta
        extinct = log_population <= params.extinction_log_threshold
        records.append(
            {
                "scenario": params.name,
                "period": period,
                "target_mode": params.target_mode,
                "institution_speed": params.institution_speed,
                "population_speed": params.population_speed,
                "survival_weight": params.survival_weight,
                "exposure": exposure,
                "target_exposure": target,
                "theta": theta,
                "material_growth": growth,
                "log_population": log_population,
                "population": math.exp(log_population),
                "extinct": extinct,
                "platform_flow_value": platform_flow_value(exposure, params),
                "material_best_response_gap": material_best_response_gap,
            }
        )
        if period == params.horizon:
            break
        if extinct:
            continue
        exposure = clamp(exposure + params.institution_speed * (target - exposure))
        log_population += params.population_speed * growth

    return records


def summarize_variant(
    records: list[dict[str, float | int | str | bool]],
    params: TimescaleVariantParams,
) -> dict[str, float | int | str | bool]:
    final = records[-1]
    tail = records[-min(50, len(records)) :]
    mean_tail_growth = sum(float(row["material_growth"]) for row in tail) / len(tail)
    min_population = min(float(row["population"]) for row in records)
    extinct_periods = [int(row["period"]) for row in records if row["extinct"] is True]
    extinct_period = extinct_periods[0] if extinct_periods else None
    survives = extinct_period is None and mean_tail_growth >= -1e-8

    return {
        "scenario": params.name,
        "target_mode": params.target_mode,
        "institution_speed": params.institution_speed,
        "population_speed": params.population_speed,
        "survival_weight": params.survival_weight,
        "final_exposure": float(final["exposure"]),
        "target_exposure": float(final["target_exposure"]),
        "final_theta": float(final["theta"]),
        "final_growth": float(final["material_growth"]),
        "final_population": float(final["population"]),
        "min_population": min_population,
        "mean_tail_growth": mean_tail_growth,
        "extinct_period": extinct_period,
        "survives_long_run": survives,
        "material_best_response_gap": float(final["material_best_response_gap"]),
    }


def fixed_rule_survival_table(
    params: TimescaleVariantParams,
    steps: int = 41,
) -> list[dict[str, float | bool]]:
    rows: list[dict[str, float | bool]] = []
    for exposure in exposure_grid(steps):
        theta = fast_theta(exposure, params.offline_anchor)
        growth = material_growth(theta, params)
        rows.append(
            {
                "fixed_exposure": exposure,
                "theta": theta,
                "material_growth": growth,
                "survives_long_run": growth >= 0.0,
                "platform_flow_value": platform_flow_value(exposure, params),
            }
        )
    return rows


def estimate_ar1_half_life(values: list[float], dt: float = 1.0) -> dict[str, float | None]:
    """Estimate a process half-life from y[t+1] = alpha + rho y[t].

    This is intentionally small and transparent. In empirical work this should
    be replaced by a latent-state or structural panel estimator when choices are
    noisy proxies for preference states.
    """

    if len(values) < 3:
        raise ValueError("At least three observations are required")
    x = values[:-1]
    y = values[1:]
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    denominator = sum((item - x_mean) ** 2 for item in x)
    if denominator <= EPSILON:
        return {"rho": None, "continuous_speed": None, "half_life": None}

    rho = sum((x_i - x_mean) * (y_i - y_mean) for x_i, y_i in zip(x, y, strict=True))
    rho /= denominator
    if rho <= 0.0 or rho >= 1.0:
        return {"rho": rho, "continuous_speed": None, "half_life": None}

    continuous_speed = -math.log(rho) / dt
    half_life = math.log(2.0) / continuous_speed
    return {
        "rho": rho,
        "continuous_speed": continuous_speed,
        "half_life": half_life,
    }
