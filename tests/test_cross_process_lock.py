"""Cross-PROCESS run-date lock test (review P2 #2).

The sibling concurrency test in test_pipeline_e2e shares one interpreter via
threads; this spawns real OS processes so the file lock itself (fcntl on POSIX,
msvcrt on Windows) is exercised rather than just the GIL. The "spawn" start
method is used on every platform so the behaviour matches Windows.
"""
from __future__ import annotations

import errno
import multiprocessing as mp
import os
import time
from pathlib import Path

import pytest

import weekly_us_stock.pipeline as pipeline
from weekly_us_stock.pipeline import WeeklyUSStockPipeline

_DATE_KEY = "20260109"
_HOLD_SECONDS = 0.4
_WORKERS = 3


def _hold_lock(output_dir: str, marker: str) -> None:
    # Take the same per-date lock the pipeline uses around promotion, hold it
    # briefly, and record enter/exit so the parent can assert serialization.
    with WeeklyUSStockPipeline._date_lock(Path(output_dir), _DATE_KEY):
        with open(marker, "a", encoding="utf-8") as fh:
            fh.write(f"ENTER {time.time():.6f}\n")
        time.sleep(_HOLD_SECONDS)
        with open(marker, "a", encoding="utf-8") as fh:
            fh.write(f"EXIT {time.time():.6f}\n")


def test_separate_processes_serialize_on_the_date_lock(tmp_path: Path) -> None:
    marker = tmp_path / "markers.txt"
    ctx = mp.get_context("spawn")
    procs = [
        ctx.Process(target=_hold_lock, args=(str(tmp_path), str(marker)))
        for _ in range(_WORKERS)
    ]
    for proc in procs:
        proc.start()
    for proc in procs:
        proc.join(timeout=60)
        assert proc.exitcode == 0, "worker process failed or deadlocked on the lock"

    events = [
        line.split()[0]
        for line in marker.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    # Mutual exclusion => critical sections never interleave => events strictly
    # alternate ENTER, EXIT, ... A failed lock would put two ENTERs back to back.
    assert len(events) == 2 * _WORKERS
    assert events == ["ENTER", "EXIT"] * _WORKERS, f"critical sections interleaved: {events}"


def test_lock_timeout_fails_closed(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    lock_path = tmp_path / "timeout.lock"
    monkeypatch.setattr(pipeline, "_LOCK_TIMEOUT_SECONDS", 0.01)
    monkeypatch.setattr(pipeline, "_LOCK_POLL_SECONDS", 0.001)
    monkeypatch.setattr(pipeline, "_try_acquire", lambda _handle: False)

    with open(lock_path, "w", encoding="utf-8") as handle:
        with pytest.raises(TimeoutError, match=r"within 0\.01s"):
            pipeline._lock_exclusive(handle)


def test_only_contention_errors_are_retried(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    lock_path = tmp_path / "classification.lock"
    native_lock = pipeline.msvcrt.locking if os.name == "nt" else pipeline.fcntl.flock
    native_module = pipeline.msvcrt if os.name == "nt" else pipeline.fcntl
    native_name = "locking" if os.name == "nt" else "flock"

    with open(lock_path, "w", encoding="utf-8") as handle:
        monkeypatch.setattr(
            native_module,
            native_name,
            lambda *_args: (_ for _ in ()).throw(OSError(errno.EACCES, "busy")),
        )
        assert pipeline._try_acquire(handle) is False

        monkeypatch.setattr(
            native_module,
            native_name,
            lambda *_args: (_ for _ in ()).throw(OSError(errno.EBADF, "bad descriptor")),
        )
        with pytest.raises(OSError) as exc_info:
            pipeline._try_acquire(handle)
        assert exc_info.value.errno == errno.EBADF

    monkeypatch.setattr(native_module, native_name, native_lock)
