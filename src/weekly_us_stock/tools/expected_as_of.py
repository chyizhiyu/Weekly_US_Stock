"""Print the as_of date the current weekly run must use.

Usage: PYTHONPATH=src python3 -m weekly_us_stock.tools.expected_as_of
"""

from __future__ import annotations

from weekly_us_stock.utils.calendar import expected_weekly_as_of


def main() -> None:
    print(expected_weekly_as_of().isoformat())


if __name__ == "__main__":
    main()
