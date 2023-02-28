# accessing attributes using dot notation
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
        
        
animal1 = Animal("cow", "domestic")
print(animal1.name)
print(animal1.type)
print("{} is {} animal".format(animal1.name, animal1.type))



# accessing attributes using getter and setters method
class Object:
    def __init__(self, name):
        self.name = name
        
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    
obj1 = Object("Apple")
print(obj1.get_name())
obj1.set_name("Mango")
print(obj1.get_name())