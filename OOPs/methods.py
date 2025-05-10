# Methods -> functions that belong to objects

# class creation
class Student:
# if we dont make constructor by our self python makes it for us-used for init

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def hello(self):
        print("hello ",self.name)
    
    def welcome(self):
        print("Welcome Student")
# We need to write self in every method even if we dont use it
    def getMarks(self):
        return self.marks

# obj creation
s1 = Student("Aarya",91)
# <objname>.<methodname>
s1.welcome()
s1.hello() #
print(s1.getMarks())