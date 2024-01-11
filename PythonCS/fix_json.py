from icecream import ic
with open('q.txt','r') as file:
    data = file.read()

ic(data)

fixed = []

for ch in data:
    if ch == "'":
        ch = '"'
    elif ch == '=':
        ch = ':'
    fixed.append(ch)

with open('q.json','w') as outfile:
    for f in fixed:
        outfile.write(f)

ic(fixed)