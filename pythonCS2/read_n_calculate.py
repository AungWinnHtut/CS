from icecream import ic
r = input('input r: ')

ic(r)
r = float(r)
ic(r)

a = 3.14 * r * r

if a <= 100:
    print('Small Area')
    print('.')
elif a >100 and a <= 200:
    print("Medium Area")
elif a != 300:
    pass
else:
    print('Large Area')



print(f'A = {a}')