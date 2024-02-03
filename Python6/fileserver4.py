import socket
import os
import threading  # Import the threading module

def handle_client(client_socket):
    # 1. List all files in the current directory
    files_list = list_files_in_current_dir()
    files_str = "\n".join(files_list)
    
    # 2. Send the file list to the client
    client_socket.send(files_str.encode())

    # 3. Receive the selected file name from the client
    filename = client_socket.recv(1024).decode()
    print(f"\nSelected file: {filename}")

    if not os.path.exists(filename):
        print('No such file in Server!, exiting.....')
        client_socket.close()
        return

    # File exists in the server, transferring now...
    print('File exists in Server, Transferring now...')

    with open(filename, 'rb') as f:
        for byte in f:
            client_socket.send(byte)

    print(f'\n\nTotal File Size is {os.path.getsize(filename)} bytes')
    print('File transferred')

    client_socket.close()

def list_files_in_current_dir():
    current_dir = os.getcwd()
    files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]
    return files

host = "s3.greenhackers.org"
port = 5001
server = socket.socket()
server.bind((host, port))
server.listen()

print('Server is Listening.....')

while True:  # Keep accepting connections
    conn, addr = server.accept()
    print(f'Accepted connection from {addr}')
    
    # Create a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(conn,))
    client_handler.start()
