#!/usr/bin/env python3
"""Run a route-agnostic audit of candidate model classes."""

from __future__ import annotations

import csv
from dataclasses import asdict
import html
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from utility_endogenous.model_selection_audit import RouteSummary, run_model_selection_audit


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


def fmt(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |"
    body = [
        "| " + " | ".join(fmt(row.get(column)) for column in columns) + " |"
        for row in rows
    ]
    return "\n".join([header, separator, *body])


def svg_text(x: float, y: float, text: str, **attrs: object) -> str:
    attributes = {"x": x, "y": y, "font-family": "Arial, sans-serif"}
    attributes.update(attrs)
    attr_text = " ".join(
        f'{key.replace("_", "-")}="{html.escape(str(value))}"'
        for key, value in attributes.items()
    )
    return f"<text {attr_text}>{html.escape(text)}</text>"


def write_model_selection_svg(path: Path, summaries: list[RouteSummary]) -> None:
    rows: list[dict[str, object]] = []
    for summary in summaries:
        if summary.route in {"neutral_control", "strategic_random_distortion"}:
            rows.append(
                {
                    "label": "Neutral control",
                    "route": summary.route,
                    "metric": "Equilibrium shift rate",
                    "value": summary.equilibrium_shift_rate,
                    "color": "#319b7b",
                }
                if summary.route == "neutral_control"
                else {
                    "label": "Random strategic closure",
                    "route": summary.route,
                    "metric": "Equilibrium shift rate",
                    "value": summary.equilibrium_shift_rate,
                    "color": "#c9822b",
                }
            )
        elif summary.route.startswith("proxy_"):
            rows.append(
                {
                    "label": summary.route.replace("proxy_", "Proxy "),
                    "route": summary.route,
                    "metric": "Material loss rate",
                    "value": summary.proxy_material_loss_rate,
                    "color": {
                        "proxy_aligned": "#319b7b",
                        "proxy_independent": "#c9822b",
                        "proxy_misaligned": "#c84f4f",
                    }[summary.route],
                }
            )

    plotted = [row for row in rows if isinstance(row["value"], float)]
    width = 920
    margin_left = 250
    margin_right = 64
    margin_top = 82
    margin_bottom = 66
    row_height = 54
    chart_width = width - margin_left - margin_right
    height = margin_top + margin_bottom + row_height * len(plotted)
    axis_max = 1.0
    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        svg_text(
            32,
            34,
            "Finite-Game Fast-Closure Audit",
            font_size=22,
            font_weight=700,
            fill="#18212f",
        ),
        svg_text(
            32,
            58,
            "5,000 random two-player games per route; neutral route is the sanity control",
            font_size=13,
            fill="#465366",
        ),
    ]
    for tick in [0.0, 0.25, 0.5, 0.75, 1.0]:
        x = margin_left + chart_width * tick / axis_max
        elements.append(
            f'<line x1="{x:.1f}" y1="{margin_top - 14}" x2="{x:.1f}" y2="{height - margin_bottom + 4}" stroke="#d9dee8" stroke-width="1"/>'
        )
        elements.append(
            svg_text(
                x,
                height - margin_bottom + 30,
                f"{tick:.2f}".rstrip("0").rstrip("."),
                font_size=11,
                fill="#596579",
                text_anchor="middle",
            )
        )
    for index, row in enumerate(plotted):
        y = margin_top + index * row_height
        value = float(row["value"])
        bar_width = chart_width * value / axis_max
        label = str(row["label"]).replace("_", " ").title()
        metric = str(row["metric"])
        color = str(row["color"])
        elements.append(svg_text(32, y + 19, label, font_size=13, font_weight=700, fill="#18212f"))
        elements.append(svg_text(32, y + 38, metric, font_size=11, fill="#667085"))
        elements.append(
            f'<rect x="{margin_left}" y="{y + 10}" width="{max(bar_width, 1):.1f}" height="24" rx="3" fill="{color}"/>'
        )
        label_x = min(margin_left + bar_width + 10, width - margin_right - 36)
        elements.append(
            svg_text(
                label_x,
                y + 27,
                f"{value:.3f}",
                font_size=12,
                font_weight=700,
                fill="#18212f",
            )
        )
    elements.append(
        svg_text(
            margin_left + chart_width / 2,
            height - 12,
            "rate",
            font_size=12,
            fill="#596579",
            text_anchor="middle",
        )
    )
    elements.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(elements) + "\n", encoding="utf-8")


def build_report(summaries: list[RouteSummary], games: int, seed: int) -> str:
    rows = [asdict(summary) for summary in summaries]
    by_route = {summary.route: summary for summary in summaries}
    strategic = by_route["strategic_random_distortion"]
    aligned = by_route["proxy_aligned"]
    independent = by_route["proxy_independent"]
    misaligned = by_route["proxy_misaligned"]

    lines = [
        "# Model Selection Audit",
        "",
        f"Generated by `python3 scripts/run_model_selection_audit.py` with seed `{seed}` and `{games}` random finite games per route.",
        "",
        "## Purpose",
        "",
        "This is a deliberately different check from the one-dimensional taste and platform simulations. It treats the fast preference limit as a payoff transformation in random two-player, two-action games. The goal is to see which qualitative predictions are generic, which require platform-specific structure, and which disappear under neutral controls.",
        "",
        "## Routes Tested",
        "",
        "- `neutral_control`: preferences move, but only by terms that are strategically irrelevant for best responses.",
        "- `strategic_random_distortion`: fast preference closure adds a random strategic payoff distortion.",
        "- `proxy_aligned`: the institution-induced proxy is close to material welfare.",
        "- `proxy_independent`: the proxy is unrelated to material welfare.",
        "- `proxy_misaligned`: the proxy is approximately the negative of material welfare.",
        "",
        "For proxy routes, each adaptation law is a value of `lambda` in `[0, 0.25, 0.75, 1.5, 3.0]`; agents play a Nash equilibrium of the fast-adapted subjective game; the platform selects the law with the highest proxy value; material selection would select the law with the highest material payoff.",
        "",
        "## Summary",
        "",
        markdown_table(
            rows,
            [
                "route",
                "games",
                "br_invariance_rate",
                "pure_br_invariance_rate",
                "equilibrium_shift_rate",
                "proxy_material_loss_rate",
                "proxy_gain_material_loss_rate",
                "all_regimes_negative_rate",
                "mean_material_loss_when_proxy_wins",
                "median_material_loss_when_proxy_wins",
            ],
        ),
        "",
        "## Readout",
        "",
        f"- Neutral preference movement preserved mixed best-response correspondences in `{fmt(by_route['neutral_control'].br_invariance_rate)}` of games, which is the intended sanity check.",
        f"- Random strategic preference closure changed the selected equilibrium in `{fmt(strategic.equilibrium_shift_rate)}` of games and preserved mixed best-response correspondences in only `{fmt(strategic.br_invariance_rate)}` of games.",
        f"- The older pure-action endpoint check gives `{fmt(strategic.pure_br_invariance_rate)}` for random strategic closure; this is weaker than the all-mixed condition in Proposition 1 and should not be described as full best-response invariance.",
        f"- When the proxy was aligned with material welfare, the platform-selected law lost material payoff in `{fmt(aligned.proxy_material_loss_rate)}` of games.",
        f"- When the proxy was independent, material loss occurred in `{fmt(independent.proxy_material_loss_rate)}` of games, so a loss result does not require an explicitly anti-material proxy.",
        f"- When the proxy was misaligned, material loss occurred in `{fmt(misaligned.proxy_material_loss_rate)}` of games; this is the route closest to the current one-dimensional platform model.",
        "",
        "## Implication For Model Choice",
        "",
        "The finite-game route should become the central theorem route. It is closer to the indirect evolutionary preference literature and avoids baking in a one-dimensional survival frontier. The current platform-control model remains valuable, but as an application that adds a proxy-choice mechanism and empirical content about whether engagement is aligned, independent, or misaligned with material welfare.",
        "",
        "The one-dimensional taste model should be demoted to an exposition and visualization model. It is too easy to make the conclusion true by choosing monotone exposure and monotone material harm. The Prisoner's Dilemma model should remain as a bridge to indirect evolutionary preferences. Cultural-transmission and OLG models should wait until the singular-limit theorem is settled, because they are naturally medium- and long-run models rather than the cleanest `T_P -> 0` laboratory.",
        "",
        "## The Non-Trivial Check",
        "",
        "The strongest check is the aligned-proxy control. If the platform proxy is close to material welfare, the bad result weakens; if the proxy is independent or misaligned, the bad result strengthens. That means the paper should not claim that fast endogenous preferences mechanically imply collapse. The qualitative prediction should be conditional:",
        "",
        "```text",
        "Fast preference closure changes the game generically.",
        "Material harm depends on the alignment between the preference-generating proxy and material welfare.",
        "Selection acts on adaptation laws or institutions after closure, not on initial preference states.",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    games = 5000
    seed = 20260620
    summaries, proxy_rows = run_model_selection_audit(games=games, seed=seed)

    results_dir = ROOT / "results"
    tables_dir = results_dir / "tables"
    figures_dir = results_dir / "figures"
    summary_rows = [asdict(summary) for summary in summaries]
    write_csv(tables_dir / "model_selection_summary.csv", summary_rows)
    write_csv(tables_dir / "model_selection_proxy_routes.csv", proxy_rows)
    write_model_selection_svg(figures_dir / "model_selection_fast_closure_audit.svg", summaries)
    report = build_report(summaries, games, seed)
    (results_dir / "model_selection_audit_report.md").write_text(report, encoding="utf-8")

    print(f"Wrote {results_dir / 'model_selection_audit_report.md'}")
    print(f"Wrote {tables_dir / 'model_selection_summary.csv'}")
    print(f"Wrote {tables_dir / 'model_selection_proxy_routes.csv'}")
    print(f"Wrote {figures_dir / 'model_selection_fast_closure_audit.svg'}")


if __name__ == "__main__":
    main()
