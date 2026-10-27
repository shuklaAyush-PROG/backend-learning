import test_setup
from app import app

client = app.test_client()

# First, create a student to update
create_response = client.post(
    "/api/student",
    json={
        "name": "Before Update",
        "age": 20,
        "course": "IT"
    }
)

assert create_response.status_code == 201

student = create_response.get_json()
student_id = student["id"]

# Now update that student
response = client.put(
    f"/api/student/{student_id}",
    json={
        "name": "After Update",
        "age": 21,
        "course": "CSE"
    }
)

assert response.status_code == 200
print("PUT update: PASSED")

# Verify that the update was actually saved
check_response = client.get(
    f"/api/student?id={student_id}"
)

assert check_response.status_code == 200

updated_student = check_response.get_json()

assert updated_student["name"] == "After Update"
assert updated_student["age"] == 21
assert updated_student["course"] == "CSE"

print("Updated data verification: PASSED")

