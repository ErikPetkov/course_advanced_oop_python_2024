class countdown_iterator:
    def __init__(self,count):
        self.count = count
        self.i = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.count:
            i = self.count
            self.count-=1
            return i
        raise StopIteration