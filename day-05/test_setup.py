
import os
import sqlite3
from pathlib import Path

# Choose a separate database for tests
TEST_DATABASE_PATH = Path(__file__).resolve().parent / "test_students.db"

# Tell the application to use the test database
os.environ["DATABASE_PATH"] = str(TEST_DATABASE_PATH)

# Create the students table if it doesn't exist
with sqlite3.connect(TEST_DATABASE_PATH) as connection:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        )
    """)
