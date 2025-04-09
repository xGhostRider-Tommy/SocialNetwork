import flask
import os
from flask import Flask, request, render_template, make_response

from SocialNetwork.User import User

RESET: bool = True

app = Flask(__name__)

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

        response: flask.Response = make_response("\"Yeiiiii\", Mia moglie 2025")
        response.set_cookie("SessionID", sessionID, max_age=60*60*24*7) # 7 days

        return response
    else:
        return "Error!"

@app.route("/register")
def Register():
    return flask.render_template("register.html")

if app.debug:
    from ClearData import ClearData
    print("Clearing data...")
    ClearData()