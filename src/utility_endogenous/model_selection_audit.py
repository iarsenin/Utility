"""Route-agnostic model-selection stress tests.

The existing toy models are deliberately interpretable. This module asks a
different question: do the qualitative fast-limit claims survive in generic
finite games where preference closure is represented as a payoff
transformation?
"""

from __future__ import annotations

from dataclasses import dataclass
import random
import statistics


PayoffVector = tuple[float, float, float, float]
Distribution = tuple[float, float, float, float]
Profile = tuple[int, int]

PROFILES: tuple[Profile, ...] = ((0, 0), (0, 1), (1, 0), (1, 1))
LAMBDA_GRID: tuple[float, ...] = (0.0, 0.25, 0.75, 1.5, 3.0)
EPSILON = 1e-10


@dataclass(frozen=True)
class RouteSummary:
    route: str
    games: int
    br_invariance_rate: float | None
    pure_br_invariance_rate: float | None
    equilibrium_shift_rate: float | None
    proxy_material_loss_rate: float | None
    proxy_gain_material_loss_rate: float | None
    all_regimes_negative_rate: float | None
    mean_material_loss_when_proxy_wins: float | None
    median_material_loss_when_proxy_wins: float | None
    verdict: str


def profile_index(row_action: int, column_action: int) -> int:
    return 2 * row_action + column_action


def vector_sum(left: PayoffVector, right: PayoffVector) -> PayoffVector:
    return tuple(a + b for a, b in zip(left, right, strict=True))  # type: ignore[return-value]


def scale_add(
    base: PayoffVector,
    scale: float,
    perturbation: PayoffVector,
) -> PayoffVector:
    return tuple(
        base_value + scale * perturbation_value
        for base_value, perturbation_value in zip(base, perturbation, strict=True)
    )  # type: ignore[return-value]


def expected_value(payoffs: PayoffVector, distribution: Distribution) -> float:
    return sum(value * probability for value, probability in zip(payoffs, distribution, strict=True))


def distribution_distance(left: Distribution, right: Distribution) -> float:
    return sum(abs(a - b) for a, b in zip(left, right, strict=True))


def best_response_set(
    payoffs: PayoffVector,
    player: int,
    opponent_action: int,
) -> frozenset[int]:
    values: list[tuple[int, float]] = []
    for action in (0, 1):
        if player == 0:
            index = profile_index(action, opponent_action)
        else:
            index = profile_index(opponent_action, action)
        values.append((action, payoffs[index]))

    best = max(value for _, value in values)
    return frozenset(action for action, value in values if abs(value - best) <= EPSILON)


def br_correspondence_invariant(
    material_1: PayoffVector,
    material_2: PayoffVector,
    subjective_1: PayoffVector,
    subjective_2: PayoffVector,
) -> bool:
    for opponent_action in (0, 1):
        if best_response_set(material_1, 0, opponent_action) != best_response_set(
            subjective_1, 0, opponent_action
        ):
            return False
        if best_response_set(material_2, 1, opponent_action) != best_response_set(
            subjective_2, 1, opponent_action
        ):
            return False
    return True


def action_zero_difference_endpoints(payoffs: PayoffVector, player: int) -> tuple[float, float]:
    """Payoff difference for action 0 vs. action 1 at opponent probabilities 0 and 1."""
    if player == 0:
        return payoffs[1] - payoffs[3], payoffs[0] - payoffs[2]
    return payoffs[2] - payoffs[3], payoffs[0] - payoffs[1]


def affine_value(endpoints: tuple[float, float], opponent_zero_probability: float) -> float:
    low, high = endpoints
    return low + (high - low) * opponent_zero_probability


def affine_roots_in_unit_interval(endpoints: tuple[float, float]) -> list[float]:
    low, high = endpoints
    slope = high - low
    if abs(slope) <= EPSILON:
        return []
    root = -low / slope
    if -EPSILON <= root <= 1.0 + EPSILON:
        return [min(1.0, max(0.0, root))]
    return []


def sign(value: float) -> int:
    if value > EPSILON:
        return 1
    if value < -EPSILON:
        return -1
    return 0


def affine_best_responses_identical(
    material_endpoints: tuple[float, float],
    subjective_endpoints: tuple[float, float],
) -> bool:
    breakpoints = sorted(
        {
            0.0,
            1.0,
            *affine_roots_in_unit_interval(material_endpoints),
            *affine_roots_in_unit_interval(subjective_endpoints),
        }
    )
    probes = list(breakpoints)
    probes.extend(
        (left + right) / 2.0
        for left, right in zip(breakpoints, breakpoints[1:], strict=False)
        if right - left > EPSILON
    )
    for probability in probes:
        if sign(affine_value(material_endpoints, probability)) != sign(
            affine_value(subjective_endpoints, probability)
        ):
            return False
    return True


def mixed_br_correspondence_invariant(
    material_1: PayoffVector,
    material_2: PayoffVector,
    subjective_1: PayoffVector,
    subjective_2: PayoffVector,
) -> bool:
    return affine_best_responses_identical(
        action_zero_difference_endpoints(material_1, 0),
        action_zero_difference_endpoints(subjective_1, 0),
    ) and affine_best_responses_identical(
        action_zero_difference_endpoints(material_2, 1),
        action_zero_difference_endpoints(subjective_2, 1),
    )


def pure_nash(payoff_1: PayoffVector, payoff_2: PayoffVector) -> list[Profile]:
    equilibria: list[Profile] = []
    for row_action, column_action in PROFILES:
        if row_action not in best_response_set(payoff_1, 0, column_action):
            continue
        if column_action not in best_response_set(payoff_2, 1, row_action):
            continue
        equilibria.append((row_action, column_action))
    return equilibria


def mixed_distribution(payoff_1: PayoffVector, payoff_2: PayoffVector) -> Distribution:
    denominator_column = payoff_1[0] - payoff_1[1] - payoff_1[2] + payoff_1[3]
    denominator_row = payoff_2[0] - payoff_2[2] - payoff_2[1] + payoff_2[3]
    if abs(denominator_column) <= EPSILON or abs(denominator_row) <= EPSILON:
        return (0.25, 0.25, 0.25, 0.25)

    column_zero = (payoff_1[3] - payoff_1[1]) / denominator_column
    row_zero = (payoff_2[3] - payoff_2[2]) / denominator_row
    if not (0.0 <= column_zero <= 1.0 and 0.0 <= row_zero <= 1.0):
        return (0.25, 0.25, 0.25, 0.25)

    return (
        row_zero * column_zero,
        row_zero * (1.0 - column_zero),
        (1.0 - row_zero) * column_zero,
        (1.0 - row_zero) * (1.0 - column_zero),
    )


def selected_equilibrium(
    game_payoff_1: PayoffVector,
    game_payoff_2: PayoffVector,
    ranking_payoff_1: PayoffVector,
    ranking_payoff_2: PayoffVector,
) -> Distribution:
    pure = pure_nash(game_payoff_1, game_payoff_2)
    if pure:
        selected = max(
            pure,
            key=lambda profile: (
                ranking_payoff_1[profile_index(*profile)]
                + ranking_payoff_2[profile_index(*profile)]
            ),
        )
        return tuple(1.0 if profile == selected else 0.0 for profile in PROFILES)  # type: ignore[return-value]
    return mixed_distribution(game_payoff_1, game_payoff_2)


def random_vector(rng: random.Random) -> PayoffVector:
    return tuple(rng.uniform(-1.0, 1.0) for _ in range(4))  # type: ignore[return-value]


def normalized(vector: PayoffVector) -> PayoffVector:
    mean = sum(vector) / len(vector)
    centered = [value - mean for value in vector]
    scale = max(abs(value) for value in centered)
    if scale <= EPSILON:
        return (0.0, 0.0, 0.0, 0.0)
    return tuple(value / scale for value in centered)  # type: ignore[return-value]


def neutral_distortion_for_player(rng: random.Random, player: int) -> PayoffVector:
    first = rng.uniform(-1.0, 1.0)
    second = rng.uniform(-1.0, 1.0)
    if player == 0:
        return (first, second, first, second)
    return (first, first, second, second)


def proxy_vector(
    material_total: PayoffVector,
    route: str,
    rng: random.Random,
    noise_weight: float = 0.25,
) -> PayoffVector:
    noise = normalized(random_vector(rng))
    material = normalized(material_total)
    if route == "proxy_aligned":
        base = material
    elif route == "proxy_independent":
        base = (0.0, 0.0, 0.0, 0.0)
        noise_weight = 1.0
    elif route == "proxy_misaligned":
        base = tuple(-value for value in material)  # type: ignore[assignment]
    else:
        raise ValueError(f"Unknown proxy route: {route}")
    return normalized(
        tuple(
            base_value + noise_weight * noise_value
            for base_value, noise_value in zip(base, noise, strict=True)
        )  # type: ignore[arg-type]
    )


def strategic_route_summary(games: int, seed: int, neutral: bool) -> RouteSummary:
    rng = random.Random(seed)
    pure_invariant_count = 0
    mixed_invariant_count = 0
    shift_count = 0

    for _ in range(games):
        material_1 = random_vector(rng)
        material_2 = random_vector(rng)
        if neutral:
            distortion_1 = neutral_distortion_for_player(rng, 0)
            distortion_2 = neutral_distortion_for_player(rng, 1)
            route = "neutral_control"
        else:
            distortion_1 = random_vector(rng)
            distortion_2 = random_vector(rng)
            route = "strategic_random_distortion"

        subjective_1 = scale_add(material_1, 1.0, distortion_1)
        subjective_2 = scale_add(material_2, 1.0, distortion_2)
        if br_correspondence_invariant(material_1, material_2, subjective_1, subjective_2):
            pure_invariant_count += 1
        if mixed_br_correspondence_invariant(material_1, material_2, subjective_1, subjective_2):
            mixed_invariant_count += 1

        material_eq = selected_equilibrium(material_1, material_2, material_1, material_2)
        # Use material payoffs for equilibrium selection in this diagnostic so
        # the metric captures Nash-set changes rather than cardinal tie-breaking
        # changes among already unchanged equilibria.
        subjective_eq = selected_equilibrium(subjective_1, subjective_2, material_1, material_2)
        if distribution_distance(material_eq, subjective_eq) > 0.25:
            shift_count += 1

    if neutral:
        verdict = "sanity check: strategically irrelevant preference movement should not change predictions"
    else:
        verdict = "generic stress test: strategic preference movement usually changes the reduced game"
    return RouteSummary(
        route=route,
        games=games,
        br_invariance_rate=mixed_invariant_count / games,
        pure_br_invariance_rate=pure_invariant_count / games,
        equilibrium_shift_rate=shift_count / games,
        proxy_material_loss_rate=None,
        proxy_gain_material_loss_rate=None,
        all_regimes_negative_rate=None,
        mean_material_loss_when_proxy_wins=None,
        median_material_loss_when_proxy_wins=None,
        verdict=verdict,
    )


def proxy_route_rows(games: int, seed: int, route: str) -> list[dict[str, float | int | str | bool]]:
    rng = random.Random(seed)
    rows: list[dict[str, float | int | str | bool]] = []

    for game_id in range(games):
        material_1 = random_vector(rng)
        material_2 = random_vector(rng)
        material_total = vector_sum(material_1, material_2)
        proxy = proxy_vector(material_total, route, rng)

        neutral_eq = selected_equilibrium(material_1, material_2, material_1, material_2)
        neutral_material = expected_value(material_total, neutral_eq)
        neutral_proxy = expected_value(proxy, neutral_eq)

        regime_records: list[dict[str, float | Distribution]] = []
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
                    "lambda": lambda_value,
                    "equilibrium": equilibrium,
                    "material": expected_value(material_total, equilibrium),
                    "proxy": expected_value(proxy, equilibrium),
                    "subjective": expected_value(
                        vector_sum(subjective_1, subjective_2),
                        equilibrium,
                    ),
                }
            )

        proxy_choice = max(regime_records, key=lambda row: float(row["proxy"]))
        material_choice = max(regime_records, key=lambda row: float(row["material"]))
        material_loss = float(material_choice["material"]) - float(proxy_choice["material"])
        proxy_gain = float(proxy_choice["proxy"]) - neutral_proxy
        platform_shift = distribution_distance(
            proxy_choice["equilibrium"],  # type: ignore[arg-type]
            neutral_eq,
        )

        rows.append(
            {
                "route": route,
                "game_id": game_id,
                "neutral_material": neutral_material,
                "neutral_proxy": neutral_proxy,
                "proxy_lambda": float(proxy_choice["lambda"]),
                "material_lambda": float(material_choice["lambda"]),
                "proxy_choice_material": float(proxy_choice["material"]),
                "material_choice_material": float(material_choice["material"]),
                "proxy_choice_proxy": float(proxy_choice["proxy"]),
                "material_choice_proxy": float(material_choice["proxy"]),
                "material_loss": material_loss,
                "proxy_gain": proxy_gain,
                "proxy_material_loss": material_loss > 1e-8,
                "proxy_gain_material_loss": proxy_gain > 1e-8 and material_loss > 1e-8,
                "all_regimes_negative": all(float(row["material"]) < 0.0 for row in regime_records),
                "equilibrium_shift": platform_shift > 0.25,
            }
        )

    return rows


def proxy_route_summary(rows: list[dict[str, float | int | str | bool]]) -> RouteSummary:
    if not rows:
        raise ValueError("No rows supplied")

    route = str(rows[0]["route"])
    games = len(rows)
    material_loss_rows = [float(row["material_loss"]) for row in rows if row["proxy_material_loss"] is True]
    if material_loss_rows:
        mean_loss = statistics.fmean(material_loss_rows)
        median_loss = statistics.median(material_loss_rows)
    else:
        mean_loss = None
        median_loss = None

    if route == "proxy_aligned":
        verdict = "control: platform proxy is close to material welfare, so losses should be limited"
    elif route == "proxy_independent":
        verdict = "diagnostic: proxy optimization can lose material welfare without built-in anti-fitness assumptions"
    elif route == "proxy_misaligned":
        verdict = "stress case: one-dimensional platform model is credible only if this misalignment is defended empirically"
    else:
        verdict = "proxy route"

    return RouteSummary(
        route=route,
        games=games,
        br_invariance_rate=None,
        pure_br_invariance_rate=None,
        equilibrium_shift_rate=sum(row["equilibrium_shift"] is True for row in rows) / games,
        proxy_material_loss_rate=sum(row["proxy_material_loss"] is True for row in rows) / games,
        proxy_gain_material_loss_rate=sum(row["proxy_gain_material_loss"] is True for row in rows)
        / games,
        all_regimes_negative_rate=sum(row["all_regimes_negative"] is True for row in rows) / games,
        mean_material_loss_when_proxy_wins=mean_loss,
        median_material_loss_when_proxy_wins=median_loss,
        verdict=verdict,
    )


def run_model_selection_audit(
    games: int = 5000,
    seed: int = 20260620,
) -> tuple[list[RouteSummary], list[dict[str, float | int | str | bool]]]:
    summaries = [
        strategic_route_summary(games, seed, neutral=True),
        strategic_route_summary(games, seed + 1, neutral=False),
    ]
    proxy_rows: list[dict[str, float | int | str | bool]] = []
    for offset, route in enumerate(
        ("proxy_aligned", "proxy_independent", "proxy_misaligned"),
        start=2,
    ):
        rows = proxy_route_rows(games, seed + offset, route)
        proxy_rows.extend(rows)
        summaries.append(proxy_route_summary(rows))
    return summaries, proxy_rows
