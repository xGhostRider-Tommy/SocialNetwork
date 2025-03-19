import os
import shutil

def ClearData():
    file = open("../Data/users.csv", "w")
    file.write("")
    file.close()

    shutil.rmtree("../Data/Posts") # remove the dir and all its content
    os.mkdir("../Data/Posts")

if __name__ == "__main__":
    ClearData()