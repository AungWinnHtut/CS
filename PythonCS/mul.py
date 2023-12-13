import random

x = random.randint(2,12)
y = random.randint(2,12)

ans = input(f' {x} * {y} =  ')
ans = int(ans)

rans = x * y

if ans == rans:
    print("Correct answer   ")
else:
    print("Wrong answer ")