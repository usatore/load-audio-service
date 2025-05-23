from app.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    audiofile = relationship("Audiofiles", back_populates="user")


    def __str__(self):
        return f"Пользователь {self.email}"
