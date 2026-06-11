"""Week-over-week comparison against the previous published rankings."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class WeekOverWeek:
    previous_as_of: str | None = None
    robust_entered: list[str] = field(default_factory=list)
    robust_exited: list[str] = field(default_factory=list)
    upside_entered: list[str] = field(default_factory=list)
    upside_exited: list[str] = field(default_factory=list)
    robust_rank_changes: pd.DataFrame = field(default_factory=pd.DataFrame)

    @property
    def has_previous(self) -> bool:
        return self.previous_as_of is not None


def find_previous_run_dir(output_dir: Path, current_key: str) -> Path | None:
    """Latest runs/YYYYMMDD directory strictly before the current run."""

    if not output_dir.exists():
        return None
    candidates = sorted(
        entry
        for entry in output_dir.iterdir()
        if entry.is_dir() and entry.name.isdigit() and entry.name < current_key
    )
    return candidates[-1] if candidates else None


def compare_with_previous(
    robust: pd.DataFrame,
    upside: pd.DataFrame,
    previous_dir: Path | None,
    top_n: int,
) -> WeekOverWeek:
    if previous_dir is None:
        return WeekOverWeek()
    previous_robust = _read_ranking(previous_dir / "robust_ranking.csv")
    previous_upside = _read_ranking(previous_dir / "upside_ranking.csv")
    if previous_robust is None or previous_upside is None:
        logger.info("Previous run at %s lacks ranking files; treating as first run", previous_dir)
        return WeekOverWeek()

    previous_as_of = _previous_as_of(previous_dir, previous_robust)

    current_top = _top_tickers(robust, top_n)
    previous_top = _top_tickers(previous_robust, top_n)
    upside_current_top = _top_tickers(upside, top_n)
    upside_previous_top = _top_tickers(previous_upside, top_n)

    changes = _rank_changes(robust, previous_robust)

    return WeekOverWeek(
        previous_as_of=previous_as_of,
        robust_entered=sorted(current_top - previous_top),
        robust_exited=sorted(previous_top - current_top),
        upside_entered=sorted(upside_current_top - upside_previous_top),
        upside_exited=sorted(upside_previous_top - upside_current_top),
        robust_rank_changes=changes,
    )


def _read_ranking(path: Path) -> pd.DataFrame | None:
    if not path.exists():
        return None
    try:
        return pd.read_csv(path)
    except Exception:
        logger.exception("Failed to read previous ranking %s", path)
        return None


def _previous_as_of(previous_dir: Path, robust: pd.DataFrame) -> str:
    metadata_path = previous_dir / "run_metadata.json"
    if metadata_path.exists():
        import json

        try:
            return str(json.loads(metadata_path.read_text(encoding="utf-8")).get("as_of"))
        except Exception:
            pass
    name = previous_dir.name
    if len(name) == 8 and name.isdigit():
        return f"{name[:4]}-{name[4:6]}-{name[6:]}"
    return "unknown"


def _top_tickers(frame: pd.DataFrame, top_n: int) -> set[str]:
    if frame.empty or "ticker" not in frame:
        return set()
    return set(frame.head(top_n)["ticker"].astype(str))


def _rank_changes(current: pd.DataFrame, previous: pd.DataFrame) -> pd.DataFrame:
    if current.empty or previous.empty:
        return pd.DataFrame()
    merged = current[["ticker", "rank"]].merge(
        previous[["ticker", "rank"]].rename(columns={"rank": "previous_rank"}),
        on="ticker",
        how="left",
    )
    merged["rank_change"] = merged["previous_rank"] - merged["rank"]
    return merged
