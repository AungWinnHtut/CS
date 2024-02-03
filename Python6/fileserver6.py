import socket
import os
import threading  # Import the threading module

def downloadFile(client_socket,addr):
    pass

def uploadFile(client_socket,addr):
    pass

def chat(client_socket,addr):
    pass

def handle_client(client_socket,addr):
   
    menu = '1-Download File\n2-Upload File\n3-Chat\n4-Exit\n'
    # 2. Send the file list to the client
    client_socket.send(menu.encode())

    # 3. Receive the selected file name from the client
    choice = client_socket.recv(1024).decode()
    match(choice):
        case '1': 
            print('Download File')
            downloadFile(client_socket,addr)

        case '2': 
            print('Upload File')
            uploadFile(client_socket,addr)
        case '3': 
            print('Chat')
            chat(client_socket,addr)
        case '4':
            print(f'client {addr} is disconnecting')
            client_socket.close()
            exit(0)
    handle_client(client_socket,addr)
    
    

def list_files_in_current_dir():
    current_dir = os.getcwd()
    files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]
    return files

host = "127.0.0.1"
port = 5001
server = socket.socket()
server.bind((host, port))
server.listen()

print('Server is Listening.....')

while True:  # Keep accepting connections
    conn, addr = server.accept()
    print(f'Accepted connection from {addr}')
    
    # Create a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(conn,addr))
    client_handler.start()
