# A simple REST API using Flask
from flask import Flask, jsonify
import users_service

app = Flask(__name__)

BASE_PATH = '/fun/users/'


@app.route(BASE_PATH)
def get_all_users():
    user = users_service.UserService()
    return jsonify(user.get_all_users())


@app.route(BASE_PATH + '<identifier>')
def get_one_user(identifier):
    user = users_service.UserService()
    return user.get_single_user(identifier)
