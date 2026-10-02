from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db import get_db
from backend.app.schemas.notification import NotificationCreate, NotificationResponse
from backend.app.services.notification_service import get_notifications, create_notification

router = APIRouter()

@router.get("/", response_model=list[NotificationResponse])
async def list_notifications(user_id: str, db: AsyncSession = Depends(get_db)):
    return await get_notifications(db, user_id)


@router.post("/", response_model=NotificationResponse)
async def create_notification_route(payload: NotificationCreate, user_id: str, db: AsyncSession = Depends(get_db)):
    return await create_notification(db, payload.model_dump(), user_id)
