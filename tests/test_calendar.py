"""US holidays, DST transitions and latest-completed-trading-day resolution."""

from __future__ import annotations

from datetime import UTC, date, datetime

from weekly_us_stock.utils.calendar import (
    easter_sunday,
    expected_weekly_as_of,
    is_trading_day,
    latest_completed_trading_day,
    most_recent_schedule_start,
    nyse_holidays,
    previous_trading_day,
    week_key,
)


class TestHolidays:
    def test_good_friday_2026(self) -> None:
        assert easter_sunday(2026) == date(2026, 4, 5)
        assert date(2026, 4, 3) in nyse_holidays(2026)
        assert not is_trading_day(date(2026, 4, 3))

    def test_independence_day_2026_saturday_observed_friday(self) -> None:
        holidays = nyse_holidays(2026)
        assert date(2026, 7, 3) in holidays
        assert date(2026, 7, 4) not in holidays

    def test_new_years_2022_on_saturday_not_observed(self) -> None:
        # NYSE did not close on 2021-12-31 even though 2022-01-01 was Saturday.
        assert date(2021, 12, 31) not in nyse_holidays(2021)
        assert date(2021, 12, 31) not in nyse_holidays(2022)
        assert is_trading_day(date(2021, 12, 31))

    def test_juneteenth_only_from_2022(self) -> None:
        assert date(2026, 6, 19) in nyse_holidays(2026)
        assert date(2021, 6, 18) not in nyse_holidays(2021)
        assert date(2021, 6, 19) not in nyse_holidays(2021)

    def test_floating_holidays_2026(self) -> None:
        holidays = nyse_holidays(2026)
        assert date(2026, 1, 19) in holidays  # MLK: 3rd Monday of January
        assert date(2026, 2, 16) in holidays  # Washington's Birthday
        assert date(2026, 5, 25) in holidays  # Memorial Day
        assert date(2026, 9, 7) in holidays  # Labor Day
        assert date(2026, 11, 26) in holidays  # Thanksgiving

    def test_weekend_not_trading(self) -> None:
        assert not is_trading_day(date(2026, 1, 10))
        assert not is_trading_day(date(2026, 1, 11))
        assert is_trading_day(date(2026, 1, 9))


class TestLatestCompletedTradingDay:
    def test_saturday_run_in_winter_est(self) -> None:
        # Saturday 00:00 UTC == Friday 19:00 EST: Friday session has closed.
        now = datetime(2026, 1, 10, 0, 0, tzinfo=UTC)
        assert latest_completed_trading_day(now) == date(2026, 1, 9)

    def test_saturday_run_in_summer_edt(self) -> None:
        # Saturday 00:00 UTC == Friday 20:00 EDT: still resolves to Friday.
        now = datetime(2026, 7, 11, 0, 0, tzinfo=UTC)
        assert latest_completed_trading_day(now) == date(2026, 7, 10)

    def test_friday_holiday_falls_back_to_thursday(self) -> None:
        # 2026-04-03 is Good Friday; the Saturday run must use Thursday.
        now = datetime(2026, 4, 4, 0, 0, tzinfo=UTC)
        assert latest_completed_trading_day(now) == date(2026, 4, 2)

    def test_midweek_before_close_uses_previous_day(self) -> None:
        # Wednesday 18:00 UTC == 13:00 EST, market still open.
        now = datetime(2026, 1, 7, 18, 0, tzinfo=UTC)
        assert latest_completed_trading_day(now) == date(2026, 1, 6)

    def test_midweek_after_close_uses_same_day(self) -> None:
        now = datetime(2026, 1, 7, 22, 0, tzinfo=UTC)
        assert latest_completed_trading_day(now) == date(2026, 1, 7)

    def test_monday_holiday_walks_back_to_friday(self) -> None:
        # MLK Monday 2026-01-19: Tuesday pre-open resolves to the prior Friday.
        now = datetime(2026, 1, 20, 12, 0, tzinfo=UTC)
        assert latest_completed_trading_day(now) == date(2026, 1, 16)

    def test_expected_weekly_as_of_matches(self) -> None:
        now = datetime(2026, 1, 10, 0, 5, tzinfo=UTC)
        assert expected_weekly_as_of(now) == date(2026, 1, 9)


class TestScheduleWindow:
    def test_saturday_just_after_trigger(self) -> None:
        now = datetime(2026, 1, 10, 0, 5, tzinfo=UTC)
        assert most_recent_schedule_start(now) == datetime(2026, 1, 10, 0, 0, tzinfo=UTC)

    def test_friday_belongs_to_previous_window(self) -> None:
        now = datetime(2026, 1, 9, 23, 59, tzinfo=UTC)
        assert most_recent_schedule_start(now) == datetime(2026, 1, 3, 0, 0, tzinfo=UTC)


def test_previous_trading_day_skips_weekend_and_holiday() -> None:
    assert previous_trading_day(date(2026, 1, 12)) == date(2026, 1, 9)
    assert previous_trading_day(date(2026, 4, 4)) == date(2026, 4, 2)


def test_week_key() -> None:
    assert week_key(date(2026, 1, 9)) == "2026-W02"
