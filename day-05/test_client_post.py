
import test_setup
from app import app
from database import get_student_by_id
client = app.test_client()

# Test 1: Create a student successfully
response = client.post(
    "/api/student",
    json={
        "name": "Test Client Student",
        "age": 20,
        "course": "IT"
    }
)

assert response.status_code == 201

data = response.get_json()


assert isinstance(data, dict)
assert data["name"] == "Test Client Student"
assert data["age"] == 20
assert data["course"] == "IT"

print("POST response content: PASSED")
student_id = data["id"]
saved_student = get_student_by_id(student_id)

assert saved_student is not None
assert saved_student[1] == "Test Client Student"
assert saved_student[2] == 20
assert saved_student[3] == "IT"

print("Database contents: PASSED")

# Test 2: Reject a student with a missing name
response = client.post(
    "/api/student",
    json={
        "age": 20,
        "course": "IT"
    }
)

assert response.status_code == 400

print("Invalid POST: PASSED")

