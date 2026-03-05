#GET Request With Validations
import requests

def test_user_validate():

    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url)

    data = response.json()

    print("Status Code:", response.status_code)
    print("Response Time:", response.elapsed.total_seconds())

    assert response.status_code == 200
    assert data["id"] == 1
    assert response.elapsed.total_seconds() < 2