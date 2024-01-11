from myconnection import connect_to_mysql
from icecream import ic

# functions start here
def create_table(cursor, table_name, table_str):
    query = "CREATE TABLE testtable (%s)"
    cursor.execute(query% (table_str,))
   



def main():
    config = {
            "host": "127.0.0.1",
            "user": "root",
            "password": "",
            "database": "schooldb",
    }

    with connect_to_mysql(config, attempts=3) as con:
        if con and con.is_connected():
            print('Database is connected')
    
            with con.cursor() as cursor:
                create_table(cursor,"test",'id int primary key auto_increment')

            con.commit()
    
            
#functions end here


# Actual code start here
if __name__ == '__main__':
    main()