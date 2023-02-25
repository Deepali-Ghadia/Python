# non local variable -> reference a variable in the nearest scope. It is not a global variable
# The nonlocal keyword is used in nested functions to reference a variable in the parent function.

# global variales => can be used anywhere in a single file
# local variable => can be used inside a single function

# example demonstrating global variable
n = 10 #global variable
def display():
    print(n) # will take the global variable
display()


# example demonstrating local variable
def display():
    a = 100 # has local scope, can be accessed inside the function only
    print(a)
# a = a +1  gives error that a is not defined
display()
#print(a)


# Example demonstrating nonlocal variable  ==> used inside nested functions
x = 100
def display():
    b = 10
    print(b) # 10
    print(x) # 100
    
    def show():
        b = b + 10
        print(b)
        print(x)
        
    show() # calling inner function
    
display() # calling main function
# This code gives error on line 31 => local variable 'b' referenced before assignment


# updating the code
def display():
    b = 10
    print(b) # 10
    print(x) # 100
    
    def show():
        nonlocal b # to use the variable of the parent function
        b = b + 10
        print(b) # 20
        print(x) # 100 | global variable
        
    show() # calling inner function
    
display() # calling main function

x = 100
del x # removes a variable from its scope

# local verses global scope
# All Python variables which are accessible at some point in code are either in local scope or in global scope.
# The explanation is that local scope includes all variables defined in the current function and global scope includes
# variables defined outside of the current function.

# global verses non local
# Both are used to reference a variable that are not local to the current functions


# inspecting scope of variables defined in this file (displayed as dictionary)
print(globals().keys()) # prints all variable names in global scope
print(locals().keys())  # prints all variable names in local scope


# modifying a global variable
def modify():
    x = x * 3
    print(x)
    
modify() # gives UnboundLocalError => local variable 'x' referenced before assignment

# modifying the above code
def modify():
    global x
    x = x * 3
    print(x)
    
modify() # 300