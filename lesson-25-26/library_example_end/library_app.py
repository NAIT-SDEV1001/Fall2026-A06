from library_tools.library import Library
from library_tools.book import Book

if __name__ == '__main__':
    print("Welcome to our library App")
    print("--------------------------")
    # create a library
    library = Library("Edmonton Public Library")
    print(library)
    # let's call the list books to observe that we have no books
    library.list_books()

    # a few books
    book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1000, 24.99)
    bookTwo = Book("The Wheel of Time", "Robert Jordan", 690, 19.99)
    bookThree = Book("The Way of Kings", "Brandon Sanderson", 1200, 29.99)
    bookFour = Book("Mistborn", "Brandon Sanderson", 640, 14.99)

    # add the books to our library
    library.add_book(book)
    library.add_book(bookTwo)
    library.add_book(bookThree)
    library.add_book(bookFour)

    # let's call the list books to see all of our books!
    library.list_books()

    # search for a book that's in our library
    result = library.find_book("Mistborn")
    if result is None:
        print("Book not found")
    else:
        print(f"Found: {result}")

    # search for a book that's NOT in our library
    result = library.find_book("Some Unknown Title")
    if result is None:
        print("Book not found")
    else:
        print(f"Found: {result}")
