
import requests


def get_posts_by_user(user_id):
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(
            url,
            params={"userId": user_id},
            timeout=5
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as error:
        print("Could not fetch posts:", error)
        return None


posts = get_posts_by_user(3)

if posts is not None:
    if posts:
        for post in posts:
            print(post["title"])
    else:
        print("No posts found.")
else:
    print("Unable to retrieve posts.")

    

