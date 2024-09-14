from abc import ABC,abstractmethod
from typing import List
from project.peaks.base_peak import BasePeak

class BaseClimber(ABC):
    def __init__( self,name: str, strength: float):
        self.name = name
        self.strength = strength
        self.initual_strenght = strength
        self.conquered_peaks: List[BasePeak] = []
        self.is_prepared = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value

    @property
    def strenght(self):
        return self.__strength

    @strenght.setter
    def strenght(self, value):
        if value<=0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value
    @abstractmethod
    def can_climb(self):
        pass

    @abstractmethod
    def climb(peak : BasePeak):
        pass

    def rest(self):
        self.strength+=15

    def __str__(self):
        type_of_climber = 'ArcticClimber' if self.initual_strenght == 200 else 'SummitClimber'
        return (f"{type_of_climber}: /// Climber name: {self.name} * "
                f"Left strength: {self.strength:.1f} * Conquered peaks: {', '.join(self.conquered_peaks)} ///")





