
# app
# schemas
# post.py

from pydantic import BaseModel
from .user import UserResponse

class PostResponse(BaseModel):
    id: int
    name: str
    author_id: int

    class Config:
        from_attributes = True

class PostCreate(BaseModel):
    name: str

class PostDelete(BaseModel):
    pass    

class PostUpdate(BaseModel):
    name: str | None 


