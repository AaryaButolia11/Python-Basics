class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    
    def showDetails(self):
        print(f"Role is {self.role}, dept. is {self.dept} & salary is {self.salary}")


class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","DB","100000")

    def showDetails(self):
        return f"name is {self.name} & age is {self.age}"

        # def showDetails(self):
        # parent_details = super().showDetails()
        # return f"{parent_details}\nname is {self.name} & age is {self.age}"

eng1 = Engineer("Aarya B", "19")
print(eng1.showDetails())
