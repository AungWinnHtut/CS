name = input('enter username: ')
password = input('enter password: ')
count = 1

while name != 'aung' or password != '1234':    
    count += 1
    print('Wrong Password: ')
    name = input('enter username: ')
    password = input('enter password: ')
    if count >= 3:
        exit(1)
    


# Passed
print('Login OK')
pass





