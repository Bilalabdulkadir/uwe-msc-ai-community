from fastapi import APIRouter, Depends
from typing import List
from ..schemas.discussion import DiscussionRead
from ..services.discussion_service import get_discussions
from ..db import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get('/', response_model=List[DiscussionRead])
async def list_discussions(session: AsyncSession = Depends(get_session)):
    return await get_discussions(session)
