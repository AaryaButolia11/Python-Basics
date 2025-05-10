# del keyword -> to delete the obj properties or the entire keyword itself.

# del s1.name
# del s1 


class Student:
    def __init__(self,name):
        self.name=name

s1 = Student("Aarya")
del s1 #deleting is s1
print(s1.name)