from fastapi import APIRouter, Depends
from typing import List
from ..schemas.user import UserRead
from ..services.user_service import get_users
from ..db import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get('/', response_model=List[UserRead])
async def list_users(session: AsyncSession = Depends(get_session)):
    return await get_users(session)
