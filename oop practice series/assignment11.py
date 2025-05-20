  #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES
#  assignment:
# create a class bookwith a class variable total_books. add a class method increment_book_count()
# to increase a count whhen a new book is added.

# solution

class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
book1 = Book(1,6)
book2 = Book(1,7)
book3 = Book(1,9)
book4 = Book(1,7)
book5 = Book(1,4)


print(f"Total Books Added: {Book.get_total_books()}")


