from aggregator import Library
from book import Book

if __name__ == "__main__":
    books = [Book("HC Verma", 200), Book("Basic C", 230)]
    library = Library(books)

    book_iterator = library.get_iterator()
    while book_iterator.has_next():
        book = book_iterator.next()
        print(book.get_name(), book.get_price())
