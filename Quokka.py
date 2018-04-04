from flask import Flask, render_template, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from pymongo import MongoClient



app = Flask(__name__)


# file = open("MONGODB_URI.key", 'r')
# MONGODB_URI = file.readline()
# file.close()
#
# client = MongoClient(MONGODB_URI)
# db = client.get_database('platters_hacks')


@app.route('/', methods=['GET'])
def landing_page():
    if request.method == "GET":
        return render_template("landing_page.html")
    else:
        return "Error, you've somehow landed on a broken page"


@app.route('/user_registration', methods=['GET', "POST"])
def sign_up():
    if request.method == "GET":
        return render_template("sign_up_page.html")
    if request.method == "POST":
        return "HI"
        # First check if this user exists (by email)
        # If user doesn't exist, create new user.


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login_page.html")
    if request.method == "POST":
        return "YOU'VE LOGGED IN"


if __name__ == '__main__':
    app.run()
