from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    user_input = ''

    while user_input != 'q':
        user_input = input(USER_CHOICE)

        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        elif 'q':
            print('Quitting program')
        else:
            print('That is not a valid command')


def prompt_add_book():
    name = input('Please enter book name: ')
    author = input('Please enter author: ')
    database.add_book(name, author)


def list_books():
    database.list_books()


def prompt_read_book():
    name = input('Please enter book name: ')
    database.read_book(name)


def prompt_delete_book():
    name = input('Please enter book name: ')
    database.delete_book(name)


menu()
