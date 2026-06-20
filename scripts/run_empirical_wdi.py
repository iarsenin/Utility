#!/usr/bin/env python3
"""Run the WDI empirical timescale/alignment diagnostic."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from utility_endogenous.empirical_wdi import DEFAULT_END_YEAR, DEFAULT_START_YEAR, run_pipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-year", type=int, default=DEFAULT_START_YEAR)
    parser.add_argument("--end-year", type=int, default=DEFAULT_END_YEAR)
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="redownload raw World Bank API JSON instead of using cached files",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    paths = run_pipeline(
        ROOT,
        start_year=args.start_year,
        end_year=args.end_year,
        refresh=args.refresh,
    )
    for label, path in paths.items():
        print(f"Wrote {label}: {path}")


if __name__ == "__main__":
    main()
