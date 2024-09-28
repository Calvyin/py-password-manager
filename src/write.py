import os
import json


def create_file():
    try:
        open("credentials.txt", "x")
    finally:
        print("File Creation error occurred")


def store(user, password):   # function stores input creds into a file after encryption
    print("Storing credentials")
    try:
        f = open("credentials.txt", "a")
        f.write("Entry: ")
        f.write(user)
        f.write(password)
    finally:
        print("File handling error occurred")


user = str()
password = str()
print("Enter your username")
input(user)
print("Enter your password")
input(password)

path = 'credentials.txt'
isExist = os.path.exists(path)

if isExist is False:
    print("Entering data into file...")
    store(user, password)
    print("Data successfully stored")

elif isExist is True:
    print("Creating new file...")
    create_file()
    print("Entering data into file...")
    store(user, password)
    print("Data successfully stored")

else:
    print("Critical error occurred isExist function most likely failed to run")
