import asyncio
import aiosqlite
from typing import List, Tuple

DATABASE_PATH = "example_async.db"

# Initialize the database and create the 'users' table
# This function is called once to set up the database.
async def initialize_database() -> None:

    #Initializes the database by creating the 'users' table and inserting sample records.
    #This function ensures the environment is ready for query execution.
    
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """)
        await db.executemany("""
            INSERT INTO users (name, age)
            VALUES (?, ?)
        """, [
            ("Alice", 30),
            ("Bob", 45),
            ("Charlie", 50),
            ("Diana", 28)
        ])
        await db.commit()

# Fetch all users from the 'users' table
async def async_fetch_users() -> List[Tuple[int, str, int]]:
    
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute("SELECT * FROM users")
        users = await cursor.fetchall()
        await cursor.close()
        return users

#this Method fetches users older than a specified age threshold
async def async_fetch_older_users(age_threshold: int = 40) -> List[Tuple[int, str, int]]:
    """
    Fetches users older than the specified age threshold.

    :param age_threshold: Minimum age to filter users.
    :return: A list of users older than the given age.
    """
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > ?", (age_threshold,))
        older_users = await cursor.fetchall()
        await cursor.close()
        return older_users

# Excute user fetch queries concurrently Function
async def fetch_concurrently() -> None:
    """
    Executes user fetch queries concurrently and prints the results.
    """
    await initialize_database()

    # Concurrent execution of both queries
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

    print("\n All Users:")
    for user in all_users:
        print(user)

    print("\n Users Older Than 40:")
    for user in older_users:
        print(user)


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
