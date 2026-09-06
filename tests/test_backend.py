"""Health / liveness / readiness endpoint tests."""

from fastapi.testclient import TestClient

from backend_service import state
from backend_service.app import create_app


def _client() -> TestClient:
    return TestClient(create_app())


def test_liveness():
    assert _client().get("/liveness").json() == {"status": "alive"}


def test_health_has_version():
    data = _client().get("/health").json()
    assert data["status"] == "healthy"
    assert data["app"] == "axiom-intelligence"
    assert "version" in data


def test_readiness_gate():
    state.mark_not_ready()
    assert _client().get("/readiness").status_code == 503
    state.mark_ready()
    assert _client().get("/readiness").json() == {"status": "ready"}
    state.mark_not_ready()
