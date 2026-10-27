
from pathlib import Path
import sqlite3
from contextlib import closing
from flask import Flask, jsonify, request
from database import get_all_students, get_student_by_id , create_student , update_student_record , delete_student_record

app = Flask(__name__)

DATABASE_PATH = Path(__file__).resolve().parent.parent / "students.db"


def connect_db():
    return sqlite3.connect(DATABASE_PATH)



@app.route("/api/student", methods=["GET"])
def get_students():
    student_id = request.args.get("id")

    # Case 1: The client requests one specific student
    if student_id is not None:
        try:
            student_id = int(student_id)
        except ValueError:
            return jsonify({"error": "id must be an integer"}), 400

        student = get_student_by_id(student_id)

        if student is None:
            return jsonify({"error": "Student not found"}), 404

        return jsonify({
            "id": student[0],
            "name": student[1],
            "age": student[2],
            "course": student[3]
        }), 200

    # Case 2: The client requests all students
    students = get_all_students()

    result = []
    for student in students:
        result.append({
            "id": student[0],
            "name": student[1],
            "age": student[2],
            "course": student[3]
        })

    return jsonify(result), 200

@app.route("/api/student", methods=["POST"])
def add_student():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object"}), 400

    name = data.get("name")
    age = data.get("age")
    course = data.get("course")

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Name is required"}), 400

    if isinstance(age, bool) or not isinstance(age, int) or age <= 0:
        return jsonify({"error": "Age must be a positive integer"}), 400

    if not isinstance(course, str) or not course.strip():
        return jsonify({"error": "Course is required"}), 400

    connection = connect_db()

    student_id = create_student(name, age, course)

    return jsonify({
        "message": "Student created successfully",
        "id": student_id,
        "name": name.strip(),
        "age": age,
        "course": course.strip()
    }), 201
@app.route("/api/student/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object"}), 400

    name = data.get("name")
    age = data.get("age")
    course = data.get("course")

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Name is required"}), 400

    if isinstance(age, bool) or not isinstance(age, int) or age <= 0:
        return jsonify({"error": "Age must be a positive integer"}), 400

    if not isinstance(course, str) or not course.strip():
        return jsonify({"error": "Course is required"}), 400

    try:
        affected_rows = update_student_record(
             student_id, name, age, course
        )

        if affected_rows == 0:
         return jsonify({"error": "Student not found"}), 404     

                

        return jsonify({
            "message": "Student updated successfully",
            "id": student_id,
            "name": name.strip(),
            "age": age,
            "course": course.strip()
        }), 200

    except sqlite3.Error:
        app.logger.exception("Database error while updating student")
        return jsonify({"error": "Database operation failed"}), 500

@app.route("/api/student/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    try:
        affected_rows = delete_student_record(student_id)

        if affected_rows == 0:
         return jsonify({"error": "Student not found"}), 404


        return jsonify({
            "message": "Student deleted successfully",
            "id": student_id
        }), 200

    except sqlite3.Error:
        app.logger.exception("Database error while deleting student")
        return jsonify({"error": "Database operation failed"}), 500
    
if __name__ == "__main__":
    app.run(debug=True)
