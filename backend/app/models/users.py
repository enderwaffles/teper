
#app
#models
#users.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"sqlite_autoincrement": True} 
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    posts = relationship("Post", back_populates="author", cascade="all, delete-orphan")
