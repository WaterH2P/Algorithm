cow = dict()


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in cow.keys():
        return cow[n]
    if n % 2:
        k = (n + 1) // 2
        cow[n] = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1)) % 1000000007
    else:
        k = n // 2
        cow[n] = (fib(k) * ((fib(k - 1) << 1) + fib(k))) % 1000000007
    return cow[n]


for t in range(int(input())):
    num = int(input())
    print(fib(num+1))