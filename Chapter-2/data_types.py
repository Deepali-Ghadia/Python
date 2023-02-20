# datatype: string
str1 = "APPLE"
print(str1[0])
print(str1[1])
print(str1[:4])

# datatype: set
fruits = {'apple', 'banana', 'orange', 'mango', 'apple', 'orange', 'orange'}
print(fruits) # duplicates will be removed
print("New item added")
fruits.add('kiwi') #adding new element to the set
print(fruits)

# defining frozen sets
print("Learning about frozen sets")
vegetables = frozenset({'tomato', 'potato', 'cabbage', 'tomato', 'cauliflower', 'potato'})
print(vegetables)

# datatype: number
sum = 100;
print("Sum is: ", sum)
division = 1/3;
print("Division is: ", division)

# datatype: list
fruits = ['apple', 'banana', 'orange', 'mango', 'apple', 'orange', 'orange']
print(fruits[0])
print(fruits[5])
print(fruits[-1])

# datatype: dictionary
dict = {'color': 'red', 'name': 'abc'}
print(dict)
print(dict.keys())

# datatype: tuples
tup = ('apple', 'banana', 'orange', 'mango', 'apple', 'orange', 'orange')
print(tup)