# Tuple is a immutable list of values

# built-in tuple functions
tup1 = ('a', 'b', 'c', 'd', 'e', 'f')
tup2 = (1, 2, 3, 4, 5,)


# length of tuple
print(len(tup1))


# max and min of a tuple
print(max(tup1))
print(min(tup1))


# convert a list into tuple
l1 = [1, 2, 3, 4, 5]
print(l1)
from_list = tuple(l1)
print(from_list)


# concatenating tuples
res = tup1 + tup2
print(res)


# Accessing elements of tuple using index
print(tup1[0])
print(tup1[1])
print(tup1[3])
print(tup1[5])
# using negative indexes
print(tup1[-1])
print(tup1[-2])
print(tup1[-3])
print(tup1[-5])
# using range
print(tup1[2::-1])


# reversing elements of a tuple
print(tup1[::-1])

print(reversed(tup1))