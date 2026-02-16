
# app
# routes
# authentication.py



#bibliotecs
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from typing import List

#modules
from database import get_db
from models import User
from schemas.user import UserSignup, UserLogin

#auth
from auth.token import create_token, decode_token
from auth.hash import hash_password, verify_password
from auth.cookie import get_user, set_auth_cookie, clear_auth_cookie



#configs
router = APIRouter(prefix="", tags=["authentication"])



#core
@router.get("/protected")
def protected(user: User = Depends(get_user)):
    return {
        "message": "access free",
        "id": user.id,
        "name": user.name,
    }

@router.post("/signup", status_code=201)
def signup(data: UserSignup, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == data.name).first()
    if user:
        raise HTTPException(status_code=400, detail="User already is")
    hashed_password = hash_password(data.password)
    obj = User(email=data.email, 
               nickname=data.nickname, 
               name=data.name.capitalize(),
               surname=data.surname.capitalize(), 
               password=hashed_password)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return {"message": "you signed up;)", "user": obj}

@router.post("/login")
def login(data: UserLogin, response: Response, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="wrong name or password")
    verified = verify_password(data.password, user.password)
    if not verified:
        raise HTTPException(status_code=401, detail="wrong name or password")
    token = create_token(user.id)
    set_auth_cookie(response, token)
    return {"message": "logged in", "token_type": "cookie", "user": user}

@router.post("/logout")
def logout(response: Response):
    clear_auth_cookie(response)
    return {"message": "logged out"}



