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
    host = "127.0.0.1"
    port = 5001

    s = socket.socket()
    s.connect((host, port))

    while True:
        # 1. Receive the file list from the server
        menu = receive_data(s)
        print("Menu:")
        print(menu)
        ans = input('Choose (1,2,3)...')
        s.send(ans.encode())
        if ans == '4':
            print('Exiting....')
            s.close()
            exit(0)
    
        

if __name__ == "__main__":
    main()
