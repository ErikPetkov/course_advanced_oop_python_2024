from typing import List, Type
from project.food import *
from project.animals.animal import Mammal

class Mouse(Mammal):

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Vegetable,Fruit]

    @property
    def weight_increment(self) -> float:
        return 0.1

    def make_sound(self):
        return "Squeak"

class Dog(Mammal):

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_increment(self) -> float:
        return 0.4

    def make_sound(self):
        return "Woof!"

class Cat(Mammal):

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Vegetable,Meat]

    @property
    def weight_increment(self) -> float:
        return 0.3

    def make_sound(self):
        return "Meow"

class Tiger(Mammal):

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_increment(self) -> float:
        return 1.0

    def make_sound(self):
        return "ROAR!!!"
