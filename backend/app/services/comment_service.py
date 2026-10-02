from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.models.models import DiscussionComment


async def get_comments(db: AsyncSession, discussion_id):
    result = await db.execute(select(DiscussionComment).where(DiscussionComment.discussion_id == discussion_id).order_by(DiscussionComment.created_at.asc()))
    return result.scalars().all()


async def create_comment(db: AsyncSession, discussion_id: str, payload: dict, author_id):
    comment = DiscussionComment(**payload, discussion_id=discussion_id, author_id=author_id)
    db.add(comment)
    await db.commit()
    await db.refresh(comment)
    return comment
