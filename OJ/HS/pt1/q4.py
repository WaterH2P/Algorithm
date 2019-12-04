u = int(input())
while u > 0:
    u -= 1
    n = int(input())
    count = 0

    def hanoi(n, a='A', b='B', c='C'):
        global count
        if n == 1:
            count += 1
        else:
            hanoi(n - 1, a, c, b)
            hanoi(n - 1, b, a, c)
            hanoi(1    , a, c, b)
            hanoi(n - 1, c, a, b)
            hanoi(n - 1, b, c, a)
            hanoi(1    , b, a, c)
            hanoi(n - 1, a, c, b)
            hanoi(n - 1, b, a, c)

    hanoi(n)
    print(count)
