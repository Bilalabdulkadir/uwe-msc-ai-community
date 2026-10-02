from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class DiscussionRead(BaseModel):
    id: UUID
    title: str
    body: Optional[str]
    author_id: Optional[UUID]
    created_at: datetime
