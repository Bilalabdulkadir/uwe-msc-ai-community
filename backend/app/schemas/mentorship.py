from uuid import UUID
from pydantic import BaseModel, ConfigDict


class MentorshipBase(BaseModel):
    mentor_id: UUID
    mentee_id: UUID
    status: str = "active"


class MentorshipCreate(MentorshipBase):
    pass


class MentorshipResponse(MentorshipBase):
    id: UUID
    created_at: str | None = None
    updated_at: str | None = None

    model_config = ConfigDict(from_attributes=True)
