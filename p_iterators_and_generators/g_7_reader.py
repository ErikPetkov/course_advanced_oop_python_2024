from typing import Iterable
def read_next(*args:Iterable):
    for c in args:
        yield from c

for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')