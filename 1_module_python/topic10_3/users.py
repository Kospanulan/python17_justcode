
class User:

    def __init__(self, name):
        self.name = name
        self.books = []

    def take_book(self, book):
        self.books.append(book)
        book.set_availability(False)

    def return_book(self, book):
        self.books.remove(book)
        book.set_availability(True)

    def get_books(self):
        return self.books

