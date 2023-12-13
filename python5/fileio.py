
with open('dir.txt','r') as file:
    start = file.tell()
    total = start
    print(f'start position of file: {start}')
    for i in range(10):
        line = file.readline()
        print(line)
        size = len(line)
        total += size
        print(total)
        oneline = file.tell()
        print(f'one line position of file: {oneline}')
    


