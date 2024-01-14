from icecream import ic

dict = {
    'name': 'aung win htut',
    'father':{
        'name': 'u aye',
        'age': 77
    },
    'age': 46,
    'books':['peace','open mind'],
    'brothers': ['aung','maung'],
    'marks': [50,60,70]


}

for key,value in dict.items():
    print(f'Key = {key} and Value = {value}')