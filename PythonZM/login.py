import mysql.connector

db_connection = mysql.connector.connect(
    host = "s4.greenhackers.org",
    user = "blue",
    passwd = "1234@Awh",
    database = 'gamedb'        
)
# NO ERROR IN CONNECTION
print('mySQL is connected successfully!')


name = input('Username: ')
password = input('Password: ')



mycursor = db_connection.cursor()

try:    
    mycursor.execute('SELECT * FROM usertb')
    found_user = False    
    for row in mycursor:        
        if row[1] == name and row[2] == password:            
            found_user = True
            print("Login Successfully")
    
    if not found_user:   
        print("No such USERNAME")
except:
    print("Database error!")







