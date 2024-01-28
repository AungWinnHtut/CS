from icecream import ic


#students = ['aung','maung','soe','toe']

#for one_student in students:
    #print(one_student)

#print(students[4])


radii = []
while True:
    r = input('Enter Radius or q to exit: ')
    if r == 'q' or r == 'Q':
        break
    else:
        r = float(r)
        radii.append(r)

ic(radii)
ic(radii[0])
ic(radii[1])
ic(radii[2])
ic(radii[3])


ic(radii[-1])
ic(radii[-2])
ic(radii[-3])
ic(radii[-4])


for r in radii:
    a = 3.14 * r * r
    print(f'for radius = {r}cm  area = {a} sqcm')
