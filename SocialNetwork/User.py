from __future__ import annotations

import csv
from datetime import datetime, timedelta

from SocialNetwork.Hashtag import Hashtag
from Utils.Hash import Hash, CheckHash
from Utils.Image import Image
from Utils.Random import RandomStr
from Utils.UniqueList import UniqueList


#from SocialNetwork.Post import Post # added at the end for circular import

class User:
    __USERS_FILE: str = "Data/users.csv"
    __SESSION_ID_DURATION: timedelta = timedelta(days = 7)
    __DATE_FORMAT: str = "%d/%m/%y"
    __SESSION_ID_LENGTH: int = 64 # 512 bit

    __Name: str

    # do not use this
    def __init__(self, name: str):
        self.__Name = name

    # use this
    # str (sessionID) if success, None if name already exists
    @staticmethod
    def Register(name: str, email: str, password: str) -> str | None:
        for user in User.getUsers():
            if user.__Name == name:
                return None

        passwordHash: str = Hash(password)

        file = open(User.__USERS_FILE, "a")
        file.write(f"{name};{email};{passwordHash};;\n")
        file.close()

        return User(name).GenerateSessionID()

    # str (sessionID) if success, bool if error: True = wrong password, False = no user
    @staticmethod
    def Login(name: str, password: str) -> str | bool:
        user = User.getUser(name)

        if user is None:
            return False

        if CheckHash(password, user.PasswordHash):
            return user.GenerateSessionID()
        return True

    # User if success, bool if error: True = wrong/expired sessionID, False = no user
    @staticmethod
    def Authenticate(name: str, sessionID: str) -> User | bool:
        user = User.getUser(name)

        if user is None:
            return False

        if CheckHash(sessionID, user.SessionIDHash):
            return user
        return True

    @staticmethod
    def getUsers() -> list[User]:
        file = csv.reader(open(User.__USERS_FILE, "r",), delimiter=";")
        users: list[User] = []

        for line in file:
            users.append(User(line[0]))
        return users

    # do not use this
    # User if exists, None if it doesn't
    @staticmethod
    def getUser(name: str) -> User | None:
        users: list[User] = User.getUsers()

        for user in users:
            if user.Name == name:
                return user
        return None

    def getContent(self) -> list[str]:
        file = csv.reader(open(User.__USERS_FILE, "r"), delimiter=";")

        for line in file:
            if line[0] == self.Name:
                return line
        return [] # u should never reach this, but who knows, world is strange sometimes

    def AddPost(self, description: str, hashtags: UniqueList[Hashtag], images: list[Image]):
        Post.CreatePost(self, description, hashtags, images)

    # can handle only one sessionID a time
    def GenerateSessionID(self) -> str:
        sessionID: str = RandomStr(self.__SESSION_ID_LENGTH)
        expiringDate: datetime = datetime.today() + self.__SESSION_ID_DURATION

        oldFile: list[list[str]] = list(csv.reader(open(User.__USERS_FILE, "r"), delimiter=";"))
        for i in range(len(oldFile)):
            if oldFile[i][0] == self.Name:
                oldFile[i][3] = Hash(sessionID)
                oldFile[i][4] = expiringDate.strftime(self.__DATE_FORMAT)
                break

        file = open(self.__USERS_FILE, "w")

        for line in oldFile:
            file.write(f"{line[0]};{line[1]};{line[2]};{line[3]};{line[4]}\n")
        file.close()

        return sessionID

    @property
    def Name(self) -> str:
        return self.__Name

    @property
    def Email(self) -> str:
        return self.getContent()[1]

    @property
    def PasswordHash(self) -> str:
        return self.getContent()[2]

    # None if the hash is expired
    @property
    def SessionIDHash(self) -> str | None:
        content: list[str] = self.getContent()

        sessionIDHash: str = content[3]
        expiringDate: datetime = datetime.strptime(content[4], self.__DATE_FORMAT)

        if expiringDate < datetime.today():
            return None
        return sessionIDHash

    @property
    def Posts(self) -> list[Post]:
        posts: list[Post] = Post.getPosts()
        userPosts: list[Post] = []

        for post in posts:
            if post.User == self:
                userPosts.append(post)
        return userPosts

    def __eq__(self, other):
        if isinstance(other, User):
            return self.Name == other.Name
        return False

from SocialNetwork.Post import Post