class Cup:
    def __init__(self,size:int,quantity:int):
        self.size = size
        self.quantity = quantity

    def fill(self,quantity):
        if self.size > self.quantity:
            self.quantity+=quantity

    def status(self):
        return abs(self.size - self.quantity)

# Test code

cup = Cup(100, 50)

print(cup.status())

cup.fill(40)

cup.fill(20)

print(cup.status())