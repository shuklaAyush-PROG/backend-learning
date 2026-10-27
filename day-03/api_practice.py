import requests 
url="https://jsonplaceholder.typicode.com/posts/1"
try:
    response=requests.get(url,timeout=10)
    response.raise_for_status()
    data=response.json()
    print("Title:", data["title"])
    print("Body:", data["body"])
except requests.exceptions.Timeout:
    print("The request took too long.")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)

except ValueError:
    print("The response could not be parsed as JSON.")    
print(response.status_code)
print(response.json())