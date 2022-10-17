from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    phone_number = Column(Integer, unique=True)
    contact_preference = Column(String(5))

    def __str__(self) -> str:
        return super().__str__() + f" {self.id}, {self.email}, {self.phone_number}, {self.contact_preference}"


