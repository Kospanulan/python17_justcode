from sqlalchemy import (
    Column, Integer, String, ForeignKey
)
from sqlalchemy.orm import relationship

from database import Base, engine


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    surname = Column(String(50))
    age = Column(Integer)

    email = relationship('EmailAddress', back_populates='user')


class EmailAddress(Base):
    __tablename__ = 'email_addresses'

    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='email')


Base.metadata.create_all(engine)

