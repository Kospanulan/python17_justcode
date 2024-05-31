
class Book:

    def __init__(self, title, author, genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year

    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title

    def __str__(self):
        return f"'{self.title}' {self.author}"


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, new_book):
        self.books.append(new_book)

    def show_books(self):
        for i, book in enumerate(self.books):
            print(f"{i+1}. {book}")

    def get_books(self):
        return self.books

    def get_book_by_name(self, book_name):
        for book in self.books:
            if book.title == book_name:
                return book

        return "Этой книги нет!"


book1 = Book("Harry Potter", "J.K. Roaling", "fantasy", 1998)
book2 = Book("1984", "Дж. Оруэл", "Антиутопия", 1899)

library = Library()

library.add_book(book1)
library.add_book(book2)

# library.show_books()


book_name = input("Book name to search for: ")
found_book = library.get_book_by_name(book_name)
print(found_book)












































