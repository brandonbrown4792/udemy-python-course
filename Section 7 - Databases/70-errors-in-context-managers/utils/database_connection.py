import sqlite3


class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    # exc_type: Exception Type, exc_val: Exception Value, exc_tb: Exception Traceback
    # This exist to add exception handling to context managers
    # All of these inputs are None by default
    def __exit__(self, exc_type, exc_val, exc_tb):
        # If exception happens, close the connection, but don't commit anything
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
