"""Gunicorn configuration with Uvicorn workers.

Usage:
    Dev:  gunicorn axiom.app:app -c server_config/multiprocessing.py --reload
    Prod: gunicorn axiom.app:app -c server_config/multiprocessing.py
"""

from server_config.settings import (
    BIND,
    FORWARDED_ALLOW_IPS,
    GRACEFUL_TIMEOUT,
    IS_PROD,
    KEEPALIVE,
    LOG_LEVEL,
    MAX_REQUESTS,
    MAX_REQUESTS_JITTER,
    PROXY_ALLOW_FROM,
    TIMEOUT,
    WORKERS,
)

bind = BIND
worker_class = "uvicorn.workers.UvicornWorker"
workers = WORKERS

timeout = TIMEOUT
graceful_timeout = GRACEFUL_TIMEOUT
keepalive = KEEPALIVE

max_requests = MAX_REQUESTS
max_requests_jitter = MAX_REQUESTS_JITTER

accesslog = "-" if IS_PROD else None
errorlog = "-"
loglevel = LOG_LEVEL

preload_app = IS_PROD

forwarded_allow_ips = FORWARDED_ALLOW_IPS
proxy_allow_from = PROXY_ALLOW_FROM
