class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def set_author(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_author(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_author()