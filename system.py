import csv

class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"\n{self.title} has been borrowed.")
        else:
            print(f"\n{self.title} is already issued.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"\n{self.title} has been returned.")
        else:
            print(f"\n{self.title} is already available.")

    def display(self):
        status = "Available" if self.available else "Issued"

        print(f"Book ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Status  : {status}")
        print("-" * 40)


def show_books(book_list):

    print("\n========== BOOK LIST ==========\n")

    for i, book in enumerate(book_list, start=1):

        print(f"Book No. : {i}")
        book.display()

# Load books
books = []

with open("library_books_20.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        book = Book(
            row["Book_ID"],
            row["Title"],
            row["Author"]
        )

        books.append(book)


while True:

    print("\n===== LIBRARY MENU =====")
    print("1. Show Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number between 1 and 4.")
        continue

    if choice == 1:

        show_books(books)

    elif choice == 2:

        book_id = input("Enter Book ID: ")

        found = False

        for book in books:

            if book.book_id == book_id:

                book.borrow_book()
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == 3:

        book_id = input("Enter Book ID: ")

        found = False

        for book in books:

            if book.book_id == book_id:

                book.return_book()
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == 4:

        print("\nThank you for using Library Manager")
        break

    else:

        print("Invalid choice Please enter a number between 1 and 4.")