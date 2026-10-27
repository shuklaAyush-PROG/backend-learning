
import requests

url = "http://127.0.0.1:5000/api/student"

new_student = {
    "name": "Amit",
    "age": 21,
    "course": "BTech IT"
}

response = requests.post(url, json=new_student)

print("Status:", response.status_code)
print("Response:", response.json())
