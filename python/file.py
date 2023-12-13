
with open("data1.txt", "w") as save_file:
    with open("data.txt","r") as data_file:
        lines = data_file.readlines()
        for line in lines:
            if not (line == " " or line == "" or line == "\n"):
                save_file.write(line)

    

    