from Author import Author
from Book import Book
from Library import Library
from User import User


def main():
    library = Library()

    print("Welcome to the Library Management System!")

    author1 = Author("John", "Doe")
    book1 = Book("Python Programming", author1)
    book2 = Book("Advanced Python", author1)
    library.add_book(book1)
    library.add_book(book2)

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    user = User(first_name, last_name)

    while True:
        print("\nMenu:")
        print("1. Show available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Show my borrowed books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("\nAvailable Books:")
            for book in library.get_available_books():
                print(f"- {book}")

        elif choice == "2":
            print("\nAvailable Books:")
            available_books = library.get_available_books()
            for count, book in enumerate(available_books, 1):
                print(f"{count}. {book}")

            if available_books:
                try:
                    book_num = int(input("Enter book number to borrow: ")) - 1
                    if 0 <= book_num < len(available_books):
                        book = available_books[book_num]
                        if user.borrow_book(library, book):
                            print(f"You've successfully borrowed '{book.get_title()}'")
                        else:
                            print("Failed to borrow the book.")
                    else:
                        print("Invalid book number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No books available to borrow.")

        elif choice == "3":
            borrowed_books = user.get_borrowed_books()
            if borrowed_books:
                print("\nYour Borrowed Books:")
                for count, book in enumerate(borrowed_books, 1):
                    print(f"{count}. {book}")

                try:
                    book_num = int(input("Enter book number to return: ")) - 1
                    if 0 <= book_num < len(borrowed_books):
                        book = borrowed_books[book_num]
                        if user.return_book(library, book):
                            print(f"You've successfully returned '{book.get_title()}'")
                        else:
                            print("Failed to return the book.")
                    else:
                        print("Invalid book number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("You haven't borrowed any books.")

        elif choice == "4":
            borrowed_books = user.get_borrowed_books()
            if borrowed_books:
                print("\nYour Borrowed Books:")
                for book in borrowed_books:
                    print(f"- {book}")
            else:
                print("You haven't borrowed any books.")

        elif choice == "5":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()