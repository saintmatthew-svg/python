from unittest import TestCase
from Author import Author
from Book import Book
from Library import Library
from User import User

class TestLibrary(TestCase):
    def setUp(self):
        self.author = Author("John", "Doe")
        self.book = Book("Emeka gos to school", self.author)
        self.library = Library()
        self.user = User("matthew", "kachi")

    def test_add_book(self):
        self.library.add_book(self.book)
        self.assertIn(self.book, self.library.get_available_books())

    def test_borrow_book(self):
        self.library.add_book(self.book)
        success = self.user.borrow_book(self.library, self.book)
        self.assertTrue(success)
        self.assertIn(self.book, self.user.get_borrowed_books())
        self.assertNotIn(self.book, self.library.get_available_books())
        self.assertIn(self.book, self.library.get_borrowed_books())

    def test_return_book(self):
        self.library.add_book(self.book)
        self.user.borrow_book(self.library, self.book)
        success = self.user.return_book(self.library, self.book)
        self.assertTrue(success)
        self.assertNotIn(self.book, self.user.get_borrowed_books())
        self.assertIn(self.book, self.library.get_available_books())
        self.assertNotIn(self.book, self.library.get_borrowed_books())

    def test_book_representation(self):
        self.assertEqual(str(self.book), f"'{self.book.title}' by {self.author} (ISBN: {self.book.isbn})")

    def test_author_representation(self):
        self.assertEqual(str(self.author), "John Doe")

    def test_unavailable_book_borrow(self):
        self.library.add_book(self.book)
        self.user.borrow_book(self.library, self.book)
        another_user = User("matthew", "sam")
        success = another_user.borrow_book(self.library, self.book)
        self.assertFalse(success)

    def test_return_unborrowed_book(self):
        success = self.user.return_book(self.library, self.book)
        self.assertFalse(success)