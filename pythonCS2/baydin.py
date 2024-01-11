from icecream import ic
initials = input('Enter your name initials: ')
ic(initials)
sum = 0

for Alpha in initials:
    ic(ord(Alpha))
    sum += ord(Alpha)


m = sum % 5
ic(sum)
ic(m)
match(m):
    case 0: print('bad')
    case 1: print('not so bad')
    case 2: print('a little good')
    case 3: print('good')
    case 4: print('excellent')
