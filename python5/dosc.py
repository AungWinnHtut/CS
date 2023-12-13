import os

cmd = "rd "

folder = "test"

cmd = cmd + folder 

for i in range(10000):
    cmd1 = ""
    i = str(i)
    cmd1 += cmd+i
    os.system(cmd1)
    

