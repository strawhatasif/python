# this class is responsible for managing the logic for retrieving a single user or all users
import simple_rest_client


class UserService:
    # instantiate the SimpleRestClient
    simple_client = simple_rest_client.SimpleRestClient()

    def __init__(self):
        print('initialized UserService')

    # returns all users by invoking the REST client
    def get_all_users(self):
        return self.simple_client.get_all_users()

    # returns a single user based on an identifier by invoking the REST client
    def get_single_user(self, identifier):
        return self.simple_client.get_single_user(identifier)
