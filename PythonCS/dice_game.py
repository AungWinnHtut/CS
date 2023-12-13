import random as rnd
uname = input('Username: ')
password = input('Password: ')

if not (uname == "aung" and password == "1234"):
    print('Incorrect username or password!')
    exit(1)

# Login Now
dice_score = []
for _ in range(10):
    dice = rnd.randint(1,6)
    dice_score.append(dice)

dice_score.sort()
print(dice_score)
