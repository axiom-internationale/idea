"""Startup and shutdown hooks for the Starlette application."""

import logging
from contextlib import asynccontextmanager

from starlette.applications import Starlette

from backend_service.state import mark_not_ready, mark_ready

log = logging.getLogger("axiom")


@asynccontextmanager
async def lifespan(app: Starlette):
    log.info("axiom-intelligence starting up")
    mark_ready()
    log.info("axiom-intelligence ready")
    yield
    log.info("axiom-intelligence shutting down")
    mark_not_ready()
    log.info("axiom-intelligence stopped")
