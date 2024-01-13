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

mycursor.execute('DROP TABLE IF EXISTS usertb')




mycursor.execute('SHOW  TABLES')

found_db = False

for row in mycursor:
    if row[0]=='usertb':
        print('usertb is not deleted')
        found_db = True
        break
   

if not found_db:    
    print('usertb is deleted successfully')