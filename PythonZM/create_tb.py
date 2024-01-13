import mysql.connector

db_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "gamedb"
    
    
)
# NO ERROR IN CONNECTION
print('mySQL is connected successfully!')

mycursor = db_connection.cursor()

mycursor.execute('CREATE TABLE IF NOT EXISTS usertb(id int primary key auto_increment, name varchar(20) UNIQUE not null, password varchar(20) not null)')




mycursor.execute('SHOW  TABLES')

found_db = False

for row in mycursor:
    if row[0]=='usertb':
        print('usertb is created successfully')
        found_db = True
        break
   

if not found_db:    
    print('usertb creation fails')