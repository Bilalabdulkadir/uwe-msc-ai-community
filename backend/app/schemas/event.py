from uuid import UUID
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class EventBase(BaseModel):
    title: str
    description: str | None = None
    start_date: datetime
    location: str | None = None


class EventCreate(EventBase):
    pass


class EventResponse(EventBase):
    id: UUID
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
