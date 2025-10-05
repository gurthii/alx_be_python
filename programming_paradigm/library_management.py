#!/usr/bin/env python3
"""
library_management.py: Implements Book and Library classes
to demonstrate OOP concepts like encapsulation and object interaction.
"""

class Book:
    """
    Represents a book in the library with title, author, and checkout status.
    """
    def __init__(self, title, author):
        """
        Initializes a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        # Public attributes
        self.title = title
        self.author = author
        # Private attribute (by convention, using a single underscore)
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Checks if the book is currently available."""
        return not self._is_checked_out

    def __str__(self):
        """String representation for user-friendly display."""
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects.
    """
    def __init__(self):
        """
        Initializes the Library with an empty list of books.
        The list is conventionally private (using a single underscore).
        """
        self._books = []

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book instance to add.
        """
        self._books.append(book)
        # print(f"Added book: {book.title}") # Optional log

    def find_book(self, title):
        """
        Helper method to find a Book object by title.

        Args:
            title (str): The title to search for.

        Returns:
            Book or None: The matching Book object, or None if not found.
        """
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        """
        Attempts to check out a book by title.

        Args:
            title (str): The title of the book to check out.
        """
        book = self.find_book(title)
        if book:
            if book.check_out():
                print(f"Successfully checked out: {title}")
            else:
                print(f"Error: {title} is already checked out.")
        else:
            print(f"Error: Book titled '{title}' not found.")

    def return_book(self, title):
        """
        Attempts to return a book by title.

        Args:
            title (str): The title of the book to return.
        """
        book = self.find_book(title)
        if book:
            if book.return_book():
                print(f"Successfully returned: {title}")
            else:
                print(f"Error: {title} was not checked out.")
        else:
            print(f"Error: Book titled '{title}' not found.")

    def list_available_books(self):
        """
        Prints the title and author of all books that are currently available.
        """
        available = [book for book in self._books if book.is_available()]
        
        if not available:
            print("No books are currently available.")
            return

        for book in available:
            print(str(book))
            
# The main execution logic will be in main.py, which imports this module.