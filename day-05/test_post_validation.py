
import requests

URL = "http://127.0.0.1:5000/api/student"

test_cases = [
    {
        "name": "Missing name",
        "data": {"age": 20, "course": "IT"},
        "expected": 400
    },
    {
        "name": "Age as text",
        "data": {"name": "Rahul", "age": "twenty", "course": "IT"},
        "expected": 400
    },
    {
        "name": "Negative age",
        "data": {"name": "Rahul", "age": -5, "course": "IT"},
        "expected": 400
    },
    {
        "name": "Valid student",
        "data": {"name": "Validation Test", "age": 20, "course": "IT"},
        "expected": 201
    }
]

for test in test_cases:
    response = requests.post(URL, json=test["data"])

    print(
        test["name"],
        "| Expected:", test["expected"],
        "| Actual:", response.status_code
    )

    assert response.status_code == test["expected"]

print("All validation tests passed!")
