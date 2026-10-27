
import requests

BASE_URL = "http://127.0.0.1:5000/api/student"

# Create a test student
response = requests.post(BASE_URL, json={
    "name": "CRUD Test",
    "age": 20,
    "course": "IT"
})
print("CREATE:", response.status_code, response.text)
assert response.status_code == 201

student_id = response.json()["id"]

# Update that student
response = requests.put(f"{BASE_URL}/{student_id}", json={
    "name": "CRUD Test Updated",
    "age": 21,
    "course": "CSE"
})
print("UPDATE:", response.status_code, response.text)
assert response.status_code == 200

# Read that student
response = requests.get(BASE_URL, params={"id": student_id})
print("READ:", response.status_code, response.text)
assert response.status_code == 200
assert response.json()["name"] == "CRUD Test Updated"

# Delete that student
response = requests.delete(f"{BASE_URL}/{student_id}")
print("DELETE:", response.status_code, response.text)
assert response.status_code == 200

# Verify deletion
response = requests.get(BASE_URL, params={"id": student_id})
print("VERIFY DELETE:", response.status_code, response.text)
assert response.status_code == 404

print("All CRUD tests passed!")
