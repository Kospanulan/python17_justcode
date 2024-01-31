from cryptography.fernet import Fernet

with open("data/source.txt", 'rb') as file:
    data = file.read()


print(data)

secret_key = Fernet.generate_key()

with open("data/secret_key.txt", 'wb') as file:
    file.write(secret_key)

fernet_key = Fernet(secret_key)

encrypted_data = fernet_key.encrypt(data)

with open("data/encrypted_data.txt", 'wb') as file:
    file.write(encrypted_data)

