# Basic slicing
string = "My name is Deepali Ghadia"
print(len(string))
print(string[::])
print(string[3:8])

# reversing an object using slicing operator
print(string[::-1])

# slice assignment
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)
# replacing multiple members in a single assignment
list1[2:5] = [6]
print(list1)


# making a shallow copy of an array
arr1 = list1
arr1_copy = arr1[:]
print(arr1_copy)