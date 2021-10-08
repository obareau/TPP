# OOP fundamentals in Python

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age): #Now i can mofify age
        self.age = age
    
d = Dog('Tim', 7)
d2 = Dog('Joe', 3)
print(d.get_name(), d.get_age())
print(d2.get_name(), d2.get_age())

# Now let's set a new age for both dogs
d.set_age(43)
d2.set_age(112)
print(d.get_name(), d.get_age())
print(d2.get_name(), d2.get_age())

    
    

