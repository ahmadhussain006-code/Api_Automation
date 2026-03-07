import requests

def test_get_user_list():

    BASE_URL = "https://jsonplaceholder.typicode.com"

    endpoint = "/posts"

    url = BASE_URL + endpoint

    # Send GET Request
    response = requests.get(url)

    # Print response for debugging
    print(response.json())

    # Validate Status Code
    assert response.status_code == 200
    print("Status Code:", response.status_code)

    # Validate Response Time (less than 2 seconds)
    response_time = response.elapsed.total_seconds()
    print("Response Time:", response_time)

    assert response_time < 3

    # Convert response to JSON
    body = response.json()

    # Validate Response is not empty
    assert len(body) > 0

    # Validate first post fields
    first_post = body[0]

    assert "userId" in first_post
    assert "id" in first_post
    assert "title" in first_post
    assert "body" in first_post

    # Validate specific data
    assert first_post["id"] == 1