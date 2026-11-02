from library_tools.book import Book

if __name__ == '__main__':
    print("Welcome to our library app!")
    print("---------------------------")

    lotr = Book("The Lord of the Rings", "J.R.R. Tolkien", 1000, 24.99)

    print(lotr)

    twilight = Book("Twilight", "Whoever Wrote Twilight", 500, 14.99)
    twilight2 = Book("Twilight", "Whoever Wrote Twilight", 600, 17.99)

    print(twilight)

    encyclopeadia = Book("Encyclopeadia", "Everyone", 12000, 499.99)

    print(encyclopeadia)

    if twilight > encyclopeadia:
        print("Twilight costs more")
    else:
        print("Twilight costs less")

    print(twilight == twilight2)

