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
    upload_url = Column(String, nullable=True)
    date = Column(DateTime, default=datetime.utcnow)
    likes = Column(Integer, default=0, nullable=False)

    #owner
    author_id = Column(Integer, ForeignKey("users.id"))

    #properties
    author = relationship("User", back_populates="posts")
    # comments = relationship("Comment", back_populates="author", cascade="all, delete-orphan")


# class Comment(Base):
#     __tablename__ = "comments"
#     __table_args__ = {"sqlite_autoincrement": True}
#     id = Column(Integer, primary_key=True)

#     #personal
#     text = Column(String, nullable=False)

#     #owners
#     post_id = Column(Integer, ForeignKey("posts.id"))
#     author_id = Column(Integer, ForeignKey("users.id"))
    
#     #properties
#     post = relationship("Post", back_populates="comments")
#     author = relationship("User", back_populates="comments")
    
