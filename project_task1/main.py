from book import Book
from member import Member

def main():
    # Establish books
    b1 = Book("Python Programming", "Programming", "Teacher Smith")
    b2 = Book("Data Structures", "Computer Science", "Professor Johnson")
    b3 = Book("Introduction to Algorithms", "Computer Science", "Professor Brown")
    b4 = Book("Artificial Intelligence", "Technology", "Expert Davis")

    # Create members
    user = Member("John", 20)

    # Simulation operation
    print(f"--- {user.name}'s borrowing operations ---")
    user.borrow_book(b1)
    user.borrow_book(b2)
    user.borrow_book(b3)
    user.borrow_book(b4)  # This will likely fail because it exceeds MAX_BOOKS (3).

    user.list_borrowed_books()

    print("\n--- Book return operations ---")
    user.return_book(b1)
    user.list_borrowed_books()

if __name__ == "__main__":
    main()