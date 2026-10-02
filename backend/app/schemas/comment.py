from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field


class CommentBase(BaseModel):
    body: str = Field(..., min_length=2)


class CommentCreate(CommentBase):
    discussion_id: UUID


class CommentResponse(CommentBase):
    id: UUID
    author_id: UUID | None = None
    discussion_id: UUID
    created_at: str | None = None

    model_config = ConfigDict(from_attributes=True)
