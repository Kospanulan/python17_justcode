from books import Book
from libraries import Library
from users import User


def get_library_with_books():
    library = Library()

    book1 = Book('Гарри Поттер', 'Дж.К. Роулинг')
    book2 = Book('1984', 'Оруэлл')
    book3 = Book('book3', 'author3')

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    return library


