from typing import Annotated
from fastapi.routing import APIRouter
from fastapi import Depends
from configurations.config import Settings
from configurations.deps import get_expensive


router = APIRouter()


@router.get("/")
async def root(content: Annotated[Settings, Depends(get_expensive)]) -> str:
    return content
