from icecream import ic
import random
import os



x = 0
y = 0
ans = 0
if os.path.exists('Q.txt'):
    os.remove('Q.txt')
with open("Q.txt",'a') as file:
    for i in range(10):
        # question variables
        x = random.randint(1,100)
        y = random.randint(1,10)
        # wrong answers
        a = random.randint(1,100)
        b = random.randint(1,100)
        c = random.randint(1,100)  
        # ans position locator      
        k = random.randint(1,3)

        ans = x * y

        match(k):
            case 1: a = ans
            case 2: b = ans
            case 3: c = ans


        file.write(f"{x}*{y} ? 1-{a}, 2-{b}, 3-{c} : #{k}\n")