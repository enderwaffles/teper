
from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    name: str

class UserUpdate(BaseModel):
    name: str | None 