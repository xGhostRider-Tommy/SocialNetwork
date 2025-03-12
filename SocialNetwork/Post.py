from __future__ import annotations

import os

from SocialNetwork.Hashtag import Hashtag
from Utils.Image import Image
from Utils.UniqueList import UniqueList


#from SocialNetwork.User import User # added at the end for circular import

class Post:
    __POSTS_DIRECTORY: str = "Data/Posts/"
    __POST_ID_LENGTH: int = 16
    __INFO_FILE_NAME: str = "info.txt"
    __MAX_IMAGES_PER_POST: int = 10

    __Id: str

    # do not use this
    def __init__(self, id: str):
        self.__Id = id

    # use this
    @staticmethod
    def CreatePost(user: User, description: str, hashtags: UniqueList[Hashtag], images: list[Image]) -> Post:
        id: str
        imagesCount: int
        postIds: list[str] = os.listdir(Post.__POSTS_DIRECTORY)

        if len(postIds) == 0:
            id = "0"
        else:
            postIds.sort(reverse=True)
            id = str(int(postIds[0]) + 1)


        # salva gli altri dati nel disco
        postDirectory: str = Post.__POSTS_DIRECTORY + id
        os.mkdir(postDirectory)
        file = open(postDirectory + "/" + Post.__INFO_FILE_NAME, "w")

        file.write(user.Name + "\n")
        file.write(description + "\n")

        hashtagsString: str = ""
        if len(hashtags) != 0:
            for hashtag in hashtags:
                hashtagsString += hashtag.Text + " "
            hashtagsString = hashtagsString[:-1]  # leva l'ultimo spazio
        file.write(hashtagsString)
        file.close()

        if len(images) <= Post.__MAX_IMAGES_PER_POST:
            imagesCount = len(images)
        else:
            imagesCount = Post.__MAX_IMAGES_PER_POST

        for i in range(imagesCount):
            file = open(postDirectory + "/" + str(i) + "." + images[i].Extension, "wb")
            file.write(images[i].Content)
            file.close()

        return Post(id)

    @staticmethod
    def getPosts() -> list[Post]:
        postsIds: list[str] = os.listdir(Post.__POSTS_DIRECTORY)
        posts: list[Post] = []

        for id in postsIds:
            posts.append(Post(id))
        return posts

    def getContent(self) -> list[str]:
        file = open(self.__POSTS_DIRECTORY + self.__Id + "/" + self.__INFO_FILE_NAME, "r")
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
        a = self.getContent()
        return a[1]

    @property
    def Hashtags(self) -> UniqueList[Hashtag]:
        hashtagsStrings: list[str] = self.getContent()[2].split(" ")
        hashtags: UniqueList[Hashtag] = UniqueList([])

        for hashtagString in hashtagsStrings:
            hashtags.Add(Hashtag.getHashtag(hashtagString))
        return hashtags

    @property
    def Photos(self) -> list[Image]:
        imagesFiles: list[str] = os.listdir(self.__POSTS_DIRECTORY + self.__Id + "/")
        imagesFiles.remove(self.__INFO_FILE_NAME)

        images: list[Image] = []

        for imageName in imagesFiles:
            images.append(Image(imageName.split(".")[1], open(imageName, "rb").read()))
        return images

from SocialNetwork.User import User