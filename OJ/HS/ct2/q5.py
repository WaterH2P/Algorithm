for t in range(int(input())):
    i, p = 1, int(input())
    x = i * 8
    kill = 0
    while p >= x:
        kill += 1
        p -= x
        i += 1
        x = i * i
    print(kill)
