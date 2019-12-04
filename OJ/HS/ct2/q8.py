for t in range(int(input())):
    p = int(input())
    i = 1
    p -= i * i
    count = 0
    while p >= 0:
        print(i)
        count += 1
        i += 1
        p -= i * i
    print(count)

