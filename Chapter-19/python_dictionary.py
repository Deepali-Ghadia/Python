from collections import OrderedDict
# creating a python dictionary
# values are accessed through keys
empty_dict = {}
dict1 = {1: "Red", 2: "Blue", 3: "Pink", 4: "Yellow"}

# KeyError exception => while accessing a key that does not exist


# Iterating over a dictionary
for key in dict1:
    print(key, dict1[key]) #dict[key] gives value of a particular key
    
    
# accessing keys and values
print(dict1.keys())
print(dict1.values())
print(dict1.items()) # prints key: value pair


# Accessing values of a dictionary
# We access values by placing the key in the square brackets
print(dict1[1])
print(dict1[3])


# Creating an ordered dictionary ==> OrderedDict from the collections module. 
# remembers the order that keys were first inserted.
print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
 
for key, value in od.items():
    print(key, value)


# dict() constructor
dict2 = dict(name = "John", age = 36, country = "Norway")
print(dict2)

dict3 = dict(first = "A", second = "B")
print(dict3)