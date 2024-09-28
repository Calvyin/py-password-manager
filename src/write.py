import os


def createFile():
    try:
        with open("credentials.txt", "x") as f:
            f.write(f"IDs : 0\n")
    except:
        print("File Creation error occurred")
        print("File either exists or program does not have access to directory")
    finally:
        pass


def store(user, password):  # function stores input creds into a file after encryption
    print("Storing credentials")
    try:
        currentId = int()
        newId = int()
        with open("credentials.txt", "r") as f:
            content = f.read()
            currentId = int(content[6])
            newId = currentId + 1
            new_content = content[:6] + str(newId) + content[7:]
        with open("credentials.txt", "r+") as f:
            f.write(new_content)

    except:
        print("Indexing error failed to get ID or ID does not exist")
    finally:
        pass

    try:
        with open("credentials.txt", "a") as f:
            f.write(f"ID: {int(newId)}\n")
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
print(isExist) # debug

if isExist is True:
    print("Entering data into file...")
    store(user, password)

elif isExist is False:
    print("Creating new file...")
    createFile()
    print("Entering data into file...")
    store(user, password)

else:
    print("Critical error occurred isExist function most likely failed to run")
