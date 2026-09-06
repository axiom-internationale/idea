"""Shared readiness state for the backend service.

In-memory ``_ready`` is per-process, which breaks with gunicorn
multi-worker (each worker has its own memory). A ready-file on disk
is the cross-worker source of truth: ``mark_ready`` touches it,
``mark_not_ready`` removes it, ``is_ready`` checks either.
"""

import contextlib
import os
import pathlib
import tempfile

_ready = False

_READY_FILE = pathlib.Path(os.getenv("AXIOM_READY_FILE", str(pathlib.Path(tempfile.gettempdir()) / "axiom.ready")))


def mark_ready() -> None:
    global _ready
    _ready = True
    with contextlib.suppress(OSError):
        _READY_FILE.touch(exist_ok=True)


def mark_not_ready() -> None:
    global _ready
    _ready = False
    with contextlib.suppress(OSError):
        _READY_FILE.unlink(missing_ok=True)


def is_ready() -> bool:
    if _ready:
        return True
    try:
        return _READY_FILE.exists()
    except OSError:
        return False
