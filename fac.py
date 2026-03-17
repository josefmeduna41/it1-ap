from math import factorial

def fac(x: int) -> int:
    n = 1
    for i in range(1, x + 1):
        n *= i
    return n

for n in range(100):
    x = fac(n)
    y = factorial(n)
    assert x == y