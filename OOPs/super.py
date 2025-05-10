# super() -> used to access the methods of the parent class 
class Car:

    def __init__(self,type):
        self.type=type
        
    @staticmethod
    def start():
        print("car started!")
    @staticmethod
    def stop():
        print("car stopped!")

# Single level
class HyundaiCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        super().start()
        self.name=name

car1 = HyundaiCar("verna","diesel")
print(car1.type)