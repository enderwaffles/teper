
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
    author_id: int

class PostDelete(BaseModel):
    author_id: int

class PostUpdate(BaseModel):
    name: str | None 
    author_id: int


