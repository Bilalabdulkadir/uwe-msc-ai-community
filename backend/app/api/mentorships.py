from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db import get_db
from backend.app.schemas.mentorship import MentorshipCreate, MentorshipResponse

router = APIRouter()

@router.get("/", response_model=list[MentorshipResponse])
async def list_mentorships(db: AsyncSession = Depends(get_db)):
    return []


@router.post("/", response_model=MentorshipResponse)
async def create_mentorship_route(payload: MentorshipCreate, db: AsyncSession = Depends(get_db)):
    return {**payload.model_dump(), "id": "11111111-1111-4111-8111-111111111111", "created_at": None, "updated_at": None}
