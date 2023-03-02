# Python is a dynamically typed language, which means you never have to explicitly indicate what kind of variable it is. But in some cases, dynamic typing can lead to some bugs that are very difficult to debug, and in those cases, Type Hints or Static Typing can be convenient. 

# The Type-Hint is completely ignored by the Python interpreter. Therefore, install mypy


def factorial(i):
    if i<0:
        return None
    if i == 0:
        return 1
    
    return i * factorial(i-1)
 

print(factorial(4))
print(factorial("4"))
print(factorial(5.01))

# to specify the data type of the value to be accepted we can use type hints

def factorial(i: int ) -> int: # first int -> dataype of parameter | second int -> datatype of return value
    if i<0:
        return None
    if i == 0:
        return 1
    return i * factorial(i-1)
 
# passing a fraction to the function
print(factorial(5.01))
# TypeError: unsupported operand type(s) for *: 'float' and 'NoneType'