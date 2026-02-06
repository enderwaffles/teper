
# app
# schemas
# user.py


from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    name: str
    password: str

    class Config:
        from_attributes = True

class UserSignup(BaseModel):
    name: str
    password: str

class UserLogin(BaseModel):
    name: str 
    password: str
