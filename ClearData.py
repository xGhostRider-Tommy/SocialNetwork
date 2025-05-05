import os

from SocialNetwork.Globals import Globals

def ClearData(users: bool, posts: bool):
    if users:
        file = open(Globals.USERS_FILE, "w")
        file.write("")
        file.close()

    if posts:
        file = open(Globals.POSTS_FILE, "w")
        file.write("")
        file.close()

        for filename in os.listdir(Globals.IMAGES_FOLDER):
            filePath = Globals.IMAGES_FOLDER + "/" + filename
            if os.path.isfile(filePath):
                os.remove(filePath)

if __name__ == "__main__":
    ClearData(True, True)