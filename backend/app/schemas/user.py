
# app
# schemas
# user.py


from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    email: str
    nickname: str
    name: str
    surname: str
    avatar_url: str | None

    class Config:
        from_attributes = True

class UserSignup(BaseModel):
    email: str
    nickname: str
    name: str
    surname: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str
