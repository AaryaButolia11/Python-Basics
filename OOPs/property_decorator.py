# property decorator is used on any method in the class to use the method as property

class Student:

    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
        # self.percentage = str((self.phy+self.chem+self.maths)/3)+"%"
    @property
    def calcPercent(self):
        return str((self.phy+self.chem+self.maths)/3)+"%"



stu1 = Student(98,92,92)
print(stu1.calcPercent)

stu1.phy = 81

print(stu1.calcPercent)