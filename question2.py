# Task 1
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_new_book(book_title, book_author):
    book_tuple = (book_title, book_author)
    if book_tuple not in library:
        library.append(book_tuple)
        print("Successfully added book!")
    else:
        print("This book is already in the library.")

add_new_book("Harry Potter", "JK Rowlings")
add_new_book("1984", "George Orwell")
