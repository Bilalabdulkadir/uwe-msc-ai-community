from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.models import Project

async def get_projects(session: AsyncSession):
    q = await session.execute(select(Project).limit(50))
    return [
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "owner_id": p.owner_id,
            "created_at": p.created_at,
        }
        for p in q.scalars().all()
    ]
