"""Axiom Intelligence package — single source of truth for version."""

try:
    from importlib.metadata import version as _pkg_version

    __version__ = _pkg_version("axiom-intelligence")
except Exception:
    __version__ = "0.1.0"

__all__ = ["__version__"]
