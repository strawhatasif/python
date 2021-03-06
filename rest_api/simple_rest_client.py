# this is a simple example of a rest client in Python

import requests


class SimpleRestClient:
    def __init__(self):
        print('initialized SimpleRestClient')

    # returns all users
    def get_all_users(self):
        response = requests.get('https://jsonplaceholder.typicode.com/users')

        return response.json()

    # returns a single user based on an identifier
    def get_single_user(self, identifier):
        response = requests.get('https://jsonplaceholder.typicode.com/users/' + identifier)

        return response.json()
