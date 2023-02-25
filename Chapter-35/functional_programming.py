# lambda function
square = lambda x: x*x
print(square(5))

# map function => map(function, iterable)
# Map takes a function and a collection of items. It makes a new, empty collection, runs the function on each item in the original collection and inserts each return value into the new collection. It returns the new collection.
def cube(x):
    return x*x*x

cubes = map(cube, [1, 2, 3, 2, 1, 2, 5, 6])
print(cubes) # prints map object
print(list(cubes))
# maps the numbers with their corresponding cubes

