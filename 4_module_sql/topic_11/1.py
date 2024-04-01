from sqlalchemy import (
    create_engine, MetaData,
    Table, Column,
    Integer, String
)

engine = create_engine("postgresql+psycopg2://postgres:internat11@localhost/python17_2")

metadata = MetaData()

user_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("surname", String)
)

metadata.create_all(engine)























