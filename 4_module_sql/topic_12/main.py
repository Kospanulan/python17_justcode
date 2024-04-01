from sqlalchemy.exc import IntegrityError

from database import Session

from crud1 import create_email, get_users, get_user_by_id, get_user_by_id_with_email, get_users_with_email, \
    get_users_with_email_test

with Session() as session:

    # new_email = create_email(email="test1@mail.ru", user_id=2, session=session)
    # session.commit()

    # users = get_users(session)
    # for user in users:
    #     print(f"Name: {user.name}")
    #     print("=============")

    # get, update and delete
    # user = get_user_by_id(user_id=3, session=session)
    # print(f"Name: {user.name}, Age: {user.age}")

    # user.age = 199

    # session.delete(user)
    # session.commit()

    # user, email = get_user_by_id_with_email(user_id=2, session=session)
    # print(f"Name: {user.name}, Age: {user.age}")
    # print(f"Email: {email.email}")

    # result = get_users_with_email(session=session)
    # for user, email in result:
    #     print(f"Name: {user.name}, Age: {user.age}")
    #     if email:
    #         print(f"Email: {email.email}")
    #     print("=============")

    users = get_users_with_email_test(session=session)
    for user in users:
        print(f"Name: {user.name}\n"
              f"Age: {user.age}\n"
              )
        for email in user.email:
            print(f"Email: {email.id}")
            print(f"Email: {email.email}")

        print("=============")


































    # try:
    #     session.commit()
    # except IntegrityError as err:
    #     print(f"Error: {err}")
    #     session.rollback()




