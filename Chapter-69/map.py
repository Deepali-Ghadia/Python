# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable
# map(function, iterable)

# mapping each value in an iterable
list1 = map(lambda x:x*2, [1, 2, 3, 4, 5])
for i in list1:
    print(i)
    
    
    
# taking list as input from user using map function
# int() => coverts the value into integer
list(map(int, input("Enter multiple value separated by whitespace: ").split()))
    
