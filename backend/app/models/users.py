
# app
# models
# users.py



#bibliotecs
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

#modules
from database import Base



#core   
class User(Base):
    __tablename__ = "users"
    __table_args__ = {"sqlite_autoincrement": True} 
    id = Column(Integer, primary_key=True)

    #personal
    email = Column(String(96), nullable=False, unique=True, index=True)
    nickname = Column(String(24), nullable=False, unique=True, index=True)

    name = Column(String(24), nullable=False)
    surname = Column(String(24), nullable=False)

    password = Column(String(256), nullable=False) #hashed by werkzeug
    avatar_url = Column(String(512), nullable=True) #profile picture  

    admin = Column(Boolean, default=False)

    #properties
    posts = relationship("Post", back_populates="author", cascade="all, delete-orphan")
    # comments = relationship("Comment", back_populates="author", cascade="all, delete-orphan")
    