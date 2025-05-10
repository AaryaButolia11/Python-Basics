# Private attr. & methods -> these are meant to be used only within the class and are not accessible from outside the class

class Account:
    def __init__(self,acc_no,acc_pswd):
        self.acc_no=acc_no
        self.__acc_pswd = acc_pswd

    def reset_pswd(self):
        print(self.__acc_pswd)

# to make any attr. or methods private use "__<name>" before it
acc1 = Account("12345","abcde")
print(acc1.acc_no)
print(acc1.reset_pswd())

class Person:
    def __init__(self):
        self.__name = "Anonymous"

    def __hello(self):
        print("hello person!!")

# to call any priv func in another fun call it by using self.
    def welcome(self):
        self.__hello()
        print(f"Welcome, {self.__name}!")

p1 = Person()
p1.welcome()  # Now this will print
