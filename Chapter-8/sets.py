# operations on sets
set1 = {"A", "B", "C", "a", "c", "d"}
set2 = {"a", "b", "c", "d"}
print(set1)
print(set2)
# intersection
print("Intersection of sets")
print(set1.intersection(set2))
# union
print("Union of sets")
print(set1.union(set2))
# difference
print("Difference of sets")
print(set1 - set2)
# symmetric difference with (either in any of the set)
print("Symmetric Difference of sets")
print(set1.symmetric_difference(set2))
print(set1 ^ set2)
# superset check
print("Checking for superset")
print(set1.issuperset(set2))
print(set1 >= set2)
# subset check
print("Checking for subset")
print(set1.issubset(set2))
print(set1 <= set2)
# disjoint check
print("Checking for disjoint")
print(set1.isdisjoint(set2))
# testing membership
print("a" in set1)
# length of set
print(len(set1))
print(len(set2))

# get unique elements of a list
fruits = ["Apple", "Banana", "Orange", "Apple", "Banana", "Apple", "Kiwi"]
print(fruits)
print("Unique elements from the list are: ", set(fruits))


# set of sets
# set_of_sets = {{1, 2, 3}, {"a", "b"}} #gives typeerror
set_of_sets = {frozenset({1, 2, 3}), frozenset({"a", "b"})}
print(len(set_of_sets))



# sets v/s multi-sets(allows for multiple instances for each of its elements.)
# in python we implement multi-sets using Counter class from Collections module
# Counter is a dictionary where where elements are stored as dictionary keys and their counts are stored dictionary values
from collections import Counter
counterA = Counter(["Apple", "Banana", "Orange", "Apple", "Banana", "Apple", "Kiwi"])
print(counterA)

