from uuid import UUID
from pydantic import BaseModel, ConfigDict


class ResourceBase(BaseModel):
    title: str
    description: str | None = None
    resource_type: str = "article"
    url: str


class ResourceCreate(ResourceBase):
    pass


class ResourceResponse(ResourceBase):
    id: UUID
    created_at: str | None = None
    updated_at: str | None = None

    model_config = ConfigDict(from_attributes=True)
