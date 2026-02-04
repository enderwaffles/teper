
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import User
from schemas.user import UserSignup, UserLogin
from auth.security import hash_password, verify_password

router = APIRouter(prefix="", tags=["authentication"])



@router.post("/signup")
def signup(data: UserSignup, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == data.name).first()
    if user:
        raise HTTPException(status_code=400, detail="User already is")
    hashed_password = hash_password(data.password)
    obj = User(name=data.name, password=hashed_password)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return {"message": "you signed up;)"}


@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == data.name).first()
    if not user:
        raise HTTPException(status_code=404, detail="wrong name")
    verified = verify_password(data.password, user.password)
    if not verified:
        raise HTTPException(status_code=401, detail="wrong password")
    return {"message": "you logged"}



