# searching an element in list
list1 = [1, 2, 3, 4,5 ,6 ,7 ,7]
print(5 in list1)
print(10 in list1)


# getting the index for strings
name = "Deepali Ghadia"
print(name.index('i')) # gives the first occurence
print(name.rindex('i')) # gives the last occurence
# index() => gives error if value is not found => value error

print(name.find('y')) # returns -1
print(name.rfind('i'))


# getting index of list and tuples
print(list1.index(6))

tup1 = (1, 2, 3, 4, 5, 6)
print(tup1.index(5))