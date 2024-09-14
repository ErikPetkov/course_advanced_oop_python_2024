from project.clients.base_client import BaseClient
import math

class VIPClient(BaseClient):
    MEMBERSHIP_TYPE = "VIP"
    def __init__(self,name: str):
        super().__init__(name,self.MEMBERSHIP_TYPE)

    def earning_points(self,order_amount: float):
        point = math.floor(order_amount / 5)
        self.points += point
        return f"{self.name} earned {point} points from the order."



