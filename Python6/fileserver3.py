import socket
import os

def list_files_in_current_dir():
    current_dir = os.getcwd() # get current working directory အခုရောက်နေတဲ့ folder ရဲ့ Path တောင်းတာ
    files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]
    return files

# cwd = /root
# a.py b.py c.py
# /root/a.py
#[a.py b.py c.py]

host = "127.0.0.1"
port = 5001
server = socket.socket()
server.bind((host, port))
server.listen()

print('Server is Listening.....')
conn, addr = server.accept()

# 1. List all files in the current directory
files_list = list_files_in_current_dir()
files_str = "\n".join(files_list)
# [a.py b.py c.py]
#a.py\nb.py\nc.py

# 2. Send the file list to the client
conn.send(files_str.encode())

# 3. Receive the selected file name from the client
filename = conn.recv(1024).decode()
print(f"\nSelected file: {filename}")

if not os.path.exists(filename):
    print('No such file in Server!, exiting.....')
    exit(1)

# File exists in the server, transferring now...
print('File exists in Server, Transferring now...')

with open(filename, 'rb') as f:
    for byte in f:
        conn.send(byte)

print(f'\n\nTotal File Size is {os.path.getsize(filename)} bytes')
print('File transferred')

conn.close()
