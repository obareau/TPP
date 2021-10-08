# coding: utf-8

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # int 0 -100 -
        
    def get_grade(self): #It's a method !!!
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] # Lets's make a list of students
        
    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
        
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
            
        return value / len(self.students)
        
    
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)       

course = Course("Science", 2)
course.add_students(s1)
course.add_students(s2)

# print(course.students[0].name)
print(course.get_average_grade())
print(course.add_students(s3))