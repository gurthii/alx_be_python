class Book:
    """Base class for all book types."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for a generic book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """Derived class for electronic books."""
    def __init__(self, title, author, file_size):
        # 1. Calls the base class __init__ to initialize title and author
        super().__init__(title, author)
        # 2. Initializes the unique attribute
        self.file_size = file_size

    def __str__(self):
        """String representation for an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """Derived class for physical/print books."""
    def __init__(self, title, author, page_count):
        # 1. Calls the base class __init__ to initialize title and author
        super().__init__(title, author)
        # 2. Initializes the unique attribute
        self.page_count = page_count

    def __str__(self):
        """String representation for a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """Class demonstrating composition by managing a collection of books."""
    def __init__(self):
        # The 'books' attribute holds other objects (Book instances)
        self.books = []

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints details of each book in the library using polymorphism."""
        for book in self.books:
            # Polymorphism in action: 'book' will call the __str__ method 
            # of its actual class (Book, EBook, or PrintBook).
            print(book)