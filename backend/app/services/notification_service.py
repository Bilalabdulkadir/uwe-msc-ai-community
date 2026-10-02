from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.models.models import Notification


async def get_notifications(db: AsyncSession, user_id):
    result = await db.execute(select(Notification).where(Notification.user_id == user_id).order_by(Notification.created_at.desc()).limit(50))
    return result.scalars().all()


async def create_notification(db: AsyncSession, payload: dict, user_id):
    notification = Notification(**payload, user_id=user_id)
    db.add(notification)
    await db.commit()
    await db.refresh(notification)
    return notification
