from users import User
from books import Book
from libraries import Library
from data import get_library_with_books

library = get_library_with_books()

maxim = User('Max')


print(f"Добро пожаловать в нашу Библиотеку!\n")
user_input = None

while user_input != 'q':
    print("Меню:\n"
          "1. Все доступные книги\n"
          "2. Взять книгу\n\n")

    user_input = input("Выберите из меню [1-2] ('q' - выйти): ")

    if user_input == '1':
        print(library.get_available_books())
    elif user_input == '2':
        books = library.get_available_books()
        for i in range(len(books)):
            print(f"{i}. {books[i]}")

        ind = int(input("Выберите книгу: "))

        maxim.take_book(books[ind])
        print("Приятного чтения!\n\n")
    elif user_input == 'q':
        print("До свидание!")
    else:
        print("Не правильная опция, прошу выбрать из меню!\n\n")





