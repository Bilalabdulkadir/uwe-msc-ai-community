from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class ProjectRead(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    owner_id: Optional[UUID]
    created_at: datetime
