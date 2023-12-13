import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def encrypt(plaintext, key):
    # Generate a random 16-byte IV.
    iv = os.urandom(16)

    # Create a cipher object using the given key and IV.
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Pad the plaintext to be a multiple of the block size.
    padder = padding.PKCS7(128).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    # Encrypt the padded plaintext.
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    return iv + ciphertext

def decrypt(ciphertext, key):
    # Extract the IV from the beginning of the ciphertext.
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]

    # Create a cipher object using the given key and IV.
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Decrypt the ciphertext.
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()

    # Unpad the plaintext.
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext

# Example usage
key = os.urandom(32)  # AES-256 key; you can also derive this from a password
plaintext = b"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"  # Plaintext must be in bytes

# Encrypt
ciphertext = encrypt(plaintext, key)
with open('.secrect','w') as myFile:
    myFile.write(ciphertext.decode('utf-8'))
with open('.key','w') as keyFile:
    keyFile.write(key)

# Decrypt
decrypted_text = decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)



key = os.environ.get('API')
print(key)