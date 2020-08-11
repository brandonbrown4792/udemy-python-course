from typing import List, Dict, Union
from .database_connection import DatabaseConnection

"""
Concerned with storing and retrieving books from a database file.
"""


database_file = 'data.db'


# Set what function is expected to return
# This is a type hint and is not enforced by Python
def create_book_table() -> None:
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)'
        )


def add_book(name: str, author: str) -> None:
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()

        cursor.execute(f'INSERT INTO books VALUES (?, ?, 0)', (name, author))


# Must import from typing module
# Here we have a list of dictionaries with every key being a string and every value being either a string or integer
# def get_all_books() -> List[Dict[str, Union[str, int]]]:

# Alternatively, we can create our own types
# Capital letter is convention
Book = Dict[str, Union[str, int]]


def get_all_books() -> List[Book]:
    books = []
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')

        books = [{'name': row[0], 'author': row[1], 'read': row[2]}
                 for row in cursor.fetchall()]

    return books


# Use colon to set type of arguments
def mark_book_as_read(name: str) -> None:
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()

        # Tuple required as inputs to SQL query
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name, ))


def delete_book(name: str) -> None:
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?', (name, ))
