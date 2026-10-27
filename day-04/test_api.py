
import requests

BASE_URL = "http://127.0.0.1:5000/api/student"

# Test 1: Existing student
response = requests.get(BASE_URL, params={"id": "1"})
assert response.status_code == 200
print("Test 1 passed: Existing student")

# Test 2: Missing student
response = requests.get(BASE_URL, params={"id": "999"})
assert response.status_code == 404
print("Test 2 passed: Missing student")

# Test 3: Unsupported method
response = requests.delete(BASE_URL)
assert response.status_code == 405
print("Test 3 passed: Unsupported method")

print("All tests passed!")
