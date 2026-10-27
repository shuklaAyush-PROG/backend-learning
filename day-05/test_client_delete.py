import test_setup
from app import app

client = app.test_client()

# 1. Create a student to delete
create_response = client.post(
    "/api/student",
    json={
        "name": "Student To Delete",
        "age": 20,
        "course": "IT"
    }
)

assert create_response.status_code == 201

student = create_response.get_json()
student_id = student["id"]

# 2. Delete the student
response = client.delete(f"/api/student/{student_id}")

assert response.status_code == 200
print("DELETE student: PASSED")

# 3. Verify the student no longer exists
check_response = client.get(f"/api/student?id={student_id}")

assert check_response.status_code == 404
print("Deleted student verification: PASSED")
