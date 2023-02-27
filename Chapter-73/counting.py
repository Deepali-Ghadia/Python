import collections


# counting occurences of all the items
list1 = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 6, 7,7, 7, 7,7, 7,7,4 ,3, 23 ,3 ,6 ,6 ,78,9,]
print(collections.Counter(list1))

tup1 = tuple(list1)
print(collections.Counter(tup1))


# getting the most common value using Counter.most_common()
print(collections.Counter(list1).most_common()) # prints all the values
print(collections.Counter(list1).most_common(2))


# counting the occurence of one item in a list and a tuple
print(list1.count(7))
print(tup1.count(1))


# counting the occurence of a substring in a string using str.count()
statement = "this is a this a n m and this a aa a a a a nn the nin h the the the the the the ht he"
print(statement.count("i"))
print(statement.count("this"))