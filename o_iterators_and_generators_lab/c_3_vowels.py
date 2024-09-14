class vowels:
    def __init__(self,ting:str):
        self.vow = ['a','e','i','u','y','o']
        self.ting = [l for l in ting if l.lower() in self.vow]
        self.curend = 0
    def __iter__(self):
        return self

    def __next__(self):
        self.curend+=1
        if self.curend <=len(self.ting):
            return self.ting[self.curend-1]
        raise StopIteration

my_string = vowels('Abcedifuty0o')

for char in my_string:
    print(char)