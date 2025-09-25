CACHE = {}

def fibonacci(x):
    if x in CACHE:
        return CACHE[x]
    if x <= 1:
        return x
    CACHE[x] = fibonacci(x - 2) + fibonacci(x - 1)
    return CACHE[x]

print(fibonacci(20))