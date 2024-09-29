import os
import functions as fs


def createFile():  # function creates two files one for storing the key and credentials
    try:
        open("fileData/credentials.txt", "x")
        fs.create_key()
    except Exception as e:
        print("File Creation error occurred")
        print("File either exists or program does not have access to directory")
        print(e)
    finally:
        pass


def store(user, password, web):  # function stores input creds into a file after encryption
    # print("Storing credentials...")
    try:
        with open("fileData/credentials.txt", "a") as f:
            password = fs.encrypt_data(password)  # encrypting password
            f.write(f"{web}|{user}|{password}\n")
            # print("Data successfully stored")
    except Exception as e:
        print(f"File handling error occurred: {e}")
    finally:
        pass


def decrypt(web):  # decrypts data and outputs it to console
    try:
        with open("fileData/key.key", "r") as f:
            key = str(f.read())
        data = fs.load_data()
        found = False
        for entry in data:
            if entry[0] == web:
                decrypted_password = fs.decrypt_data(entry[2].encode())
                print(f"Username: {entry[1]}, Password: {decrypted_password}")
                found = True
                break
            elif found is False:
                print("Could not find the data you were looking for")

    except Exception as e:
        print(f"Failed to fetch data: {e}")
    finally:
        pass


while True:

    option = int(input("1.Store \n2.Read \n3.Debug \n4.Exit \n\nOption: "))
    if option == 1:
        web = input("Enter the website: ")
        user = input("Enter your username: ")
        password = input("Enter your password: ")
        path = 'fileData/credentials.txt'
        isExist = os.path.exists(path)

        if isExist is True:
            print("Entering data into file...")
            store(user, password, web)
        elif isExist is False:
            # print("Creating new file...")
            createFile()
            # print("Entering data into file...")
            store(user, password, web)
        else:
            print("Critical error occurred isExist function most likely failed to work")
    elif option == 2:
        web = int(input("Enter the website you wish to read: "))
        decrypt(web)
    elif option == 3:
        print("Work in progress")
    elif option == 4:
        break
    else:
        print("Invalid option")

