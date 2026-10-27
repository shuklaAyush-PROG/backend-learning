
import requests


def get_posts_by_user(user_id):
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        params = {"userId": user_id}

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()
        data = response.json()
        return data

    except requests.exceptions.Timeout:
        print("Timeout error")
        return None

    except requests.exceptions.HTTPError as error:
        print("HTTP error:", error)
        return None

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)
        return None

data=int(input("enter user id:"))
posts = get_posts_by_user(data)

if posts is not None:
    print("Number of posts:", len(posts))

    if posts:
        for post in posts:
            print(post["title"])
    else:
        print("No posts found.")
else:
    print("Unable to retrieve posts.")

 