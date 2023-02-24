# List comprehensions are utilized to generate lists from other lists by applying functions to each element in the list. 

# List Comprehensions
# offers a shorter syntax when you want to create a new list based on the values of anexisting list.
# A list comprehension creates a new list by applying an expression to each element of an iterable. The most basic form is: [ <expression> for <element> in <iterable> ]

# creating squares of integers using list comprehension     
squares = [x*x for x in (1,2,3,4,5,6)]
print(squares)

# alternative ==> slower than the above method
squares = []
for x in (1, 2, 3, 4, 5, 6):
    squares.append(x*x)
print(squares)

# get a list of uppercase characters from string
characters = [s.upper() for s in "Deepali Ghadia"]
print(characters)

# using if in list comprehension
squares_of_even = [x*x for x in range(1, 20) if x%2==0]
print(squares_of_even)

# using if-else in list comprehension
# while using if-else together put the condition checking before the for loop
squares_or_cubes = [x*x if x%2==0 else x*x*x for x in range(1, 10) ]
print(squares_or_cubes)

# double iteration in list
num = [1, 2, 3]
for i in num:
    for j in num:
        print(i*j)



# dictionary comprehensions
# method1
cubes = {x: x*x*x for x in (1,2,3,4)}
print(cubes)
# method2
cubes = dict((x, x*x*x) for x in (1,2,3,4))
print(cubes)


# merging dictionaries using dictionary comprehension
dict1 = {1:"A", 2:"B", 3:"C", 4:"D"}
dict2 = {3:"e", 4:"f", 5:"g", 6:"h"}
combined_dict = {k:v for d in [dict1, dict2] for k,v in d.items()}
print(combined_dict)


# set comprehensions
numbers = {x for x in range(1,5)}
print(numbers)





