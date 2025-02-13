from __future__ import annotations
import random

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Libs.User import User
    from Utils.UniqueList import UniqueList

class Post:
    __CHARS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    Posts: list[Post] = []

    def __init__(self, user: User, text: str, hashtags: UniqueList[str], id: str):
        self.__User: User = user
        self.__Text: str = text
        self.__Id: str = id
        self.__Hashtags: UniqueList[str] = hashtags
        self.Posts.append(self)

    @staticmethod
    def AddPost(user: User, text: str, hashtags: UniqueList[str]) -> Post:
        currentId: str = ""
        notUnique: bool = True

        while notUnique:
            currentId = "".join(random.choice(Post.__CHARS) for _ in range(16))

            notUnique = False
            for post in Post.Posts:
                if post.__Id == currentId:
                    notUnique = True

        return Post(user, text, hashtags, currentId)
    
    def getUser(self) -> User:
        return self.__User
    
    def getText(self) -> str:
        return self.__Text
    
    def getHashtags(self) -> UniqueList[str]:
        return self.__Hashtags

    def getId(self) -> str:
        return self.__Id
    
    User = property(
        fget = getUser
    )
    
    Text = property(
        fget = getText
    )
    
    Hashtags = property(
        fget = getHashtags
    )

    Id = property(
        fget = getId
    )