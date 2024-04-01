from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine(
    "postgresql+psycopg2://postgres:internat11@localhost/python17_2",
    echo=True
)

Session = sessionmaker(engine)

Base = declarative_base()

