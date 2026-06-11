"""NYSE trading calendar and "latest completed trading day" resolution.

Standard library only: OpenClaw hosts and GitHub Actions helper steps import
this module without installing pandas.

Covers regular NYSE full-day holidays with observed-date rules and is correct
across US daylight-saving transitions because all market-time decisions happen
in America/New_York. Ad-hoc closures (e.g. national days of mourning) are not
modelled; the weekly workflow's freshness check is the backstop for those.
"""

from __future__ import annotations

import os
from datetime import UTC, date, datetime, time, timedelta
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

DEFAULT_TIMEZONE = "Asia/Shanghai"
MARKET_TIMEZONE = "America/New_York"
MARKET_CLOSE = time(16, 0)


def easter_sunday(year: int) -> date:
    """Gregorian Easter via the Anonymous Gregorian algorithm."""

    a = year % 19
    b, c = divmod(year, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    le = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * le) // 451
    month, day = divmod(h + le - 7 * m + 114, 31)
    return date(year, month, day + 1)


def _nth_weekday(year: int, month: int, weekday: int, n: int) -> date:
    first = date(year, month, 1)
    offset = (weekday - first.weekday()) % 7
    return first + timedelta(days=offset + 7 * (n - 1))


def _last_weekday(year: int, month: int, weekday: int) -> date:
    next_month = date(year + (month == 12), month % 12 + 1, 1)
    last = next_month - timedelta(days=1)
    return last - timedelta(days=(last.weekday() - weekday) % 7)


def _observed(holiday: date) -> date | None:
    if holiday.weekday() == 5:  # Saturday -> preceding Friday
        observed = holiday - timedelta(days=1)
        # NYSE rule: no observance when it would land in the prior year
        # (e.g. 2022-01-01 was a Saturday and the market opened 2021-12-31).
        return observed if observed.year == holiday.year else None
    if holiday.weekday() == 6:  # Sunday -> following Monday
        return holiday + timedelta(days=1)
    return holiday


def nyse_holidays(year: int) -> set[date]:
    fixed = [date(year, 1, 1), date(year, 7, 4), date(year, 12, 25)]
    if year >= 2022:  # Juneteenth became a NYSE holiday in 2022.
        fixed.append(date(year, 6, 19))

    holidays: set[date] = set()
    for holiday in fixed:
        observed = _observed(holiday)
        if observed is not None:
            holidays.add(observed)

    holidays.add(_nth_weekday(year, 1, 0, 3))  # Martin Luther King Jr. Day
    holidays.add(_nth_weekday(year, 2, 0, 3))  # Washington's Birthday
    holidays.add(easter_sunday(year) - timedelta(days=2))  # Good Friday
    holidays.add(_last_weekday(year, 5, 0))  # Memorial Day
    holidays.add(_nth_weekday(year, 9, 0, 1))  # Labor Day
    holidays.add(_nth_weekday(year, 11, 3, 4))  # Thanksgiving
    return holidays


def is_trading_day(value: date) -> bool:
    return value.weekday() < 5 and value not in nyse_holidays(value.year)


def previous_trading_day(value: date) -> date:
    candidate = value - timedelta(days=1)
    while not is_trading_day(candidate):
        candidate -= timedelta(days=1)
    return candidate


def latest_completed_trading_day(now: datetime | None = None) -> date:
    """Most recent US trading day whose regular session has already closed.

    DST-safe: the comparison happens in America/New_York wall time, so the
    16:00 close is correct in both EST and EDT.
    """

    moment = now or datetime.now(UTC)
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=UTC)
    eastern = moment.astimezone(ZoneInfo(MARKET_TIMEZONE))
    candidate = eastern.date()
    if is_trading_day(candidate) and eastern.time() >= MARKET_CLOSE:
        return candidate
    return previous_trading_day(candidate)


def expected_weekly_as_of(now: datetime | None = None) -> date:
    """The as_of date the scheduled Saturday run must use."""

    return latest_completed_trading_day(now)


def week_key(value: date) -> str:
    iso = value.isocalendar()
    return f"{iso.year}-W{iso.week:02d}"


def most_recent_schedule_start(now: datetime | None = None) -> datetime:
    """Most recent Saturday 00:00 UTC (the weekly cron trigger) at or before now."""

    moment = now or datetime.now(UTC)
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=UTC)
    moment = moment.astimezone(UTC)
    days_since_saturday = (moment.weekday() - 5) % 7
    start = (moment - timedelta(days=days_since_saturday)).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    return start


def parse_date(value: str | date | None) -> date:
    if value is None:
        return latest_completed_trading_day()
    if isinstance(value, date):
        return value
    return datetime.strptime(value, "%Y-%m-%d").date()


def configured_timezone() -> ZoneInfo:
    name = (
        os.environ.get("WEEKLY_US_STOCK_TIMEZONE")
        or os.environ.get("TZ")
        or DEFAULT_TIMEZONE
    )
    try:
        return ZoneInfo(name)
    except ZoneInfoNotFoundError:
        return ZoneInfo(DEFAULT_TIMEZONE)
