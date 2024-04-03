from crud.posts import create_post, get_post, get_posts_with_author_name
from crud.users import get_user, create_user

from database import Session



if __name__ == '__main__':

    with Session() as session:

        posts = get_posts_with_author_name(
            session=session
        )

        for post in posts:
            print(post, f"Author name: {post.author_username}")

        # Creating a new post
        # new_post = create_post(
        #     session=session,
        #     content="Ninth post for test 3",
        #     author_id=3
        # )
        # session.commit()

        # Creating a new user
        # new_post = create_user(
        #     session=session,
        #     username="sasha"
        # )
        # session.commit()

        # user = get_user(session=session, user_id=3)
        # session.delete(user)
        # session.commit()

        # post = get_post(session=session, post_id=6)
        # print("==================================================")
        # print(post)
        # print("==================================================")
        # print(post.author)


