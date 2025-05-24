import sqlite3
from typing import Any, List, Tuple, Optional


class ExecuteQuery:
    """
    A reusable context manager that manages database connection and executes
    a given SQL query with optional parameters.
    """
    # Initialize the ExecuteQuery context manager and Initialize the context manager, param query: SQL query to be executed.
    # param params: Optional parameters for the query.
    def __init__(self, db_path: str, query: str, params: Optional[Tuple[Any, ...]] = None):
       
        self.db_path = db_path
        self.query = query
        self.params = params or ()
        self.connection = None
        self.cursor = None
        self.results = []

    def __enter__(self) -> List[Tuple[Any, ...]]:
        """
        Opens the database connection, executes the query, and returns the result.
        """
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        self.results = self.cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Ensures that the connection is closed when the context is exited.
        """
        if self.connection:
            self.connection.close()


# Example usage of the ExecuteQuery context manager, This function demonstrates how to use the ExecuteQuery context manager
def main():
    db_path = 'example.db'

    # Optional: Ensure users table exists with appropriate data
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
        cursor.executemany('INSERT INTO users (name, age) VALUES (?, ?)', [
            ('Abdi', 30),
            ('Abeba', 20),
            ('Charles', 35)
        ])
        conn.commit()

    # Use ExecuteQuery to fetch users older than 25
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)

    with ExecuteQuery(db_path, query, params) as results:
        print("Users older than 25:")
        for row in results:
            print(row)


if __name__ == '__main__':
    main()
