from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.models.models import Event


async def get_events(db: AsyncSession):
    result = await db.execute(select(Event).order_by(Event.start_date.asc()).limit(50))
    return result.scalars().all()


async def create_event(db: AsyncSession, payload: dict):
    event = Event(**payload)
    db.add(event)
    await db.commit()
    await db.refresh(event)
    return event
