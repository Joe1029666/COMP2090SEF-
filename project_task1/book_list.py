class BookList:
    def __init__(self):
        self._books = []          

    def add_book(self, book):
        if book not in self._books:
            self._books.append(book)
            return True
        return False

    def remove_book(self, book):
        if book in self._books:
            self._books.remove(book)
            return True
        return False

    def contains(self, book):
        return book in self._books

    def is_empty(self):
        return len(self._books) == 0

    def find_by_name(self, name):
        for book in self._books:
            if book.name == name: # Fix here
                return book
        return None

    def __iter__(self):
        return iter(self._books)

    def __len__(self):
        return len(self._books)