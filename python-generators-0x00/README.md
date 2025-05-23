# 🐍 MySQL User Data Seeder & Streamer
This project is a Python-based solution designed to efficiently handle large datasets stored in a MySQL database by utilizing Python generators. It covers everything from database setup to row-by-row and batch data processing.

## 🎯 Overview & Objective

The objective of this project is to:

- **Efficiently seed a MySQL database (`ALX_prodev`)** with sample user data.
- **Create a structured table (`user_data`)** with specific fields: `user_id`, `name`, `email`, and `age`.
- **Load user data from a CSV file (`user_data.csv`)**.
- **Stream user data from the database one row or batch at a time** using memory-efficient Python generators.
- **Demonstrate advanced generator usage** such as batch processing, lazy pagination, and aggregate computations (e.g., average age).

This project is ideal for those learning about efficient data processing, Python database integration, and generator functions.


## ⚙️ Features

- ✅ MySQL database connection and schema creation.
- ✅ CSV data seeding into the database.
- ✅ Row-by-row streaming using `yield` for memory efficiency.
- ✅ Batch data streaming and filtering logic.
- ✅ Lazy pagination simulation using offsets.
- ✅ Aggregate computation (e.g., average age) without SQL `AVG()`.

## 📁 Project Structure
├── seed.py # Core logic for DB setup, connection, insertion, and queries.

├── user_data.csv # Sample user dataset for database seeding.

├── 0-main.py # Executes single-row streaming and validation.

├── 1-main.py # Validates generator streaming from the database.

├── 2-main.py # Demonstrates batch processing of user data.

├── 3-main.py # Lazy pagination demo using generators.

├── 3-average_age.py # Calculates average age from streamed data.

├── README.md # Project documentation (this file).

## 📦 Requirements

Python 3.6+
MySQL Server
`mysql-connector-python` library

# bash
pip install mysql-connector-python
