import os

from SocialNetwork.User import User


# # RESET FOR TESTING THINGS
# def Reset(wait: bool):
#     from ClearData import ClearData
#
#     if wait:
#         input("Waiting before reset...")
#     ClearData()
#
# # GENERATE DATA DEFAULT CONTENTS IF NOT EXISTS
# if not os.path.exists("Data"):
#     os.mkdir("Data")
#     os.mkdir("Data/Posts")
#     file = open("Data/users.csv", "w")
#     file.write("")
#     file.close()
#
# Reset(False)
#
# User.Register("ciao", "ciao@example.com", "ciao123")
#
# sessionID = User.Login("ciao", "ciao123")
# a = User.Authenticate("ciao", sessionID)
#
# print(a.Name)
#
#
list = [User("a"), User("b"), User("c")]
list.remove(User("a"))
print(list)