import seed
# This script demonstrates how to use a generator function to stream user ages and yield them one by one.
def stream_user_ages():
    
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    
    for row in cursor:
        yield row['age']

    cursor.close()
    connection.close()

#culculate average age using by streaming ages
def calculate_average_age():
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    if count == 0:
        print("No user data found.")
    else:
        average_age = total_age / count
        print(f"Average age of users: {average_age:.2f}")



if __name__ == "__main__":
    calculate_average_age()
