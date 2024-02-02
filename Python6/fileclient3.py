import socket

s = socket.socket()
host = "0.tcp.ap.ngrok.io"
port = 12668

print('Connecting to Server...')
s.connect((host, port))

# 1. Receive and print the file list from the server
files_list = s.recv(4096).decode()
print(f'Available Files in Server:\n{files_list}')

# 2. Request a file from the user
file_name = input('Enter Filename to transfer: ')
s.send(file_name.encode())

response = s.recv(1024).decode()

if response == 'No such file in Server!':
    print(response)
    s.close()
    exit(1)

print(f'\nRequesting {file_name} from Server...')

i = 0

with open(file_name, 'wb') as f:   # wb writes in binary mode
    while True:
        if i == 0:
            print('Receiving data...')
        data = s.recv(1)
        i += 1
        if not data:
            break
        f.write(data)

print(f'\nSuccessfully received {file_name}, total {i-1} bytes')
s.close()
print('Connection closed')
