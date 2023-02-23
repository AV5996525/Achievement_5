#Name:          achieve_5.py
#Author:        AJ Varatharajan
#Date Created:  February 22, 2023
#Date Last Modified: February 23, 2023
#Purpose: Program will cycle through the values one to ten and will output each value expressed in cubed form.
# 
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
    store2 = store.append(store1) 
    numbers2 = {}
    numbers2 = {base, calcu}
    print(numbers2)
    print(store)
    







    