# this is a simple example of a rest client in Python

import requests


def main():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    print('the status code is? ' + str(response.status_code))
    print(response.json())


main()
