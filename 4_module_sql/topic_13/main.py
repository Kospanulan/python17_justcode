from crud import create_post, get_user, get_post, get_posts_with_author_name
from database import Session


with Session() as session:

    posts = get_posts_with_author_name(
        session=session
    )

    for post in posts:
        print(post, f"Author name: {post.author_name}")


    # new_post = create_post(
    #     session=session,
    #     content="Seventh post for test 1",
    #     author_id=1
    # )
    # session.commit()

    # user = get_user(session=session, user_id=6)
    # session.delete(user)
    # session.commit()

    # post = get_post(session=session, post_id=6)
    # print("==================================================")
    # print(post)
    # print("==================================================")
    # print(post.author)


