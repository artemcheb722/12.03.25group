import pytest

from models import Book, Library


@pytest.fixture
def example_book() -> Book:
    return Book(author="Arthur Conan Doyle", title="Sherlock Holms")


@pytest.fixture
def another_book() -> Book:
    return Book(author="Rowling", title="Harry Potter")


@pytest.fixture
def example_library() -> Library:
    return Library("City Library")
