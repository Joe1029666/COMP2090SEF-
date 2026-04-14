from book_list import BookList  

class Member:
    MAX_BOOKS = 3

    def __init__(self, name, age):
        self._name = name
        self.age = age  
        self._borrowed_books = BookList()

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        """Ensure age is greater than 0"""
        if value < 0:
            print("Warning: Age cannot be negative! Set to default value 0.")
            self._age = 0
        else:
            self._age = value
    
    def borrow_book(self, book):
        if len(self._borrowed_books) >= self.MAX_BOOKS:
            print(f"You have borrowed the maximum {self.MAX_BOOKS} books, cannot borrow more!")
            return False
        if self._borrowed_books.contains(book):
            print(f"You have already borrowed '{book.name}', cannot borrow again!")
            return False
    
        if book.borrow_book():
            self._borrowed_books.add_book(book)
            print(f"Successfully borrowed '{book.name}'")
            return True
        else:
            print(f"'{book.name}' is currently unavailable")
            return False
    
    def return_book(self, book):
        if self._borrowed_books.contains(book):
            if book.return_book():  
                self._borrowed_books.remove_book(book)
                print(f"{self.name} successfully returned '{book.name}'")
                return True
        else:
            print(f"You haven't borrowed '{book.name}'")
        return False

    def list_borrowed_books(self):
        if self._borrowed_books.is_empty():
            print("Currently no books borrowed")
        else:
            print(f"{self.name} has borrowed the following books:")
            for book in self._borrowed_books:
                print(f"  - '{book.name}' (Author: {book.author})")