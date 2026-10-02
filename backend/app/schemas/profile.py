from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field


class ProfileBase(BaseModel):
    full_name: str = Field(..., min_length=2)
    bio: str | None = None
    linkedin_url: str | None = None
    github_url: str | None = None
    skills: str | None = None


class ProfileCreate(ProfileBase):
    pass


class ProfileResponse(ProfileBase):
    id: UUID
    user_id: UUID

    model_config = ConfigDict(from_attributes=True)
