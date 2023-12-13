with open("data1.txt", "r+") as f:
    f.seek(5)
    f.write('a')