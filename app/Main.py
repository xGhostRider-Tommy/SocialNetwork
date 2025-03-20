import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def Homepage():
    return flask.render_template("Homepage.html")

@app.route("/login")
def Login():
    return flask.render_template("Login.html")