# this class is responsible for managing the logic for retrieving a single user or all users
from rest_api import simple_rest_client


class UserService:
    def __init__(self):
        print('initialized UserService')

    def get_all_users(self):
        simple_client = simple_rest_client.SimpleRestClient()
        return simple_client.get_all_users()

    def get_single_user(self, identifier):
        simple_client = simple_rest_client.SimpleRestClient()
        return simple_client.get_single_user(identifier)
