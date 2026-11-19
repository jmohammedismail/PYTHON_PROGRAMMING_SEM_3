"""Simple Library Management System using classes and objects."""

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if any(item.book_id == book.book_id for item in self.books):
            print("A book with this ID already exists.")
            return
        self.books.append(book)
        print(f'Book "{book.title}" added successfully.')

    def display_books(self):
        print("\n----- LIBRARY BOOKS -----")
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(f"{book.book_id} | {book.title} | {book.author} | {status}")

    def search_book(self, keyword):
        matches = [b for b in self.books
                   if keyword.lower() in b.title.lower()
                   or keyword.lower() in b.author.lower()]
        if matches:
            for book in matches:
                status = "Issued" if book.is_issued else "Available"
                print(f"{book.book_id} | {book.title} | {book.author} | {status}")
        else:
            print("No matching book found.")

    def issue_book(self, book_id):
        book = self.find_by_id(book_id)
        if book is None:
            print("Book ID not found.")
        elif book.is_issued:
            print("Book is already issued.")
        else:
            book.is_issued = True
            print(f'Book "{book.title}" issued successfully.')

    def return_book(self, book_id):
        book = self.find_by_id(book_id)
        if book is None:
            print("Book ID not found.")
        elif not book.is_issued:
            print("This book was not issued.")
        else:
            book.is_issued = False
            print(f'Book "{book.title}" returned successfully.')

    def find_by_id(self, book_id):
        return next((b for b in self.books if b.book_id == book_id), None)


def main():
    library = Library()
    library.add_book(Book(101, "Python Basics", "A. Kumar"))
    library.add_book(Book(102, "Object Oriented Programming", "R. Sharma"))
    library.add_book(Book(103, "Data Science with Python", "S. Iyer"))

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Display Books\n2. Search Book\n3. Issue Book")
        print("4. Return Book\n5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            library.display_books()
        elif choice == "2":
            library.search_book(input("Enter title or author: ").strip())
        elif choice == "3":
            try:
                library.issue_book(int(input("Enter book ID to issue: ")))
            except ValueError:
                print("Enter a valid numeric book ID.")
        elif choice == "4":
            try:
                library.return_book(int(input("Enter book ID to return: ")))
            except ValueError:
                print("Enter a valid numeric book ID.")
        elif choice == "5":
            print("Thank you for visiting the library.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
