import socket

s = socket.socket()
host = "127.0.0.1"
port = 5001


file_name = input('Enter Filename to transfer: ')

print(f'Requesting {file_name} from Server...')
s.connect((host, port))
s.send(file_name.encode())

i = 0

with open(file_name, 'wb') as f:   #wb ဆိုတာ write in binary mode
   while True:
      if i == 0:
         print('receiving data...')
      data = s.recv(1)
      i += 1
      if not data:
         break
      f.write(data)
      
f.close()
print(f'Successfully received {file_name}, total {i-1}bytes')
s.close()
print('connection closed')