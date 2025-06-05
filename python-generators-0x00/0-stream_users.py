import mysql.connector
# This function streams rows from a MySQL database table
def stream_users():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",   
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield row

    cursor.close()
    connection.close()
