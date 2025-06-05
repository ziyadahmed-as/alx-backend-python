#!/usr/bin/python3
import seed

# This script demonstrates how to lazily paginate through user data
def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

## This function uses the paginate_users function to lazily paginate through user data
# It yields pages of user data until there are no more pages to fetch
# It uses a generator to yield each page of user data
def lazy_pagination(page_size):
    
    offset = 0
    while True:  
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
