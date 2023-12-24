import subprocess
import time

def backup_database():
    # Replace with your MySQL connection details
    mysql_username = 'root'
    mysql_password = ''
    database_name = 'schooldb'
    
    # Replace with the desired file path for the backup
    backup_file_path = "e:\\cs2024\\schooldb.sql"

    # Build the mysqldump command
    mysqldump_cmd = f"mysqldump -u {mysql_username} -p{mysql_password} {database_name} > {backup_file_path}"

    # Execute the mysqldump command
    subprocess.run(mysqldump_cmd, shell=True)
    

def restore_database():
    # Replace with your MySQL connection details
    mysql_username = 'root'
    mysql_password = ''
    database_name = 'test'
    
    # Replace with the file path of the backup to restore
    backup_file_path = "e:\\cs2024\\schooldb.sql"

    # Build the mysql command for restoring
    mysql_cmd = f"mysql -u {mysql_username} -p{mysql_password} {database_name} < {backup_file_path}"

    # Execute the mysql command for restoring
    subprocess.run(mysql_cmd, shell=True)

# Run the backup and restore process every 20 minutes

try:
    restore_database()
except Exception as e:
    print(f"An error occurred: {e}")
