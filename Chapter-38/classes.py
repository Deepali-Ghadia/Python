# Animal class 
# name |  sound

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def makes(self):
        print("{} can {}".format(self.name, self.sound))
        
        


obj1 = Animal("Cow", "Moo")
print(obj1.name)
print(obj1.sound)
print(obj1.makes())

obj2 = Animal("Cat", "Meow")
print(obj2.name)
print(obj2.sound)
print(obj2.makes())