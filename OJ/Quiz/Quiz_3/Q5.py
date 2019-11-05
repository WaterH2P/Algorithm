f = {0: 0, 1: 1, 2: 1}


def fib(n):
    global f
    # print(f)
    if n in f:
        return f[n]
    if n % 2 == 0:
        k = n // 2
        f[n] = (fib(k) * (fib(k-1) << 1 + fib(k))) % 1000000007
    else:
        k = (n+1) // 2
        f[n] = (fib(k)**2 + fib(k-1)**2) % 1000000007
    return f[n]


for i in range(int(input().strip())):
    res = fib(int(input().strip())+1)
    print(res)