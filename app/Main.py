import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def Homepage():
    return flask.render_template("homepage.html")

@app.route("/login")
def Login():
    return flask.render_template("login.html")

@app.route("/register")
def Register():
    return flask.render_template("register.html")