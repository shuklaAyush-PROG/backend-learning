
import test_setup
from app import app

client = app.test_client()

# Test 1: Invalid student ID in the query string
response = client.get("/api/student?id=abc")
assert response.status_code == 400
print("Invalid student ID: PASSED")

# Test 2: Student ID that doesn't exist
response = client.get("/api/student?id=999999")
assert response.status_code == 404
print("Nonexistent student: PASSED")

# Test 3: Negative age
response = client.post(
    "/api/student",
    json={
        "name": "Test Student",
        "age": -5,
        "course": "IT"
    }
)
assert response.status_code == 400
print("Negative age: PASSED")
