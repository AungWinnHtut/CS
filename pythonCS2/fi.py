data_file = open('hello.txt','r')
data = data_file.readlines()

for d in data:
    print(d.strip())

data_file.close()