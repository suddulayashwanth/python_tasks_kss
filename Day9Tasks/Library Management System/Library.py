class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("File Size:", self.file_size, "MB")


ebook = EBook("Python Basics", "John", 500, 15)
ebook.display_details()