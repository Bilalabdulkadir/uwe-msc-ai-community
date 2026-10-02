from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.models import Event

async def get_events(session: AsyncSession):
    q = await session.execute(select(Event).limit(50))
    return [
        {
            "id": e.id,
            "title": e.title,
            "description": e.description,
            "starts_at": e.starts_at,
            "ends_at": e.ends_at,
            "created_at": e.created_at,
        }
        for e in q.scalars().all()
    ]
