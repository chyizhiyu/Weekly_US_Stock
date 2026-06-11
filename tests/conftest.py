from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from weekly_us_stock.config import Settings, load_settings, project_root
from weekly_us_stock.models.screening import PipelineRequest
from weekly_us_stock.pipeline import WeeklyUSStockPipeline
from weekly_us_stock.providers.sample import SampleDataProvider

AS_OF = date(2026, 1, 9)  # canonical sample-data Friday
NEXT_AS_OF = date(2026, 1, 16)  # following Friday, used for week-over-week tests


@pytest.fixture(scope="session")
def settings(tmp_path_factory: pytest.TempPathFactory) -> Settings:
    loaded = load_settings()
    loaded.app.output_dir = str(tmp_path_factory.mktemp("runs"))
    return loaded


@pytest.fixture(scope="session")
def sample_provider() -> SampleDataProvider:
    return SampleDataProvider(project_root() / "data" / "samples")


@pytest.fixture(scope="session")
def pipeline_runs(settings: Settings) -> dict[str, Path]:
    """Run the offline pipeline for two consecutive weeks once per session."""

    pipeline = WeeklyUSStockPipeline(settings=settings)
    pipeline.run(PipelineRequest(as_of=AS_OF, provider="sample"))
    pipeline.run(PipelineRequest(as_of=NEXT_AS_OF, provider="sample"))
    output_dir = Path(settings.app.output_dir)
    return {
        "first": output_dir / AS_OF.strftime("%Y%m%d"),
        "second": output_dir / NEXT_AS_OF.strftime("%Y%m%d"),
    }
