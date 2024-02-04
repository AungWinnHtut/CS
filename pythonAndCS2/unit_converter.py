while True:
    print('1. inches to cm:')
    print('2. cm to inches:')
    print('3. miles to km:')
    print('4. km to mile:')
    print('5. Exit')
    ans = input('Choose one (1,2,3,4,5)')

    if ans == '1':
        coe = 2.54
        inches = input('Enter inches: ')
        inches = int(inches)    
        cm = coe * inches
        print(f' {inches} inches = {cm} cm')

    elif ans == '2':
        coe = 0.393701
        cm = input('Enter cm: ')
        cm = int(cm)    
        inches = coe * cm
        print(f' {cm} cm = {inches} inches')

    elif ans == '3':
        coe = 1.60934
        miles = input('Enter miles: ')
        miles = int(miles)    
        km = coe * miles
        print(f' {miles} miles = {km} km')

    elif ans == '4':
        coe = 0.621371
        km = input('Enter km: ')
        km = int(km)    
        miles = coe * km
        print(f' {km} km = {miles} miles')

    elif ans == '5':
        print('Bye!')
        exit(0)  # zero - success
