from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Libs.User import User
    from Utils.UniqueList import UniqueList

class Post:
    def __init__(self, user: User, text: str, hashtags: UniqueList[str]):
        self.__User: User = user
        self.__Text: str = text
        self.__Hashtags: UniqueList[str] = hashtags
    
    def getUser(self) -> User:
        return self.__User
    
    def getText(self) -> str:
        return self.__Text
    
    def getHashtags(self) -> UniqueList[str]:
        return self.__Hashtags
    
    User = property(
        fget = getUser
    )
    
    Text = property(
        fget = getText
    )
    
    Hashtags = property(
        fget = getHashtags
    )