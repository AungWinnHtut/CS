import os
from icecream import ic

current_folder = os.getcwd()
files = os.listdir(current_folder)

for file in files:    
    if file[0]!='.':
        print(file)



fname = input('Which file to copy?: ')

if not os.path.exists(fname):
    print('Error! no such file, Bye...')
    exit(1)


newfname = input('What is the new file name: ')
if os.path.exists(newfname):
    print('Alert! File already exists, Bye...')
    exit(1)

fin = open(fname,'rb')
fout = open(newfname,'wb')
byte = 0
while True:
    data_block = fin.read(1)
    if data_block:
        byte += 1
        fout.write(data_block)
    else:
        break

print(f'Total {byte}bytes file')
fin.close()
fout.close()
