
name = input('What is your name: ')
x = input('enter x(int): ')
y = input('enter y (float): ')

try:
    x = int(x) #casting
except:
    print('Error! You must enter only int value!')
    exit(1)

try:
    y = float(y)
except:
    print('Error! You must enter only int value!')
    exit(1)




print(f'x = {x} and y = {y} and name = {name}')

