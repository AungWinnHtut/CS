import json

f = open("test.json",'r')

# json.dump(x,f)
x = json.load(f)
print(x)