for t in range(int(input())):
    n, m = map(int, input().split())
    arr, query = list(map(int, input().split())), list(map(int, input().split()))
    res = []
    for q in query:
        count = 0
        for i in arr:
            if not i % q:
                count += 1
        res.append(count)
    print(*res)

