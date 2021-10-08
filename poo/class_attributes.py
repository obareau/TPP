# coding: utf-8

class Person:
    number_of_people = 0 # Specific to the class
    GRAVITY = 9.8 # we define constants in the generic class
    
    def __init__(self, name):
        self.name = name
        Person.add_person()
    
    # Decorator
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people # it acts only in the class itself
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
    
p1 = Person("Tim")
p2 = Person("Jill")
print(Person.number_of_people_())

