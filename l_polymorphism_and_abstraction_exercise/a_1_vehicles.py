from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

class Car(Vehicle):
    INCREASED = 0.9
    def __init__(self,fuel_quantity:int,fuel_consumption:int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self,distance):
        fuel_needed = distance*(self.fuel_consumption+Car.INCREASED)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity-=fuel_needed
    def refuel(self,fuel):
        self.fuel_quantity+=fuel

class Truck(Vehicle):
    INCREASED = 1.6
    TANK = 0.95

    def __init__(self,fuel_quantity:int,fuel_consumption:int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self,distance):
        fuel_needed = distance*(self.fuel_consumption+Truck.INCREASED)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity-=fuel_needed
    def refuel(self,fuel):
        self.fuel_quantity+=fuel*Truck.TANK

#Test code

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)