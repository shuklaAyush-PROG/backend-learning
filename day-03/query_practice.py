
import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 2,
    "id":15
}

response = requests.get(url, params=params, timeout=10)

response.raise_for_status()

posts = response.json()

print("Total posts:", len(posts))
print("First post:", posts[0]["title"])
