#POST Request (Create Data)

import requests

def test_create_user():

    url = "https://jsonplaceholder.typicode.com/users"

    payload = {
        "name": "Ahmad",
        "username": "qa_tester",
        "email": "ahmad@test.com"
    }

    response = requests.post(url, json=payload)

    data = response.json()

    print(data)

    assert response.status_code == 201
    assert data["name"] == "Ahmad"