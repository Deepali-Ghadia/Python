# creating a stack class using list object
class Stack:
    def __init__(self):
        self.items = [] # intially stack is empty
    
    #method to check the stack is empty or not
    def isEmpty(self):
        return self.items == []
    
    #method for pushing an item
    def push(self, item):
        self.items.append(item) # uisng append method
        
        
    #method for popping an item
    def pop(self):
        return self.items.pop() # using pop method
    
    #check what item is on top of the stack without removing it
    def peek(self):
        return self.items[-1] #latest element 
    
    #method to get the size
    def size(self):
        return len(self.items)
    
    #to view the entire stack
    def fullStack(self):
        return self.items


# creating an object of stack class
stack = Stack()
print(stack.isEmpty())
stack.push(1)
stack.push(3)
stack.push(5)
stack.push(10)
print(stack.fullStack())
print(stack.peek())
