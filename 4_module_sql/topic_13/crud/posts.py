from sqlalchemy.orm import Session

from models import Post, User


def create_post(
        session: Session,
        content: str,
        author_id: int
):
    new_post = Post(
        content=content,
        author_id=author_id
    )

    session.add(new_post)

    return new_post


def get_post(
        session: Session,
        post_id: int
):
    post = (
        session
        .query(Post)
        .filter(Post.id == post_id)
        .one()
    )

    return post


def get_posts_with_author_name(
        session: Session
):
    t1 = session.query(User).subquery()

    result = (
        session
        .query(Post, t1.c.username)
        .join(
            t1,
            t1.c.id == Post.author_id
        )
        .all()
    )

    posts = []
    for post, username in result:
        post.author_username = username
        posts.append(post)

    return posts


def delete_post(
        session: Session,
        post_id: int
):
    post = (
        session
        .query(Post)
        .filter(Post.id == post_id)
        .one()
    )

    session.delete(post)

    return post

