from __future__ import annotations

import csv
from typing import TYPE_CHECKING

from Libs.Hashtag import Hashtag
from Utils.Hash import Hash, CheckHash
from Utils.UniqueList import UniqueList

if TYPE_CHECKING:
    from Libs.Post import Post

class User:
    __USERS_FILE = "Data\\users.csv"

    # do not use this
    def __init__(self, name: str):
        self.__Name: str = name

    # use this
    @staticmethod
    def Register(name: str, email: str, password: str) -> User | None:
        for user in User.getUsers():
            if user.__Name == name:
                return None

        passwordHash: str = Hash(password)

        file = open(User.__USERS_FILE, "a")
        file.write(f"{name};{email};{passwordHash}")

        file.close()

        return User(name)

    # User if success, int if error: True = wrong password, False = no user
    @staticmethod
    def Login(name: str, password: str) -> User | bool:
        users: list[User] = User.getUsers()
        currentUser: User = User("default") # placeholder

        userExists: bool = False
        for user in users:
            if user.Name == name:
                userExists = True
                currentUser = user
                break

        if userExists:
            if CheckHash(password, User.HashedPassword):
                return currentUser
        return userExists

    @staticmethod
    def getUsers() -> list[User]:
        file = csv.reader(open(User.__USERS_FILE, "r"))
        users: list[User] = []

        for line in file:
            users.append(User(line[0]))
        return users

    def getContent(self) -> list[str]:
        file = csv.reader(open(User.__USERS_FILE, "r"))

        for line in file:
            if line[0] == self.__Name:
                return line
        return [] # u should never reach this, but who knows, world is strange sometimes

    def AddPost(self, description: str, hashtags: UniqueList[Hashtag]):
        Post.CreatePost(self, description, hashtags)

    @property
    def Name(self):
        return self.__Name

    @property
    def Email(self):
        return self.getContent()[1]

    @property
    def HashedPassword(self):
        return self.getContent()[2]

    @property
    def Posts(self) -> list[Post]:
        posts: list[Post] = Post.getPosts()
        userPosts: list[Post] = []

        for post in posts:
            if post.User == self:
                userPosts.append(post)
        return userPosts
