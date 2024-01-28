def areaOfCircle(r):    
    a = 3.14 * r * r
    return a


def areaOfRectangle(l,w):    
    a = l * w
    return a


def vol(a,h):
    v = a * h
    return v



# Program start here
areaofcircle = areaOfCircle(12.5)
areaofrectangle = areaOfRectangle(12,5.6)

print(f'Area of Circle is {areaofcircle}')
print(f'Area of Rectangle is {areaofrectangle}')



print(f'Volume of Cylinder {vol(areaofcircle,231)}')
print(f'Volume of Box {vol(areaofrectangle,213)}')