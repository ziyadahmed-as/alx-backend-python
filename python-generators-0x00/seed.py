#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error
import uuid
import csv

def connect_db():
    """Connects to the MySQL database server"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_database(connection):
    """Creates the database ALX_prodev if it does not exist"""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
    except Error as e:
        print(f"Error creating database: {e}")

def connect_to_prodev():
    """Connects to the ALX_prodev database in MySQL"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ALX_prodev'
        )
        return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev database: {e}")
        return None

def create_table(connection):
    """Creates a table user_data if it does not exists with the required fields"""
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(10,0) NOT NULL,
                INDEX (user_id)
            )
        """)
        print("Table user_data created successfully")
        cursor.close()
    except Error as e:
        print(f"Error creating table: {e}")

def insert_data(connection, csv_file):
    """Inserts data in the database if it does not exist"""
    try:
        cursor = connection.cursor()
        
        # Read data from CSV file
        with open(csv_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                # Check if the user_id already exists
                cursor.execute("SELECT user_id FROM user_data WHERE user_id = %s", (row['user_id'],))
                result = cursor.fetchone()
                
                if not result:
                    # Insert new record
                    cursor.execute("""
                        INSERT INTO user_data (user_id, name, email, age)
                        VALUES (%s, %s, %s, %s)
                    """, (row['user_id'], row['name'], row['email'], row['age']))
        
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error inserting data: {e}")
    except FileNotFoundError:
        print(f"Error: File {csv_file} not found")