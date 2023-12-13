import random 
hidden_password = '1234'
password = input('Enter your password: ')
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0


if password != hidden_password:
    print('Incorrect password ')
    exit(1)


print('Correct password ')


for i in range(1000000000):  
    dice = random.randint(1,6)
    #print(dice)
    if dice  == 1:
        one = one + 1
    elif dice == 2:
        two = two + 1
    elif dice == 3:
        three = three + 1
    elif dice == 4:
        four = four + 1
    elif dice == 5:
        five = five + 1
    elif dice == 6:
        six = six + 1

print(f'One = {one }times')
print(f'Two = {two} times')
print(f'Three = {three} times  ')
print(f'Four = {four} times')
print(f'Five = {five} times')
print(f'Six = {six} times')



biggest = max(one, two, three, four, five, six)
smallest = min(one,two,three,four,five,six)
diff = biggest - smallest
print(f'The diff is {diff}')






