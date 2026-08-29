class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print(self.title, "has been borrowed.")

    def return_book(self):
        self.is_borrowed = False
        print(self.title, "has been returned.")


# Create 3 Book objects
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("Atomic Habits", "James Clear")

# Demonstrate borrowing and returning
book1.borrow()
book1.return_book()

book2.borrow()
book2.return_book()

book3.borrow()
book3.return_book()

