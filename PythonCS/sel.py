import random as rnd

coin = 0
coin = int(input('How many coil?: '))

while True:
    bet = int(input('your bet: '))
    if(bet>coin):
        print(f'you cannot bet more than you have, your bet will be {coin}')
        bet = coin

    print(f'Your bet is now {bet}')

    sel = rnd.randint(1,3)
    if bet > 100:
        sel = 4
        
    choice = int(input('Please Choose CUP 1,2,3: '))

    if(sel==choice):
        coin += bet * 2
        print("Correct!")
    else:
        coin -= bet
        print("Wrong CUP, it is empty!")
    
    print(f'Now your coin is {coin}')

    ans = input('will you continue? Y/N: ')
    if ans == 'n' or ans == 'N':
        exit(0)
    
    if(coin<=0):
        coin += int(input('How mahy coin to buy: '))
