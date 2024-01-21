import os
from icecream import ic

current_folder = os.getcwd()
files = os.listdir(current_folder)

for file in files:
    parts = file.split('.')
    count = len(parts)
    if parts[count-1] != 'py':
        print(file)



fname = input('Which file to copy?: ')
