
from functools import reduce

def char2num(c):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[c]

def str2num(s):
    def f(x, y):
        return x * 10 + y
    return reduce(f, map(char2num, s))

N = str2num('12345')
print(N)

def str2num2(s):
    f = lambda x, y : x + y
    return reduce(f, map(char2num, s))

N = str2num('67890')
print(N)