def f(x):
    return x**2

N = map(f, [x for x in range(10)])
print(list(N))

S = map(str, [x for x in range(10)])
print(list(S))