from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from weekly_us_stock.config import load_settings
from weekly_us_stock.logging import configure_logging
from weekly_us_stock.models.screening import DataNotReadyError, PipelineRequest
from weekly_us_stock.pipeline import WeeklyUSStockPipeline
from weekly_us_stock.utils.calendar import expected_weekly_as_of, parse_date

app = typer.Typer(help="Weekly US stock screener. Research and reports only; no trading.")

# Exit code asking the caller (GitHub Actions retry loop) to try again later.
EXIT_DATA_NOT_READY = 75


@app.callback()
def main() -> None:
    """Weekly US Stock command group."""


@app.command()
def run(
    as_of: Annotated[
        str | None,
        typer.Option(
            "--as-of",
            help="Market data date YYYY-MM-DD; defaults to the latest completed US trading day.",
        ),
    ] = None,
    provider: Annotated[
        str | None,
        typer.Option("--provider", help="Data source override: sample | fmp | auto."),
    ] = None,
    config: Annotated[
        Path | None,
        typer.Option("--config", help="Path to YAML config."),
    ] = None,
    strict_freshness: Annotated[
        bool,
        typer.Option(
            "--strict-freshness/--no-strict-freshness",
            help=f"Exit with code {EXIT_DATA_NOT_READY} when price data has not caught up yet.",
        ),
    ] = False,
    previous_dir: Annotated[
        str | None,
        typer.Option(
            "--previous-dir",
            help="Directory holding last week's rankings for the week-over-week diff.",
        ),
    ] = None,
    limit: Annotated[
        int | None,
        typer.Option(
            "--limit",
            help="Smoke testing only: keep the N largest universe names.",
        ),
    ] = None,
) -> None:
    configure_logging()
    settings = load_settings(config)
    request = PipelineRequest(
        as_of=parse_date(as_of),
        provider=provider,
        strict_freshness=strict_freshness,
        previous_dir=previous_dir,
        limit=limit,
    )
    pipeline = WeeklyUSStockPipeline(settings=settings)
    try:
        result = pipeline.run(request)
    except DataNotReadyError as exc:
        typer.echo(f"Data not ready: {exc}", err=True)
        raise typer.Exit(code=EXIT_DATA_NOT_READY) from exc

    dashboard = next(path for path in result.artifacts if path.endswith("dashboard.md"))
    typer.echo(
        f"Weekly US Stock run complete: {len(result.robust_top)} ranked names, "
        f"{len(result.watchlist)} watchlisted"
    )
    typer.echo(f"Dashboard: {dashboard}")


@app.command("expected-as-of")
def expected_as_of_command() -> None:
    """Print the as_of date the current weekly run should use."""

    typer.echo(expected_weekly_as_of().isoformat())


if __name__ == "__main__":
    app()
