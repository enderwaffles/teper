# app
# models
# posts.py

#bibliotecs
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

#modules
from database import Base

#core
class Post(Base):
    __tablename__ = "posts"
    __table_args__ = {"sqlite_autoincrement": True}
    id = Column(Integer, primary_key=True)
    
    #personal
    title = Column(String(24), nullable=False)
    text = Column(String, nullable=False)
    # upload_url = Column(String, nullable=True)
    date = Column(DateTime, default=datetime.utcnow)

    #owner
    author_id = Column(Integer, ForeignKey("users.id"))

    #properties
    author = relationship("User", back_populates="posts")
    uploads = relationship("PostsUploads", back_populates="post", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")


class PostsUploads(Base):
    __tablename__ = "posts_uploads"
    __table_args__ = {"sqlite_autoincrement": True}
    id = Column(Integer, primary_key=True)
    
    upload_url = Column(String, nullable=False)
    
    post_id = Column(Integer, ForeignKey("posts.id"))

    post = relationship("Post", back_populates="uploads")

