
import sqlite3

connection = sqlite3.connect("students.db")

connection.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT
    )
""")

cursor = connection.execute(
    "SELECT id, name, age, course FROM students"
)

students = cursor.fetchall()

for student in students:
    print(student)

connection.close()


