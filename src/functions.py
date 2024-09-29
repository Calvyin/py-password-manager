from cryptography.fernet import Fernet
import os


def create_key():

    key = Fernet.generate_key()
    with open("fileData/key.key", "wb") as f:
        f.write(key)
    return key


def load_key():
    # load key to ram
    with open('fileData/key.key', 'rb') as key_file:
        key = key_file.read()
    return key


def encrypt_data(data):
    #function for encryption
    fernet = Fernet(load_key())
    encrypted = fernet.encrypt(data.encode())
    return encrypted


def decrypt_data(encrypted_data):
    # decryption function
    fernet = Fernet(load_key())
    decrypted_data = fernet.decrypt(encrypted_data)
    decrypted_data = decrypted_data.decode()
    return decrypted_data


def load_data():
    # load data to ram
    if not os.path.exists('fileData/credentials.txt'):
        return []
    with open('fileData/credentials.txt', 'r') as file:
        return [line.strip().split('|') for line in file.readlines()]