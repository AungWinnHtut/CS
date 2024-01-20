import socket
import time
import os

s = socket.socket()
host = "s3.greenhackers.org"
port = 5001

file_name = input('Enter Filename to transfer: ')

print(f'Requesting {file_name} from Server...')
s.connect((host, port))
s.send(file_name.encode())

i = 0

start_time = time.time()
file_name2, file_extension = os.path.splitext(file_name)
file_name2 += '_copy'
file_name2 += file_extension

with open(file_name2, 'wb') as f:   # wb is for writing in binary mode
    while True:
        if i == 0:
            print('Receiving data...')
        data = s.recv(1)  # Adjust the buffer size as needed
        i += len(data)
        if not data:
            break
        f.write(data)

end_time = time.time()

transfer_time = end_time - start_time
transfer_speed = i / transfer_time /1  # Transfer speed in KB/s

f.close()

print(f'Successfully received {file_name}, total {i} bytes')
print(f'Transfer time: {transfer_time:.2f} seconds')
print(f'Transfer speed: {transfer_speed:.2f} KB/s')

s.close()
print('Connection closed')
