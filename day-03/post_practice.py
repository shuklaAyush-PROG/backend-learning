
import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "my Backend journey",
    "body": "My first POST request",
    "userId": 1
}

response = requests.post(url, json=data, timeout=10)

print("Status:", response.status_code)
data=response.json()
print("response:", data["id"])
