from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self,name:str,budget:int,animal_capacity:int,workers_capacity:int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self,animal:Animal, price:int) -> str:
        if self.__animal_capacity<= len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.__budget-=price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self,worker:Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self,worker_name:str) -> str:
        worker = next((w for w in self.workers if w.name == worker_name),None)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salary = sum(w.salary for w in self.workers)
        if self.__budget < total_salary:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget-=total_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_care = sum(a.money_for_care for a in self.animals)
        if self.__budget >= total_care:
            self.__budget-=total_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self,amount:int):
        self.__budget+=amount

    def animals_status(self) -> str:
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(repr(animal))
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(repr(animal))
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(repr(animal))
        result = [f"You have {len(self.animals)} animals",f'----- {len(lions)} Lions:']
        result.extend(lions)
        result.append(f'----- {len(tigers)} Tigers:')
        result.extend(tigers)
        result.append(f'----- {len(cheetahs)} Cheetahs:')
        result.extend(cheetahs)
        return '\n'.join(result)

    def workers_status(self):
        keeper = []
        caretaker = []
        vet = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keeper.append(repr(worker))
            elif worker.__class__.__name__ == "Caretaker":
                caretaker.append(repr(worker))
            elif worker.__class__.__name__ == "Vet":
                vet.append(repr(worker))
        result = [f"You have {len(self.workers)} workers", f'----- {len(keeper)} Keepers:']
        result.extend(keeper)
        result.append(f'----- {len(caretaker)} Caretakers:')
        result.extend(caretaker)
        result.append(f'----- {len(vet)} Vets:')
        result.extend(vet)
        return '\n'.join(result)
