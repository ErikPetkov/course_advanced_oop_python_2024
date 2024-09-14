from typing import List, Type

from project.food import *
from project.animals.animal import Bird

class Owl(Bird):

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_increment(self) -> float:
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"

class Hen(Bird):

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat,Seed,Vegetable,Fruit]

    @property
    def weight_increment(self) -> float:
        return 0.35

    def make_sound(self):
        return "Cluck"
