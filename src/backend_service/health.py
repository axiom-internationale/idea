"""Health check endpoint."""

import time

from fastapi import APIRouter

from axiom import __version__

router = APIRouter()

_START_TIME = time.monotonic()


@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "app": "axiom-intelligence",
        "version": __version__,
        "uptime_seconds": round(time.monotonic() - _START_TIME, 2),
    }
