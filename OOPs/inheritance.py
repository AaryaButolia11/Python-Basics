# when one class(child/derived) derives the prop. & methods of aother class(parent/base)

# class car:               ->parent
# class hyundai(car):      -> child


class Car:
    @staticmethod
    def start():
        print("car started!")
    @staticmethod
    def stop():
        print("car stopped!")

# Single level
class HyundaiCar(Car):
    def __init__(self,brand):
        self.brand=brand

# Multilevel
class Tuscon(HyundaiCar):
    def __init__(self,type):
        self.type=type



car1 = Tuscon("diesel")
# car2 = HyundaiCar("Verna")
# print(car1.brand)
print(car1.start())
# print(car2.name)