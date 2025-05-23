## Python Decorators – Database Operations
# 📘 Project Overview
This project showcases the power and flexibility of Python decorators in the context of SQLite3 database operations. By modularizing cross-cutting concerns such as logging, connection management, transaction control, error resilience, and caching, decorators help promote cleaner, more maintainable, and reusable code.

Each task within this project is designed to progressively build your understanding of how decorators can simplify and enhance database interaction in Python applications.

# 🗂️ Tasks Overview
Task 0: Logging Database Queries
Objective: Implement a log_queries decorator that logs each SQL query before execution.

# File: 0-log_queries.py

Task 1: Automatic Database Connection Handling
Objective: Create a with_db_connection decorator that automatically opens and closes database connections.

# File: 1-with_db_connection.py

Task 2: Transaction Management
Objective: Implement a transactional decorator to handle commit/rollback logic around database operations.

# File: 2-transactional.py
Task 3: Retry on Failure
Objective: Design a retry_on_failure decorator that retries database operations if transient errors occur.

# File: 3-retry_on_failure.py
Task 4: Caching Query Results
Objective: Develop a cache_query decorator that caches SQL query results to minimize redundant database access.

# File: 4-cache_query.py
# ✅ Requirements
To successfully run and test this project, ensure you have the following:

Python 3.8 or higher

SQLite3 installed and accessible

A SQLite database file named users.db containing a users table

Git and GitHub for version control and submission

SQLite and database operations

Exception handling in Python

# 📁 Directory Structure
python-decorators-0x01/
│
├── 0-log_queries.py             # Logs SQL queries
├── 1-with_db_connection.py      # Manages database connections
├── 2-transactional.py           # Implements transaction management
├── 3-retry_on_failure.py        # Adds retry mechanism for transient errors
├── 4-cache_query.py             # Implements query result caching
├── README.md                    # Project documentation