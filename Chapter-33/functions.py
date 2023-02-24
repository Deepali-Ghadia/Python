# To define a function with arbitrary number of arguments add a * before the parameter name in the function definition
# function will receive a tuple of arguments, and can access the items accordingly
def sum(*elements):
    sum = 0
    for i in elements:
        sum = sum + i
    return sum

res1 = sum(1, 2, 3, 4, 5, 6, 7)
print(res1)

res2 = sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(res2)


# arbitrary number of keyword arguments ==>arguments can be passed in terms of key:value pairs
# in this case, the order of arguments does not matter

# normal function accepting keyword arguments i.e. arguments in the form of key-value pairs
def print_colors(color1, color2):
    print(color1)
    print(color2)
        
print_colors(color1= "Red", color2= "Blue")

# function accepting arbitrary number of keyword arguments
def print_colors(**kwargs):
    for name, value in kwargs.items(): # names=> keys  values=>values
        print(name, value)
        
print_colors(color1= "Red", color2= "Blue")
print_colors(color1= "Red", color2= "Blue", color3 = "Yellow", color4= "Black")


# lambda functions => inline functions => anonymous functions
# take any number of arguments, but can only have one expression.
# The lambda keyword creates an inline function that contains a single expression. The value of this expression is what the function returns when invoked.
x = lambda(x): x*x
res = x(5)
print(res)