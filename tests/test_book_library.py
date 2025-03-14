from models import Book, Library
import uuid

def test_create_book():
    book = Book("George Orwell", "1984")
    assert book.author == "George Orwell"
    assert book.title == "1984"
    assert isinstance(book.inn, uuid.UUID)


def test_book_str():
    book = Book("George Orwell", "1984")
    assert str(book).startswith("<Book 1984 by George Orwell")


def test_book_id():
    book1 = Book("Author1", "Book1")
    book2 = Book("Author2", "Book2")
    assert book1.inn != book2.inn




def test_add_book():
    library = Library("My Library")
    book = Book("Author", "Title")
    library.add_book(book)
    assert len(library.books) == 1


def test_remove_book():
    library = Library("My Library")
    book = Book("Author", "Title")
    library.add_book(book)
    library.remove_book(book.inn)
    assert len(library.books) == 0


def test_list_books():
    library = Library("My Library")
    book1 = Book("Author1", "Title1")
    book2 = Book("Author2", "Title2")
    library.add_book(book1)
    library.add_book(book2)
    books = library.list_books()
    assert len(books) == 2
