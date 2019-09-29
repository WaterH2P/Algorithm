def iter_odd():
    n = 1
    while True:
        n += 2
        yield n

def not_div(n):
    return lambda x : x % n > 0

def prime():
    yield 2
    l = iter_odd()
    while True :
        n = next(l)
        yield n
        l = filter(not_div(n), l)

for n in prime() :
    if n < 1000 :
        print(n)
    else :
        break