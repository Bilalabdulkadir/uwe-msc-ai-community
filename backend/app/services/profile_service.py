from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.models.models import Profile


async def get_profiles(db: AsyncSession):
    result = await db.execute(select(Profile).order_by(Profile.created_at.desc()).limit(50))
    return result.scalars().all()


async def create_profile(db: AsyncSession, payload: dict, user_id):
    profile = Profile(**payload, user_id=user_id)
    db.add(profile)
    await db.commit()
    await db.refresh(profile)
    return profile
