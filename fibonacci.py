def fib(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fib(x-1) + fib(x-2)

for i in range (1,100):
    print(fib(i))