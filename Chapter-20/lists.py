list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19]

# adding new element at the end of the list using append
list1.append(10)
print(list1)
#  the append() method only appends one new element to the end of the list. If you append a list to another list, the list that you append becomes a single element at the end of the first list.

# extend a list
list1.extend(list2)
print(list1)

# index(value, [startIndex])
print(list1.index(11))
print(list1.index(11, 5)) # start searching from the 5th index


# insert element into a list ==> inserts element just before the specified index
list2.insert(4, 200)
print(list2)

# pop element from a particular index
list2.pop(4)
print(list2)

# remove the first occurence of an element from the list
list2.remove(13)
print(list2)

# reverse a list ==> reverses the list inplace
print(list2.reverse()) # return None

# reverse a list using sort function

print(list2.sort(reverse=True))


# count occurence of some value
rep_list = [1,1,2,3,4,2,3,4,5,5,55,5,3,2,1,2]
print(rep_list.count(1))


# sorting a list
alpha = ['A', 'C', 'B', 'E', 'D']
print(alpha.sort()) # returns None


# replication a list
dash = ["---"]
print(dash*20)


# deleting an element using del keyword and slice notation ==>can delete multiple items
del list1[6:]
print(list1)


# Checking if a list is empty
empty_list = []
num_list = [1]
if not empty_list:
    print("Empty")
    
if not num_list:
    print("Empty")
else:
    print("Contains element")
    
    
    
# Iterating over a list
for item in list1:
    print(item)
    
    
# Checking whether a item is present in a list or not
fruits = ["Apple", "Banana", "Mango", "Orange", "Papaya"]
print("Apple" in fruits) # True
print("Kiwi" in fruits) # False


# Reversing elements of a list
print(fruits.reverse()) # returns None
reversed_list = fruits.reverse()
# print(reversed)  ==> prints None
print(reversed(fruits))
# using slicing
print(fruits[::-1])


# concatenate and merge lists
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
res = list1 + list2
print(res)

# printing length of list
print(len(res))


# removing duplicate values from a list  ==> convert into set and then back to list
print(rep_list)
print(list(set(rep_list)))


# Comparing lists
l1 = [1,2,3]
l2 = [2,5,-1]
print(l1 < l2)


# initializing a list to a fixed number of elements
listt = [1] * 10
print(listt)

name = ["Deepali"]*5
print(name)