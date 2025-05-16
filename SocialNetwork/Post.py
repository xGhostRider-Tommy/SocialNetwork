from __future__ import annotations

from SocialNetwork.Globals import Globals
from SocialNetwork.Hashtag import Hashtag
from Utils.UniqueList import UniqueList


#from SocialNetwork.User import User # added at the end for circular import

class Post:
    __Id: int

    # do not use this
    def __init__(self, id: int):
        self.__Id = id

    # use this
    @staticmethod
    def CreatePost(user: User, description: str, hashtags: UniqueList[Hashtag], images: UniqueList[str]) -> Post:
        fileContent: list[str] = open(Globals.POSTS_FILE, "r").read().split("\n")
        id: int = len(fileContent)

        file = open(Globals.POSTS_FILE, "a")
        if fileContent[0] != "":
            file.write("\n")
        file.write(f"{user.Name};{description};{str(hashtags)};{str(images)};")
        file.close()

        return Post(id)

    @staticmethod
    def getPosts() -> list[Post]:
        postsData: list[str] = open(Globals.POSTS_FILE, "r").read().split("\n")
        posts: list[Post] = []

        if postsData[0] != "":
            for i in range(len(postsData) - 1, -1, -1):  # for in reverse
                posts.append(Post(i))
        return posts

    @staticmethod
    def getPostsByHashtag(hashtag: Hashtag) -> list[Post]:
        allPosts: list[Post] = Post.getPosts()
        posts: list[Post] = []

        for post in allPosts:
            for postHashtag in post.Hashtags:
                if postHashtag == hashtag:
                    posts.append(post)
                    break
        return posts

    # True if success, False if error
    def Like(self, user: User):
        if self.HasLiked(user): # Unlike
            users: UniqueList[User] = self.getUserLikes()
            names: UniqueList[str] = UniqueList([])

            for currentUser in users:
                names.Add(currentUser.Name)

            for i in range(len(names) + 1):
                if names[i] == user.Name:
                    names.Remove(i)
                    break

            fileContent: list[str] = open(Globals.POSTS_FILE, "r").read().split("\n")
            fileContent[self.Id] = f"{self.Author.Name};{self.Description};{str(self.Hashtags)};{self.Images};{names}"

            content: str = ""
            for line in fileContent:
                content += line + "\n"
            content = content[:-1]  # leva l'ultimo invio

            file = open(Globals.POSTS_FILE, "w")
            file.write(content)
            file.close()
        else: # Like
            fileContent: list[str] = open(Globals.POSTS_FILE, "r").read().split("\n")

            if self.Likes != 0:
                fileContent[self.Id] += " "
            fileContent[self.Id] += user.Name

            content: str = ""
            for line in fileContent:
                content += line + "\n"
            content = content[:-1]  # leva l'ultimo invio

            file = open(Globals.POSTS_FILE, "w")
            file.write(content)
            file.close()

    def getContent(self) -> list[str]:
        postsContent: list[str] = open(Globals.POSTS_FILE, "r").read().split("\n")
        return postsContent[self.Id].split(";")

    def getUserLikes(self) -> UniqueList[User]:
        users: list[User] = []
        likes: list[str] = self.getContent()[4].split(" ")

        if likes[0] != "":
            for username in likes:
                users.append(User(username))
        return UniqueList(users)

    def HasLiked(self, user: User) -> bool:
        users: UniqueList[User] = self.getUserLikes()
        return user in users

    @property
    def Id(self) -> int:
        return self.__Id

    @property
    def Author(self) -> User | None:
        username: str = self.getContent()[0]

        for user in User.getUsers():
            if user.Name == username:
                return user
        return None

    @property
    def Description(self) -> str:
        description: list[str] = self.getContent()
        return description[1]

    @property
    def Hashtags(self) -> UniqueList[Hashtag]:
        hashtagsStrings: list[str] = self.getContent()[2].split(" ")
        hashtags: UniqueList[Hashtag] = UniqueList([])

        for hashtagString in hashtagsStrings:
            hashtags.Add(Hashtag(hashtagString))
        return hashtags

    @property
    def Images(self) -> UniqueList[str]:
        imagesList: list[str] = self.getContent()[3].split(" ")
        return UniqueList(imagesList)

    @property
    def Likes(self) -> int:
        return len(self.getUserLikes())

from SocialNetwork.User import User