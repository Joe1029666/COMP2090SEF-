class Book:
    def __init__(self, name, book_type, author):
        self._name = name
        self._type = book_type 
        self._author = author
        self._borrowed = False
    
    @property
    def name(self):
        return self._name
  
    @property
    def author(self):
        return self._author

    @property
    def is_available(self):
        return not self._borrowed

    def borrow_book(self):
        if self._borrowed:
            return False
        self._borrowed = True
        return True

    def return_book(self):
        if self._borrowed:
            self._borrowed = False
            return True
        return False