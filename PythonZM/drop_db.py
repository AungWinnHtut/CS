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

mycursor.execute('DROP DATABASE IF EXISTS gamedb')




mycursor.execute('SHOW  DATABASES')

found_db = False

for row in mycursor:
    if row[0]=='gamedb':
        print('found gamedb')
        found_db = True
        break
   

if not found_db:    
    print('NOT found gamedb')