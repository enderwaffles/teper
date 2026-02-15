# app
# schemas
# post.py

from pydantic import BaseModel
from typing import Optional, List
from .user import UserResponse
from .comment import CommentResponse
from datetime import datetime

class PostsResponse(BaseModel):
    id: int
    title: str
    text: str
    upload_url: Optional[str] = None
    date: datetime

    author: UserResponse

    class Config:
        from_attributes = True


class PostResponse(BaseModel):
    id: int
    title: str
    text: str
    upload_url: Optional[str] = None
    date: datetime

    author: UserResponse
    comments: List[CommentResponse] = []

    class Config:
        from_attributes = True



