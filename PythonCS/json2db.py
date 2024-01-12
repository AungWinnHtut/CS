import json
import mysql.connector


db_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "schooldb"
)

found = False

# no error!
print('Database is connected successfully!')

mycursor = db_connection.cursor()
mycursor.execute("CREATE TABLE  IF NOT EXISTS examtb(id int primary key auto_increment, question text not null, option1 text not null, option2 text not null, option3 text not null, correct_ans text not null)")


mycursor.execute("SHOW TABLES")
for row in mycursor:
    #print(row)
    if row[0] == 'examtb':
        print('Table created successfully')
        found = True

if not found:
    print('Table creation Fails')