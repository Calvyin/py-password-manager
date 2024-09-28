import functionset1 as fs

key = fs.generate_key()
user_input = input("USERNAME")
encrypted_data = fs.encrypt_data(user_input, key)
filename = "credentials.bin"
#saving encrypted data
fs.save_to_file(filename, encrypted_data)
#saving key
with open('keyfile.key', 'wb') as keyfile:
    keyfile.write(key)



