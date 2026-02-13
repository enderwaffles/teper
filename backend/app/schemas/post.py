
# app
# schemas
# post.py

from pydantic import BaseModel
from .user import UserResponse

class PostResponse(BaseModel):
    id: int
    title: str
    author: UserResponse
    
    class Config:
        from_attributes = True

class PostCreate(BaseModel):
    title: str

class PostDelete(BaseModel):
    pass    

class PostUpdate(BaseModel):
    title: str | None 


