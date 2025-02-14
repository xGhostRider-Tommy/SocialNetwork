import os

from Libs.Hashtag import Hashtag
from Libs.Post import Post
from Libs.User import User
from Utils.UniqueList import UniqueList


# RESET FOR TESTING THINGS
def Reset(wait: bool):
    from ClearData import ClearData

    if wait:
        input("Waiting before reset...")
    ClearData()

# GENERATE DATA DEFAULT CONTENTS IF NOT EXISTS
if not os.path.exists("Data"):
    os.mkdir("Data")
    os.mkdir("Data/Posts")
    file = open("Data/users.csv", "w")
    file.write("")
    file.close()

a = User.Register("ciao", "ciao@example.com", "ciao123")

a.AddPost("ciaooo", UniqueList([Hashtag.getHashtag("myhashtag"), Hashtag.getHashtag("boh")]))

print(Post.getPosts()[0].Description, Post.getPosts()[0].User.Name, Post.getPosts()[0].Hashtags)
#print(a.Posts[0].Description)

Reset(False)