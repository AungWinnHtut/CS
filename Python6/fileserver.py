import socket
host = "127.0.0.1"
port = 5001
server = socket.socket()
server.bind((host, port))
server.listen()
conn, addr = server.accept()
data = conn.recv(1).decode()
filename='logo.jpg'
f = open(filename,'rb')  # rb ဆိုတာ read in binary mode
i = 0
while True:
   i += 1
   l = f.read(1)
   if not l: #IF L IS NOTHING, THEN EXIT LOOP
      break
   conn.send(l)
   if i > 1809000:
    print(f'Data Block No. {i}')
    print('Sent.... ',repr(l))
    print()

print(f'\n\nTotal File Size is {i}')
f.close()
print('File transferred')
conn.close()