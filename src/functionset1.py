from cryptography.fernet import Fernet

def generate_key():
    #generate key and store locally
    return Fernet.generate_key()

def encrypt_data(data, key):
    #encrypting function
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def load_key():
    #load key to ram
    with open('key.key', 'rb') as key_file:
        return key_file.read()

def decrypt_data(encrypted_data, key):
    #decryption function
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

def load_from_file(filename):
    #open the file from local storage
    with open(filename, 'rb') as file:
        return file.read()

def save_to_file(filename, data):
    #saving files locally
    with open(filename, 'wb') as file:
        file.write(data)