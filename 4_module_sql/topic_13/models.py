import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.orm import relationship

from database import Base, engine


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(30), unique=True)

    created_at = sa.Column(sa.DateTime, server_default=func.timezone('UTC', func.now()))
    updated_at = sa.Column(
        sa.DateTime,
        server_default=func.timezone('UTC', func.now()),
        onupdate=func.timezone('UTC', func.now())
    )

    posts = relationship('Post', cascade="all,delete", back_populates='author')
    comments = relationship('Comment', uselist=False, back_populates="author")

    def __repr__(self):
        return (f"User ({self.id}): "
                f"Username: {self.username}.")


class Post(Base):
    __tablename__ = 'posts'

    id = sa.Column(sa.Integer, primary_key=True)

    content = sa.Column(sa.Text, nullable=False)
    author_id = sa.Column(sa.Integer, sa.ForeignKey('users.id', ondelete="CASCADE"))

    created_at = sa.Column(sa.DateTime, server_default=func.timezone('UTC', func.now()))
    updated_at = sa.Column(
        sa.DateTime,
        server_default=func.timezone('UTC', func.now()),
        onupdate=func.timezone('UTC', func.now())
    )

    author = relationship('User', uselist=False, lazy="joined", back_populates="posts")
    comments = relationship('Comment', uselist=False, lazy="joined", back_populates="post")

    def __repr__(self):
        return (f"Post ({self.id}): "
                # f"Author_id: {self.author_id}; "
                f"Content: {self.content}.")


class Comment(Base):
    __tablename__ = 'comments'

    id = sa.Column(sa.Integer, primary_key=True)

    content = sa.Column(sa.Text, nullable=False)
    author_id = sa.Column(sa.Integer, sa.ForeignKey('users.id', ondelete="CASCADE"))
    post_id = sa.Column(sa.Integer, sa.ForeignKey('posts.id', ondelete="CASCADE"))

    created_at = sa.Column(sa.DateTime, server_default=func.timezone('UTC', func.now()))
    updated_at = sa.Column(
        sa.DateTime,
        server_default=func.timezone('UTC', func.now()),
        onupdate=func.timezone('UTC', func.now())
    )

    author = relationship('User', uselist=False, lazy="joined", back_populates="comments")
    post = relationship('Post', uselist=False, back_populates="comments")

    def __repr__(self):
        return (f"Comment ({self.id}): "
                f"Author_id: {self.author_id}; "
                f"Post_id: {self.post_id}; "
                f"Content: {self.content}.")


Base.metadata.create_all(engine)
