import mysql.connector
from mysql.connector import errorcode
import csv
import uuid
#Connect to MySQL server (without specifying database).
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    # Create ALX_prodev database if it does not exist.
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

def connect_to_prodev():
    #Connect to the ALX_prodev database.
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to ALX_prodev: {err}")
        return None
#Create user_data table with specified schema if it does not exist.
def create_table(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id VARCHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL,
        INDEX (user_id)
    )
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Failed creating table: {err}")
#Insert data from CSV into user_data table, skip if user_id exists.
def insert_data(connection, csv_file):
    try:
        cursor = connection.cursor()

        # Read CSV rows
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Assume user_id already in CSV as UUID string
                user_id = row.get('user_id')
                name = row.get('name')
                email = row.get('email')
                age = row.get('age')

                # If user_id not present, generate UUID
                if not user_id:
                    user_id = str(uuid.uuid4())

                # Check if this user_id already exists
                cursor.execute("SELECT COUNT(*) FROM user_data WHERE user_id = %s", (user_id,))
                (count,) = cursor.fetchone()
                if count == 0:
                    cursor.execute(
                        "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                        (user_id, name, email, age)
                    )
        connection.commit()
        cursor.close()
    except FileNotFoundError:
        print(f"CSV file {csv_file} not found.")
    except mysql.connector.Error as err:
        print(f"Failed inserting data: {err}")

def stream_user_data(connection):
    """Generator to yield user_data rows one by one."""
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    row = cursor.fetchone()
    while row:
        yield row
        row = cursor.fetchone()
    cursor.close()
