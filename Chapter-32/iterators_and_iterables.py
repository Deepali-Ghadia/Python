# Iterable -> an object that can be iterated (list, tuple, strings, dict, etc) | __get_item__() or __iter__()
# Iterator -> is an object that has next() method defined. | __nex__() method
# Iteration -> The process of iterating an object and fetching its next elements


# extract values one by one
name = "Deepali"
iterator = iter(name) # this function is used to get iterator for the iterable i.e get iterator for num so that we can iterate over it using the iterator
# Analogy: to iterate over anything we need an iterator. Eg. to iterate a list, we use i as an iterator
print(next(iterator)) # next method is used to iterate and print next value. Prints single value at a time
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) Here the iteration is stopped automatically as there is no further element in the iterable



# iterating over entire iterable
lis1 = [1, 2, 3, 4, 5, 6, 7]
for i in lis1:
    print(i)
