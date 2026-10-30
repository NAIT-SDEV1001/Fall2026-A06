from library_tools.book import Book

class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books = list[Book] = []

    def __str__(self) -> str:
        return self.name

    def add_book(self, book: Book) -> bool:
        if book in self.books:
            return False

        self.books.append(book)
        return True

    def remove_book(self, title: str) -> bool:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False

    def list_books(self) -> None:
        for book in self.books:
            print(book)

    def find_book(self, title: str) -> Book | None:
        for book in self.books:
            if book.title == title:
                return book

        return None

    def find_books(self, title: str) -> list[Book]:
        return [book for book in self.books if book.title == title]