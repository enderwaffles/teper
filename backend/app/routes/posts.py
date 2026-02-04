
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Post
from schemas.post import PostCreate, PostResponse, PostUpdate, PostDelete

router = APIRouter(prefix="/posts", tags=["posts"])



@router.get("/", response_model=List[PostResponse])
def posts(db: Session = Depends(get_db)):
    return db.query(Post).all()
    
@router.get("/{id}", response_model=PostResponse)
def post(id: int, db: Session = Depends(get_db)):
    obj = db.query(Post).filter(Post.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Post not found")
    return obj

@router.post("/", response_model=PostResponse)
def create_post(data: PostCreate, db: Session = Depends(get_db)):
    obj = Post(name=data.name, author_id=data.author_id)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.delete("/{id}", status_code=204)
def delete_post(id: int, data: PostDelete, db: Session = Depends(get_db)):
    obj = db.query(Post).filter(Post.id == id).first()
    #there must be user session check so he deletes only his own article
    if not obj:
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        if data.author_id == obj.author_id:
            db.delete(obj)
            db.commit()
            return None

@router.patch("/{id}", response_model=PostResponse)
def update_post(id: int, data: PostUpdate, db: Session = Depends(get_db)):
    obj = db.query(Post).filter(Post.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    else:
        if data.author_id == obj.author_id:
            if data is not None:
                obj.name = data.name
            db.commit()
            db.refresh()
            return obj

