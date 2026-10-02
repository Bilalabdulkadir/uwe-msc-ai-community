from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class ResourceRead(BaseModel):
    id: UUID
    title: str
    url: Optional[str]
    created_at: datetime
