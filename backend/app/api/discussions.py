from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db import get_db
from backend.app.schemas.discussion import DiscussionCreate, DiscussionResponse
from backend.app.services.discussion_service import get_discussions, create_discussion

router = APIRouter()

@router.get("/", response_model=list[DiscussionResponse])
async def list_discussions(db: AsyncSession = Depends(get_db)):
    return await get_discussions(db)


@router.post("/", response_model=DiscussionResponse)
async def create_discussion_route(payload: DiscussionCreate, db: AsyncSession = Depends(get_db)):
    owner_id = "11111111-1111-4111-8111-111111111111"
    return await create_discussion(db, payload.model_dump(), owner_id)
