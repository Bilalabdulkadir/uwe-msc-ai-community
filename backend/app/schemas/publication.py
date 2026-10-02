from uuid import UUID
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class PublicationBase(BaseModel):
    title: str
    abstract: str | None = None
    url: str | None = None
    published_at: datetime | None = None


class PublicationCreate(PublicationBase):
    pass


class PublicationResponse(PublicationBase):
    id: UUID
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
