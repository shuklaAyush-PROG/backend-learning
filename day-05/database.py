import os
import sqlite3
from contextlib import closing
from pathlib import Path

DATABASE_PATH = Path(
    os.environ.get(
        "DATABASE_PATH",
        Path(__file__).resolve().parent.parent / "students.db"
    )
)

def get_all_students():
    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        cursor = connection.execute(
            "SELECT id, name, age, course FROM students"
        )
        return cursor.fetchall()


def get_student_by_id(student_id):
    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        cursor = connection.execute(
            "SELECT id, name, age, course FROM students WHERE id = ?",
            (student_id,)
        )
        return cursor.fetchone()

def create_student(name, age, course):
    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        with connection:
            cursor = connection.execute(
                """
                INSERT INTO students (name, age, course)
                VALUES (?, ?, ?)
                """,
                (name, age, course)
            )

            student_id = cursor.lastrowid

    return student_id

def update_student_record(student_id, name, age, course):
    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        with connection:
            cursor = connection.execute(
                """
                UPDATE students
                SET name = ?, age = ?, course = ?
                WHERE id = ?
                """,
                (name, age, course, student_id)
            )

            return cursor.rowcount

def delete_student_record(student_id):
    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        with connection:
            cursor = connection.execute(
                "DELETE FROM students WHERE id = ?",
                (student_id,)
            )

            return cursor.rowcount
