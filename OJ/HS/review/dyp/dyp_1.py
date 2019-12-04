# 订单问题
for t in range(int(input())):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    diff = [abs(x - y) for x, y in zip(a, b)]
    index = list(range(n))
    zipped = zip(diff, index)
    z = [x for _, x in sorted(zipped)]
    print(diff)
    print(z)

    res = 0
    for i in reversed(z):
        if a[i] >= b[i] and x > 0:
            x = x - 1
            res = res + a[i]
        elif a[i] >= b[i]:
            y = y - 1
            res = res + b[i]
        elif b[i] >= a[i] and y > 0:
            y = y - 1
            res = res + b[i]
        elif b[i] >= a[i]:
            x = x - 1
            res = res + a[i]

    print(res)