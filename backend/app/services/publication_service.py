from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.models.models import Publication


async def get_publications(db: AsyncSession):
    result = await db.execute(select(Publication).order_by(Publication.published_at.desc()).limit(50))
    return result.scalars().all()


async def create_publication(db: AsyncSession, payload: dict):
    publication = Publication(**payload)
    db.add(publication)
    await db.commit()
    await db.refresh(publication)
    return publication
