import unittest
from src.library import Library, LibraryError


class TestLibrary(unittest.TestCase):

    # Sprint-1 Tests
    def test_add_book_success(self):
        lib = Library()
        lib.add_book("B1", "Clean Code", "Robert Martin")
        self.assertIn("B1", lib.books)

    def test_add_duplicate_book(self):
        lib = Library()
        lib.add_book("B1", "Clean Code", "Robert Martin")
        with self.assertRaises(LibraryError):
            lib.add_book("B1", "Another Book", "Someone")

    # Sprint-2 Tests
    def test_borrow_available_book(self):
        lib = Library()
        lib.add_book("B1", "Clean Code", "Robert Martin")
        lib.borrow_book("B1")
        self.assertTrue(lib.books["B1"]["borrowed"])

    def test_borrow_unavailable_book(self):
        lib = Library()
        lib.add_book("B1", "Clean Code", "Robert Martin")
        lib.borrow_book("B1")
        with self.assertRaises(LibraryError):
            lib.borrow_book("B1")

    def test_return_book(self):
        lib = Library()
        lib.add_book("B1", "Clean Code", "Robert Martin")
        lib.borrow_book("B1")
        lib.return_book("B1")
        self.assertFalse(lib.books["B1"]["borrowed"])

    # Sprint-3 Tests
    def test_report_contains_header(self):
        lib = Library()
        report = lib.generate_report()
        self.assertIn("Book ID | Title | Author | Status", report)

    def test_report_contains_book_entry(self):
        lib = Library()
        lib.add_book("B1", "Clean Code", "Robert Martin")
        report = lib.generate_report()
        self.assertIn("Clean Code", report)


if __name__ == "__main__":
    unittest.main()
