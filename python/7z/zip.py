from os import system as sys
import os



basic ="7za "
archive = " a"
extract_archive = " x"
password_options = " -p"
password="12345"
archive_path =" archive.7z"
archive_path_options = " *.txt  "
unzip_path = "./unzip"
list_archive_option = " l "
compression_options = " -mx="
compression_ratio ="9"
encrypt_file_names =" -mhe="
encrypt_file_names_enable = "on"
encrypt_file_names_disable = "off"

command =""

# archive command
def archive():
    global command
    sys("del *.7z")
    command += basic + archive + password_options+password+archive_path+ archive_path_options+encrypt_file_names+encrypt_file_names_enable
    sys("cls")
    print(command)
    sys(command)

# list command
def list_archive():
    global command
    command += basic + list_archive_option + archive_path +password_options+password 
    sys("cls")
    print(command)
    sys(command)


if __name__ == "__main__":
    list_archive()