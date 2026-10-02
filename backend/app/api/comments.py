from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db import get_db
from backend.app.schemas.comment import CommentCreate, CommentResponse
from backend.app.services.comment_service import get_comments, create_comment

router = APIRouter()

@router.get("/", response_model=list[CommentResponse])
async def list_comments(discussion_id: str, db: AsyncSession = Depends(get_db)):
    return await get_comments(db, discussion_id)


@router.post("/", response_model=CommentResponse)
async def create_comment_route(payload: CommentCreate, db: AsyncSession = Depends(get_db)):
    author_id = "11111111-1111-4111-8111-111111111111"
    return await create_comment(db, str(payload.discussion_id), payload.model_dump(exclude={"discussion_id"}), author_id)
