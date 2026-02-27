
# app
# routes
# users.py

#bibliotecs
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
import os
from datetime import datetime

#modules
from database import get_db
from models import User
from schemas.user import UserResponse
from auth import User, get_user


#configs
router = APIRouter(prefix="/users", tags=["users"])



#core
# @router.get("/", response_model=List[UserResponse])
@router.get("/")
def users(db: Session = Depends(get_db)):
    return db.query(User).all()

# @router.get("/{id}", response_model=UserResponse)
@router.get("/{nickname}")
def user(nickname: str, db: Session = Depends(get_db)):
    obj = db.query(User).options(
        joinedload(User.posts)
    ).filter(User.nickname == nickname).first()
    if not obj:
        raise HTTPException(status_code=404, detail="User not found")
    return obj

@router.post("/")
def add_avatar(file: Optional[UploadFile] = File(None), 
               db: Session = Depends(get_db), 
               user: User = Depends(get_user)
               ):

    os.makedirs("static", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f") 
    name = f"{timestamp}_{file.filename}"
    disk_path = f"static/{name}"
    with open(disk_path, "wb") as f:
        f.write(file.file.read())
    
    user.avatar_url = f"/static/{name}"
    db.commit()

    return user

# @router.post("/", response_model=UserResponse)
# def create_user(data: UserCreate, db: Session = Depends(get_db)):
#     obj = User(name=data.name)
#     db.add(obj)
#     db.commit()
#     db.refresh(obj)
#     return obj

@router.delete("/{id}", status_code=204)
def delete_user(id: int, db: Session = Depends(get_db)):
    obj = db.query(User).filter(User.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        db.delete(obj)
        db.commit()
        return None
    
# @router.patch("/{id}", response_model=UserResponse)
# def update_user(id: int, data: UserUpdate, db: Session = Depends(get_db)):
#     obj = db.query(User).filter(User.id == id).first()
#     if not obj:
#         raise HTTPException(status_code=404, detail="Not found")
#     else:
#         if data is not None:
#             obj.name = data.name
#         db.commit()
#         db.refresh()
#         return obj
