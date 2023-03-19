import requests
from constants import TOKEN, URL


def request_data() -> list:
    response = requests.get(url=URL, headers={'X-Auth-Token': TOKEN})
    print(response)
    return response.json()['message']