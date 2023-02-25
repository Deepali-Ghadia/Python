# Implementing basic inheritance in python
class Object:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("Name of this object is {}".format(self.name))

class Animal(Object):
    def print_type(self):
        print("{} is an Animal".format(self.name))


animal1 = Animal("Cow") #object of animal class i.e child class
print(animal1.name) # accessing attributes from parent class
animal1.print_name() # accessing method of parent class
animal1.print_type() # accessing method of child class
     

animal2 = Animal("Cat") #object of animal class i.e child class
print(animal2.name) # accessing attributes from parent class
animal2.print_name() # accessing method of parent class
animal2.print_type() # accessing method of child class