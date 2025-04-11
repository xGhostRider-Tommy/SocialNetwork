from __future__ import annotations

import os

import flask
from flask import Flask, request, render_template, make_response, abort, redirect, url_for

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
        return flask.render_template("login.html")

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
            return render_template("login.html", error = error)

        response: flask.Response = make_response(redirect(url_for("Feed")))
        response.set_cookie("SessionID", sessionID)
        response.set_cookie("Username", username)

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

        response: flask.Response = make_response(redirect(url_for("Feed")))
        response.set_cookie("SessionID", sessionID)
        response.set_cookie("Username", username)

        return response
    else:
        abort(404)

@app.route("/authenticate", methods = ["POST"])
def Authenticate():
    user: User = User.Authenticate(request.form["username"], request.form["sessionID"])
    print(user)
    if isinstance(user, User):
        return render_template("feed.html")
    else:
        return redirect(url_for("Login"))

@app.route("/feed", methods = ["GET"])
def Feed():
    return redirect(url_for("Authenticate"))


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