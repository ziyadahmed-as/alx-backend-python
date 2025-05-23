import sqlite3
import functools

query_cache = {}
# Decorator to log SQL queries before execution
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper
# Decorator to log SQL queries before execution
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        query = kwargs.get('query') or (args[1] if len(args) > 1 else None)
        if query in query_cache:
            print("Using cached result")
            return query_cache[query]
        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper
# Example of two decorators to manage the connection and cache the query result
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

users = fetch_users_with_cache(query="SELECT * FROM users")
users_again = fetch_users_with_cache(query="SELECT * FROM users")
