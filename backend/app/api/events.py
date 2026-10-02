from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db import get_db
from backend.app.schemas.event import EventCreate, EventResponse
from backend.app.services.event_service import get_events, create_event

router = APIRouter()

@router.get("/", response_model=list[EventResponse])
async def list_events(db: AsyncSession = Depends(get_db)):
    return await get_events(db)


@router.post("/", response_model=EventResponse)
async def create_event_route(payload: EventCreate, db: AsyncSession = Depends(get_db)):
    return await create_event(db, payload.model_dump())
