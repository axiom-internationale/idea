"""FastAPI application for the Axiom Intelligence backend service."""

from fastapi import FastAPI

from axiom import __version__
from backend_service.health import router as health_router
from backend_service.liveness import router as liveness_router
from backend_service.readiness import router as readiness_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Axiom Intelligence API",
        version=__version__,
        description="Backend service for Axiom Intelligence",
    )
    app.include_router(health_router)
    app.include_router(liveness_router)
    app.include_router(readiness_router)
    return app
