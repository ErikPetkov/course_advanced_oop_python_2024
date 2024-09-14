def reverse_text(string:str):
    rev_t = string[::-1]
    yield rev_t

for char in reverse_text("step"):
    print(char, end='')