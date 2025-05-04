from Book import Book

class Library:
    def __init__(self):
        self.books = []
        self.borrowed = {}

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("Can only add Book objects")

    def borrow_book(self, book, user):
        if book in self.books and book.check_availability():
            self.books.remove(book)
            self.borrowed[book] = (user.get_first_name(), user.get_last_name())
            book.is_available = False
            return True
        else:
            return False

    def return_book(self, book):
        if book in self.borrowed:
            self.books.append(book)
            del self.borrowed[book]
            book.is_available = True
            return True
        return False

    def show_books(self):
        if self.books:
            print("Available books:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books available.")

    def get_available_books(self):
        return self.books

    def get_borrowed_books(self):
        return self.borrowed