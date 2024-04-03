from crud.posts import create_post, get_post, get_posts_with_author_name
from crud.users import get_user, create_user, get_user_by_username

from database import Session

current_user = None
with Session() as session:
    print(f"Добро пожаловать!")
    while True:
        menu_text = f"\nМеню:\n"
        menu_items = []
        if current_user:
            menu_items.extend([f"Logout ({current_user.username})", "Create new post", "Get Posts", "Write Comment For Post"])
        else:
            menu_items.extend(["Registration", "Login"])

        for ind, item in enumerate(menu_items):
            menu_text += f"{ind + 1}. {item}\n"

        menu_text += f"q. Выйти из приложения\n"
        menu_text += f"Вы выбрали: "

        user_input = input(menu_text)

        if user_input == 'q':
            print("Вы вышли из приложения!\n")
            break

        if not current_user:
            if user_input == '1':
                new_username = input("Юзернейм нового пользователя: ")

                create_user(session, username=new_username)

                try:
                    session.commit()
                    print("Регистрация прошла успешно!\n")
                except:
                    print("Ошибка при регистрации\n")
                    session.rollback()
            elif user_input == '2':
                current_username = input("Введите ваш юзернейм: ")

                current_user = get_user_by_username(session, username=current_username)
                if current_user:
                    print(f"Вы успешно зашли от имени {current_user.username} "
                          f"по ID {current_user.id}!\n")
                else:
                    print("Этого юзера нет в базе!")
        # if current_user есть и вы залогинены
        else:
            if user_input == '1':  # Logout
                current_user = None
                print("Вы вышли из аккаунта!")

            elif user_input == '2':  # New Post
                content = input("Введите текст поста: ")

                new_post = create_post(
                    session=session,
                    content=content,
                    author_id=current_user.id
                )
                session.commit()
                print("Ваш пост создался успешно!\n")

            elif user_input == '3':  # Get Posts
                posts = get_posts_with_author_name(session)
                print("Все посты:\n")
                for post in posts:
                    print(post, f"Author name: {post.author_username}")
                print("\n")


