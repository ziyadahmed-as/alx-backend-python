import sqlite3

class DatabaseConnection:
    """
    A custom context manager for managing SQLite database connections.
    Automatically opens and closes the connection.
    """
    #Initialize the DatabaseConnection context manager.
    #param db_path: Path to the SQLite database file.
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = None
        self.cursor = None
    #
    def __enter__(self):
        """
        Enter the runtime context and return the database cursor.
        """
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        return self.cursor
    #Exit method to close the connection and commit changes
    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the runtime context, committing changes if no exceptions occurred,
        and close the connection.
        """
        if self.connection:
            if exc_type is None:
                self.connection.commit()
            self.connection.close()

# Example usage of the DatabaseConnection context manager, This function demonstrates how to use the DatabaseConnection context manager
def main():
    database_path = 'example.db'

    # Initial setup: Create 'users' table and insert sample data (for demonstration)
    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
        cursor.executemany('INSERT INTO users (name) VALUES (?)', [('Alice',), ('Bob',)])
        conn.commit()

    # Use the custom context manager to query the database
    with DatabaseConnection(database_path) as cursor:
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()

        print("User Records:")
        for user in users:
            print(user)

if __name__ == '__main__':
    main()
