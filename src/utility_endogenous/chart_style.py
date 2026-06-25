"""Shared SVG chart style for the working paper.

The visual direction is an original publication style: warm paper,
high-contrast typography, a restrained red editorial accent, and semantic colors
that remain legible when printed.
"""

from __future__ import annotations

import html


CHART_BG = "#fffaf2"
CHART_PANEL = "#ffffff"
CHART_INK = "#171411"
CHART_MUTED = "#5f5a52"
CHART_AXIS = "#756f66"
CHART_GRID = "#e7dfd3"
CHART_ACCENT = "#d5412f"
CHART_TEAL = "#007f83"
CHART_AMBER = "#c7831f"
CHART_BLUE = "#3867a6"
CHART_RED = "#c74332"
CHART_VIOLET = "#7658a5"
CHART_GREEN = "#5e883a"
CHART_FONT = 'Inter, "Helvetica Neue", Arial, sans-serif'


def svg_text(x: float, y: float, text: str, **attrs: object) -> str:
    attributes = {"x": x, "y": y, "font-family": CHART_FONT}
    attributes.update(attrs)
    attr_text = " ".join(
        f'{key.replace("_", "-")}="{html.escape(str(value))}"'
        for key, value in attributes.items()
    )
    return f"<text {attr_text}>{html.escape(text)}</text>"


def svg_open(width: int, height: int) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        f'<rect width="100%" height="100%" fill="{CHART_BG}"/>',
        f'<rect x="18" y="18" width="{width - 36}" height="{height - 36}" rx="0" fill="{CHART_PANEL}" stroke="#eadfce"/>',
        f'<line x1="18" y1="18" x2="{width - 18}" y2="18" stroke="{CHART_ACCENT}" stroke-width="5"/>',
    ]


def chart_header(title: str, subtitle: str, width: int) -> list[str]:
    return [
        svg_text(36, 44, title, font_size=22, font_weight=800, fill=CHART_INK),
        svg_text(36, 68, subtitle, font_size=13, fill=CHART_MUTED),
        f'<line x1="36" y1="82" x2="{width - 36}" y2="82" stroke="{CHART_GRID}" stroke-width="1"/>',
    ]


def chart_footer(note: str, width: int, height: int) -> str:
    return svg_text(36, height - 22, note, font_size=10.5, fill=CHART_MUTED)
