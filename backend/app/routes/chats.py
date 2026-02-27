# app
# routes
# chats.py

from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session, joinedload
from typing import List

from database import get_db
from models import Chat, Message, User
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
        joinedload(Chat.messages), joinedload(Chat.user1), joinedload(Chat.user2)
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
                 text: str = Form(...), 
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
    return message


# Получить все сообщения чата
@router.get("/{chat_id}/messages")
def get_messages(chat_id: int, user: User = Depends(get_user), db: Session = Depends(get_db)):
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    if user.id not in [chat.user1_id, chat.user2_id]:
        raise HTTPException(status_code=403, detail="Access denied")

    return db.query(Message).filter(Message.chat_id == chat.id).all()
