import socket
import os

def receive_data(sock):
    try:
        data = sock.recv(1024).decode('utf-8')
        return data
    except UnicodeDecodeError:
        # Handle binary data
        return sock.recv(1024)

def download_file(server_socket, filename):
    with open(filename, 'wb') as f:
        while True:
            data = server_socket.recv(1024)
            if not data:
                break
            f.write(data)

def main():
    host = "0.tcp.ap.ngrok.io"
    port = 18179

    s = socket.socket()
    s.connect((host, port))

    # 1. Receive the file list from the server
    files_list = receive_data(s)
    print("Available Files:")
    print(files_list)

    # 2. Select a file to download
    selected_file = input("Enter the filename to download: ")
    s.send(selected_file.encode())

    # 3. Receive the file from the server
    download_file(s, selected_file)

    print(f"\nFile {selected_file} downloaded successfully.")

    s.close()

if __name__ == "__main__":
    main()
