#!/usr/bin/python3
"""
Module: library_system
Demonstrates inheritance (Book, EBook, PrintBook)
and composition (Library managing books).
"""


class Book:
    """
    Base class representing a generic book.

    Attributes:
        title (str): Title of the book.
        author (str): Author of the book.
    """

    def __init__(self, title, author):
        """
        Initialize the Book instance.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        String representation of a Book instance.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Class representing an electronic book (inherits from Book).

    Attributes:
        file_size (int): File size in KB.
    """

    def __init__(self, title, author, file_size):
        """
        Initialize the EBook instance.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.
            file_size (int): Size of the ebook in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        String representation of an EBook instance.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Class representing a printed book (inherits from Book).

    Attributes:
        page_count (int): Number of pages in the book.
    """

    def __init__(self, title, author, page_count):
        """
        Initialize the PrintBook instance.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.
            page_count (int): Number of pages.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        String representation of a PrintBook instance.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Class representing a library that contains books (composition).
    """

    def __init__(self):
        """
        Initialize the Library with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Add a book (Book, EBook, or PrintBook) to the library.

        Args:
            book (Book): The book instance to add.
        """
        self.books.append(book)

    def list_books(self):
        """
        Print details of all books in the library.
        """
        for book in self.books:
            print(book)
