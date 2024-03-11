from abc import  ABC, abstractmethod
from book import Book
from iterator import Iterator, BookIterator


class Aggregator(ABC):
    @abstractmethod
    def get_iterator(self) -> Iterator:
        pass


class Library(Aggregator):
    def __init__(self, book_list: list[Book]):
        self.book_list = book_list

    def get_iterator(self) -> Iterator:
        return BookIterator(self.book_list)