from typing import List

from project.subscription import Subscription
from project.exercise_plan import ExercisePlan
from project.equipment import Equipment
from project.trainer import Trainer
from project.customer import Customer


class Gym:
    def __init__(self):
        self.customers : List[Customer] = []
        self.trainers :List[Trainer] = []
        self.equipment :List[Equipment] = []
        self.plans :List[ExercisePlan] = []
        self.subscriptions :List[Subscription] = []

    def add_customer(self,customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self,trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self,equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self,plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self,subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self,subscription_id: int):
        result = []
        result.append(next(repr(s) for s in self.subscriptions if s.id ==subscription_id))
        result.append(next(repr(c) for c in self.customers if c.id ==subscription_id))
        result.append(next(repr(t) for t in self.trainers if t.id ==subscription_id))
        result.append(next(repr(p) for p in self.plans if p.id ==subscription_id))
        result.append(next(repr(e) for e in self.equipment if e.id ==subscription_id))
        return '\n'.join(result)



