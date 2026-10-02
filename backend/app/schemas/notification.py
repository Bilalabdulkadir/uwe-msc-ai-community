from uuid import UUID
from pydantic import BaseModel, ConfigDict


class NotificationBase(BaseModel):
    message: str
    read: bool = False


class NotificationCreate(NotificationBase):
    pass


class NotificationResponse(NotificationBase):
    id: UUID
    user_id: UUID
    created_at: str | None = None

    model_config = ConfigDict(from_attributes=True)
