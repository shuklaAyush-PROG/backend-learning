
import requests

base_url = "http://127.0.0.1:5000/api/student"

# Test 1: Existing student
response = requests.get(base_url, params={"id": 1})
print("Existing student:", response.status_code)
print(response.json())

# Test 2: Student that does not exist
response = requests.get(base_url, params={"id": 99})
print("\nMissing student:", response.status_code)
print(response.json())

# Test 3: Invalid course filter
response = requests.get(
    base_url,
    params={"id": 1, "course": "BTech CSE"}
)
print("\nCourse mismatch:", response.status_code)
print(response.json())
response = requests.post(
    base_url,
    json={
        "name": "Amit",
        "age": -5,
        "course": "BTech IT"
    }
)

print("\nInvalid age:", response.status_code)
print(response.json())
