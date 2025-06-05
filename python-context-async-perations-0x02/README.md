# Async SQLite Query Executor

This project demonstrates how to run multiple SQLite database queries concurrently using Python's `asyncio` and the `aiosqlite` library. It includes two asynchronous functions to fetch users from a database — all users and users older than 40 — and executes them in parallel using `asyncio.gather()`.

---

## 🚀 Features

- Asynchronous interaction with SQLite using `aiosqlite`
- Concurrent execution of queries with `asyncio.gather()`
- Clean and modular structure with type hints and docstrings
- Automatic database setup with sample data

## 📦 Requirements
- Python 3.7+
- [`aiosqlite`](https://pypi.org/project/aiosqlite/)a

Install dependencies using pip:
aiosqlite

## 🧩 Function Overview
| Function                    | Description                                                 |
| --------------------------- | ----------------------------------------------------------- |
| `initialize_database()`     | Sets up the database schema and inserts sample data         |
| `async_fetch_users()`       | Asynchronously retrieves all users from the database        |
| `async_fetch_older_users()` | Retrieves users older than 40 asynchronously                |
| `fetch_concurrently()`      | Executes both queries concurrently using `asyncio.gather()` |
