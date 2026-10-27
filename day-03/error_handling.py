
import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url, timeout=5)

    print("Status:", response.status_code)

    response.raise_for_status()

    data = response.json()
    print(data)

except requests.exceptions.Timeout:
    print("The request took too long.")

except requests.exceptions.HTTPError as error:
    print("The server returned an HTTP error:", error)

except requests.exceptions.RequestException as error:
    print("The request failed:", error)

except ValueError:
    print("The response could not be parsed as JSON.")
