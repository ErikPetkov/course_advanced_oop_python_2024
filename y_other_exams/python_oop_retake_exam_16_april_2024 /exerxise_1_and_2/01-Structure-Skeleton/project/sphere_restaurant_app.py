from typing import List

from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    VALID_WAITER_TYPES = {'HalfTimeWaiter':HalfTimeWaiter, 'FullTimeWaiter':FullTimeWaiter}
    VALID_CLIENT_TYPES = {'RegularClient':RegularClient,'VIPClient':VIPClient}
    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self,waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.VALID_WAITER_TYPES.keys():
            return f"{waiter_type} is not a recognized waiter type."
        is_waiter_name = next((w for w in self.waiters if w.name == waiter_name),None)
        if is_waiter_name:
            return f"{waiter_name} is already on the staff."

        waiter = self.VALID_WAITER_TYPES[waiter_type](waiter_name,hours_worked)
        self.waiters.append(waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self,client_type: str, client_name: str):
        if client_type not in self.VALID_CLIENT_TYPES.keys():
            return f"{client_type} is not a recognized client type."
        # is_client_name = next((c for c in self.clients if c.name == client_name),None)
        is_client_name = [c for c in self.clients if c.name == client_name]
        if is_client_name:
            return f"{client_name} is already a client."
        client = self.VALID_CLIENT_TYPES[client_type](client_name)
        self.clients.append(client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        for w in self.waiters:
            if w.name == waiter_name:
                return w.report_shift()
        return f"No waiter found with the name {waiter_name}."

    def process_client_order(self,client_name: str, order_amount: float):
        for c in self.clients:
            if c.name == client_name:
                return c.earning_points(order_amount)
        return f"{client_name} is not a registered client."

    def apply_discount_to_client(self,client_name: str):
        for c in self.clients:
            if c.name == client_name:
                return c.apply_discount()
        return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self):
        result = ["$$ Monthly Report $$"]

        total_earnings = 0
        for w in self.waiters:
            w.calculate_earnings()
            total_earnings+=w.total_earnings
        result.append(f'Total Earnings: ${total_earnings}')

        total_client_points = 0
        for c in self.clients:
            total_client_points+=c.points
        result.append(f'Total Clients Unused Points: {total_client_points}')

        result.append(f'Total Clients Count: {len(self.clients)}')
        result.append('** Waiter Details **')
        ordered_weiters = sorted(self.waiters,key=lambda w: -w.total_earnings)
        for w in ordered_weiters:
            result.append(str(w))
        return '\n'.join(result)




