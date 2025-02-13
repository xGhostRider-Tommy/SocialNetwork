from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Libs.Post import Post

class User:
    __Users: dict[str, User] = {}
    
    def __init__(self, username: str, email: str, password: str):
        self.__Name: str = username
        self.__Email: str = email
        self.__PasswordHash: str = password # FARE HASH
        self.Posts: list[Post] = []
    
    @staticmethod
    def Register(username: str, email: str, password: str):
        if username in User.__Users:
            return None
        
        user: User = User(username, email, password)
        User.__Users[username] = user
        
        return user
    
    @staticmethod
    def Login(username: str, password: str) -> User | None:
        if username in User.__Users:
            currentUser: User = User.__Users[username]
            
            if currentUser.__PasswordHash == password: # FARE HASH
                return currentUser
        return None