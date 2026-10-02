from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class EventRead(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    created_at: datetime
