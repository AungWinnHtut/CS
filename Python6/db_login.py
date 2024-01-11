import mysql.connector
from icecream import ic

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "schooldb"
)

print('Database is connected')

uname = 'aung'
password = '1234'
found = False
mycursor = db.cursor()
#sql_cmd = 'CREATE TABLE users (id int primary key auto_increment, name varchar(20) not null UNIQUE, password varchar(20) not null)'
#sql_cmd = 'DESCRIBE users'
#sql_cmd = "INSERT INTO users(name,password) values ('aung','1234'),('maung','5678')"
sql_cmd = 'SELECT * FROM users'
mycursor.execute(sql_cmd)
data = mycursor.fetchall()
#db.commit()

for row in data:
    ic(row)
    if row[1] == uname and row[2] == password:
        print("Signin successfully!")
        found = True
        break


if not found:
    print('Signin Failed')