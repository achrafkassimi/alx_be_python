# library_management.py

class Book:
    def __init__(self, title, author):
        """Initialize the book with a title, author, and set it as not checked out."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Book starts off available

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book and mark it as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available (not checked out)."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {book}")
                    return True
                else:
                    print(f"Sorry, {book} is already checked out.")
                    return False
        print(f"Book '{title}' not found in library.")
        return False

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {book}")
                    return True
                else:
                    print(f"Book '{title}' was not checked out.")
                    return False
        print(f"Book '{title}' not found in library.")
        return False

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are available right now.")

