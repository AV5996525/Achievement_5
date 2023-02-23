numbers = {
    1: {},
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
    8: {},
    9: {},
    10: {}
}

for base, power in numbers.items():
    
    calcu = base ** 3  
    store = [list[base]]
    store1 = [list[calcu]]
    store2 = store1.extend(store) 
    numbers2 = {}
    numbers2 = {base, calcu}
    print(numbers2)
    print(store1)
    







    