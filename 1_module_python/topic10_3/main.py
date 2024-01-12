# Alt + Enter
from books import Book
from libraries import Library
from users import User


library = Library()

book1 = Book('Гарри Поттер', 'Дж.К. Роулинг')
book2 = Book('1984', 'Оруэлл')
book3 = Book('book3', 'author3')

library.add_book(book1)
library.add_book(book2)

maxim = User('Max')

print("В библиотеке:", library.get_available_books())
print("У Максима:", maxim.get_books())

print("\nМаксим берет книгу из библиотеки...\n")
maxim.take_book(book1)

print("В библиотеке:", library.get_available_books())
print("У Максима:", maxim.get_books())

print("\nМаксим возвращает книгу в библиотеку...\n")
maxim.return_book(book1)

print("В библиотеке:", library.get_available_books())
print("У Максима:", maxim.get_books())


