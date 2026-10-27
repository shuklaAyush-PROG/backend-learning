
import requests

url = "http://127.0.0.1:5000/api/student"

# Test 1: Missing required field
response = requests.post(
    url,
    json={
        "name": "Amit",
        "course": "BTech IT"
    }
)
print("Missing age:", response.status_code, response.json())


# Test 2: Incorrect age type
response = requests.post(
    url,
    json={
        "name": "Amit",
        "age": "twenty",
        "course": "BTech IT"
    }
)
print("Age as string:", response.status_code, response.json())


# Test 3: Negative age
response = requests.post(
    url,
    json={
        "name": "Amit",
        "age": -5,
        "course": "BTech IT"
    }
)
print("Negative age:", response.status_code, response.json())


# Test 4: Malformed JSON
response = requests.post(
    url,
    data='{"name": "Amit", "age": ',
    headers={"Content-Type": "application/json"}
)
print("Malformed JSON:", response.status_code, response.json())
# Test 5: Valid student data
response = requests.post(
    url,
    json={
        "name": "Amit",
        "age": 20,
        "course": "BTech IT"
    }
)

print("Valid request:", response.status_code, response.json())

# Test 6: Unsupported HTTP method
response = requests.put(
    url,
    json={
        "name": "Amit",
        "age": 20,
        "course": "BTech IT"
    }
)

print("Unsupported method:", response.status_code)
print(response.text)

# Test 7: Successful GET request
response = requests.get(url, params={"id": "1"})
print("Valid GET:", response.status_code, response.json())

# Test 8: Student does not exist
response = requests.get(url, params={"id": "999"})
print("Missing student:", response.status_code, response.json())

# Test 9: Unsupported method
response = requests.delete(url)
print("Unsupported method:", response.status_code, response.json())
