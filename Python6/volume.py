from icecream import ic
with open('area.txt','r') as file:
    lines = file.readlines()

h = float(input('Enter h: '))

out_file = open('volume.txt','a')

for line in lines:
    ic(line)
    r,a = line.split('-')
    r = float(r.strip())
    a = float(a.strip())
    v = a * h
    out_file.write(str(r)+'-'+str(a)+'-'+str(h)+'-'+str(v)+'\n')

out_file.close()