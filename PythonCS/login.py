username = input('Username: ')
password = input('Password: ')

if username == 'Aung Win Htut':
    print('Username OK!')
    if password == '1234':
        print('Login successful')
        
    else:
        print('Login failed')
else:
    print('Error! No such Username!')
