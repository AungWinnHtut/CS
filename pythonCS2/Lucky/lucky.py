name = input('What is your name: ')
sum = 0
for alpha in name:
    if alpha != ' ':
        num = ord(alpha)
        sum = sum + num
        print(f'{alpha} - {num}')

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