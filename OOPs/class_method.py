# class arg -> method that is bound to the class and receives the class as an implicit first argument


# class Person:
#     name = "anonymous"

#     def change_name(self,name):
#         # self.name=name
#         # Person.name = name
#         self.__class__.name=name

# p1 = Person()
# p1.change_name("aarya")
# print(p1.name)
# print(Person.name)


class Person:
    name = "anonymous"

    # def change_name(self,name):
    #     # self.name=name
    #     # Person.name = name
    #     self.__class__.name=name

    @classmethod
    def changeName(cls,name):
        cls.name=name
    
p1=Person()
print(p1.changeName("Aarya"))
print(p1.name)