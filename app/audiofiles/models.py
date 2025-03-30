from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class Audiofiles(Base):
    __tablename__ = "audiofiles"

    id = Column(Integer, primary_key=True, nullable=False)
    filename = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    user_id = Column(ForeignKey("users.id"))

    user = relationship("Users", back_populates="audiofile")

    def __str__(self):
        return f"Файл {self.filename} по адресу {self.filepath}"



