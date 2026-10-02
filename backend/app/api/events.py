from fastapi import APIRouter, Depends
from typing import List
from ..schemas.event import EventRead
from ..services.event_service import get_events
from ..db import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get('/', response_model=List[EventRead])
async def list_events(session: AsyncSession = Depends(get_session)):
    return await get_events(session)
