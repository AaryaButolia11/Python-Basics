# Polymorphism -> operator ooverloading := when same operator is allowed to have different meaning according to the context

# a+b => a.__add__(b)
# a-b => a.__subtract__(b)
# a*b => a.__multiply__(b)
# a/b => a.__truediv__(b)
# a%b => a.__mod__(b)


# print(1+2)
# print("Aarya"+" Butolia") #concatenate
# print([1,2,3]+[4,5,6]) #merge 


class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def showNo(self):
        print(f"{self.real}i + {self.img}j")

    # By using dunder func. u can directly use "+" symbol for calc
    def __add__(self,num2):
        newReal = self.real+num2.real
        newImg = self.img+num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)


num1 = Complex(1,3)
num1.showNo()
num2 = Complex(4,6)
num2.showNo()

num3=num1+num2
num3.showNo()

num3=num1-num2
num3.showNo()