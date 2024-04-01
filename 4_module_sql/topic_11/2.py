from sqlalchemy import (
    create_engine, Column,
    Integer, String
)

from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(
    "postgresql+psycopg2://postgres:internat11@localhost/python17_2",
    echo=True
)

Session = sessionmaker(bind=engine)

Base = declarative_base()


# Модели, схемы
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    surname = Column(String(50))
    age = Column(Integer)


# Base.metadata.create_all(engine)

with Session() as session:
    # new_user = User(name="Max", surname="Petrov", age="40")
    # session.add(new_user)
    #
    # session.commit()

    # users = session.query(User).all()
    # users = session.query(User).filter(User.name == "Ulan", User.surname == "Qospan")
    # users = session.query(User).filter(User.age > 45)

    users = (
        session
        .query(User)
        .order_by(User.age)
        .limit(2)
        .offset(1)
    )

    for user in users:
        print(user)
        print("id:", user.id)
        print("name:", user.name)
        print("surname:", user.surname)
        print("age:", user.age)
        print("=============================")
