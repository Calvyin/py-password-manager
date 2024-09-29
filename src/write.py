import os
import functionset1 as fs


def createFile():  # function creates two files one for storing IdNo and other for credentials
    try:
        with open("fileData/credentials.txt", "x") as f:
            f.write("Stored credentials: \n")
        with open("fileData/credId.txt", "x") as f:
            f.write("IDs : 0")
    except Exception as e:
        print("File Creation error occurred")
        print("File either exists or program does not have access to directory")
        print(e)
    finally:
        pass


def store(user, password, web):  # function stores input creds into a file after encryption
    print("Storing credentials...")
    try:
        currentId = int()
        newId = int()
        with open("fileData/credId.txt", "r") as f:
            content = f.read()
            currentId = int(content[6])
            newId = currentId + 1
            new_content = content[:6] + str(newId) + content[7:]
        with open("fileData/credId.txt", "r+") as f:
            f.write(new_content)

    except Exception as e:
        print("Indexing error failed to get ID or ID does not exist")
        print(e)
    finally:
        pass

    try:
        with open("fileData/credentials.txt", "a") as f:
            f.write("\n")
            f.write(f"ID: {int(newId)}\n")
            f.write(f"Website: {str(web)}\n")
            f.write(f"Username: {str(user)}\n")
            f.write(f"Password: {str(password)}\n")
            print("Data successfully stored")
    except Exception as e:
        print(f"File handling error occurred: {e}")
    finally:
        pass


def encrypt():
    print("Attempting to encrypt data...")
    try:
        path = 'fileData/key.key'
        isExist = os.path.exists(path)
        if isExist is False:  # checking if key exists
            key = fs.generate_key()
            print("Generated new key")
            # print(key)  # debug
        elif isExist is True:
            key = fs.load_key()
            print("Key found\n")
            # print(key)  # debug
        else:
            print("Unable to determine existence of key")

        with open("fileData/credentials.txt", "w+") as f:  # encrypting file data
            rawContent = f.read()
            encContent = fs.encrypt_data(rawContent, key)
            f.write("\n")
            f.write(str(encContent))
        print("Data successfully encrypted and stored")
    except Exception as e:
        print(f"Failed to encrypt data: {e}")
    finally:
        pass


web = input("Enter the website: ")
user = input("Enter your username: ")
password = input("Enter your password: ")
# print(type(password)) # debug

path = 'fileData/credentials.txt'
isExist = os.path.exists(path)
# print(isExist) # debug

if isExist is True:
    print("Entering data into file...")
    store(user, password, web)
    encrypt()

elif isExist is False:
    print("Creating new file...")
    createFile()
    print("Entering data into file...")
    store(user, password)
    encrypt()

else:
    print("Critical error occurred isExist function most likely failed to run")
