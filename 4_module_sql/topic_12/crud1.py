from sqlalchemy.orm import Session, joinedload

from models import EmailAddress, User


def create_email(
        email: str,
        user_id: int,
        session: Session
):
    new_email = EmailAddress(email=email, user_id=user_id)
    session.add(new_email)

    return new_email


def create_user(
        name: str,
        surname: str,
        age: int,
        session: Session
):
    new_user = User(
        name=name,
        surname=surname,
        age=age
    )
    session.add(new_user)

    return new_user


def get_users(session: Session):
    users = session.query(User).all()

    return users


def get_user_by_id(
        user_id: int,
        session: Session
):
    user = session.query(User).filter(User.id == user_id).one()

    return user


def get_user_by_id_with_email(
        user_id: int,
        session: Session
):
    user = (
        session
        .query(User, EmailAddress)
        .join(EmailAddress)
        .filter(User.id == user_id)
        .one()
    )

    return user


def get_users_with_email(
        session: Session
):
    users = (
        session
        .query(User, EmailAddress)
        .join(EmailAddress, User.id == EmailAddress.user_id, isouter=True)
        .all()
    )

    return users


def get_users_with_email_test(
        session: Session
):
    users = (
        session
        .query(User)
        .options(
            joinedload(User.email)
        )
        .all()
    )

    return users

