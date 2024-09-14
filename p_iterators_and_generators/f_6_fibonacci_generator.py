def fibonacci():
    curent,next_n = 0,1

    while True:
        yield curent
        curent,next_n = next_n,next_n+curent

generator = fibonacci()
for i in range(5):
    print(next(generator))