# coding: utf-8

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def speak(self):
#         print('Meow')
    
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def speak(self):
#         print('Bark')   
        
        
# We can do in in a bette way

class Pet: # General Class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old ") 
    
    def speak(self):
        print("I dont' know what to say")

class Cat(Pet): # Specific Class
    def __init__(self, name, age, color):
        super().__init__(name, age) # SuperClass
        self.color = color
            
    def speak(self):
        print("Meow")
        
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
    
class Dog(Pet):
        
    def speak(self): # Specific Class
        print("Bark")
        
class Monkey(Pet):
    
    def speak(self): # Specific Class
        print("woogloo")
        
class Fish(Pet):
    pass
    
# Test
p = Pet("Tim", 19)
p.show()
p.speak()
c = Cat("Sullyvan", 13, "Brown")
c.show() # .show is inheritad from Pet
c.speak()
d =Dog("Boule", 44)
d.show()
d.speak()
m = Monkey("Sheetah", 11)
m.show()
m.speak()
f = Fish("Doris", 5)
f.show()
f.speak() # Without  a specific method global will be used instead
