fDict = dict()


def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n in fDict.keys():
        return fDict[n]

    if n % 2 == 0:
        k = n // 2
        fDict[n] = (fib(k) * ((fib(k - 1) << 1) + fib(k))) % 1000000007
    else:
        k = (n + 1) // 2
        fDict[n] = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1)) % 1000000007
    return fDict[n]


for t in range(int(input())):
    num = int(input())
    print(fib(num+1))