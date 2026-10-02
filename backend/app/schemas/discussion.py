from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field


class DiscussionBase(BaseModel):
    title: str = Field(..., min_length=2)
    content: str = Field(..., min_length=2)


class DiscussionCreate(DiscussionBase):
    pass


class DiscussionResponse(DiscussionBase):
    id: UUID
    author_id: UUID | None = None
    created_at: str | None = None
    updated_at: str | None = None

    model_config = ConfigDict(from_attributes=True)
