"""Centralized configuration loaded from .env at import time.

Every module that needs a setting imports from here instead of
calling ``os.getenv`` directly.
"""

import logging as _logging
import multiprocessing as _mp
import os
import pathlib

_log = _logging.getLogger("axiom.settings")

_ROOT = pathlib.Path(__file__).resolve().parent.parent


def _parse_dotenv_line(line: str) -> tuple[str, str] | None:
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    if line.startswith("export "):
        line = line[len("export ") :].strip()
    key, sep, value = line.partition("=")
    if not sep:
        return None
    key, value = key.strip(), value.strip()
    # strip inline comments and surrounding quotes
    if "#" in value and not (value.startswith('"') or value.startswith("'")):
        value = value.split("#", 1)[0].strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
        value = value[1:-1]
    if not key or not key.replace("_", "").isalnum():
        return None
    return key, value


_env_file = _ROOT / ".env"
if _env_file.exists():
    try:
        for raw in _env_file.read_text(encoding="utf-8").splitlines():
            parsed = _parse_dotenv_line(raw)
            if parsed is None:
                continue
            key, value = parsed
            if key and key not in os.environ:
                os.environ[key] = value
    except OSError as exc:
        _log.warning("could not read .env: %s", exc)


def _get_int(name: str, default: int, minimum: int = 0) -> int:
    raw = os.getenv(name)
    if raw is None or raw == "":
        return default
    try:
        value = int(raw.strip())
    except ValueError:
        _log.warning("invalid %s=%r, using default %d", name, raw, default)
        return default
    if value < minimum:
        _log.warning("invalid %s=%d < %d, using default %d", name, value, minimum, default)
        return default
    return value


_LOG_LEVELS = {"debug", "info", "warning", "error", "critical"}

ENV: str = os.getenv("AXIOM_ENV", "development").strip().lower() or "development"
IS_PROD: bool = ENV == "production"

BIND: str = os.getenv("AXIOM_BIND", "0.0.0.0:4000").strip() or "0.0.0.0:4000"
WORKERS: int = _get_int("AXIOM_WORKERS", _mp.cpu_count() * 2 + 1 if IS_PROD else 1, minimum=1)
TIMEOUT: int = _get_int("AXIOM_TIMEOUT", 120, minimum=1)
GRACEFUL_TIMEOUT: int = _get_int("AXIOM_GRACEFUL_TIMEOUT", 30, minimum=1)
KEEPALIVE: int = _get_int("AXIOM_KEEPALIVE", 5, minimum=0)
_raw_level = os.getenv("AXIOM_LOG_LEVEL", "info" if IS_PROD else "debug").strip().lower()
LOG_LEVEL: str = _raw_level if _raw_level in _LOG_LEVELS else "info"

MAX_REQUESTS: int = _get_int("AXIOM_MAX_REQUESTS", 1000 if IS_PROD else 0, minimum=0)
MAX_REQUESTS_JITTER: int = _get_int("AXIOM_MAX_REQUESTS_JITTER", 50 if IS_PROD else 0, minimum=0)

FORWARDED_ALLOW_IPS: str = os.getenv("AXIOM_FORWARDED_ALLOW_IPS", "127.0.0.1" if IS_PROD else "*").strip()
PROXY_ALLOW_FROM: str = os.getenv("AXIOM_PROXY_ALLOW_FROM", "127.0.0.1" if IS_PROD else "*").strip()
if IS_PROD and FORWARDED_ALLOW_IPS == "*":
    _log.warning("AXIOM_FORWARDED_ALLOW_IPS='*' in production; refusing, using 127.0.0.1")
    FORWARDED_ALLOW_IPS = "127.0.0.1"
if IS_PROD and PROXY_ALLOW_FROM == "*":
    _log.warning("AXIOM_PROXY_ALLOW_FROM='*' in production; refusing, using 127.0.0.1")
    PROXY_ALLOW_FROM = "127.0.0.1"
