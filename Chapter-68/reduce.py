# reduce reduces an iterable by applying a function repeatedly on the next element of an iterable and the   cumulative result so far
# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.
''' At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.
'''
# reduce(function,iterable)
import functools
list_of_elements = [1,2,3,2,2,1,3,4,5,6,7,4,3,2,1,5,6,2,3,4,5,4,3,2,2,2,4,5,6,7,8,8,9]

# we are using reduce function to calculate sum of values
print(functools.reduce(lambda x,y: x+y, list_of_elements))


# calculating cumulative product using reduce
print(functools.reduce(lambda a,b: a*b, list_of_elements))