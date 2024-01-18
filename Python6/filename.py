import os

fname = input('enter file name to transfer: ')
if not os.path.exists(fname):
    print('File does not exist, Quit now...')
    exit(1)

print('File exists and will transfer soon....')
