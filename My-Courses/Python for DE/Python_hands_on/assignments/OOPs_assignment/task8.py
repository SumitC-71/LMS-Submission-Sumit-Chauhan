'''
Task 8: Real-World Application
1. Create a class Library with attributes:
    ○ books(list of book titles)
2. Add methods to:
    ○ Display all books in the library.
    ○ Borrow abook (remove it from the list).
    ○ Return a book (add it back to the list).
3. Write a program to:
    ○ Create a Library object with an initial list of books.
    ○ Allow the user to interact with the library through a menu-driven program:
        ■ Display books
        ■ Borrow abook
        ■ Return a book
        ■ Exit

'''

class Library:

    def __init__(self, books):
        self.books = books

    def display_books(self):
        if len(self.books) == 0:
            print("No books available")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                print("-", book)

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"You borrowed '{book_name}'")
        else:
            print("Book not available")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"You returned '{book_name}'")


# initial books
library = Library([
    "Python Programming",
    "Data Structures",
    "Machine Learning",
    "Database Systems"
])


while True:

    print("\n===== Library Menu =====")
    print("1. Display Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()

    elif choice == "2":
        book = input("Enter book name to borrow: ")
        library.borrow_book(book)

    elif choice == "3":
        book = input("Enter book name to return: ")
        library.return_book(book)

    elif choice == "4":
        print("Exiting Library System")
        break

    else:
        print("Invalid choice")

