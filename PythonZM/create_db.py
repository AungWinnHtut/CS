import mysql.connector
from mycon import connect_to_mysql
from db_config import config


# cnx = database connection object
cnx = connect_to_mysql(config, attempts=3)

# NO ERROR IN CONNECTION
print('mySQL is connected successfully!')

mycursor = cnx.cursor()

mycursor.execute('CREATE DATABASE IF NOT EXISTS gamedb')




mycursor.execute('SHOW  DATABASES')

found_db = False

for row in mycursor:
    if row[0]=='gamedb':
        print('found gamedb')
        found_db = True
        break
   

if not found_db:    
    print('NOT found gamedb')