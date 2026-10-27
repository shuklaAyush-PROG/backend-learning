

from flask import Flask, jsonify, request

app = Flask(__name__)

students = {
    "1": {
        "name": "Rahul",
        "age": 20,
        "course": "BTech IT"
    },
    "2": {
        "name": "Priya",
        "age": 19,
        "course": "BTech CSE"
    }
}


@app.route("/")
def home():
    return "Hello, world! My backend is working."


@app.route("/about")
def about():
    return "This is my first Flask backend project."


@app.route("/api/student", methods=["GET", "POST"])
def student_api():

    if request.method == "GET":
        student_id = request.args.get("id", "1")
        student_course = request.args.get("course")

        if student_id not in students:
            return jsonify({"error": "Student not found"}), 404

        student = students[student_id]

        if (
            student_course is not None
            and student["course"] != student_course
        ):
            return jsonify({"error": "Course mismatch"}), 404

        return jsonify(student), 200

    elif request.method == "POST":
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({"error": "Expected a JSON object"}), 400

        name = data.get("name")
        age = data.get("age")
        course = data.get("course")

        if (
            not isinstance(name, str)
            or not name.strip()
            or not isinstance(age, int)
            or isinstance(age, bool)
            or age <= 0
            or not isinstance(course, str)
            or not course.strip()
        ):
            return jsonify({
                "error": "Provide a name, positive integer age, and course"
            }), 400

        new_id = str(max(map(int, students.keys())) + 1)

        new_student = {
            "name": name.strip(),
            "age": age,
            "course": course.strip()
        }

        students[new_id] = new_student

        return jsonify({
            "id": new_id,
            **new_student
        }), 201


if __name__ == "__main__":
    app.run(debug=True)




