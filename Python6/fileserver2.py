import socket
import os


host = "127.0.0.1"
port = 5001
server = socket.socket()
server.bind((host, port))
server.listen()
print('Server is Listening.....')
conn, addr = server.accept()
data = conn.recv(1024).decode()
filename = data.strip()
print()

if not os.path.exists(filename):
   print('No such file in Server!, exiting.....')
   exit(1)

#######################
print('File exists in Server, Transferring now...')

f = open(filename,'rb')  # rb ဆိုတာ read in binary mode
i = 0
while True:
   i += 1
   l = f.read(1)
   if not l: #IF L IS NOTHING, THEN EXIT LOOP
      break
   conn.send(l)
   

print(f'\n\nTotal File Size is {i-1}')
f.close()
print('File transferred')
conn.close()