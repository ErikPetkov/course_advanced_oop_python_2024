import math

from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    MEMBERSHIP_TYPE = "Regular"
    def __init__(self,name: str):
        super().__init__(name,self.MEMBERSHIP_TYPE)

    def earning_points(self, order_amount: float):
        point = math.floor(order_amount / 10)
        self.points += point
        return f"{self.name} earned {point} points from the order."



