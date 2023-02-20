# string datatype
str1 = "APPLE"
print(str1[0])
print(str1[1])
print(str1[:4])

# set datatype
fruits = {'apple', 'banana', 'orange', 'mango', 'apple', 'orange', 'orange'}
print(fruits) # duplicates will be removed
print("New item added")
fruits.add('kiwi') #adding new element to the set
print(fruits)

# defining frozen sets
print("Learning about frozen sets")
vegetables = frozenset({'tomato', 'potato', 'cabbage', 'tomato', 'cauliflower', 'potato'})
print(vegetables)