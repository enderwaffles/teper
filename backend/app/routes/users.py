
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import User
from schemas.user import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserResponse])
def users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/{id}", response_model=UserResponse)
def user(id: int, db: Session = Depends(get_db)):
    obj = db.query(User).filter(User.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="User not found")
    return obj

@router.post("/", response_model=UserResponse)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    obj = User(name=data.name)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.delete("/{id}", status_code=204)
def delete_user(id: int, db: Session = Depends(get_db)):
    obj = db.query(User).filter(User.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        db.delete(obj)
        db.commit()
        return None
    
@router.patch("/{id}", response_model=UserResponse)
def update_user(id: int, data: UserUpdate, db: Session = Depends(get_db)):
    obj = db.query(User).filter(User.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    else:
        if data is not None:
            obj.name = data.name
        db.commit()
        db.refresh()
        return obj
