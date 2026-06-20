"""World Bank WDI diagnostics for timescales and proxy alignment.

This module is deliberately dependency-light. It downloads World Bank API JSON,
caches it under ``data/raw``, builds a country-year panel, estimates transparent
panel diagnostics, and writes CSV/SVG/Markdown outputs.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import UTC, datetime
import html
import json
import math
from pathlib import Path
import statistics
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen


WORLD_BANK_API = "https://api.worldbank.org/v2"
DEFAULT_START_YEAR = 1990
DEFAULT_END_YEAR = 2024
EPSILON = 1e-12


@dataclass(frozen=True)
class IndicatorSpec:
    code: str
    slug: str
    label: str
    role: str
    units: str
    higher_is_materially_better: bool | None
    transform: str = "level"


@dataclass(frozen=True)
class OutcomeSpec:
    slug: str
    label: str
    units: str
    transform: str
    min_annualized_change: float
    max_annualized_change: float


@dataclass(frozen=True)
class OLSResult:
    coefficients: list[float]
    standard_errors: list[float]
    r_squared: float
    observations: int
    clusters: int


INDICATORS: tuple[IndicatorSpec, ...] = (
    IndicatorSpec(
        code="IT.NET.USER.ZS",
        slug="internet_users_pct",
        label="Individuals using the Internet",
        role="digital exposure proxy",
        units="percent of population",
        higher_is_materially_better=None,
    ),
    IndicatorSpec(
        code="IT.CEL.SETS.P2",
        slug="mobile_subscriptions_per_100",
        label="Mobile cellular subscriptions",
        role="digital infrastructure proxy",
        units="per 100 people",
        higher_is_materially_better=None,
    ),
    IndicatorSpec(
        code="NY.GDP.PCAP.KD",
        slug="gdp_pc_constant",
        label="GDP per capita",
        role="material proxy",
        units="constant 2015 US dollars",
        higher_is_materially_better=True,
        transform="log",
    ),
    IndicatorSpec(
        code="SP.DYN.LE00.IN",
        slug="life_expectancy",
        label="Life expectancy at birth",
        role="material proxy",
        units="years",
        higher_is_materially_better=True,
    ),
    IndicatorSpec(
        code="SP.DYN.TFRT.IN",
        slug="fertility_rate",
        label="Fertility rate",
        role="demographic adjustment proxy",
        units="births per woman",
        higher_is_materially_better=None,
    ),
    IndicatorSpec(
        code="SH.STA.SUIC.P5",
        slug="suicide_mortality",
        label="Suicide mortality rate",
        role="mental-health material proxy",
        units="deaths per 100,000 population",
        higher_is_materially_better=False,
    ),
)


OUTCOMES: tuple[OutcomeSpec, ...] = (
    OutcomeSpec(
        slug="gdp_pc_constant",
        label="GDP per capita",
        units="annualized log points",
        transform="log_percent",
        min_annualized_change=-50.0,
        max_annualized_change=50.0,
    ),
    OutcomeSpec(
        slug="life_expectancy",
        label="Life expectancy",
        units="annualized years",
        transform="level",
        min_annualized_change=-5.0,
        max_annualized_change=5.0,
    ),
    OutcomeSpec(
        slug="fertility_rate",
        label="Fertility rate",
        units="annualized births per woman",
        transform="level",
        min_annualized_change=-1.0,
        max_annualized_change=1.0,
    ),
    OutcomeSpec(
        slug="suicide_mortality",
        label="Suicide mortality",
        units="annualized deaths per 100,000",
        transform="level",
        min_annualized_change=-20.0,
        max_annualized_change=20.0,
    ),
)


def percentile(values: list[float], probability: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    position = probability * (len(ordered) - 1)
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def median_or_none(values: list[float]) -> float | None:
    if not values:
        return None
    return statistics.median(values)


def safe_float(value: object) -> float | None:
    if value is None or value == "":
        return None
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(result):
        return None
    return result


def transformed_value(value: float, transform: str) -> float | None:
    if transform == "level":
        return value
    if transform in {"log", "log_percent"}:
        if value <= 0.0:
            return None
        return math.log(value)
    raise ValueError(f"Unknown transform: {transform}")


def api_json(url: str) -> Any:
    request = Request(url, headers={"User-Agent": "utility-endogenous-wdi/0.1"})
    with urlopen(request, timeout=60) as response:
        return json.load(response)


def paged_world_bank_request(path: str, params: dict[str, object]) -> tuple[dict[str, Any], list[Any]]:
    records: list[Any] = []
    page = 1
    latest_meta: dict[str, Any] = {}
    while True:
        query = dict(params)
        query["page"] = page
        url = f"{WORLD_BANK_API}/{path}?{urlencode(query)}"
        payload = api_json(url)
        if not isinstance(payload, list) or len(payload) < 2:
            raise RuntimeError(f"Unexpected World Bank response for {url}")
        if isinstance(payload[0], dict) and "message" in payload[0]:
            raise RuntimeError(f"World Bank API error for {url}: {payload[0]}")
        latest_meta = payload[0]
        records.extend(payload[1] or [])
        pages = int(latest_meta.get("pages", 1))
        if page >= pages:
            break
        page += 1
    return latest_meta, records


def read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def raw_indicator_path(raw_dir: Path, code: str, start_year: int, end_year: int) -> Path:
    safe_code = code.replace(".", "_")
    return raw_dir / f"wdi_{safe_code}_{start_year}_{end_year}.json"


def fetch_countries(raw_dir: Path, refresh: bool = False) -> dict[str, Any]:
    path = raw_dir / "wdi_countries.json"
    if path.exists() and not refresh:
        return read_json(path)

    meta, records = paged_world_bank_request(
        "country",
        {"format": "json", "per_page": 400},
    )
    payload = {
        "source": "World Bank API v2 country endpoint",
        "fetched_utc": datetime.now(UTC).isoformat(),
        "metadata": meta,
        "records": records,
    }
    write_json(path, payload)
    return payload


def fetch_indicator(
    spec: IndicatorSpec,
    raw_dir: Path,
    start_year: int,
    end_year: int,
    refresh: bool = False,
) -> dict[str, Any]:
    path = raw_indicator_path(raw_dir, spec.code, start_year, end_year)
    if path.exists() and not refresh:
        return read_json(path)

    params = {
        "format": "json",
        "per_page": 20000,
        "date": f"{start_year}:{end_year}",
    }
    meta, records = paged_world_bank_request(
        f"country/all/indicator/{spec.code}",
        params,
    )
    payload = {
        "source": "World Bank API v2 indicator endpoint",
        "indicator_code": spec.code,
        "indicator_label": spec.label,
        "request": {
            "url": f"{WORLD_BANK_API}/country/all/indicator/{spec.code}",
            "params": params,
        },
        "fetched_utc": datetime.now(UTC).isoformat(),
        "metadata": meta,
        "records": records,
    }
    write_json(path, payload)
    return payload


def valid_countries(country_payload: dict[str, Any]) -> dict[str, dict[str, str]]:
    countries: dict[str, dict[str, str]] = {}
    for record in country_payload["records"]:
        country_code = str(record.get("id") or "")
        region = record.get("region") or {}
        region_name = str(region.get("value") or "")
        if not country_code or region_name == "Aggregates":
            continue
        income = record.get("incomeLevel") or {}
        countries[country_code] = {
            "country_code": country_code,
            "country_name": str(record.get("name") or ""),
            "region": region_name,
            "income_level": str(income.get("value") or ""),
        }
    return countries


def build_long_rows(
    indicator_payloads: dict[str, dict[str, Any]],
    countries: dict[str, dict[str, str]],
) -> list[dict[str, object]]:
    specs_by_code = {spec.code: spec for spec in INDICATORS}
    rows: list[dict[str, object]] = []
    for code, payload in indicator_payloads.items():
        spec = specs_by_code[code]
        for record in payload["records"]:
            country_code = str(record.get("countryiso3code") or "")
            if country_code not in countries:
                continue
            value = safe_float(record.get("value"))
            if value is None:
                continue
            year = int(record["date"])
            country = countries[country_code]
            rows.append(
                {
                    "country_code": country_code,
                    "country_name": country["country_name"],
                    "region": country["region"],
                    "income_level": country["income_level"],
                    "year": year,
                    "indicator_code": code,
                    "indicator_slug": spec.slug,
                    "indicator_label": spec.label,
                    "value": value,
                    "units": spec.units,
                    "role": spec.role,
                }
            )
    rows.sort(key=lambda row: (str(row["country_code"]), int(row["year"]), str(row["indicator_code"])))
    return rows


def build_panel_rows(long_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    panel: dict[tuple[str, int], dict[str, object]] = {}
    for row in long_rows:
        key = (str(row["country_code"]), int(row["year"]))
        if key not in panel:
            panel[key] = {
                "country_code": row["country_code"],
                "country_name": row["country_name"],
                "region": row["region"],
                "income_level": row["income_level"],
                "year": row["year"],
            }
        panel[key][str(row["indicator_slug"])] = row["value"]

    rows = list(panel.values())
    rows.sort(key=lambda row: (str(row["country_code"]), int(row["year"])))
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    fieldnames: list[str] = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def coverage_rows(long_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for spec in INDICATORS:
        indicator_rows = [row for row in long_rows if row["indicator_code"] == spec.code]
        years = [int(row["year"]) for row in indicator_rows]
        country_counts: dict[str, int] = {}
        for row in indicator_rows:
            country = str(row["country_code"])
            country_counts[country] = country_counts.get(country, 0) + 1
        rows.append(
            {
                "indicator_code": spec.code,
                "indicator_slug": spec.slug,
                "indicator_label": spec.label,
                "role": spec.role,
                "observations": len(indicator_rows),
                "countries": len(country_counts),
                "countries_with_10plus_observations": sum(
                    1 for count in country_counts.values() if count >= 10
                ),
                "first_year": min(years) if years else None,
                "last_year": max(years) if years else None,
            }
        )
    return rows


def panel_index(panel_rows: list[dict[str, object]]) -> dict[tuple[str, int], dict[str, object]]:
    return {
        (str(row["country_code"]), int(row["year"])): row
        for row in panel_rows
    }


def country_series(
    panel_rows: list[dict[str, object]],
    slug: str,
    transform: str = "level",
) -> dict[str, list[tuple[int, float]]]:
    series: dict[str, list[tuple[int, float]]] = {}
    for row in panel_rows:
        value = safe_float(row.get(slug))
        if value is None:
            continue
        transformed = transformed_value(value, transform)
        if transformed is None:
            continue
        country = str(row["country_code"])
        series.setdefault(country, []).append((int(row["year"]), transformed))
    for values in series.values():
        values.sort()
    return series


def traversal_years(series: list[tuple[int, float]]) -> float | None:
    if len(series) < 8:
        return None
    values = [value for _, value in series]
    low = min(values)
    high = max(values)
    observed_range = high - low
    if observed_range <= EPSILON:
        return None
    first_value = values[0]
    last_value = values[-1]
    increasing = last_value >= first_value
    normalized: list[tuple[int, float]] = []
    for year, value in series:
        if increasing:
            share = (value - low) / observed_range
        else:
            share = (high - value) / observed_range
        normalized.append((year, share))

    start_candidates = [year for year, share in normalized if share >= 0.10]
    if not start_candidates:
        return None
    start = start_candidates[0]
    end_candidates = [year for year, share in normalized if year >= start and share >= 0.90]
    if not end_candidates:
        return None
    duration = end_candidates[0] - start
    if duration <= 0:
        return None
    return float(duration)


def annual_absolute_changes(series: list[tuple[int, float]]) -> list[float]:
    changes: list[float] = []
    by_year = dict(series)
    for year, value in series:
        next_value = by_year.get(year + 1)
        if next_value is None:
            continue
        changes.append(abs(next_value - value))
    return changes


def internet_gap_closure_rows(panel_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    series = country_series(panel_rows, "internet_users_pct")
    rows: list[dict[str, object]] = []
    for country, values in series.items():
        speeds: list[float] = []
        by_year = dict(values)
        for year, value in values:
            next_value = by_year.get(year + 1)
            if next_value is None:
                continue
            gap = 100.0 - value
            if gap <= 5.0:
                continue
            delta = next_value - value
            if delta < 0.0:
                continue
            speed = max(0.0, min(1.0, delta / gap))
            speeds.append(speed)
        if not speeds:
            continue
        median_speed = statistics.median(speeds)
        if 0.0 < median_speed < 1.0:
            half_life = math.log(0.5) / math.log(1.0 - median_speed)
        else:
            half_life = None
        rows.append(
            {
                "country_code": country,
                "observed_year_pairs": len(speeds),
                "median_annual_gap_closure_speed": median_speed,
                "implied_remaining_gap_half_life_years": half_life,
            }
        )
    rows.sort(key=lambda row: str(row["country_code"]))
    return rows


def timescale_rows(
    panel_rows: list[dict[str, object]],
    gap_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    gap_speeds = [
        float(row["median_annual_gap_closure_speed"])
        for row in gap_rows
        if safe_float(row.get("median_annual_gap_closure_speed")) is not None
    ]
    gap_half_lives = [
        float(row["implied_remaining_gap_half_life_years"])
        for row in gap_rows
        if safe_float(row.get("implied_remaining_gap_half_life_years")) is not None
    ]
    rows: list[dict[str, object]] = []
    for spec in INDICATORS:
        transform = "log" if spec.transform == "log" else "level"
        by_country = country_series(panel_rows, spec.slug, transform=transform)
        durations: list[float] = []
        changes: list[float] = []
        countries_with_annual_pairs = 0
        for values in by_country.values():
            duration = traversal_years(values)
            if duration is not None:
                durations.append(duration)
            country_changes = annual_absolute_changes(values)
            if country_changes:
                countries_with_annual_pairs += 1
                changes.extend(country_changes)

        row: dict[str, object] = {
            "indicator_code": spec.code,
            "indicator_slug": spec.slug,
            "indicator_label": spec.label,
            "role": spec.role,
            "transform_for_timescale": transform,
            "countries_with_10_90_traversal": len(durations),
            "median_10_90_traversal_years": median_or_none(durations),
            "p25_10_90_traversal_years": percentile(durations, 0.25),
            "p75_10_90_traversal_years": percentile(durations, 0.75),
            "countries_with_annual_pairs": countries_with_annual_pairs,
            "median_abs_annual_change": median_or_none(changes),
            "p75_abs_annual_change": percentile(changes, 0.75),
        }
        if spec.slug == "internet_users_pct":
            row["countries_with_gap_closure"] = len(gap_rows)
            row["median_annual_gap_closure_speed"] = median_or_none(gap_speeds)
            row["median_remaining_gap_half_life_years"] = median_or_none(gap_half_lives)
        rows.append(row)
    return rows


def invert_matrix(matrix: list[list[float]]) -> list[list[float]]:
    size = len(matrix)
    augmented = [
        [float(matrix[row][col]) for col in range(size)]
        + [1.0 if row == col else 0.0 for col in range(size)]
        for row in range(size)
    ]
    for col in range(size):
        pivot = max(range(col, size), key=lambda row: abs(augmented[row][col]))
        if abs(augmented[pivot][col]) <= EPSILON:
            raise ValueError("Singular matrix in OLS")
        if pivot != col:
            augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        pivot_value = augmented[col][col]
        augmented[col] = [value / pivot_value for value in augmented[col]]
        for row in range(size):
            if row == col:
                continue
            factor = augmented[row][col]
            if abs(factor) <= EPSILON:
                continue
            augmented[row] = [
                value - factor * pivot_col_value
                for value, pivot_col_value in zip(augmented[row], augmented[col], strict=True)
            ]
    return [row[size:] for row in augmented]


def mat_vec_mul(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(value * item for value, item in zip(row, vector, strict=True)) for row in matrix]


def mat_mul(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    columns = list(zip(*right, strict=True))
    return [
        [sum(a * b for a, b in zip(row, column, strict=True)) for column in columns]
        for row in left
    ]


def ols_cluster(
    y_values: list[float],
    x_rows: list[list[float]],
    clusters: list[str],
) -> OLSResult:
    nobs = len(y_values)
    if nobs != len(x_rows) or nobs != len(clusters):
        raise ValueError("OLS input lengths differ")
    if not x_rows:
        raise ValueError("No OLS rows")
    nvars = len(x_rows[0])
    xtx = [[0.0 for _ in range(nvars)] for _ in range(nvars)]
    xty = [0.0 for _ in range(nvars)]
    for y_value, x_row in zip(y_values, x_rows, strict=True):
        for i in range(nvars):
            xty[i] += x_row[i] * y_value
            for j in range(nvars):
                xtx[i][j] += x_row[i] * x_row[j]
    xtx_inv = invert_matrix(xtx)
    coefficients = mat_vec_mul(xtx_inv, xty)
    residuals = [
        y_value - sum(coef * x for coef, x in zip(coefficients, x_row, strict=True))
        for y_value, x_row in zip(y_values, x_rows, strict=True)
    ]

    score_by_cluster: dict[str, list[float]] = {}
    for cluster, residual, x_row in zip(clusters, residuals, x_rows, strict=True):
        score = score_by_cluster.setdefault(cluster, [0.0 for _ in range(nvars)])
        for index, x_value in enumerate(x_row):
            score[index] += x_value * residual

    meat = [[0.0 for _ in range(nvars)] for _ in range(nvars)]
    for score in score_by_cluster.values():
        for i in range(nvars):
            for j in range(nvars):
                meat[i][j] += score[i] * score[j]

    covariance = mat_mul(mat_mul(xtx_inv, meat), xtx_inv)
    clusters_count = len(score_by_cluster)
    if clusters_count > 1 and nobs > nvars:
        correction = (clusters_count / (clusters_count - 1.0)) * ((nobs - 1.0) / (nobs - nvars))
        covariance = [[value * correction for value in row] for row in covariance]

    standard_errors = [math.sqrt(max(covariance[i][i], 0.0)) for i in range(nvars)]
    y_mean = sum(y_values) / nobs
    rss = sum(residual * residual for residual in residuals)
    tss = sum((value - y_mean) ** 2 for value in y_values)
    r_squared = 1.0 - rss / tss if tss > EPSILON else 0.0
    return OLSResult(
        coefficients=coefficients,
        standard_errors=standard_errors,
        r_squared=r_squared,
        observations=nobs,
        clusters=clusters_count,
    )


def outcome_change(
    start_value: float,
    end_value: float,
    years: int,
    outcome: OutcomeSpec,
) -> float | None:
    if years <= 0:
        return None
    if outcome.transform == "log_percent":
        if start_value <= 0.0 or end_value <= 0.0:
            return None
        return 100.0 * (math.log(end_value) - math.log(start_value)) / years
    if outcome.transform == "level":
        return (end_value - start_value) / years
    raise ValueError(f"Unknown outcome transform: {outcome.transform}")


def alignment_observations(
    panel_rows: list[dict[str, object]],
    outcome: OutcomeSpec,
    horizon: int,
) -> list[dict[str, object]]:
    index = panel_index(panel_rows)
    observations: list[dict[str, object]] = []
    for row in panel_rows:
        country = str(row["country_code"])
        year = int(row["year"])
        lag_row = index.get((country, year - 1))
        future_row = index.get((country, year + horizon))
        if lag_row is None or future_row is None:
            continue

        internet_now = safe_float(row.get("internet_users_pct"))
        internet_lag = safe_float(lag_row.get("internet_users_pct"))
        outcome_lag = safe_float(lag_row.get(outcome.slug))
        outcome_future = safe_float(future_row.get(outcome.slug))
        gdp_lag = safe_float(lag_row.get("gdp_pc_constant"))
        if (
            internet_now is None
            or internet_lag is None
            or outcome_lag is None
            or outcome_future is None
            or gdp_lag is None
            or gdp_lag <= 0.0
        ):
            continue
        internet_delta = internet_now - internet_lag
        if internet_delta < -20.0 or internet_delta > 50.0:
            continue
        years = horizon + 1
        y_value = outcome_change(outcome_lag, outcome_future, years, outcome)
        if y_value is None:
            continue
        if y_value < outcome.min_annualized_change or y_value > outcome.max_annualized_change:
            continue
        transformed_lag = transformed_value(
            outcome_lag,
            "log" if outcome.transform == "log_percent" else "level",
        )
        if transformed_lag is None:
            continue
        observations.append(
            {
                "country_code": country,
                "year": year,
                "outcome_value": y_value,
                "internet_delta_10pp": internet_delta / 10.0,
                "lag_internet_share": internet_lag / 100.0,
                "lag_log_gdp_pc": math.log(gdp_lag),
                "lag_outcome": transformed_lag,
            }
        )
    return observations


def fit_alignment(
    panel_rows: list[dict[str, object]],
    horizons: tuple[int, ...] = (0, 1, 3, 5),
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for outcome in OUTCOMES:
        for horizon in horizons:
            observations = alignment_observations(panel_rows, outcome, horizon)
            years = sorted({int(observation["year"]) for observation in observations})
            if len(observations) < 80 or len(years) < 4:
                continue
            base_year = years[0]
            include_lag_outcome = outcome.slug != "gdp_pc_constant"
            variable_names = [
                "intercept",
                "internet_delta_10pp",
                "lag_internet_share",
                "lag_log_gdp_pc",
            ]
            if include_lag_outcome:
                variable_names.append("lag_outcome")
            variable_names.extend(f"year_{year}" for year in years if year != base_year)
            x_rows: list[list[float]] = []
            y_values: list[float] = []
            clusters: list[str] = []
            for observation in observations:
                year = int(observation["year"])
                x_row = [
                    1.0,
                    float(observation["internet_delta_10pp"]),
                    float(observation["lag_internet_share"]),
                    float(observation["lag_log_gdp_pc"]),
                ]
                if include_lag_outcome:
                    x_row.append(float(observation["lag_outcome"]))
                x_row.extend(1.0 if year == dummy_year else 0.0 for dummy_year in years if dummy_year != base_year)
                x_rows.append(x_row)
                y_values.append(float(observation["outcome_value"]))
                clusters.append(str(observation["country_code"]))

            try:
                result = ols_cluster(y_values, x_rows, clusters)
            except ValueError:
                continue
            beta_index = variable_names.index("internet_delta_10pp")
            beta = result.coefficients[beta_index]
            se = result.standard_errors[beta_index]
            t_stat = beta / se if se > EPSILON else None
            p_value = math.erfc(abs(t_stat) / math.sqrt(2.0)) if t_stat is not None else None
            rows.append(
                {
                    "outcome_slug": outcome.slug,
                    "outcome_label": outcome.label,
                    "horizon_years_after_internet_change": horizon,
                    "dependent_variable_units": outcome.units,
                    "coefficient_per_10pp_internet_jump": beta,
                    "clustered_standard_error": se,
                    "ci95_low": beta - 1.96 * se,
                    "ci95_high": beta + 1.96 * se,
                    "normal_approx_p_value": p_value,
                    "observations": result.observations,
                    "country_clusters": result.clusters,
                    "r_squared": result.r_squared,
                    "controls": (
                        "lag internet share, lag log GDP pc, lag outcome, year fixed effects"
                        if include_lag_outcome
                        else "lag internet share, lag log GDP pc, year fixed effects"
                    ),
                    "base_year_omitted": base_year,
                }
            )
    return rows


def fmt(value: object, digits: int = 3) -> str:
    number = safe_float(value)
    if number is None:
        return ""
    return f"{number:.{digits}f}"


def svg_text(x: float, y: float, text: str, **attrs: object) -> str:
    attributes = {"x": x, "y": y, "font-family": "Arial, sans-serif"}
    attributes.update(attrs)
    attr_text = " ".join(f'{key.replace("_", "-")}="{html.escape(str(value))}"' for key, value in attributes.items())
    return f"<text {attr_text}>{html.escape(text)}</text>"


def write_timescale_svg(path: Path, rows: list[dict[str, object]]) -> None:
    plotted = [
        row
        for row in rows
        if safe_float(row.get("median_10_90_traversal_years")) is not None
    ]
    plotted.sort(key=lambda row: float(row["median_10_90_traversal_years"]))
    width = 900
    row_height = 42
    margin_left = 245
    margin_right = 45
    margin_top = 72
    margin_bottom = 56
    chart_width = width - margin_left - margin_right
    height = margin_top + margin_bottom + row_height * len(plotted)
    max_value = max(float(row["median_10_90_traversal_years"]) for row in plotted)
    axis_max = max(10.0, math.ceil(max_value / 5.0) * 5.0)
    colors = ["#2f6fbb", "#319b7b", "#c9822b", "#8b5fbf", "#c84f4f", "#4b8a8f"]
    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        svg_text(
            32,
            34,
            "Observed WDI Timescales",
            font_size=22,
            font_weight=700,
            fill="#18212f",
        ),
        svg_text(
            32,
            56,
            "Median years to traverse 10-90% of each country-specific observed range",
            font_size=13,
            fill="#465366",
        ),
    ]
    for tick in range(0, int(axis_max) + 1, 5):
        x = margin_left + chart_width * tick / axis_max
        elements.append(
            f'<line x1="{x:.1f}" y1="{margin_top - 12}" x2="{x:.1f}" y2="{height - margin_bottom + 4}" stroke="#d9dee8" stroke-width="1"/>'
        )
        elements.append(
            svg_text(x, height - margin_bottom + 28, str(tick), font_size=11, fill="#596579", text_anchor="middle")
        )
    elements.append(
        svg_text(
            margin_left + chart_width / 2,
            height - 10,
            "years",
            font_size=12,
            fill="#596579",
            text_anchor="middle",
        )
    )
    for index, row in enumerate(plotted):
        y = margin_top + index * row_height
        value = float(row["median_10_90_traversal_years"])
        bar_width = chart_width * value / axis_max
        label = str(row["indicator_label"])
        role = str(row["role"])
        color = colors[index % len(colors)]
        elements.append(svg_text(32, y + 18, label, font_size=13, font_weight=700, fill="#18212f"))
        elements.append(svg_text(32, y + 35, role, font_size=11, fill="#667085"))
        elements.append(
            f'<rect x="{margin_left}" y="{y + 8}" width="{bar_width:.1f}" height="20" rx="3" fill="{color}"/>'
        )
        elements.append(
            svg_text(
                margin_left + bar_width + 8,
                y + 23,
                f"{value:.1f}",
                font_size=12,
                font_weight=700,
                fill="#18212f",
            )
        )
    elements.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(elements) + "\n", encoding="utf-8")


def write_alignment_svg(path: Path, rows: list[dict[str, object]]) -> None:
    outcomes = []
    for row in rows:
        slug = str(row["outcome_slug"])
        if slug not in outcomes:
            outcomes.append(slug)
    outcome_labels = {str(row["outcome_slug"]): str(row["outcome_label"]) for row in rows}
    units = {str(row["outcome_slug"]): str(row["dependent_variable_units"]) for row in rows}
    width = 920
    panel_height = 178
    margin_left = 78
    margin_right = 38
    margin_top = 74
    margin_bottom = 42
    height = margin_top + margin_bottom + panel_height * len(outcomes)
    chart_width = width - margin_left - margin_right
    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        svg_text(
            32,
            34,
            "Internet Adoption and Material-Proxy Changes",
            font_size=22,
            font_weight=700,
            fill="#18212f",
        ),
        svg_text(
            32,
            56,
            "OLS coefficients per 10 percentage point internet-user jump, with country-clustered 95% intervals",
            font_size=13,
            fill="#465366",
        ),
    ]
    color = "#2f6fbb"
    horizon_values = sorted({int(row["horizon_years_after_internet_change"]) for row in rows})
    if not horizon_values:
        path.write_text("", encoding="utf-8")
        return
    min_horizon = min(horizon_values)
    max_horizon = max(horizon_values)
    horizon_span = max(1, max_horizon - min_horizon)
    for panel_index_value, outcome in enumerate(outcomes):
        panel_rows = [row for row in rows if row["outcome_slug"] == outcome]
        panel_y = margin_top + panel_index_value * panel_height
        lows = [float(row["ci95_low"]) for row in panel_rows]
        highs = [float(row["ci95_high"]) for row in panel_rows]
        y_min = min(min(lows), 0.0)
        y_max = max(max(highs), 0.0)
        if abs(y_max - y_min) <= EPSILON:
            y_min -= 1.0
            y_max += 1.0
        padding = 0.12 * (y_max - y_min)
        y_min -= padding
        y_max += padding
        chart_top = panel_y + 30
        chart_bottom = panel_y + panel_height - 34
        chart_height = chart_bottom - chart_top

        def x_pos(horizon: int) -> float:
            return margin_left + chart_width * (horizon - min_horizon) / horizon_span

        def y_pos(value: float) -> float:
            return chart_bottom - chart_height * (value - y_min) / (y_max - y_min)

        elements.append(
            svg_text(
                32,
                panel_y + 18,
                f"{outcome_labels[outcome]} ({units[outcome]})",
                font_size=14,
                font_weight=700,
                fill="#18212f",
            )
        )
        zero_y = y_pos(0.0)
        elements.append(
            f'<line x1="{margin_left}" y1="{zero_y:.1f}" x2="{width - margin_right}" y2="{zero_y:.1f}" stroke="#98a2b3" stroke-width="1"/>'
        )
        elements.append(
            f'<line x1="{margin_left}" y1="{chart_top}" x2="{margin_left}" y2="{chart_bottom}" stroke="#d0d5dd" stroke-width="1"/>'
        )
        elements.append(
            f'<line x1="{margin_left}" y1="{chart_bottom}" x2="{width - margin_right}" y2="{chart_bottom}" stroke="#d0d5dd" stroke-width="1"/>'
        )
        elements.append(svg_text(38, y_pos(y_max), f"{y_max:.2g}", font_size=10, fill="#667085"))
        elements.append(svg_text(38, y_pos(y_min), f"{y_min:.2g}", font_size=10, fill="#667085"))
        for horizon in horizon_values:
            x = x_pos(horizon)
            elements.append(
                svg_text(x, chart_bottom + 20, str(horizon), font_size=11, fill="#596579", text_anchor="middle")
            )
        sorted_panel_rows = sorted(panel_rows, key=lambda row: int(row["horizon_years_after_internet_change"]))
        points: list[str] = []
        for row in sorted_panel_rows:
            horizon = int(row["horizon_years_after_internet_change"])
            beta = float(row["coefficient_per_10pp_internet_jump"])
            low = float(row["ci95_low"])
            high = float(row["ci95_high"])
            x = x_pos(horizon)
            y = y_pos(beta)
            y_low = y_pos(low)
            y_high = y_pos(high)
            elements.append(
                f'<line x1="{x:.1f}" y1="{y_low:.1f}" x2="{x:.1f}" y2="{y_high:.1f}" stroke="{color}" stroke-width="2"/>'
            )
            elements.append(
                f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{color}" stroke="#ffffff" stroke-width="1.5"/>'
            )
            points.append(f"{x:.1f},{y:.1f}")
        if len(points) >= 2:
            elements.append(
                f'<polyline points="{" ".join(points)}" fill="none" stroke="{color}" stroke-width="1.6" opacity="0.65"/>'
            )
    elements.append(
        svg_text(
            margin_left + chart_width / 2,
            height - 12,
            "horizon after internet change, years",
            font_size=12,
            fill="#596579",
            text_anchor="middle",
        )
    )
    elements.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(elements) + "\n", encoding="utf-8")


def latest_api_update(indicator_payloads: dict[str, dict[str, Any]]) -> str:
    dates = [
        str(payload.get("metadata", {}).get("lastupdated"))
        for payload in indicator_payloads.values()
        if payload.get("metadata", {}).get("lastupdated")
    ]
    return max(dates) if dates else "unknown"


def markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |"
    body = []
    for row in rows:
        body.append("| " + " | ".join(str(row.get(column, "")) for column in columns) + " |")
    return "\n".join([header, separator, *body])


def build_memo(
    start_year: int,
    end_year: int,
    coverage: list[dict[str, object]],
    timescales: list[dict[str, object]],
    fits: list[dict[str, object]],
    indicator_payloads: dict[str, dict[str, Any]],
) -> str:
    api_update = latest_api_update(indicator_payloads)
    internet_timescale = next(row for row in timescales if row["indicator_slug"] == "internet_users_pct")
    coverage_compact = [
        {
            "indicator": row["indicator_slug"],
            "obs": row["observations"],
            "countries": row["countries"],
            "first": row["first_year"],
            "last": row["last_year"],
        }
        for row in coverage
    ]
    timescale_compact = [
        {
            "indicator": row["indicator_slug"],
            "countries": row["countries_with_10_90_traversal"],
            "median_years": fmt(row.get("median_10_90_traversal_years"), 1),
            "p25": fmt(row.get("p25_10_90_traversal_years"), 1),
            "p75": fmt(row.get("p75_10_90_traversal_years"), 1),
        }
        for row in timescales
    ]
    fit_compact = [
        {
            "outcome": row["outcome_slug"],
            "h": row["horizon_years_after_internet_change"],
            "beta_10pp": fmt(row["coefficient_per_10pp_internet_jump"], 4),
            "se": fmt(row["clustered_standard_error"], 4),
            "ci95": f"[{fmt(row['ci95_low'], 4)}, {fmt(row['ci95_high'], 4)}]",
            "n": row["observations"],
            "clusters": row["country_clusters"],
        }
        for row in fits
        if int(row["horizon_years_after_internet_change"]) in {0, 3, 5}
    ]
    lines = [
        "# Round 1 Modeller Memo: WDI Timescale And Alignment Diagnostic",
        "",
        f"Generated by `python3 scripts/run_empirical_wdi.py` for WDI years `{start_year}-{end_year}`.",
        f"World Bank API metadata reports WDI `lastupdated` = `{api_update}` for the downloaded indicator calls.",
        "",
        "## Purpose",
        "",
        "This is an empirical diagnostic for the paper's singular-limit theory, not a causal estimate. It asks whether a fast-moving digital exposure proxy has visibly different timescales from slower material or demographic proxies, and whether internet-adoption changes are aligned with changes in material proxies.",
        "",
        "## Data",
        "",
        "Source: World Bank World Development Indicators API v2. The pipeline downloads country metadata plus these indicators:",
        "",
        markdown_table(
            coverage_compact,
            ["indicator", "obs", "countries", "first", "last"],
        ),
        "",
        "Raw JSON caches are written under `data/raw/`; cleaned long and wide panels are written under `data/processed/`.",
        "",
        "## Equations",
        "",
        "For internet adoption, define `I_ct` as individuals using the Internet, in percent of population. For consecutive annual observations with remaining non-user gap above 5 percentage points, the annual gap-closure speed is:",
        "",
        "```text",
        "s_ct = max(0, I_c,t+1 - I_ct) / (100 - I_ct).",
        "half_life_ct = log(0.5) / log(1 - s_ct).",
        "```",
        "",
        "The cross-indicator timescale diagnostic is the number of years needed for a country to move from 10% to 90% of its own observed range. GDP per capita is logged for this calculation.",
        "",
        "The alignment fit is a first-difference panel diagnostic:",
        "",
        "```text",
        "Delta_h y_c,t = alpha + beta Delta I_ct + gamma_1 I_c,t-1",
        "              + gamma_2 log GDPpc_c,t-1 + gamma_3 y_c,t-1",
        "              + year fixed effects + error_c,t.",
        "```",
        "",
        "`Delta I_ct` is measured in 10 percentage point jumps. The response `Delta_h y_c,t` is annualized from `t-1` to `t+h`. Standard errors are clustered by country.",
        "For the GDP-per-capita fit, `y_c,t-1` and `log GDPpc_c,t-1` are the same control, so the pipeline includes that lag only once.",
        "",
        "## Exact Findings",
        "",
        f"The median country-level internet remaining-gap half-life is `{fmt(internet_timescale.get('median_remaining_gap_half_life_years'), 2)}` years across `{internet_timescale.get('countries_with_gap_closure')}` countries with usable rising annual pairs.",
        "",
        "Observed 10-90 range traversal times:",
        "",
        markdown_table(
            timescale_compact,
            ["indicator", "countries", "median_years", "p25", "p75"],
        ),
        "",
        "Alignment coefficients, per 10 percentage point internet-adoption jump:",
        "",
        markdown_table(
            fit_compact,
            ["outcome", "h", "beta_10pp", "se", "ci95", "n", "clusters"],
        ),
        "",
        "## Interpretation",
        "",
        "The diagnostic supports using timescale separation as an empirical object rather than an assumption. Internet adoption moves on a visibly fast macro timescale in the WDI panel. Material and demographic proxies are more persistent by the observed-range measure, although GDP growth can move sharply in crises.",
        "",
        "The alignment results should be read as signs and magnitudes conditional on controls, not causal effects. Positive coefficients for GDP or life expectancy would be consistent with alignment between digital expansion and material proxies. Fertility is a demographic adjustment variable rather than a welfare measure; suicide mortality is an adverse proxy, so negative coefficients are directionally favorable but still not causal. Mixed or imprecise coefficients are evidence against a universal claim that fast preference-generating exposure is automatically material-welfare improving or destroying.",
        "",
        "## Identification Limits",
        "",
        "- Internet use is an exposure/infrastructure proxy, not a direct preference-state observation.",
        "- First differences remove time-invariant country levels but not policy shocks, business cycles, wars, health shocks, or endogenous rollout.",
        "- Year fixed effects absorb common global shocks, but country-specific trends remain a concern.",
        "- WDI country aggregates are macro diagnostics and cannot identify individual preference closure.",
        "- The estimates are suitable as calibration targets and motivation for the theory article, not as proof of the platform-control mechanism.",
        "",
        "## Outputs",
        "",
        "- `data/processed/wdi_empirical_long.csv`",
        "- `data/processed/wdi_empirical_panel.csv`",
        "- `results/tables/empirical_wdi_coverage.csv`",
        "- `results/tables/empirical_wdi_country_gap_closure.csv`",
        "- `results/tables/empirical_wdi_timescales.csv`",
        "- `results/tables/empirical_wdi_alignment_fits.csv`",
        "- `results/figures/empirical_wdi_timescales.svg`",
        "- `results/figures/empirical_wdi_alignment_coefficients.svg`",
    ]
    return "\n".join(lines) + "\n"


def run_pipeline(
    root: Path,
    start_year: int = DEFAULT_START_YEAR,
    end_year: int = DEFAULT_END_YEAR,
    refresh: bool = False,
) -> dict[str, Path]:
    raw_dir = root / "data/raw"
    processed_dir = root / "data/processed"
    tables_dir = root / "results/tables"
    figures_dir = root / "results/figures"
    docs_dir = root / "docs/agent_rounds"

    country_payload = fetch_countries(raw_dir, refresh=refresh)
    countries = valid_countries(country_payload)
    indicator_payloads = {
        spec.code: fetch_indicator(spec, raw_dir, start_year, end_year, refresh=refresh)
        for spec in INDICATORS
    }
    long_rows = build_long_rows(indicator_payloads, countries)
    panel_rows = build_panel_rows(long_rows)
    coverage = coverage_rows(long_rows)
    gap_rows = internet_gap_closure_rows(panel_rows)
    timescales = timescale_rows(panel_rows, gap_rows)
    fits = fit_alignment(panel_rows)

    long_path = processed_dir / "wdi_empirical_long.csv"
    panel_path = processed_dir / "wdi_empirical_panel.csv"
    coverage_path = tables_dir / "empirical_wdi_coverage.csv"
    gap_path = tables_dir / "empirical_wdi_country_gap_closure.csv"
    timescale_path = tables_dir / "empirical_wdi_timescales.csv"
    fits_path = tables_dir / "empirical_wdi_alignment_fits.csv"
    timescale_svg = figures_dir / "empirical_wdi_timescales.svg"
    alignment_svg = figures_dir / "empirical_wdi_alignment_coefficients.svg"
    memo_path = docs_dir / "round_1_modeller.md"

    write_csv(long_path, long_rows)
    write_csv(panel_path, panel_rows)
    write_csv(coverage_path, coverage)
    write_csv(gap_path, gap_rows)
    write_csv(timescale_path, timescales)
    write_csv(fits_path, fits)
    write_timescale_svg(timescale_svg, timescales)
    write_alignment_svg(alignment_svg, fits)
    memo_path.parent.mkdir(parents=True, exist_ok=True)
    memo_path.write_text(
        build_memo(start_year, end_year, coverage, timescales, fits, indicator_payloads),
        encoding="utf-8",
    )

    manifest_path = raw_dir / "wdi_manifest.json"
    manifest = {
        "generated_utc": datetime.now(UTC).isoformat(),
        "start_year": start_year,
        "end_year": end_year,
        "world_bank_api": WORLD_BANK_API,
        "indicator_codes": [spec.code for spec in INDICATORS],
        "wdi_lastupdated": latest_api_update(indicator_payloads),
        "raw_files": [
            str(raw_indicator_path(raw_dir, spec.code, start_year, end_year).relative_to(root))
            for spec in INDICATORS
        ],
    }
    write_json(manifest_path, manifest)

    return {
        "long": long_path,
        "panel": panel_path,
        "coverage": coverage_path,
        "gap_closure": gap_path,
        "timescales": timescale_path,
        "fits": fits_path,
        "timescale_svg": timescale_svg,
        "alignment_svg": alignment_svg,
        "memo": memo_path,
        "manifest": manifest_path,
    }
