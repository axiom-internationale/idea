"""Starlette application — mounts the FastHTML website on '/'."""

import logging
import pathlib

from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

from axiom.lifecycle import lifespan
from backend_service.app import create_app as create_backend_app
from website.app import create_app as create_website_app

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")

_STATIC = pathlib.Path(__file__).resolve().parent.parent / "website" / "static"
_MEDIA = pathlib.Path(__file__).resolve().parent.parent / "website" / "media"

app = Starlette(
    debug=False,
    routes=[
        Mount("/api", app=create_backend_app()),
        Mount("/static", app=StaticFiles(directory=str(_STATIC)), name="static"),
        Mount("/media", app=StaticFiles(directory=str(_MEDIA)), name="media"),
        Mount("/", app=create_website_app()),
    ],
    lifespan=lifespan,
)
app.state.name = "axiom-intelligence"
app.state.version = "0.1.0"
app.state.description = "Axiom Intelligence — autonomous agentic factory"
