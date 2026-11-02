import csv

def add_book(file_path: str, book: dict) -> None:
    print(book)
    with open(file_path, 'a', newline='') as file:
        writer = csv.DictWriter(file, ["Author", "Title"])
        writer.writerow(book)

book = {
        "Author": "Author Name", 
        "Title": "Book Title"
        }

add_book("test.csv", book)