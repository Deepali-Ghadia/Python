# Allows to modify the behaviour of functions and methods
# A way to extend the functionality of a function/method without modifying the source code
# Decorator is a function that takes anotehr function as an argument and returns new function that modifies the behaviour of original function  ===> new function is called decorated function

def smart_function(fxn):
    def add():
        print("Welcome")
        fxn()
        print("Thankyou")
        
    return add

@smart_function
def hello():
    print("Hello")
    
    
hello()