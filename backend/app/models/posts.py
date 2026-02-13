# app
# models
# posts.py

#bibliotecs
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

#modules
from database import Base

#core
class Post(Base):
    __tablename__ = "posts"
    __table_args__ = {"sqlite_autoincrement": True}
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    file_path = Column(String, nullable=True)  # <-- тут будет "/static/1_xxx.jpg"

    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
