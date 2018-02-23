from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', "POST"])
def sign_in_page():
    if request.method == "GET":
        return render_template("user_info.html")
    if request.method == "POST":
        # First check if this user exists (by email)
        # If user doesn't exist, create new user.
        #
        return 'YOU"RE ALL SIGNED UP '


if __name__ == '__main__':
    app.run()
