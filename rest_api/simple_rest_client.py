# this is a simple example of a rest client in Python

import requests


class SimpleRestClient:
    def __init__(self):
        print('initialized SimpleRestClient')

    def get_all_users(self):
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        print('the status code is? ' + str(response.status_code))
        print(response.json())
        return response.json()

    def get_single_user(self, identifier):
        response = requests.get('https://jsonplaceholder.typicode.com/users/' + identifier)
        print('the status code is? ' + str(response.status_code))
        print(response.json())
        return response.json()
