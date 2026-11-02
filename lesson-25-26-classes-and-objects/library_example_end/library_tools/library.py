from library_tools.book import Book


class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books = []

    def __str__(self) -> str:
        return f"{self.name}"

    # allows users to add books to our library
    def add_book(self, book: Book) -> None:
        self.books.append(book)

    # allows users to list all the books in our library
    def list_books(self) -> None:
        print("Current books in our library:")
        if len(self.books) == 0:
            print("No books in our library")
        for book in self.books:
            print(F"- {book}")

    # search for a book by title; returns the Book if found, or None
    def find_book(self, title: str) -> Book | None:
        for book in self.books:
            if book.title == title:
                return book
        return None
