# arrays in python are closer to lists

# creating an array using array library
from array import *
# arrayIdentifierName = array(typecode, [Initializers]) | Typecodes are the codes that are used to define the type of array values or the type of array (refer the table)

# creating an array of signed integers each of size 2bytes
signed_array = array('i', [10, 20, 30, 40, 50, 60])


# accessing individual elements of array using indexes
print(signed_array[0])
print(signed_array[3])


# appending any value to array using append method
signed_array.append(70)
print(signed_array)


# insert value in an array using insert method
signed_array.insert(2, 55) # insert 55 at 2nd index
print(signed_array)


# extend python array using extend method ==> extending by more than one value
arr1 = array('i', [1,2,3,4,5])
arr2 = array('i', [6,7,8,9,10])
arr1.extend(arr2)
print(arr1)


# add items from list to array using fromlist() method
list1 = [100, 101, 102, 103]
arr1.fromlist(list1)
print(arr1)


# remove any array element using remove() method
arr1.remove(100)
print(arr1)


# remove last element using pop()
arr1.pop
print(arr1)

# reverse an python array using reverse method
arr1.reverse()
print(arr1)

# get array buffer information using buffer_info method  ==> buffer start address and number of elements
print(arr1.buffer_info())


# no of occurences of an element using count method
freq_array = array('i', [1,2,3,2,3,4,5,5,5,5,6,7,8,8,7,6])
print(freq_array.count(5))


# convert array to list using tolist() method
array_to_list = arr1.tolist()
print(array_to_list)