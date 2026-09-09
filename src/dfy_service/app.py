"""Build MkDocs site and return a Starlette-mountable static-file app."""

import logging
import pathlib
import subprocess
import sys

from starlette.staticfiles import StaticFiles

log = logging.getLogger("axiom.docs")

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
SITE_DIR = PROJECT_ROOT / "_docs_site"


def build_docs() -> pathlib.Path:
    """Run ``mkdocs build`` and return the output directory."""
    log.info("building docs site → %s", SITE_DIR)
    subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--clean", "--quiet"],
        cwd=str(PROJECT_ROOT),
        check=True,
    )
    log.info("docs site built successfully")
    return SITE_DIR


def create_app() -> StaticFiles:
    """Build the docs and return a StaticFiles app serving them.

    The ``html=True`` flag makes StaticFiles serve ``index.html`` for
    directory requests so MkDocs page URLs work without a trailing
    ``index.html``.
    """
    build_docs()
    return StaticFiles(directory=str(SITE_DIR), html=True)
