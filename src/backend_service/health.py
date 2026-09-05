"""Health check endpoint."""

import time

from fastapi import APIRouter

router = APIRouter()

_START_TIME = time.monotonic()


@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "app": "axiom-intelligence",
        "version": "0.1.0",
        "uptime_seconds": round(time.monotonic() - _START_TIME, 2),
    }
