# Generators are iterators from which you can generate value only once i.e. they can be iterated only once
# range() is a generator => can be iterated only once.
# Generator functions are similar to regular functions, except that they have one or more yield statements in their body.
''' for i in range(10000000):
        print(i)
This block of code will take time and will consume RAM as well.
Solution: you can create a generator that does not actually print the value of i but is capable to generate these kind of values. You make use of the yield keyword.
It creates a generator object that can be then used in the code. Basically, it just creates an object and does not occupy the significant portion of the RAM
'''

def gen(n):
    for i in range(n):
        yield i
  
  
res =  gen(10000000)     
print(res)
print(next(res))
print(next(res))
print(next(res))

# for i in gen(10000000):
#     print(i)



