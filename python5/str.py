import random as rnd
name = 'Aung Win Htut and Min Htut'

t = (1,1,3)


s = {1,2,3}
p = {1,1,3}
d = set()

for i in range(100000):
    dice = rnd.randint(1,6)
    d.add(dice)


print(d)