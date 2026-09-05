"""Liveness probe endpoint."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/liveness")
async def liveness():
    return {"status": "alive"}
