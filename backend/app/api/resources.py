from fastapi import APIRouter, Depends
from typing import List
from ..schemas.resource import ResourceRead
from ..services.resource_service import get_resources
from ..db import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get('/', response_model=List[ResourceRead])
async def list_resources(session: AsyncSession = Depends(get_session)):
    return await get_resources(session)
