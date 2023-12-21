from myconnection import connect_to_mysql
from icecream import ic

def drop_table(cursor,table_name):
    query = "DROP TABLE if exists %s"
    cursor.execute(query % table_name)

def create_table(cursor, table_name, table_str):
    query = "CREATE TABLE %s (%s)"
    cursor.execute(query % (table_name, table_str))


def create_student(cursor, name, age):
    query = "INSERT INTO students (name, age) VALUES (%s, %s)"
    cursor.execute(query , (name, age))

def read_students(cursor):
    query = "SELECT * FROM students"
    cursor.execute(query)
    return cursor.fetchall()

def update_student(cursor, student_id, new_name, new_age):
    query = "UPDATE students SET name=%s, age=%s WHERE id=%s"
    cursor.execute(query, (new_name, new_age, student_id))

def delete_student(cursor, student_id):
    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (student_id,))

def main():
    config = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "",
        "database": "schooldb",
    }

    cnx = connect_to_mysql(config, attempts=3)

    if cnx and cnx.is_connected():
        with cnx.cursor() as cursor:
            drop_table(cursor,'customers')
            create_table(cursor, 'customers', 'id int primary key auto_increment,name varchar(20) not null')
            # Create a new student
            create_student(cursor, "Aung Win Htut", 20)
            

            # Read all students
            print("All students:")
            students = read_students(cursor)
            for student in students:
                print(student)

            # Update a student
            update_student(cursor, 1, "New Student", 25)

            # Read all students after update
            print("\nAll students after update:")
            students = read_students(cursor)
            for student in students:
                print(student)

            # Delete a student
            delete_student(cursor, 1)

            # Read all students after delete
            print("\nAll students after delete:")
            students = read_students(cursor)
            for student in students:
                print(student)

        cnx.commit()
        cnx.close()
    else:
        print("Could not connect to the database")

if __name__ == "__main__":
    main()
    # pass
