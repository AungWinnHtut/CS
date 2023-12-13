password = '123'
fail = 0
passwordinput = input('Enter password:')

while passwordinput != password:
    fail += 1
    if fail > 2:
        print('Sorry, wrong password 3 times. Bye bye')
        exit(1)
    passwordinput = input('Enter password:')


print("Password Correct!    ")