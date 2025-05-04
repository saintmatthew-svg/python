class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        self.isbn = self.generate_isbn()

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def get_author(self):
        return str(self.author)

    def check_availability(self):
        return self.is_available

    def generate_isbn(self):
        import random
        isbn = ""
        for _ in range(13):
            isbn += str(random.randint(0, 9))
        return isbn

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"