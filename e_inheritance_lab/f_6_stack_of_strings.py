from typing import List
class Stack:
    def __init__(self) -> None:
        self.data: List[str] = []

    def push(self,element:str) -> None:
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        if self.data:
            return False
        return True

    def __str__(self):
        return '['+', '.join(self.data)+']'


stack = Stack()
stack.push("apple")
print(stack)
stack.push("carrot")
print(stack)
stack.pop()
print(stack)
stack.top()
print(stack)
stack.push("cucumber")
print(stack)
stack.is_empty()