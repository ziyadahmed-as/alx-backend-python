
import mysql.connector
from mysql.connector import Error

# This function streams rows from a MySQL database table in batches
def stream_users_in_batches(batch_size): 
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="ALX_prodev"
    )
        
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            offset = 0
            
            while True:
                # Fetch a batch of users
                query = f"SELECT * FROM users LIMIT {offset}, {batch_size}"
                cursor.execute(query)
                batch = cursor.fetchall()
                
                if not batch:
                    break
                
                yield batch
                offset += batch_size
                
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

#processing each user in the batch
def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):  
        for user in batch:                             
            if user['age'] > 25:
                print(user)
