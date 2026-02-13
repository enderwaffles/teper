# app
# schemas
# post.py

from pydantic import BaseModel
from typing import Optional
from .user import UserResponse
from datetime import datetime

class PostResponse(BaseModel):
    id: int
    title: str
    text: str
    upload_url: Optional[str] = None
    date: datetime
    author: UserResponse
    
    class Config:
        from_attributes = True

class PostUpdate(BaseModel):
    title: str | None
    text: str | None

