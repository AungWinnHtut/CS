import mysql.connector

# Replace with your actual database credentials
user = 'blue'
password = '1234@Awh'
host = 's3.greenhackers.org'
database = 'schooldb'

try:
    # Establish a connection
    conn = mysql.connector.connect(user=user, password=password, host=host, database=database)

    # Create a cursor
    cursor = conn.cursor()

    # Execute a simple query
    cursor.execute("select * from students")
    #conn.commit()

    for row in cursor:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
