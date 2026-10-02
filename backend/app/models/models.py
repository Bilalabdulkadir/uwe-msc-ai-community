from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, func, ForeignKey, Text, Enum, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import enum

Base = declarative_base()

class UserRole(str, enum.Enum):
    student = "student"
    lecturer = "lecturer"
    alumni = "alumni"
    researcher = "researcher"

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.student)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    profile = relationship('Profile', back_populates='user', uselist=False)

class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False, unique=True)
    full_name = Column(String(255))
    bio = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    user = relationship('User', back_populates='profile')

class Discussion(Base):
    __tablename__ = 'discussions'
    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String(400), nullable=False)
    body = Column(Text)
    author_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='SET NULL'))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    comments = relationship('DiscussionComment', back_populates='discussion')

class DiscussionComment(Base):
    __tablename__ = 'discussion_comments'
    id = Column(UUID(as_uuid=True), primary_key=True)
    discussion_id = Column(UUID(as_uuid=True), ForeignKey('discussions.id', ondelete='CASCADE'), nullable=False, index=True)
    author_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='SET NULL'))
    body = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class Event(Base):
    __tablename__ = 'events'
    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String(400), nullable=False)
    description = Column(Text)
    starts_at = Column(DateTime(timezone=True))
    ends_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class Project(Base):
    __tablename__ = 'projects'
    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String(400), nullable=False)
    description = Column(Text)
    owner_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='SET NULL'))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class Resource(Base):
    __tablename__ = 'resources'
    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String(400), nullable=False)
    url = Column(String(2048))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class Mentorship(Base):
    __tablename__ = 'mentorships'
    id = Column(UUID(as_uuid=True), primary_key=True)
    mentor_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='SET NULL'))
    mentee_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='SET NULL'))
    started_at = Column(DateTime(timezone=True), server_default=func.now())

class Publication(Base):
    __tablename__ = 'publications'
    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String(500))
    abstract = Column(Text)
    published_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Notification(Base):
    __tablename__ = 'notifications'
    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    message = Column(Text)
    read = Column(String(5), server_default='false')
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# Indexes
Index('ix_users_created_at', User.created_at)
Index('ix_discussions_created_at', Discussion.created_at)
Index('ix_projects_created_at', Project.created_at)
