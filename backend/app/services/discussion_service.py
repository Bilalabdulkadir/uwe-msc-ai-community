from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.models.models import Discussion


async def get_discussions(db: AsyncSession):
    result = await db.execute(select(Discussion).order_by(Discussion.created_at.desc()).limit(50))
    return result.scalars().all()


async def create_discussion(db: AsyncSession, payload: dict, author_id):
    discussion = Discussion(**payload, author_id=author_id)
    db.add(discussion)
    await db.commit()
    await db.refresh(discussion)
    return discussion
