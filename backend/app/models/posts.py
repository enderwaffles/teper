
#app
#models
#posts.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Post(Base):
    __tablename__ = "posts"
    __table_args__ = {"sqlite_autoincrement": True} 
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")

