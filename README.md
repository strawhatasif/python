# python
Just me exploring Python while learning more in my grad school course - BCIS 5390: Python Programming

## IDE and Textbook information
FYI - Python offers a free IDLE that is perfect for beginners!
* https://wiki.python.org/moin/BeginnersGuide/Download

My personal favorite is `PyCharm` which is offered by JetBrains!
* The community edition is free! https://www.jetbrains.com/pycharm/

For my graduate school course, I am renting a digital version of this textbook:
* *Starting Out With Python, 4th Edition* by Tony Gaddis.
* https://www.amazon.com/Starting-Out-Python-Tony-Gaddis-dp-0134444329/dp/0134444329/

## *How do I run these programs?*
* Run these programs using your terminal or command line tool.
* Type `python name_of_program.py` 
    * For example, `python print_favorite_things.py`
  
## *What about unit tests?*
* I explored a simple example for the `Greeting` class
* Using *pytest*, run this command `pytest -q test_greeting.py`
  
## *Bonus: files in the `rest_api` directory*
* On my own, I explored creating a simple REST API that invokes a public REST API.
  * This uses the *Flask* framework - https://flask.palletsprojects.com/en/2.0.x/quickstart/#
* It calls one API (https://jsonplaceholder.typicode.com/) and returns fake user data.
* Two endpoints - one for getting a collection of users and another for retrieving specific user data.

## Running the API and testing it
* *Prerequisite* - make sure `Flask` is installed
* switch to the `rest_api` directory
* in a terminal, run the following commands:
  * `set FLASK=development`
  * `set FLASK_APP=app.py`


* run the `flask run` command
* Invoke the API using your favorite API testing tool (OR, in the browser!).
    * I prefer Postman 
    * `GET` all users - `http://127.0.0.1:5000/users/`
    * `GET` one user - `http://127.0.0.1:5000/users/<id>`