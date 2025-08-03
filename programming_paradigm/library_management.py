# library_management.py

class Book:
    """Represents a book with title, author, and availability status."""

    def __init__(self, title, author):
        self.title = title            # public attribute
        self.author = author          # public attribute
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out (unavailable)."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is currently available."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books and their availability."""

    def __init__(self):
        self._books = []  # private list of Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by title.
        If available, mark as checked out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        # If book not found or already checked out, do nothing

    def return_book(self, title):
        """
        Return a book by title.
        If checked out, mark as returned.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        # If book not found or already available, do nothing

    def list_available_books(self):
        """Print all books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
