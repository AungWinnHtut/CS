from icecream import ic
radius_file = open('r.txt','r')
area_file = open('a.txt','a')
radii = radius_file.readlines()
for r in radii:
    ic(r.strip())
    radius = float(r)
    area = 3.14 * radius * radius
    print(f'Area for R={radius} is {area}')
    area_file.write(str(area)+'\n')

radius_file.close()