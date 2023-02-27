#Name:          achieve_5.py
#Author:        AJ Varatharajan
#Date Created:  February 22, 2023
#Date Last Modified: February 26, 2023
#Purpose: Program will cycle through the values one to ten and will output each value expressed in cubed form.
# 
numbers = { #creating dictionary
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

for base, power in numbers.items(): #cycling through each entry in the dictionary
    
    calcu = base ** 3  #Raising each entry to power of three and saving it to a variable
    store = [list[base]] #Saving our base values as a list
    store1 = [list[calcu]] #Saving our final calculation as a list
    store2 = store.append(store1) #joining our two lists together
    numbers2 = {} #creating an empty dictionary
    numbers2 = {base, calcu} #creating an entry for each cycle
    print(store)
    







    