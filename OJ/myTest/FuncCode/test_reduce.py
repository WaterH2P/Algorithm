
from functools import reduce

def add(a, b):
    return a+b

sum = reduce(add, [x for x in range(10)])
print(sum)

def f(x, y):
    return x * 10 + y

# 计算 13579
N = reduce(f, [1, 3, 5, 7, 9])
print(N)