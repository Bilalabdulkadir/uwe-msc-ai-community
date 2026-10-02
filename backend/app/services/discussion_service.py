from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.models import Discussion

async def get_discussions(session: AsyncSession):
    q = await session.execute(select(Discussion).limit(50))
    return [
        {
            "id": d.id,
            "title": d.title,
            "body": d.body,
            "author_id": d.author_id,
            "created_at": d.created_at,
        }
        for d in q.scalars().all()
    ]
