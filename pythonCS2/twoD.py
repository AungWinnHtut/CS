import random
import time
from icecream import ic

# Use the current time as the seed value
seed_value = int(time.time())
random.seed(seed_value)

bank_acc = 1000

player_number = input('What is your number: ')
player_number = int(player_number)
ic(player_number)

fn = player_number // 10
ic(fn)

sn = player_number % 10
ic(sn)


bet = input('what is your bet: ')
bet = int(bet)



# Generate a random integer between 1 and 10
first_number = random.randint(0, 9)
print("First Number:", first_number)

second_number = random.randint(0, 9)
print("Second Number:", second_number)


if fn != first_number or sn != second_number:
    bank_acc = bank_acc - bet
else:
    bank_acc = bank_acc + (bet * 80)