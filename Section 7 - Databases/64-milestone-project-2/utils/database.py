"""
Concered with storing and retrieving books from a list
"""

books = []


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


def list_books():
    print(books)


def read_book(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True
            break
    else:
        print('Book was not found')


def delete_book(name):
    for book in books:
        if book['name'] == name:
            books.remove(book)
            break
    else:
        print('book was not found')
