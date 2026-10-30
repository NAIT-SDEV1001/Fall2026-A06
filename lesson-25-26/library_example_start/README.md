# Classes and Objects

## Why is this important?

Classes and objects are a way to organize your code and data. They are a way to model real world objects in code. There's a whole bunch of benefits of using classes and objects, let's take a look at a few of them.
- Encapsulation
  - This is a fancy word that means that you can group data and functions together.
- Reusability/Code maintenance
  - You can reuse classes and objects in your code.
- Abstraction
  - This is a fancy word that means that you can hide the details of how something works.
- Many other benefits that you'll learn more about the more you program like inheritance, polymorphism and much more.

When programming in Python and using the immense ecosystem, many times you'll inherit from classes that other people have written. This is a great way to supercharge your code and get a lot of functionality for free.

## What are we going to do?

We're going to build an application that will help us keep track of books in a library. We'll be able to add books to our library, remove books from our library, see all the books in our library, and find a book in our library.

In this example, we'll have two classes, a `Book` class and a `Library` class. The `Book` class will represent a single book and the `Library` class will represent a collection of books.

## A note on type hints

Starting with this lesson, we'll use **type hints** in our Python code. A type hint tells Python (and other developers reading your code) what type a function expects for its parameters and what type it returns.

Here's a tiny example without a class:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```
- `name: str` says the `name` parameter is expected to be a `str`.
- `-> str` says the function returns a `str`.
- If a function doesn't return anything, we use `-> None`.

A few things to keep in mind:
- **Hints are documentation, not enforcement.** Python won't raise an error if you call `greet(42)` — it'll just run. Tools like editors and linters use the hints to warn you, but they don't change runtime behaviour. Some programming languages, like C#, require types to be specified.
- **All methods get hints** — including dunder methods like `__init__` (which returns `None`) and `__str__` (which returns `str`).
- **For lists**, write `list[Book]` to mean "a list of `Book` objects".
- **For "X or nothing"**, write `X | None`. We'll see this later in the lesson when we write a method that searches for a book and might not find one.

For more on Python type hints see visit the official documentation https://docs.python.org/3/library/typing.html.

## Steps

1. let's create a file named `library_app.py` in this folder. This is going to be where we write the main pieces of our code.
Let's also add a bit of code here:
```python
if __name__ == '__main__':
    print("Welcome to our library App")
    print("--------------------------")
```
2. We're going to create a directory named `library_tools` inside of the current folder so that we can keep our code organized. 
- Inside of the library folder to be able to import anything into this folder, we need to create a file named `__init__.py`. This file can be empty, but it needs to exist. 
  - This file is telling Python that this folder is a **Python package** and that it can be imported.
3. Inside of the `library_tools` folder, let's create a file named `book.py`. This is where we'll write our `Book` class. Let's create it below.
```python
class Book:
    def __init__(self, title: str, author: str, pages: int, price: float) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
```
- This will be our blueprint for what a book is, but this isn't a book yet. In the next step, we'll import this into our `library_app.py` file and create a book.
- Note that in Python classes are named in `PascalCase` and functions are named in `snake_case`. This is a convention that is used in Python.
- The function `__init__` is called a constructor. This is a special function that is called when you create an instance of a class. 
  - The first argument of this function is always `self`. This is a reference to the instance of the class that is being created. 
  - The other arguments are the arguments that are passed in when the class is created. 
  - In this case, we're passing in `title`, `author`, `pages`, and `price`. 
  - We're then setting the attributes of the class to the values that are passed in.
- Notice the type hints on the parameters (`title: str`, `pages: int`, etc.) and the `-> None` after `__init__`. `__init__` doesn't return a value — its job is to set up `self` so its return type is `None`.
4. Let's import our `Book` class into our `library_app.py` file and create a book. We can do this by adding the following line to the top of our file.
```python
from library_tools.book import Book

if __name__ == '__main__':
    print("Welcome to our library App")
    print("--------------------------")
    book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1000, 24.99)
    # let's print the books properties.
    print("The properties of our book are:")
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    # let's print the book.
    print("The book is:")
    print(book)
```
- Two quick notes about the syntax above:
  - We create a `Book` by calling the class like a function: `Book("...", "...", 1000, 24.99)`. In some other languages (like Java or C#) you'd use a `new` keyword to do this — in Python, you just call the class.
  - We use dot notation (`book.title`, `book.author`) to read attributes.
- Now if you run the program you'll get output that looks like this.
```
$ python library_app.py
Welcome to our library App
--------------------------
The properties of our book are:
Title: The Lord of the Rings
Author: J.R.R. Tolkien
The book is:
<library_tools.book.Book object at 0x0000011EF5A57D60>
```
- Note that the last line here is a little weird. This because we haven't told python how to print our book. We're going to use *double underscore* (also called *dunder*) methods to do this. 

5. Let's add a `__str__` method to our `Book` class. This is a special method that is called when you try to convert an object to a string. Let's add it to our `Book` class in the `library_tools/book.py` file.
```python
class Book:
    def __init__(self, title: str, author: str, pages: int, price: float) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    # representation of our object when
    # we print it out in a string.
    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
```
- note that we're using the `self` keyword to access the attributes of the class.
- now if you run the program you'll get output that looks like this.
```
$ python library_app.py
Welcome to our library App
--------------------------
The properties of our book are:
Title: The Lord of the Rings
Author: J.R.R. Tolkien
The book is:
The Lord of the Rings by J.R.R. Tolkien
```
- If you look at the last line you have a nice representation of the book. This is much better than the output we had before.
- `__init__` and `__str__` are just two of the many dunder methods that you can use in Python. You can find a list of them [here](https://docs.python.org/3/reference/datamodel.html#special-method-names). In the next two steps, we'll add a few more dunder methods to our `Book` class to customize how books are compared.

6. Let's add an `__eq__` method to our `Book` class. This dunder method controls how Python checks whether two objects are equal (using `==`). For our library, let's say two books are "the same" if they have the same title (regardless of edition, page count, or author). Add it to `library_tools/book.py`:
```python
class Book:
    def __init__(self, title: str, author: str, pages: int, price: float) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

    # two books are considered equal if their titles match
    def __eq__(self, other: "Book") -> bool:
        return self.title == other.title
```
- To see this in action, you can **temporarily** compare a few books in `library_app.py`:
```python
book_one = Book("The Lord of the Rings", "J.R.R. Tolkien", 1000, 24.99)
book_two = Book("The Lord of the Rings", "Different Author", 500, 24.99)
book_three = Book("The Hobbit", "J.R.R. Tolkien", 300, 24.99)

print(book_one == book_two)     # True — same title
print(book_one == book_three)   # False — different title
```
- Without `__eq__`, Python compares whether the two variables point to the *same object in memory*, which is always `False` for separately created books, even if their titles match.
- "Equal" is up to you to define. You're not limited to one attribute. Some classes compare multiple attributes (title AND author, for example).
- You might notice `other: "Book"` is in quotes. That's because we're inside the `Book` class definition. The class isn't fully defined yet at this line, so we wrap the name in quotes as a **forward reference** to tell Python "this will be a `Book`, trust me." You'll see this any time a class refers to itself in its own type hints.
- `-> bool` because `__eq__` answers a yes/no question: are these two books equal?

7. Let's add `__gt__` and `__lt__` methods to compare books by price (greater-than and less-than). These are the dunder methods Python uses when you write `book_a > book_b` or `book_a < book_b`. Update `library_tools/book.py`:
```python
class Book:
    def __init__(self, title: str, author: str, pages: int, price: float) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

    # two books are considered equal if their titles match
    def __eq__(self, other: "Book") -> bool:
        return self.title == other.title

    # one book is "greater than" another if it costs more
    def __gt__(self, other: "Book") -> bool:
        return self.price > other.price

    # one book is "less than" another if it costs less
    def __lt__(self, other: "Book") -> bool:
        return self.price < other.price
```
- To see this in action, you can temporarily compare two books in `library_app.py`:
```python
expensive_book = Book("Hardcover Edition", "Author A", 500, 49.99)
cheap_book = Book("Paperback Edition", "Author B", 300, 12.99)

print(expensive_book > cheap_book)   # True — 49.99 > 12.99
print(expensive_book < cheap_book)   # False
```
- We chose `price` for the comparison, but you could just as easily compare by `pages` if you wanted to find the longest book. It's up to you to define what "greater than" and "less than" mean for your class.
- A nice side benefit: defining `__gt__` and `__lt__` also lets you sort a list of books with `sorted(books)`. Python uses these methods to order them.

8. Now let's add a `Library` class to our `library_tools/library.py` file. This is where we'll write our `Library` class. Let's create it below.
```python
class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books = []

    def __str__(self) -> str:
        return f"{self.name}"
```
- This is just the blueprint for a library. It has a name and a list of books.
- Let's import our `Library` class into our `library_app.py` file and create a library. We can do this by adding the following line to the top of our file.
  - Let's also create a library and remove all of the code that `print`s attributes about the book, along with the `__eq__` and `__gt__`/`__lt__` demos we added in the last two steps. Your `library_app.py` file should look like this:
```python
from library_tools.library import Library
from library_tools.book import Book

if __name__ == '__main__':
    print("Welcome to our library App")
    print("--------------------------")
    # create a library
    library = Library("Edmonton Public Library")
    print(library)

    book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1000, 24.99)
```
- You can see here that we imported the `Library` class the same way that we imported the `Book` class and also initialized it the same way (except with different arguments).
- Now if you run the program you'll get output that looks like this:
```
$ python library_app.py
Welcome to our library App
--------------------------
Edmonton Public Library
```
- Now we have a library, but we don't have any books in it. Let's add a method to our `Library` class that will allow us to add books to our library.
  
9. Create two functions to add and remove books from our library. Let's add them to our `Library` class in the `library_tools/library.py` file.
```python
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

```
- Note that here in the `add_book` method we're using `self.books.append(book)` to add a book to our list of books.
  - This works because the `self.books` was created in the `__init__` method, which is the constructor of the class.
- In the `list_books` we're going to loop through all of the books in our library and print them out.
  - You'll see that we're using the `__str__` method that we created in the `Book` class to print out the book.
- Notice the new `from library_tools.book import Book` import at the top. When you reference a class in a type hint, the class has to be imported.
- `add_book` and `list_books` both return `-> None` because they don't produce a return value, they just modify the library or print to the screen.
- Now let's add some code to our `library_app.py` file to use these methods.
```python
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

    book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1000, 24.99)
    library.add_book(book)

    # let's call the list books to see that we have one book!
    library.list_books()
```
- Notice that when we call `library.add_book(book)`, we only pass `book`, not `self`. Python automatically passes the object you're calling the method on (here, `library`) in as `self` behind the scenes. The method *definition* needs `self` as its first parameter, but you never pass it explicitly when *calling*.
- Let's go observe the output to see what happens here.
```
$ python library_app.py
Welcome to our library App
--------------------------
Edmonton Public Library
Current books in our library:
No books in our library
Current books in our library:
- The Lord of the Rings by J.R.R. Tolkien
```
- So you can see that we have no books in our library, then we add a book to our library, and then we have one book in our library.

10. Let's add a few more books to our library so that we can see how this works with more than one book. Let's add the following code to our `library_app.py` file.
```python
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
```
- Now if you take a look at the output here we can see that we have all of the books in our library.
```
$ python library_app.py
Welcome to our library App
--------------------------
Edmonton Public Library
Current books in our library:
No books in our library
Current books in our library:
- The Lord of the Rings by J.R.R. Tolkien
- The Wheel of Time by Robert Jordan
- The Way of Kings by Brandon Sanderson
- Mistborn by Brandon Sanderson
```

11. Sometimes we want to look up a book by its title — and the book might not be in the library. Let's add a `find_book` method to our `Library` class that returns the matching book, or `None` if no match is found. Add this to `library_tools/library.py`:
```python
class Library:
    # ... other methods ...

    # search for a book by title; returns the Book if found, or None
    def find_book(self, title: str) -> Book | None:
        for book in self.books:
            if book.title == title:
                return book
        return None
```
- The return type `Book | None` reads as "a `Book` **or** `None`". This is how we tell future readers (and tools like our editor) that this method might not find a match, so the caller needs to handle the `None` case.
- Now let's use it from `library_app.py`. Add this to the bottom of the `if __name__ == '__main__':` block:
```python
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
```
- Notice that we always check `if result is None` before using `result`. That's the discipline the `| None` return type is reminding us to follow. If you forget and just call `print(result.title)`, your program will crash on the second lookup.
- Running the program now adds these lines to the bottom of the output:
```
Found: Mistborn by Brandon Sanderson
Book not found
```

## Conclusion
This shows some of the fundamentals of class and objects in classes. Here's what we've learned a bit about:
- How to create a class
- How to create an instance of a class
- How to add attributes to a class
- How to add methods to a class
- How to use dunder methods like `__str__`, `__eq__`, `__gt__`, and `__lt__` to customize the behaviour of a class.
- How to use type hints to document method parameters and return values, including the `X | None` pattern for methods that might not find a result.
