u = int(input())
while u > 0:
    u -= 1
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    n = len(a)
    diff = abs(sum(a) - sum(b))
    while True:
        switched = False
        for i in range(n):
            for j in range(n):
                if abs(diff - 2 * (a[i] - b[j])) < diff:
                    print('a', a, sum(a))
                    print('b', b, sum(b))
                    a[i] = a[i] + b[j]
                    b[j] = a[i] - b[j]
                    a[i] = a[i] - b[j]
                    diff = abs(sum(a) - sum(b))
                    switched = True
        if switched is False:
            break

    print(abs(sum(a) - sum(b)))

