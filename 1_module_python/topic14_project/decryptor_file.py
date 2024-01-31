from cryptography.fernet import Fernet

with open("data/secret_key.txt", 'rb') as file:
    secret_key = file.read()

with open("data/encrypted_data.txt", 'rb') as file:
    encrypted_data = file.read()


fernet_key = Fernet(secret_key)

decrypted_data = fernet_key.decrypt(encrypted_data)

with open("data/decrypted_data.txt", 'wb') as file:
    file.write(decrypted_data)

