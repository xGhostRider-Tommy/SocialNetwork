import flask
from flask import Flask, request, render_template, make_response, render_template_string, abort

from SocialNetwork.User import User

RESET: bool = True

app = Flask(__name__)

@app.errorhandler(404)
def ErrorHandler():
    return render_template("404.html")

@app.route("/")
def Homepage():
    return flask.render_template("homepage.html")

@app.route("/login", methods = ["POST", "GET"])
def Login():
    if request.method == "GET":
        return flask.render_template("login.html")

    elif request.method == "POST":
        username: str = request.form['username']
        password: str = request.form['password']

        sessionID = User.Login(username, password)

        if sessionID is not str:
            error: str
            if sessionID:
                error = "Wrong password!"
            else:
                error = "No user!"
            return render_template("login.html", error = error)

        response: flask.Response = make_response(render_template_string("<h1>\"Yeiiiii\", Mia moglie 2025</h1>"))
        response.set_cookie("SessionID", sessionID)  # 7 days

        return response
    else:
        abort(404)

@app.route("/register", methods = ["POST", "GET"])
def Register():
    if request.method == "GET":
        return flask.render_template("register.html")

    elif request.method == "POST":
        username: str = request.form['username']
        email: str = request.form["email"]
        password: str = request.form['password']

        sessionID = User.Register(username, email, password)

        if not sessionID:
            return render_template("register.html", error = "Name already exists!")

        response: flask.Response = make_response(render_template_string("<h1>\"Yeiiiii\", Mia moglie 2025</h1>"))
        response.set_cookie("SessionID", sessionID)  # 7 days

        return response
    else:
        abort(404)

if app.debug:
    from ClearData import ClearData
    print("Clearing data...")
    ClearData()