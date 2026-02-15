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
class Comment(Base):
    __tablename__ = "comments"
    __table_args__ = {"sqlite_autoincrement": True}
    id = Column(Integer, primary_key=True)

    #personal
    text = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    #owners
    post_id = Column(Integer, ForeignKey("posts.id"))
    author_id = Column(Integer, ForeignKey("users.id"))
    
    #properties
    post = relationship("Post", back_populates="comments")
    author = relationship("User", back_populates="comments")
    