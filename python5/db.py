import mysql.connector

def create_connection():   
    return mysql.connector.connect(
        host="localhost",  # or your host
        user="root",
        password="",
        database="store"
    )

def read_all_data(inputcursor):
    sql_cmd = 'select * from inventory'
    inputcursor.execute(sql_cmd)
    return inputcursor.fetchall()


con = create_connection()
if not con.is_connected():
    exit(1)

# Start real code here
mycursor = con.cursor()
result = read_all_data(mycursor)
print(result)