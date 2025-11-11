from fastapi import APIRouter, HTTPException, Header, status, Body, Depends
from src.app.config import settings

router = APIRouter(prefix="/auth", tags=["auth"], redirect_slashes=False)


@router.get("/health", status_code=status.HTTP_200_OK)
async def get_health():
    """Return the actual public key for frontend"""
    return {"Message": "Api is running!"}