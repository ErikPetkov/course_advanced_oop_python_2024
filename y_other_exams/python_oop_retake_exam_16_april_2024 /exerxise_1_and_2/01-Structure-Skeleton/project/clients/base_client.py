from abc import ABC,abstractmethod


class BaseClient(ABC):
    ALOWED_MEMBERSHIPS = ['Regular','VIP']
    def __init__(self,name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type
        self.points = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Client name should be determined!")
        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in self.ALOWED_MEMBERSHIPS:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self.__membership_type = value

    # if not work make a property on points
    @abstractmethod
    def earning_points(self,order_amount: float):
        pass

    def apply_discount(self):
        if self.points >= 100:
            self.points -= 100
            discount = 10
        elif 50 <= self.points and self.points < 100:
            self.points -= 50
            discount = 5
        else:
            discount = 0

        return f"{self.name} received a {discount}% discount. Remaining points {self.points}"