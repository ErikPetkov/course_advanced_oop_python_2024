class take_skip:
    def __init__(self,step:int,count:int):
        self.step = step
        self.count = count
        self.curent = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.curent < self.count:
            i = self.curent
            self.curent += 1
            return i*self.step
        raise StopIteration

numbers = take_skip(2, 6)
for number in numbers:
    print(number)