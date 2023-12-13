import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Function to generate a key from the password and salt
def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Function to encrypt a file
def encrypt_file(file_path: str, key: bytes, iv: bytes):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = encryptor.update(original) + encryptor.finalize()
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(iv + encrypted)  # Prepend the IV

# Function to decrypt a file
def decrypt_file(file_path: str, key: bytes):
    with open(file_path, 'rb') as file:
        iv = file.read(16)  # The first 16 bytes are the IV
        encrypted = file.read()
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted) + decryptor.finalize()
    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

# Function to process all files in a directory
def process_files(folder_path: str, password: str, mode: str):
    salt = os.urandom(16)  # Generates a random salt
    if mode == 'decrypt':
        salt = bytes.fromhex(input("Enter the salt (as a hexadecimal string): "))
    key = generate_key(password, salt)
    iv = os.urandom(16) if mode == 'encrypt' else None

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            if mode == 'encrypt':
                encrypt_file(file_path, key, iv)
                print(f"Encrypted {filename}")
            elif mode == 'decrypt':
                decrypt_file(file_path, key)
                print(f"Decrypted {filename}")

    if mode == 'encrypt':
        print(f"Use this salt for decryption: {salt.hex()}")

# Main function
def main():
    folder_path = input("Enter the folder path: ")
    password = input("Enter password: ")
    mode = input("Enter mode (encrypt/decrypt): ").lower()
    process_files(folder_path, password, mode)

if __name__ == "__main__":
    main()
