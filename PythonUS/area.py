pi = 3.1415
try:
    r = float(input('enter r: '))
except:
    print('Error! You must enter float value: ')
    exit(1)
    
a = pi * r ** 2 
print(f'Area = {a}')

with open('area_archive.txt','a') as file: 
    file.write(str(a) + '\n') # + string join

 
    
