from abc import ABC, abstractmethod
from book import Book


class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Book:
        pass


class BookIterator(Iterator):
    def __init__(self, books: list[Book]):
        self.books = books
        self.index = 0

    def has_next(self) -> bool:
        return self.index < len(self.books)

    def next(self) -> Book | None:
        result = None

        if self.has_next():
            result = self.books[self.index]
            self.index += 1

        return result
