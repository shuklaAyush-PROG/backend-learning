import test_setup
from app import app

client = app.test_client()

# Test 1: Fetch all students
response = client.get("/api/student")

assert response.status_code == 200

data = response.get_json()
assert isinstance(data, list)

print("GET all students: PASSED")

# Test 2: Fetch a student ID that should not exist
response = client.get("/api/student?id=999999")

assert response.status_code == 404

print("GET missing student: PASSED")

