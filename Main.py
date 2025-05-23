from __future__ import annotations

import os

import flask
from flask import Flask, request, render_template, make_response, abort, redirect, url_for, send_from_directory

from SocialNetwork.Globals import Globals
from SocialNetwork.Hashtag import Hashtag
from SocialNetwork.Post import Post
from SocialNetwork.User import User
from Utils.Random import RandomStr
from Utils.UniqueList import UniqueList

app = Flask(__name__)

@app.route("/<path:filename>")
def HandleStatic(filename):
    return send_from_directory("static", filename)

@app.errorhandler(404)
def Error404(error):
    return render_template("404.html"), 404

@app.errorhandler(400)
def Error400(error):
    return render_template("400.html"), 400

@app.route("/", methods = ["GET"])
def Root():
    return redirect(url_for("Feed"))

@app.route("/homepage", methods = ["GET"])
def Homepage():
    return render_template("homepage.html")

@app.route("/login", methods = ["POST", "GET"])
def Login():
    if request.method == "GET":
        return flask.render_template(
            "login.html",
            min = Globals.MIN_USERNAME_LENGTH,
            max = Globals.MAX_USERNAME_LENGTH
        )

    elif request.method == "POST":
        username: str = request.form['username']
        password: str = request.form['password']

        sessionID: str = User.Login(username, password)

        if not isinstance(sessionID, str):
            error: str

            if sessionID:
                error = "Wrong password!"
            else:
                error = "No user!"

            return render_template(
                "login.html",
                error = error,
                min = Globals.MIN_USERNAME_LENGTH,
                max = Globals.MAX_USERNAME_LENGTH
            )

        response: flask.Response = make_response(redirect(url_for("Feed")))
        response.set_cookie("SessionID", sessionID)
        response.set_cookie("Username", username)

        return response
    abort(404)

@app.route("/register", methods = ["POST", "GET"])
def Register():
    if request.method == "GET":
        return flask.render_template(
            "register.html",
            min = Globals.MIN_USERNAME_LENGTH,
            max = Globals.MAX_USERNAME_LENGTH
        )

    elif request.method == "POST":
        username: str = request.form['username']
        email: str = request.form["email"]
        password: str = request.form['password']

        if username == "" or email == "" or password == "":
            return render_template(
                "register.html",
                error = "All fields are required!",
                min = Globals.MIN_USERNAME_LENGTH,
                max = Globals.MAX_USERNAME_LENGTH
            )

        sessionID: str = User.Register(username, email, password)

        if not isinstance(sessionID, str):
            error: str

            if isinstance(sessionID, bool):
                if sessionID:
                    error = f"Name should be between {Globals.MIN_USERNAME_LENGTH} and {Globals.MAX_USERNAME_LENGTH} characters long!"
                else:
                    error = "Name should contain only alphanumeric characters and/or '_'!"
            else:
                error = "Name already exists!"

            return render_template(
                "register.html",
                error = error,
                min = Globals.MIN_USERNAME_LENGTH,
                max = Globals.MAX_USERNAME_LENGTH
            )

        response: flask.Response = make_response(redirect(url_for("Feed")))
        response.set_cookie("SessionID", sessionID)
        response.set_cookie("Username", username)

        return response
    abort(404)

def Authenticate() -> tuple[bool, User]:
    user: User = User.Authenticate(request.form["username"], request.form["sessionID"])
    return isinstance(user, User), user

@app.route("/logout", methods = ["GET"])
def Logout() -> str | flask.Response:
    response: flask.Response = make_response(redirect(url_for("Feed")))
    response.delete_cookie("SessionID")
    response.delete_cookie("Username")

    return response

@app.route("/feed", methods = ["GET", "POST"])
def Feed():
    query: str = request.args.get("hashtag", default = "")

    if request.method == "GET":
        if query != "":
            query = "?hashtag=" + query

        return render_template(
            "authenticate.html",
            action = "/feed" + query
        )
    elif request.method == "POST":
        authenticateResult: tuple[bool, User] = Authenticate()
        if authenticateResult[0]:
            posts: list[Post]
            postsHtml: str = ""

            if query == "":
                posts = Post.getPosts()
            else:
                posts = Post.getPostsByHashtag(Hashtag(query))


            for post in posts:
                images: str = ""
                for image in post.Images:
                    images += render_template("feed.post.image.html", image = image)

                textButton: str
                if post.HasLiked(authenticateResult[1]):
                    textButton = "Unlike"
                else:
                    textButton = "Like"

                postsHtml += render_template(
                    "feed.post.html",
                    images = images,
                    author = post.Author.Name,
                    description = post.Description,
                    hashtags = str(post.Hashtags),
                    likes = post.Likes,
                    textButton = textButton,
                    id = post.Id
                )
            return render_template("feed.html", posts = postsHtml)
        return redirect(url_for("Homepage"))
    abort(404)

@app.route("/feed/like", methods=["POST"])
def LikePost():
    if request.method == "POST":
        authenticateResult: tuple[bool, User] = Authenticate()
        if authenticateResult[0]:
            id: int
            try:
                id = int(request.form["id"])
            except ValueError:
                abort(404)

            post: Post = Post(id)
            post.Like(authenticateResult[1])

            return redirect(url_for("Feed"))
    abort(400)

@app.route("/new_post", methods = ["GET", "POST"])
def NewPost():
    if request.method == "GET":
        return render_template(
            "authenticate.html",
            action = "/new_post"
        )
    elif request.method == "POST":
        authenticateResult: tuple[bool, User] = Authenticate()
        if authenticateResult[0]:
            return render_template("new_post.html")
        return redirect(url_for("Feed"))
    abort(404)

@app.route("/new_post/submit", methods = ["POST"])
def SubmitPost():
    if request.method == "POST":
        authenticateResult: tuple[bool, User] = Authenticate()
        if authenticateResult[0]:
            images = request.files.getlist('images')
            imagesList: list[str] = []

            for image in images:
                if image.filename == "":
                    pass

                extension: str = image.filename.split(".")[-1]
                filename: str = ""

                exists: bool = True
                while exists:
                    filename = RandomStr(254 - len(extension)) + "." + extension
                    exists = os.path.exists("static/images/" + filename)

                image.save("static/images/" + filename)
                imagesList.append(filename)

            hashtags: UniqueList[Hashtag] = UniqueList([])
            hashtagsStr: list[str] = (request.form["hashtags"]
                .replace(" #", " ")
                .replace("# ", " ")
                .replace("#", " ")
                .split(" ")
            )

            for hashtag in hashtagsStr:
                hashtags.Add(Hashtag(hashtag))

            authenticateResult[1].AddPost(
                request.form["description"],
                hashtags,
                UniqueList(imagesList)
            )
            return redirect(url_for("Feed"))
    abort(400)

# GENERATE DATA DEFAULT CONTENTS IF NOT EXISTS
if not os.path.exists("Data"):
    os.mkdir("Data")

    file = open("Data/users.csv", "w")
    file.write("")
    file.close()

    file = open("Data/posts.csv", "w")
    file.write("")
    file.close()
if not os.path.exists("static/images"):
    os.mkdir("static/images")

if app.debug: # per testing
    RESET_USERS: bool = False
    RESET_POSTS: bool = False

    if RESET_USERS or RESET_POSTS:
        from ClearData import ClearData

        print("Clearing data...")
        ClearData(RESET_USERS, RESET_POSTS)