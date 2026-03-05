import requests

def test_getUser():

    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    print(response.json())

    assert response.status_code == 200
    print('Hussain')
    print('Shiza')
    print('Ahmad')