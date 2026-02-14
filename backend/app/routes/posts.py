# app
# routes
# posts.py

#bibliotecs
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
import os
from datetime import datetime

#modules
from database import get_db
from models import Post
from schemas.post import PostResponse, PostUpdate
from auth import User, get_user

#configs
router = APIRouter(prefix="/posts", tags=["posts"])

#core
@router.get("/", response_model=List[PostResponse])
def posts(db: Session = Depends(get_db)):
    obj = db.query(Post).options(joinedload(Post.author)).all()
    return obj

@router.get("/{id}", response_model=PostResponse)
def post(id: int, db: Session = Depends(get_db)):
    obj = db.query(Post).options(joinedload(Post.author)).filter(Post.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Post not found")
    return obj

@router.post("/", status_code=201, response_model=PostResponse)
def create_post(
    title: str = Form(...),
    text: str = Form(...),
    file: Optional[UploadFile] = File(None),  # <-- было upload
    db: Session = Depends(get_db),
    user: User = Depends(get_user),
):
    os.makedirs("static", exist_ok=True)

    obj = Post(title=title, text=text, author_id=user.id)
    db.add(obj)
    db.commit()
    db.refresh(obj)

    if file is not None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f") 
        name = f"{obj.author_id}_{timestamp}_{obj.id}_{file.filename}"
        disk_path = f"static/{name}"

        with open(disk_path, "wb") as f:
            f.write(file.file.read())

        obj.upload_url = f"/static/{name}"
        db.commit()
        db.refresh(obj)

    return obj

@router.delete("/{id}", status_code=204)
def delete_post(id: int, db: Session = Depends(get_db), user: User = Depends(get_user)):
    obj = db.query(Post).filter(Post.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Post not found")
    if obj.author_id != user.id:
        raise HTTPException(status_code=403, detail="Method not allowed")
    db.delete(obj)
    db.commit()
    return None

@router.patch("/{id}", status_code=202)
def update_post(id: int, data: PostUpdate, db: Session = Depends(get_db), user: User = Depends(get_user)):
    obj = db.query(Post).filter(Post.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    if obj.author_id != user.id:
        raise HTTPException(status_code=405, detail="Method not allowed")
    if data.title.strip() == "" or data.text.strip() == "":
        raise HTTPException(status_code=400, detail="Bad request")
    obj.title = data.title
    obj.text = data.text
    db.commit()
    db.refresh(obj)
    return {"message": f"updated post {obj.title}"}
