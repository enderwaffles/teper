# app
# models
# chats.py

#bibliotecs
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

#modules
from database import Base

#core
class Chat(Base):
    __tablename__ = "chats"
    __table_args__ = {"sqlite_autoincrement": True}
    id = Column(Integer, primary_key=True)

    #personal
    user1_id = Column(Integer, ForeignKey("users.id"))
    user2_id = Column(Integer, ForeignKey("users.id"))

    date = Column(DateTime, default=datetime.utcnow)

    #properties
    messages = relationship("Message", back_populates="chat", cascade="all, delete-orphan")
    user1 = relationship("User", foreign_keys=[user1_id])
    user2 = relationship("User", foreign_keys=[user2_id])

class Message(Base):
    __tablename__ = "messages"
    __table_args__ = {"sqlite_autoincrement": True}
    id = Column(Integer, primary_key=True)

    #personal
    text = Column(String(1024), nullable=True)
    # upload_url = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    #owner
    chat_id = Column(Integer, ForeignKey("chats.id"))
    author_id = Column(Integer, ForeignKey("users.id"))

    #properties
    chat = relationship("Chat", back_populates="messages")
    author = relationship("User", foreign_keys=[author_id])
    uploads = relationship("MessageUploads", back_populates="message", cascade="all, delete-orphan")


class MessageUploads(Base):
    __tablename__ = "messages_uploads"
    __table_args__ = {"sqlite_autoincrement": True}
    id = Column(Integer, primary_key=True)

    upload_url = Column(String, nullable=False)
    
    message_id = Column(Integer, ForeignKey("messages.id"))

    message = relationship("Message", back_populates="uploads")

