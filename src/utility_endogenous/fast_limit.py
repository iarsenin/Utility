"""Singular limit calculations for infinitely fast preference adaptation."""

from __future__ import annotations

from dataclasses import dataclass

from utility_endogenous.endogenous_taste import (
    TasteDriftParams,
    algorithmic_field,
    biological_fitness,
    cobb_douglas_satisfaction,
)
from utility_endogenous.indirect_evolution import (
    SocialPreferenceParams,
    clamp as clamp_lambda,
    cooperate,
    equilibrium_cooperation_rate,
    material_payoff,
)
from utility_endogenous.platform_control import (
    EPSILON,
    PlatformControlParams,
    fitness as platform_fitness,
    initial_distribution as platform_initial_distribution,
    initial_preference_value,
    local_indirect_utility,
    theta_grid,
)


@dataclass(frozen=True)
class FastTasteLimit:
    scenario: str
    fast_attractor_theta: float | None
    mean_fitness: float | None
    subjective_satisfaction: float | None
    selection_can_move_preferences: bool
    note: str


@dataclass(frozen=True)
class FastSocialLimit:
    scenario: str
    fast_attractor_lambda: float | None
    cooperation_rate: float | None
    material_payoff: float | None
    subjective_value: float | None
    material_nash: bool | None
    note: str


@dataclass(frozen=True)
class FastPlatformLimit:
    scenario: str
    penalty_case: str
    exposure: float
    fast_attractor_theta: float
    platform_value: float
    fitness: float
    local_subjective_value: float
    initial_preference_value: float
    autonomy_penalty: float


def _bisect_root(func, lower: float = 0.0, upper: float = 1.0) -> float | None:
    """Find a root when the endpoints weakly bracket zero."""

    f_lower = func(lower)
    f_upper = func(upper)
    if abs(f_lower) < 1e-12:
        return lower
    if abs(f_upper) < 1e-12:
        return upper
    if f_lower * f_upper > 0.0:
        return None

    lo = lower
    hi = upper
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        f_mid = func(mid)
        if abs(f_mid) < 1e-13:
            return mid
        if f_lower * f_mid <= 0.0:
            hi = mid
            f_upper = f_mid
        else:
            lo = mid
            f_lower = f_mid
        if abs(hi - lo) < 1e-12:
            break
    _ = f_upper
    return 0.5 * (lo + hi)


def fast_taste_drift(theta: float, params: TasteDriftParams) -> float:
    """Fast subsystem for the taste-drift model without the rate multiplier."""

    return algorithmic_field(theta, params) * (1.0 - theta) - params.offline_anchor * theta


def taste_fast_attractor(params: TasteDriftParams) -> float | None:
    """Return the unique monotone fast attractor in the current taste model."""

    if params.offline_anchor == 0.0 and algorithmic_field(0.0, params) == 0.0:
        return None
    root = _bisect_root(lambda theta: fast_taste_drift(theta, params))
    if root is None:
        return None
    return max(0.0, min(1.0, root))


def taste_fast_limit(params: TasteDriftParams) -> FastTasteLimit:
    theta_star = taste_fast_attractor(params)
    if theta_star is None:
        return FastTasteLimit(
            scenario=params.name,
            fast_attractor_theta=None,
            mean_fitness=None,
            subjective_satisfaction=None,
            selection_can_move_preferences=True,
            note=(
                "No active fast preference law; the model reduces to selection "
                "over inherited tastes."
            ),
        )

    return FastTasteLimit(
        scenario=params.name,
        fast_attractor_theta=theta_star,
        mean_fitness=biological_fitness(theta_star, params),
        subjective_satisfaction=cobb_douglas_satisfaction(theta_star),
        selection_can_move_preferences=False,
        note="Unique fast attractor; Darwinian selection has no preference variation left to sort.",
    )


def social_fast_limit(params: SocialPreferenceParams) -> FastSocialLimit:
    if params.influence_rate == 0.0:
        return FastSocialLimit(
            scenario=params.name,
            fast_attractor_lambda=None,
            cooperation_rate=None,
            material_payoff=None,
            subjective_value=None,
            material_nash=None,
            note="No active fast preference law; this is the inherited-preference benchmark.",
        )

    lambda_star = clamp_lambda(params.lambda_target, params.lambda_min, params.lambda_max)
    cooperation = equilibrium_cooperation_rate([lambda_star], [1.0], params.norm_bonus)
    action_c = cooperate(lambda_star, cooperation, params.norm_bonus)
    own = material_payoff(action_c, cooperation)
    other = 3.0 * cooperation if action_c else 1.0 - cooperation
    subjective = own + lambda_star * other + (params.norm_bonus if action_c else 0.0)

    material_nash = cooperation < 1e-8
    if cooperation > 1.0 - 1e-8:
        material_nash = False

    return FastSocialLimit(
        scenario=params.name,
        fast_attractor_lambda=lambda_star,
        cooperation_rate=cooperation,
        material_payoff=own,
        subjective_value=subjective,
        material_nash=material_nash,
        note="Fast preference adaptation pins the social motive before material selection acts.",
    )


def platform_theta_star(exposure: float, params: PlatformControlParams) -> float:
    denominator = exposure + params.offline_anchor
    if denominator <= EPSILON:
        return params.initial_center
    return max(0.0, min(1.0, exposure / denominator))


def expected_jump_loss(theta_star: float, params: PlatformControlParams) -> float:
    points = theta_grid(params.grid_size)
    distribution = platform_initial_distribution(
        points, params.initial_center, params.initial_spread
    )
    return sum(
        (theta - theta_star) ** 2 * mass
        for theta, mass in zip(points, distribution, strict=True)
    )


def platform_fast_objective(
    exposure: float,
    params: PlatformControlParams,
    penalty_case: str,
) -> tuple[float, float, float]:
    theta_star = platform_theta_star(exposure, params)
    jump_loss = expected_jump_loss(theta_star, params)
    steady_entropy = 0.0

    if penalty_case == "steady":
        autonomy_penalty = 0.0
    elif penalty_case == "boundary_layer":
        autonomy_penalty = jump_loss
    else:
        raise ValueError(f"Unknown penalty case: {penalty_case}")

    value = (
        params.engagement_weight * theta_star
        + params.predictability_weight * (1.0 - steady_entropy)
        - params.exposure_cost * exposure * exposure
        - params.autonomy_weight * autonomy_penalty
    )
    return value, theta_star, autonomy_penalty


def platform_fast_limit(
    params: PlatformControlParams, penalty_case: str = "steady"
) -> FastPlatformLimit:
    candidates = [
        params.max_exposure * i / max(params.exposure_grid_size - 1, 1)
        for i in range(params.exposure_grid_size)
    ]
    if params.policy == "fixed":
        candidates = [max(0.0, min(params.max_exposure, params.fixed_exposure))]

    best: tuple[float, float, float, float] | None = None
    for exposure in candidates:
        value, theta_star, autonomy_penalty = platform_fast_objective(
            exposure, params, penalty_case
        )
        if best is None or value > best[0]:
            best = (value, exposure, theta_star, autonomy_penalty)

    if best is None:
        raise RuntimeError("No exposure candidates available")

    value, exposure, theta_star, autonomy_penalty = best
    return FastPlatformLimit(
        scenario=params.name,
        penalty_case=penalty_case,
        exposure=exposure,
        fast_attractor_theta=theta_star,
        platform_value=value,
        fitness=platform_fitness(theta_star, params),
        local_subjective_value=local_indirect_utility(theta_star),
        initial_preference_value=initial_preference_value(theta_star, params.initial_center),
        autonomy_penalty=autonomy_penalty,
    )


def point_mass_entropy() -> float:
    """Entropy of the singular limit distribution."""

    return 0.0
