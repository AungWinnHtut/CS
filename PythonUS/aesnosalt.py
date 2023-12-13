import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from hashlib import sha256

# Function to generate a key from the password
def generate_key(password: str) -> bytes:
    return sha256(password.encode()).digest()

# Function to encrypt a file
def encrypt_file(file_path: str, key: bytes):
    iv = os.urandom(16)  # Generate a random IV
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(file_path, 'rb') as file:
        original = file.read()

    encrypted = encryptor.update(original) + encryptor.finalize()

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(iv + encrypted)  # Prepend the IV for decryption

# Function to decrypt a file
def decrypt_file(file_path: str, key: bytes):
    with open(file_path, 'rb') as file:
        iv = file.read(16)  # Read the IV from the file
        encrypted = file.read()

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted) + decryptor.finalize()

    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

# Function to process all files in a directory
def process_files(folder_path: str, password: str, mode: str):
    key = generate_key(password)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            if mode == 'encrypt':
                encrypt_file(file_path, key)
                print(f"Encrypted {filename}")
            elif mode == 'decrypt':
                decrypt_file(file_path, key)
                print(f"Decrypted {filename}")

# Main function
def main():
    folder_path = input("Enter the folder path: ")
    password = input("Enter password: ")
    mode = input("Enter mode (encrypt/decrypt): ").lower()
    process_files(folder_path, password, mode)

if __name__ == "__main__":
    main()