class LibraryError(Exception):
    pass


class Library:
    def __init__(self):
        self.books = {}

    # Sprint-1
    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise LibraryError("Duplicate Book ID")
        self.books[book_id] = {
            "title": title,
            "author": author,
            "borrowed": False
        }

    # Sprint-2
    def borrow_book(self, book_id):
        if self.books[book_id]["borrowed"]:
            raise LibraryError("Book already borrowed")
        self.books[book_id]["borrowed"] = True

    def return_book(self, book_id):
        self.books[book_id]["borrowed"] = False

    # Sprint-3
    def generate_report(self):
        report = ["Book ID | Title | Author | Status"]
        for book_id, data in self.books.items():
            status = "Borrowed" if data["borrowed"] else "Available"
            report.append(
                f"{book_id} | {data['title']} | {data['author']} | {status}"
            )
        return "\n".join(report)
