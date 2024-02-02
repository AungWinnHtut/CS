file = open('unicode.txt','w',encoding='utf-8')
for i in range(0,55291):
    char = chr(i)
    print(f'{i} - {char}')
    file.write(str(i)+' - '+char+'\n')

file.close()