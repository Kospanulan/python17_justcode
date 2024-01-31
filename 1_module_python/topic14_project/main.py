
from cryptography.fernet import Fernet


# secret_key = Fernet.generate_key()
secret_key = b'volgoJzYvSs0tq3r2yUuKvVZnme0rk1Ry0mUc1geJRw='

fernet_key = Fernet(secret_key)

print(f"{secret_key=}")
# print(fernet_key)

data = b'qwerty123'  # f, r, b (binary) = b''
encrypted_data = fernet_key.encrypt(data)
print(f"{encrypted_data=}")
















































# class Test():
#     def __init__(self, key):
#         self.key = key
#
#     def create_key(self):
#         """Create a key"""
#         key = "123"
#         return key


