from __future__ import annotations

import os
import random
from typing import TYPE_CHECKING

from Libs.Hashtag import Hashtag

if TYPE_CHECKING:
    from Libs.User import User
    from Utils.UniqueList import UniqueList

class Post:
    __POSTS_DIRECTORY: str = "Data\\Posts\\"
    __CHARS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    # do not use this
    def __init__(self, id: str):
        self.__Id: str = id

    # use this
    @staticmethod
    def CreatePost(user: User, description: str, hashtags: UniqueList[Hashtag]) -> Post:
        id: str = "" # placeholder
        notUnique: bool = True

        while notUnique:
            id = "".join(random.choice(Post.__CHARS) for _ in range(16)) # random id

            notUnique = False
            for post in Post.getPosts():
                if post.__Id == id:
                    notUnique = True

        # salva gli altri dati nel disco
        postDirectory: str = Post.__POSTS_DIRECTORY + id
        os.makedirs(postDirectory)
        file = open(postDirectory + "\\info.txt", "w")

        file.write(user.Name)
        file.write(description)

        hashtagsString: str = ""
        if len(hashtags) != 0:
            for hashtag in hashtags:
                hashtagsString += hashtag.Text + " "
            hashtagsString = hashtagsString[:-1]  # leva l'ultimo spazio
        file.write(hashtagsString)

        file.close()

        return Post(id)

    @staticmethod
    def getPosts() -> list[Post]:
        postsIds: list[str] = os.walk(Post.__POSTS_DIRECTORY)[1]
        posts: list[Post] = []

        for id in postsIds:
            posts.append(Post(id))
        return posts

    def getContent(self) -> list[str]:
        file = open(self.__POSTS_DIRECTORY + self.__Id + "\\info.txt", "r")
        return file.read().split("\n")

    @property
    def User(self) -> User | None:
        username = self.getContent()[0]

        for user in User.getUsers():
            if user.Name == username:
                return user
        return None

    @property
    def Description(self) -> str:
        return self.getContent()[1]

    @property
    def Hashtags(self) -> UniqueList[Hashtag]:
        hashtagsStrings: list[str] = self.getContent()[2].split(" ")
        hashtags: UniqueList[Hashtag] = UniqueList([])

        for hashtagString in hashtagsStrings:
            hashtags.Add(Hashtag.getHashtag(hashtagString))
        return hashtags