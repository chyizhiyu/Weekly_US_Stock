"""GitHub Actions configuration: schedule timezone and CI gates."""

from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

import yaml

from weekly_us_stock.config import project_root


def _load(name: str) -> dict:
    payload = yaml.safe_load(
        (project_root() / ".github" / "workflows" / name).read_text(encoding="utf-8")
    )
    # Unquoted `on:` parses as boolean True in YAML 1.1.
    triggers = payload.get("on", payload.get(True, {}))
    return {"workflow": payload, "on": triggers}


def test_weekly_cron_is_saturday_0800_beijing() -> None:
    triggers = _load("weekly_run.yml")["on"]
    crons = [entry["cron"] for entry in triggers["schedule"]]
    assert crons == ["0 0 * * 6"]

    # Prove the conversion: Saturday 00:00 UTC == Saturday 08:00 Asia/Shanghai.
    utc_fire = datetime(2026, 1, 10, 0, 0, tzinfo=ZoneInfo("UTC"))
    beijing = utc_fire.astimezone(ZoneInfo("Asia/Shanghai"))
    assert beijing.weekday() == 5  # Saturday
    assert (beijing.hour, beijing.minute) == (8, 0)


def test_weekly_workflow_supports_openclaw_tag_trigger() -> None:
    triggers = _load("weekly_run.yml")["on"]
    assert "weekly-us-stock-*" in triggers["push"]["tags"]
    assert "workflow_dispatch" in triggers


def test_weekly_workflow_publishes_results_branch() -> None:
    workflow = _load("weekly_run.yml")["workflow"]
    text = yaml.dump(workflow)
    assert "weekly-us-stock-results" in text
    assert "history/$RUN_KEY" in text
    assert "latest" in text


def test_weekly_workflow_retries_when_data_not_ready() -> None:
    workflow = _load("weekly_run.yml")["workflow"]
    steps = workflow["jobs"]["full-market-screen"]["steps"]
    run_step = next(step for step in steps if "data-readiness retries" in step.get("name", ""))
    assert "--strict-freshness" in run_step["run"]
    assert "75" in run_step["run"]  # the try-again-later exit code
    assert "sleep" in run_step["run"]


def test_ci_runs_ruff_and_pytest_and_offline_smoke() -> None:
    workflow = _load("ci.yml")["workflow"]
    commands = "\n".join(
        step.get("run", "") for step in workflow["jobs"]["test"]["steps"]
    )
    assert "ruff check ." in commands
    assert "pytest" in commands
    assert "--provider sample" in commands
