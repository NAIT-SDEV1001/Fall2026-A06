class Book:
    def __init__(self, title: str, author: str, pages: int, price: float) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, ${self.price}"

    def __eq__(self, other: Book) -> bool: # ==
        '''
        Check if this book is equal to another book
        '''
        return self.title == other.title

    def __gt__(self, other: Book) -> bool: # >
        '''
        Check if this book costs more than another book
        '''
        return self.price > other.price

    def __lt__(self, other: Book) -> bool: # <
        '''
        Check if this book costs less than another book
        '''
        return self.price < other.price