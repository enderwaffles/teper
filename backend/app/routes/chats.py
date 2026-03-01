# app
# routes
# chats.py

from fastapi import APIRouter, Depends, HTTPException, Form, UploadFile, File
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from datetime import datetime
import os
from pathlib import Path

from database import get_db
from models import Chat, Message, User, MessageUploads
from auth import get_user, User

router = APIRouter(prefix="/chats", tags=["chats"])


# Получить все чаты пользователя
@router.get("/")
def get_user_chats(user: User = Depends(get_user), db: Session = Depends(get_db)):
    chats = db.query(Chat).options(
            joinedload(Chat.user1), joinedload(Chat.user2)
        ).filter(
            (Chat.user1_id == user.id) | (Chat.user2_id == user.id)
        ).all()
    return chats

# Получить конкретный чат
@router.get("/{chat_id}")
def get_chat(chat_id: int, user: User = Depends(get_user), db: Session = Depends(get_db)):
    chat = db.query(Chat).filter(Chat.id == chat_id).options(
        joinedload(Chat.messages).joinedload(Message.uploads)   , joinedload(Chat.user1), joinedload(Chat.user2)
    ).first()

    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    if user.id not in [chat.user1_id, chat.user2_id]:
        raise HTTPException(status_code=403, detail="Access denied")
    return chat


# Создать чат между двумя пользователями
@router.post("/{other_user_id}")
def create_chat(other_user_id: int, user: User = Depends(get_user), db: Session = Depends(get_db)):
    if user.id == other_user_id:
        raise HTTPException(status_code=400, detail="Cannot chat with yourself")

    existing_chat = db.query(Chat).filter(
        ((Chat.user1_id == user.id) & (Chat.user2_id == other_user_id)) |
        ((Chat.user1_id == other_user_id) & (Chat.user2_id == user.id))
    ).first()
    if existing_chat:
        return existing_chat

    chat = Chat(user1_id=user.id, user2_id=other_user_id)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat



# Отправить сообщение в чат
@router.post("/{chat_id}/messages")
def send_message(chat_id: int, 
                 text: Optional[str] = Form(None), 
                 files: Optional[List[UploadFile]] = File(None),  
                 user: User = Depends(get_user), 
                 db: Session = Depends(get_db)):
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    if user.id not in [chat.user1_id, chat.user2_id]:
        raise HTTPException(status_code=403, detail="Access denied")

    message = Message(chat_id=chat.id, author_id=user.id, text=text)
    db.add(message)
    db.commit()
    db.refresh(message)

    if files:
        for file in files:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f") 
            name = f"{user.id}_{timestamp}_{file.filename}"
            disk_path = f"static/{name}"
            with open(disk_path, "wb") as f:
                f.write(file.file.read())

            message_uploads = MessageUploads(message_id=message.id, upload_url=f"/static/{name}")
            db.add(message_uploads)

        db.commit()

    db.refresh(message)
    return message


# Получить все сообщения чата
@router.get("/{chat_id}/messages")
def get_messages(chat_id: int, user: User = Depends(get_user), db: Session = Depends(get_db)):
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    if user.id not in [chat.user1_id, chat.user2_id]:
        raise HTTPException(status_code=403, detail="Access denied")

    messages = db.query(Message).options(
        joinedload(Message.uploads)
    ).filter(Message.chat_id == chat.id).all()

    return messages

@router.delete("/messages/{message_id}")
def delete_message(message_id: int, user: User = Depends(get_user), db: Session = Depends(get_db)):
    message = db.query(Message).filter(Message.id == message_id).first()
    if not message:
        raise HTTPException(status_code=404)
    if message.author_id != user.id:
        raise HTTPException(status_code=403)
    
    uploads = db.query(MessageUploads).filter(MessageUploads.message_id == message.id).all()
    for upload in uploads:
        filename = upload.upload_url.replace("/static/", "")
        file_path = Path("static") / filename
        if file_path.exists():
            file_path.unlink()
        db.delete(upload)

    db.delete(message)
    db.commit()

    return None
