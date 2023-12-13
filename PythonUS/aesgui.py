import os
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import urlsafe_b64encode, urlsafe_b64decode, b64encode, b64decode


# Function to derive a key from a password
def derive_key(password: str):
    password = password.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'',  # Empty salt as per requirement
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password)

# AES Encryption
def pad(s):
    return s + b"=" * ((4 - len(s) % 4) % 4)

def encrypt_aes(key, plaintext):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Properly pad the base64-encoded string
    encoded = urlsafe_b64encode(iv + ciphertext)
    return pad(encoded).decode()

def decrypt_aes(key, ciphertext):
    # Ensure the input is correctly padded
    ciphertext = pad(urlsafe_b64decode(ciphertext.encode()))

    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()

    return (unpadder.update(padded_plaintext) + unpadder.finalize()).decode()


# Updated file encryption and decryption functions
def encrypt_files_in_folder(folder_path, key):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                file_data = file.read()
            encrypted_data = encrypt_aes(key, file_data.decode('utf-8', 'ignore'))
            with open(file_path, 'w') as file:
                file.write(encrypted_data)

def decrypt_files_in_folder(folder_path, key):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                file_data = file.read()
            decrypted_data = decrypt_aes(key, file_data)
            with open(file_path, 'wb') as file:
                file.write(decrypted_data.encode('utf-8'))


# GUI Functions
def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_path_entry.delete(0, tk.END)
        folder_path_entry.insert(0, folder_path)





# Updated GUI Functions
def encrypt_folder():
    folder_path = folder_path_entry.get()
    password = password_entry.get()
    if not folder_path or not password:
        messagebox.showerror("Error", "Folder path and password are required.")
        return

    key = derive_key(password)
    encrypt_files_in_folder(folder_path, key)

    messagebox.showinfo("Success", "Folder encrypted successfully.")

def decrypt_folder():
    folder_path = folder_path_entry.get()
    password = password_entry.get()
    if not folder_path or not password:
        messagebox.showerror("Error", "Folder path and password are required.")
        return

    key = derive_key(password)
    decrypt_files_in_folder(folder_path, key)

    messagebox.showinfo("Success", "Folder decrypted successfully.")

def encrypt_text():
    text = text_entry.get()
    password = password_entry.get()
    if not text or not password:
        messagebox.showerror("Error", "Text and password are required.")
        return

    key = derive_key(password)
    encrypted_text = encrypt_aes(key, text)

    result_text.delete(0, tk.END)
    result_text.insert(0, encrypted_text)

def decrypt_text():
    encrypted_text = text_entry.get()
    password = password_entry.get()
    if not encrypted_text or not password:
        messagebox.showerror("Error", "Encrypted text and password are required.")
        return

    key = derive_key(password)
    decrypted_text = decrypt_aes(key, encrypted_text)

    result_text.delete(0, tk.END)
    result_text.insert(0, decrypted_text)

# GUI Layout
main_window = tk.Tk()
main_window.title("AES Encryption/Decryption")

window = tk.Frame(main_window, padx=15, pady=15)
window.grid(row=6, column=0, columnspan=3, sticky="ew")

tk.Label(window, padx=5, pady=5, text="Folder Path:").grid(row=0, column=0,sticky='w')
folder_path_entry = tk.Entry(window, width=50)
folder_path_entry.grid(row=0, column=1)

browse_frame = tk.Frame(window,padx=5, pady=5,)
browse_frame.grid(row=0, column=3, sticky="ew")
tk.Button(browse_frame,padx=15, pady=5, text="Browse", command=browse_folder).grid(row=0, column=2)

folder_ops_frame = tk.Frame(window,padx=5, pady=5,)
folder_ops_frame.grid(row=1, column=1, sticky="ew")

# Center the buttons in the frame and space them equally
tk.Button(folder_ops_frame, text="Encrypt Folder", command=encrypt_folder).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
tk.Button(folder_ops_frame, text="Decrypt Folder", command=decrypt_folder).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)


tk.Label(window,padx=5, pady=5, text="Text:").grid(row=2, column=0,sticky='w')
text_entry = tk.Entry(window, width=50)
text_entry.grid(row=2, column=1)

file_ops_frame = tk.Frame(window,padx=5, pady=5,)
file_ops_frame.grid(row=3, column=1, sticky="ew")

# Center the buttons in the frame and space them equally
tk.Button(file_ops_frame, text="Encrypt Text", command=encrypt_text).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
tk.Button(file_ops_frame, text="Decrypt Text", command=decrypt_text).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)


tk.Label(window,padx=5, pady=5, text="Password:").grid(row=4, column=0,sticky='w')
password_entry = tk.Entry(window, show="*", width=50)
password_entry.grid(row=4, column=1)

tk.Label(window,padx=5, pady=5, text="Result:").grid(row=5, column=0,sticky='w')
result_text = tk.Entry(window, width=50)
result_text.grid(row=5, column=1)

window.mainloop()

