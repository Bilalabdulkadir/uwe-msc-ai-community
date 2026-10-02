from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from uuid import UUID

class UserRead(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    role: str
    created_at: datetime

    model_config = {"json_schema_extra": {"example": {"username": "alice", "email": "alice@example.com", "role": "student"}}}
