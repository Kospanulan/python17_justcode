from main import App, User

instagram = App()
current_user = None

while True:

    # ==== Main Menu =======================================
    print(f"\n\nДобро пожаловать! {current_user}\n"
          f"1. Регистрация\n"
          f"2. Создать пост\n"
          f"3. Показать все посты\n"
          f"4. Показать всеx юзеров\n"
          f"q. Выйти\n")

    user_input = input("Выберите из меню: ")

    if user_input == 'q':
        break

    # ==== Реализация опции ================================

    if user_input == '1':
        """Registration"""

        user_name = input("Имя юзера: ")
        user_surname = input("Фамилия юзера: ")

        current_user = User(user_name, user_surname)

        current_user.registration(instagram)
        print("Вы зарегистрировались!")
        continue
    elif user_input == '2':
        if current_user is None:
            print("Сперва нужно зарегистрироваться!")
            continue
        else:
            post_text = input("Ваш пост:\n")
            current_user.create_post(post_text)
            print("Ваш пост создан!")
            continue
    elif user_input == '3':
        print(f"Все посты: {instagram.get_all_posts()}")

    elif user_input == '4':
        print(f"Все юзеры: {instagram.get_all_users()}")


    # ==== Exit or Continue =================================
    print("1. В главное меню\n"
          "q. Выйти\n")

    user_input = input("Выберите из меню: ")

    if user_input == 'q':
        break

