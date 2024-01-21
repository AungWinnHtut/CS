from icecream import ic
name = input('What is your name: ')
sum = 0

parts = name.split(' ')
ic(parts)

for part in parts:
    num = ord(part[0])
    sum = sum + num
    print(f'{part[0]} - {num}')



print(f'Total Value is {sum}')

result = (sum % 3) + 1
print(result)
filename = str(result) + '.txt'
print(filename)

with open(filename,'r') as file:
    data = file.read()
    data = data.replace('. ','.\n')  
    #data = data.replace('.','.\n')    
    print(data)