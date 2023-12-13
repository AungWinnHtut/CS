with open('questions.txt','r') as file:
    all_lines = file.readlines()


for line in all_lines:
    print(line.strip())