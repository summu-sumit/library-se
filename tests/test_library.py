import unittest
from src.library import Library, LibraryError


class TestLibrarySprint1(unittest.TestCase):

    def test_add_book_success(self):
        lib = Library()
        lib.add_book("B1", "Clean Code", "Robert Martin")
        self.assertIn("B1", lib.books)

    def test_add_duplicate_book(self):
        lib = Library()
        lib.add_book("B1", "Clean Code", "Robert Martin")
        with self.assertRaises(LibraryError):
            lib.add_book("B1", "Another Book", "Someone")


if __name__ == "__main__":
    unittest.main()
