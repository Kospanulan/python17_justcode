from cryptography.fernet import Fernet

secret_key = b'volgoJzYvSs0tq3r2yUuKvVZnme0rk1Ry0mUc1geJRw='

# encrypted_data = b'gAAAAABluksUw5B8rqwQYBr1N-UlIUoKT1XrVbMH-3EtHLKf28T0caSa8GGEgNCGxxGjmgoL-B3iVIxrWvL23mviIbiqnRqVjw=='
encrypted_data = b'gAAAAABlukwJjCJ-J7pvKzP70umJ_AVfly1Nijk7TkybMC5d4RGX6gNAnLIwx8SQdOlySd2y1HIIa4A-xtcveQYmuWC0uhuVew=='

fernet_key = Fernet(secret_key)

decrypted_data = fernet_key.decrypt(encrypted_data)

print(decrypted_data.decode('utf-8'))
