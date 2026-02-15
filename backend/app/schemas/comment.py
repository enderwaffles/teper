# app
# schemas
# comments.py

from pydantic import BaseModel
from typing import Optional, List
from .user import UserResponse
from datetime import datetime

class CommentResponse(BaseModel):
    id: int
    text: str
    date: datetime
    
    author: UserResponse
    post_id: int

    class Config:
        from_attributes = True



