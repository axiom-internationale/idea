"""Centralized configuration loaded from .env at import time.

Every module that needs a setting imports from here instead of
calling ``os.getenv`` directly.
"""

import multiprocessing as _mp
import os
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parent.parent

_env_file = _ROOT / ".env"
if _env_file.exists():
    for line in _env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip()
        if key and key not in os.environ:
            os.environ[key] = value

ENV: str = os.getenv("AXIOM_ENV", "development")
IS_PROD: bool = ENV == "production"

BIND: str = os.getenv("AXIOM_BIND", "0.0.0.0:8000")
WORKERS: int = int(os.getenv("AXIOM_WORKERS", _mp.cpu_count() * 2 + 1 if IS_PROD else 1))
TIMEOUT: int = int(os.getenv("AXIOM_TIMEOUT", "120"))
GRACEFUL_TIMEOUT: int = int(os.getenv("AXIOM_GRACEFUL_TIMEOUT", "30"))
KEEPALIVE: int = int(os.getenv("AXIOM_KEEPALIVE", "5"))
LOG_LEVEL: str = os.getenv("AXIOM_LOG_LEVEL", "info" if IS_PROD else "debug")

MAX_REQUESTS: int = int(os.getenv("AXIOM_MAX_REQUESTS", "1000" if IS_PROD else "0"))
MAX_REQUESTS_JITTER: int = int(os.getenv("AXIOM_MAX_REQUESTS_JITTER", "50" if IS_PROD else "0"))

FORWARDED_ALLOW_IPS: str = os.getenv("AXIOM_FORWARDED_ALLOW_IPS", "127.0.0.1" if IS_PROD else "*")
PROXY_ALLOW_FROM: str = os.getenv("AXIOM_PROXY_ALLOW_FROM", "127.0.0.1" if IS_PROD else "*")
