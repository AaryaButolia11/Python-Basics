# Class attr -> common to whole class
# Instance attr -> belongs to obj particularly and declared by self.<name> as it refers the object
class Student:

    # class atr-> stored in memory once as not defined with self
    college_name = "VIT BHOPAL" 


    # paramaterized constructor
    def __init__(self,fullName,marks):
        self.name=fullName #object attr
        self.marks=marks #object attr
        print("Adding new student in DB")

s1 = Student("Aarya Butolia",91)
print(s1)
print(s1.name)
print(s1.name)
print(s1.marks)
# print(s1.college_name)

s2 = Student("Rashi Butolia",98)
print(s2)
print(s2.name)
print(s2.marks)
# print(s2.college_name)

# class attr can be accessed using class name directly
print(Student.college_name)

# the precedence of obj attr is higher than class attr
# OBJECT >> CLASS ATTR.