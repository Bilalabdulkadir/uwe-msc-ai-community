from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.models.models import Resource


async def get_resources(db: AsyncSession):
    result = await db.execute(select(Resource).order_by(Resource.created_at.desc()).limit(50))
    return result.scalars().all()


async def create_resource(db: AsyncSession, payload: dict):
    resource = Resource(**payload)
    db.add(resource)
    await db.commit()
    await db.refresh(resource)
    return resource
