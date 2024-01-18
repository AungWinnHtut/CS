import json
import mysql.connector


db_connection = mysql.connector.connect(
    host = "s4.greenhackers.org",
    user = "blue",
    passwd = "1234@Awh",
    database = "schooldb"
)

found = False

# no error!
print('Database is connected successfully!')

mycursor = db_connection.cursor()
mycursor.execute("SHOW DATABASES")

for row in mycursor:
    print(row)
    