import uuid
from typing import List


class Book:
    def __init__(self, author: str, title: str):
        self.author: author = author
        self.title: title = title
        self.inn: uuid.UUID = uuid.uuid4()

    def __str__(self):
        return f"<Book {self.title} by {self.author} - {self.inn}>"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book_id: uuid.UUID):
        for book in self.books:
            if book.inn == book_id:
                self.books.remove(book)
                break

    def list_books(self):
        return self.books
