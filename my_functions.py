import rich
from rich import print

def greet(x):
    result = ''
    for i in range(len(x)):
        if i % 2 == 0:
            result += x[i].upper()
        else:
            result += x[i]
    return result

def hello(y):
    return f"[italic red]Hello, {y}![italic red]"