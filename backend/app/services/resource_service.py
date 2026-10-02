from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.models import Resource

async def get_resources(session: AsyncSession):
    q = await session.execute(select(Resource).limit(50))
    return [
        {
            "id": r.id,
            "title": r.title,
            "url": r.url,
            "created_at": r.created_at,
        }
        for r in q.scalars().all()
    ]
