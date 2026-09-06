"""Readiness probe endpoint."""

from fastapi import APIRouter, Response

from backend_service.state import is_ready

router = APIRouter()


@router.get("/readiness")
async def readiness(response: Response):
    if not is_ready():
        response.status_code = 503
        return {"status": "not_ready"}
    return {"status": "ready"}
