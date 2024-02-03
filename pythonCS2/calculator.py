
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b


while True:
    a = input('enter a: ')
    b = input('enter b: ')
    a = float(a)
    b = float(b)

    o = input('enter operator: (+,-,*,/,e) >> ')

    if o == '+':
        sum = add(a,b)
        print(f'a + b = {sum}')

    elif o == '-':
        sub1 = sub(a,b)
        print(f'a - b = {sub1}')

    elif o == '*':
        mul1 = mul(a,b)
        print(f'a * b = {mul1}')

    elif o == '/':
        div1 = div(a,b)
        print(f'a / b = {div1}')
    else:
        print('bye')
        exit(0)