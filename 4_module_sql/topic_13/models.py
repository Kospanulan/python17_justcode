import sqlalchemy as sa
from sqlalchemy.orm import relationship

from database import Base, engine


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(30))
    surname = sa.Column(sa.String(50))
    age = sa.Column(sa.Integer)

    posts = relationship('Post', cascade="all,delete", back_populates='author')

    def __repr__(self):
        return (f"User ({self.id}): "
                f"Name: {self.name}; "
                f"Surname: {self.surname}.")


class Post(Base):
    __tablename__ = 'posts'

    id = sa.Column(sa.Integer, primary_key=True)

    content = sa.Column(sa.Text, nullable=False)
    author_id = sa.Column(sa.Integer, sa.ForeignKey('users.id', ondelete="CASCADE"))

    author = relationship('User', uselist=False, lazy="joined", back_populates="posts")

    def __repr__(self):
        return (f"Post ({self.id}): "
                # f"Author_id: {self.author_id}; "
                f"Content: {self.content}.")


Base.metadata.create_all(engine)


