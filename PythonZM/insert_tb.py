import mysql.connector

db_connection = mysql.connector.connect(
    host = "s4.greenhackers.org",
    user = "blue",
    passwd = "1234@Awh",
    database = 'gamedb'        
)
# NO ERROR IN CONNECTION
print('mySQL is connected successfully!')

mycursor = db_connection.cursor()

try:    
    mycursor.execute('SELECT * FROM usertb')
    found_user = False    
    for row in mycursor:        
        if row[1] == 'aung':            
            found_user = True
            print("Duplicate data !! user name tun1 already exists")
    
    if not found_user:   
        mycursor.execute("INSERT INTO usertb(name,password) values ('aung','234');")
        db_connection.commit()
except:
    print("Data insertion error!")



mycursor.execute('SELECT * FROM usertb')

found_db = False

total_user = 0
for row in mycursor:
    print(row)
    total_user += 1
   

print(f'total users is {total_user}')

