import json

import requests

"""This module is demoing an API request to sanic server"""


login_url = "http://127.0.0.1:8000/login"


def get_auth_token(username, password):
    url = login_url

    payload = json.dumps({
        "username": username,
        "pass": password
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text


def post_to_sanic(token):


    url = "http://127.0.0.1:8000/secret"

    payload = json.dumps([
        {
            "name": "device",
            "strVal": "iPhone",
            "metadata": "not interesting"
        },
        {
            "name": "isAuthorized",
            "boolVal": "false",
            "lastSeen": "not interesting"
        }
    ])


    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    token = get_auth_token("user1", "1234")
    post_to_sanic(token)
