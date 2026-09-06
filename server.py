"""Spawns the server as an independent background process on 127.0.0.1:4000.

Runs (POSIX):
    gunicorn axiom.app:axiom_app -c server_config/multiprocessing.py --bind 127.0.0.1:4000

Runs (Windows — gunicorn needs POSIX/fcntl and cannot start here):
    uvicorn axiom.app:axiom_app --host 127.0.0.1 --port 4000

Usage:
    python server.py
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 4000
APP = "axiom.app:axiom_app"
CONFIG = "server_config/multiprocessing.py"


def build_command() -> list[str]:
    if os.name == "nt":
        # Gunicorn imports fcntl and cannot run on Windows; serve the
        # same ASGI app with uvicorn instead.
        return [
            sys.executable,
            "-m",
            "uvicorn",
            APP,
            "--host",
            HOST,
            "--port",
            str(PORT),
        ]
    return [
        sys.executable,
        "-m",
        "gunicorn",
        APP,
        "-c",
        CONFIG,
        "--bind",
        f"{HOST}:{PORT}",
    ]


def spawn() -> subprocess.Popen:
    env = os.environ.copy()
    src = str(ROOT / "src")
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = src + (os.pathsep + existing if existing else "")

    cmd = build_command()
    print(f"Starting: {' '.join(cmd)} (cwd={ROOT})")

    if os.name == "nt":
        creationflags = getattr(subprocess, "DETACHED_PROCESS", 0) | getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
        return subprocess.Popen(
            cmd,
            cwd=str(ROOT),
            env=env,
            stdout=None,
            stderr=None,
            stdin=None,
            close_fds=True,
            creationflags=creationflags,
        )

    return subprocess.Popen(
        cmd,
        cwd=str(ROOT),
        env=env,
        stdout=None,
        stderr=None,
        stdin=None,
        close_fds=True,
        start_new_session=True,
    )


def main() -> int:
    proc = spawn()
    print(f"Server spawned with PID {proc.pid} on http://{HOST}:{PORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
