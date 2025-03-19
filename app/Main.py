from flask import Flask

app = Flask(__name__)

def homepage():
    return "Hello World!"

@app.route("/")
def homepage():
    return "Hello World!"

@app.route("/contatti")
def contatti():
    return "Contattaci!"