# static methods -> methods that dont use the self parameter (work at class level)


# DECORATORS -> allow us to wrap another function in order to extend the behaviour of the wrapped func without modifying it permanently
class Student:
    @staticmethod #decorator
    def college():
        print("VIT BHOPAL")


s1 = Student()
s1.college()

# Abstraction -> Hiding the implementation details of a class and only showing the essential features to the user
# Encapsulation -> wraping data and func into a single unit (obj)