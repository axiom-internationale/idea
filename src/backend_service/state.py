"""Shared readiness state for the backend service."""

_ready = False


def mark_ready():
    global _ready
    _ready = True


def mark_not_ready():
    global _ready
    _ready = False


def is_ready() -> bool:
    return _ready
