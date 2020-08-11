import sqlite3

connection = sqlite3.connect('data.db')

# All operations are made with cursors, and not with the connection. This is because we can only have one connection.
# Multiple cursors can read at the same time
cursor = connection.cursor()

# Commit means save the result of the query to the disk (database)
cursor.execute('Your SQL QUERY HERE')
connection.commit()

connectio.close()
