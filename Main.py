from __future__ import annotations

import os

import flask
from flask import Flask, request, render_template, make_response, abort, redirect, url_for

from SocialNetwork.Globals import Globals
from SocialNetwork.User import User

RESET: bool = True

app = Flask(__name__)

@app.errorhandler(404)
def ErrorHandler():
    return render_template("404.html")

@app.route("/", methods = ["GET"])
def Homepage():
    return flask.render_template("homepage.html")

@app.route("/login", methods = ["POST", "GET"])
def Login():
    if request.method == "GET":
        return flask.render_template("login.html", min = Globals.MIN_LENGTH, max = Globals.MAX_LENGTH)

    elif request.method == "POST":
        username: str = request.form['username']
        password: str = request.form['password']

        sessionID = User.Login(username, password)

        if not isinstance(sessionID, str):
            error: str
            if sessionID:
                error = "Wrong password!"
            else:
                error = "No user!"
            return render_template("login.html", error = error, min = Globals.MIN_LENGTH, max = Globals.MAX_LENGTH)

        response: flask.Response = make_response(redirect(url_for("FeedRoute")))
        response.set_cookie("SessionID", sessionID)
        response.set_cookie("Username", username)

        return response
    else:
        abort(404)

@app.route("/register", methods = ["POST", "GET"])
def Register():
    if request.method == "GET":
        return flask.render_template("register.html", min = Globals.MIN_LENGTH, max = Globals.MAX_LENGTH)

    elif request.method == "POST":
        username: str = request.form['username']
        email: str = request.form["email"]
        password: str = request.form['password']

        if username == "" or email == "" or password == "":
            return render_template("register.html", error = "All fields are required!", min = Globals.MIN_LENGTH, max = Globals.MAX_LENGTH)

        sessionID = User.Register(username, email, password)

        if not isinstance(sessionID, str):
            error: str
            if isinstance(sessionID, bool):
                if sessionID:
                    error = f"Name should be between {Globals.MIN_LENGTH} and {Globals.MAX_LENGTH} characters long!"
                else:
                    error = "Name should contain only alphanumeric characters and/or '_'!"
            else:
                return "Name already exists!"

            return render_template("register.html", error = error, min = Globals.MIN_LENGTH, max = Globals.MAX_LENGTH)

        response: flask.Response = make_response(redirect(url_for("FeedRoute")))
        response.set_cookie("SessionID", sessionID)
        response.set_cookie("Username", username)

        return response
    else:
        abort(404)

@app.route("/feed", methods = ["GET", "POST"])
def FeedRoute():
    if request.method == "GET":
        return render_template("authenticate.html", action = "feed")
    elif request.method == "POST":
        return Authenticate()
    else:
        abort(404)

def Feed() -> str | flask.Response:
    return render_template("feed.html")

def Authenticate() -> str | flask.Response:
    user: User = User.Authenticate(request.form["username"], request.form["sessionID"])

    if isinstance(user, User):
        return Feed()
    else:
        return redirect(url_for("Login"))

@app.route("/logout", methods = ["GET"])
def Logout() -> str | flask.Response:
    response: flask.Response = make_response(redirect(url_for("Homepage")))
    response.delete_cookie("SessionID")
    response.delete_cookie("Username")

    return response

# GENERATE DATA DEFAULT CONTENTS IF NOT EXISTS
if not os.path.exists("Data"):
    os.mkdir("Data")
    os.mkdir("Data/Posts")
    file = open("Data/users.csv", "w")
    file.write("")
    file.close()

if app.debug:
    RESET: bool = True

    if RESET:
        from ClearData import ClearData

        print("Clearing data...")
        ClearData()