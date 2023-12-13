cities = ['yangon','mandalay','pyin oo lwin','taung gyi','lashio']
index = 0
while(1):
    ans = input('What is your command, V for traverse, A for append, D for delete: ')
    match(ans):
        case 'V':
            print(f'Next city is : {cities[index]}')            
            index += 1
            if index > (len(cities) - 1):
                index = 0
            
        case 'A':
            city_to_add = input('City name please: ')
            cities.append(city_to_add)
            
        case 'D':
            city_to_delete = input('City name please: ')
            cities.remove(city_to_delete)
            
        case 'E':
            exit(0)
        case _:
            print("Wrong command, Pls Try again!")