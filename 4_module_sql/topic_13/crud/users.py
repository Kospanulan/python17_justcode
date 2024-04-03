from sqlalchemy.orm import Session

from models import User


def create_user(
        session: Session,
        username: str
):
    new_user = User(
        username=username
    )

    session.add(new_user)

    return new_user


def get_user(
        session: Session,
        user_id: int
):
    user = (
        session
        .query(User)
        .filter(User.id == user_id)
        .one()
    )

    return user


def get_user_by_username(
        session: Session,
        username: str
):
    user = (
        session
        .query(User)
        .filter(User.username == username)
    )

    return user.scalar()


