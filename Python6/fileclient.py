import socket

s = socket.socket()
host = "127.0.0.1"
port = 5001

s.connect((host, port))
s.send("Hello server!".encode())

with open('logorecv.jpg', 'wb') as f:   #wb ဆိုတာ write in binary mode
   while True:
      #print('receiving data...')
      data = s.recv(1)
      if not data:
         break
      f.write(data)
      
f.close()
print('Successfully received')
s.close()
print('connection closed')