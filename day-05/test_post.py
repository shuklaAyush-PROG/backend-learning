
import requests

URL = "http://127.0.0.1:5000/api/student"

response = requests.post(
    URL,
    json={
        "name": "Test Student",
        "age": 21,
        "course": "IT"
    }
)

print("Status:", response.status_code)
print("Response:", response.json())
