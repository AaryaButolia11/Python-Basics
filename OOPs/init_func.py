# __init__ function (Constructor) 
# All classes have a function called _init_(), which is always executed when the class is being initiated
# Always self parameter is taken by constructor
# It marks the obj by which the class is init.

class Student:


    # default constructor
    # def __init__(self):
    #     # print("Constructor Init")
    #     pass
    
    # paramaterized constructor
    def __init__(self,fullName,marks):
        self.name=fullName
        self.marks=marks
        print("Adding new student in DB")

s1 = Student("Aarya Butolia",91)
print(s1)
print(s1.name)
print(s1.name)
print(s1.marks)

s2 = Student("Rashi Butolia",98)
print(s2)
print(s2.name)
print(s2.marks)


s3 = Student()
print(s3.name)
# the self parameter is the reference to the current instance of the class and is used to access variables that belong to the class


# data -> attributes
# func -> methods