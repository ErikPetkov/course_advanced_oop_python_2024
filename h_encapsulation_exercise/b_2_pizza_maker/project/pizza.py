from typing import Dict
from project.topping import Topping
from project.dough import Dough
class Pizza:
    def __init__(self,name: str,dough: Dough,max_number_of_toppings: int,):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: Dict = dict()

    @property
    def name(self):
        return

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value == None:
            raise ValueError("You should add dough to the pizza")
        self.__dough:Dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <=0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value

    def add_topping(self,topping: Topping):
        if self.__max_number_of_toppings <= len(self.toppings):
            raise ValueError("Not enough space for another topping")
        if topping.topping_type not in self.toppings.keys():
            self.toppings[topping.topping_type] = 0
        self.toppings[topping.topping_type]+=topping.weight

    def calculate_total_weight(self):
        topping_w = sum(v for v in self.toppings.values())
        dough_w = self.__dough.weight
        return topping_w+dough_w

