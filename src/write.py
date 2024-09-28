import os
import json

n = 0  # Global variable


def create_file():
    try:
        open("credentials.txt", "x")
    except:
        print("File Creation error occurred")
        print("File either exists or program does not have access to directory")
    finally:
        pass


def store(user, password):   # function stores input creds into a file after encryption
    print("Storing credentials")
    global n
    n += 1

    try:
        with open("credentials.txt", "a") as f:
            f.write(f"Entry: {int(n)}\n")
            f.write(f"Username: {str(user)}\n")
            f.write(f"Password: {str(password)}\n")
            print("Data successfully stored")
    except:
        print("File handling error occurred")
    finally:
        pass


print("Enter your username")
user = input()
print(type(user))
print("Enter your password")
password = input()
print(type(password))

path = 'credentials.txt'
isExist = os.path.exists(path)
print(isExist)

if isExist is True:
    print("Entering data into file...")
    store(user, password)

elif isExist is False:
    print("Creating new file...")
    create_file()
    print("Entering data into file...")
    store(user, password)

else:
    print("Critical error occurred isExist function most likely failed to run")
