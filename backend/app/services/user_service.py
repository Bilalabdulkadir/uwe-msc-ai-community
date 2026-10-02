from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.models.models import User


async def get_users(db: AsyncSession):
    result = await db.execute(select(User).order_by(User.created_at.desc()).limit(50))
    return result.scalars().all()


async def create_user(db: AsyncSession, user_data: dict):
    user = User(**user_data)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
