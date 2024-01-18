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

#mycursor.execute("CREATE DATABASE schooldb")
#mycursor.execute("SHOW DATABASES")
#mycursor.execute("CREATE TABLE students(id int primary key auto_increment, name varchar(20) not null, age int not null)")

mycursor.execute("SHOW Tables")
print('Table Lists')
print('___________')
for row in mycursor:
    print(row)

mycursor.execute("DESCRIBE students")
print('Table Structure')
print('___________')
for row in mycursor:
    print(row)

name = input('what is your name: ')
age = int(input('How old are you: '))

sql = "INSERT INTO students(name,age) values (%s,%s)"
params = (name,age) # Tuple

mycursor.execute(sql,params)
db_connection.commit()

mycursor.execute("SELECT name FROM students")
print('Table DATA')
print('___________')
for row in mycursor:
    print(row)

print('User under 10 years old are deleted')
mycursor.execute("DELETE from students where age < 10")
db_connection.commit()

mycursor.execute("SELECT name FROM students")
print('Table DATA')
print('___________')
for row in mycursor:
    print(row)

mycursor.close()
db_connection.close()