class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.borrowed_books = []

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def borrow_book(self, library, book):
        if library.borrow_book(book, self):
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, library, book):
        if book in self.borrowed_books:
            if library.return_book(book):
                self.borrowed_books.remove(book)
                return True
        return False

    def get_borrowed_books(self):
        return self.borrowed_books