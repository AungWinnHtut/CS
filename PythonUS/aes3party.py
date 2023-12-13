from tkinter import Tk, Label, Button, Entry, StringVar
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def derive_key(password, salt, iterations=100000):
    return PBKDF2(password, salt, dkLen=32, count=iterations)  # AES-256 key length

def encrypt_message(password, plain_text):
    salt = get_random_bytes(16)  # A new salt for each encryption
    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    salt_encoded = base64.b64encode(salt).decode('utf-8')
    return iv, ct, salt_encoded

def decrypt_message(password, iv, cipher_text, salt_encoded):
    salt = base64.b64decode(salt_encoded)
    key = derive_key(password, salt)
    iv = base64.b64decode(iv)
    ct = base64.b64decode(cipher_text)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

def on_encrypt():
    password = password_entry.get()
    plain_text = text_entry.get()
    iv, encrypted, salt = encrypt_message(password, plain_text)
    iv_var.set(iv)
    salt_var.set(salt)
    cipher_var.set(encrypted)
    result_label.config(text="Encryption Successful")

def on_decrypt():
    password = password_entry.get()
    iv = iv_var.get()
    cipher_text = cipher_var.get()
    salt = salt_var.get()
    decrypted = decrypt_message(password, iv, cipher_text, salt)
    result_label.config(text=f"Decrypted: {decrypted}")

# Set up the GUI
root = Tk()
root.title("AES Encryption/Decryption with Password")

# StringVars for holding the values
iv_var = StringVar()
salt_var = StringVar()
cipher_var = StringVar()

Label(root, text="Text:").pack()
text_entry = Entry(root, width=40)
text_entry.pack()

Label(root, text="Password:").pack()
password_entry = Entry(root, width=40, show='*')
password_entry.pack()

Label(root, text="IV:").pack()
iv_entry = Entry(root, width=40, textvariable=iv_var)
iv_entry.pack()

Label(root, text="Salt:").pack()
salt_entry = Entry(root, width=40, textvariable=salt_var)
salt_entry.pack()

Label(root, text="Cipher Text:").pack()
cipher_entry = Entry(root, width=40, textvariable=cipher_var)
cipher_entry.pack()

Button(root, text="Encrypt", command=on_encrypt).pack()
Button(root, text="Decrypt", command=on_decrypt).pack()

result_label = Label(root, text="Result:")
result_label.pack()

root.mainloop()
