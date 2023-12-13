from icecream import ic
r = float(input('Enter r: '))
a = 3.14 * r * r 
ic(r)
ic(a)
with open('area.txt','a') as file:
    file.write(str(r)+'-'+str(a)+'\n')