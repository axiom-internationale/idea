"""data_service — site content as plain JSON.

Instead of managing tables and schema migrations, page copy lives in one
JSON file per page (``index.json`` for ``/``, ``dfy.json`` for ``/dfy``).
Sections are keyed by their page anchor id; use :func:`get_section` to
fetch one.
"""

from __future__ import annotations

import json
from functools import cache
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent
INDEX_PATH = DATA_DIR / "index.json"
DFY_PATH = DATA_DIR / "dfy.json"

#: Page name → content file. Add new pages here as they are extracted.
PAGE_FILES = {"index": INDEX_PATH, "dfy": DFY_PATH}


def _load_page_file(page: str) -> dict:
    try:
        path = PAGE_FILES[page]
    except KeyError:
        raise KeyError(f"unknown content page {page!r}; available: {sorted(PAGE_FILES)}") from None
    return json.loads(path.read_text(encoding="utf-8"))


@cache
def load_index(page: str = "index") -> dict:
    """Load and cache the full content index for one page (``index``/``dfy``)."""
    return _load_page_file(page)


def get_section(name: str, page: str = "index") -> dict:
    """Return the content block for one section (e.g. ``"hero"``).

    Raises:
        KeyError: If the page or section does not exist.
    """
    index = load_index(page)
    if name not in index or not isinstance(index[name], dict):
        available = sorted(k for k in index if not k.startswith("_"))
        raise KeyError(f"unknown content section {name!r} on page {page!r}; available: {available}")
    return index[name]


__all__ = ["DFY_PATH", "INDEX_PATH", "PAGE_FILES", "get_section", "load_index"]
