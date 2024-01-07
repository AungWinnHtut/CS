from myconnection import connect_to_mysql
from icecream import ic
config = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "",
        "database": "schooldb",
    }

con = connect_to_mysql(config, attempts=3)

if con and con.is_connected():
    print('Database is connected')
    with con.cursor() as cursor:
        sql = 'SELECT * FROM students'
        cursor.execute(sql)
        result = cursor.fetchall()
        #ic(result)
        for row in result:
            ic(row)