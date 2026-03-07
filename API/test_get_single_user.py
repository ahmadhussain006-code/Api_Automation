import requests


def test_get_single_user():

    BASE_URL = "https://jsonplaceholder.typicode.com"

    endpoint = "/posts/1"
    url = BASE_URL + endpoint

    # Send GET request
    response = requests.get(url)

    # Print response for debugging
    print(response.json())

    # Validate status code
    assert response.status_code == 200
    print("Status Code:", response.status_code)

    # Validate response time
    response_time = response.elapsed.total_seconds()
    print("Response Time:", response_time)

    assert response_time < 2

    # Convert response to JSON
    body = response.json()

    # Validate response structure
    assert "userId" in body
    assert "id" in body
    assert "title" in body
    assert "body" in body

    # Validate specific values
    assert body["id"] == 1
    assert body["userId"] == 1