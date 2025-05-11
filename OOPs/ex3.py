import math
class Circle():
    def __init__(self,r):
        self.r=r
        print("Circle created!")
    
    def area(self):
        return (math.pi*self.r**2)
    
    def perimeter(self):
        return (math.pi*2*self.r)

c1 = Circle(5)
print(c1.area())
print(c1.perimeter())
