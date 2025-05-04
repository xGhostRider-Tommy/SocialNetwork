def ClearData():
    file = open("Data/users.csv", "w")
    file.write("")
    file.close()

    file = open("Data/posts.csv", "w")
    file.write("")
    file.close()

if __name__ == "__main__":
    ClearData()