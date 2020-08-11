from .database_connection import DatabaseConnection

"""
Concerned with storing and retrieving books from a database file.
"""


database_file = 'data.db'


def create_book_table():
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)'
        )


def add_book(name, author):
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()

        cursor.execute(f'INSERT INTO books VALUES (?, ?, 0)', (name, author))


def get_all_books():
    books = []
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')

        books = [{'name': row[0], 'author': row[1], 'read': row[2]}
                 for row in cursor.fetchall()]

    return books


def mark_book_as_read(name):
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()

        # Tuple required as inputs to SQL query
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name, ))


def delete_book(name):
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?', (name, ))
