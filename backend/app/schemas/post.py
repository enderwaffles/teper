# app
# schemas
# post.py

from pydantic import BaseModel
from typing import Optional
from .user import UserResponse

class PostResponse(BaseModel):
    id: int
    title: str
    file_path: Optional[str] = None
    author: UserResponse

    class Config:
        from_attributes = True

class PostUpdate(BaseModel):
    title: str | None
